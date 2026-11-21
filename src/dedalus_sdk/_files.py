from __future__ import annotations

import io
import os
import inspect
import pathlib
from typing import Sequence, cast, overload
from typing_extensions import TypeVar, TypeGuard

import anyio

from ._types import (
    FileTypes,
    FileContent,
    RequestFiles,
    HttpxFileTypes,
    Base64FileInput,
    HttpxFileContent,
    HttpxRequestFiles,
)
from ._utils import is_list, is_mapping, is_tuple_t, is_mapping_t, is_sequence_t

_T = TypeVar("_T")


def is_base64_file_input(obj: object) -> TypeGuard[Base64FileInput]:
    return isinstance(obj, io.IOBase) or isinstance(obj, os.PathLike)


def is_file_content(obj: object) -> TypeGuard[FileContent]:
    return (
        isinstance(obj, bytes) or isinstance(obj, tuple) or isinstance(obj, io.IOBase) or isinstance(obj, os.PathLike)
    )


def assert_is_file_content(obj: object, *, key: str | None = None) -> None:
    if not is_file_content(obj):
        prefix = f"Expected entry at `{key}`" if key is not None else f"Expected file input `{obj!r}`"
        raise RuntimeError(
            f"{prefix} to be bytes, an io.IOBase instance, PathLike or a tuple but received {type(obj)} instead."
        ) from None


@overload
def to_httpx_files(files: None) -> None: ...


@overload
def to_httpx_files(files: RequestFiles) -> HttpxRequestFiles: ...


def to_httpx_files(files: RequestFiles | None) -> HttpxRequestFiles | None:
    if files is None:
        return None

    if is_mapping_t(files):
        files = {key: _transform_file(file) for key, file in files.items()}
    elif is_sequence_t(files):
        files = [(key, _transform_file(file)) for key, file in files]
    else:
        raise TypeError(f"Unexpected file type input {type(files)}, expected mapping or sequence")

    return files


def _transform_file(file: FileTypes) -> HttpxFileTypes:
    if is_file_content(file):
        if isinstance(file, os.PathLike):
            path = pathlib.Path(file)
            return (path.name, path.read_bytes())

        return file

    if is_tuple_t(file):
        return (file[0], read_file_content(file[1]), *file[2:])

    raise TypeError(f"Expected file types input to be a FileContent type or to be a tuple")


def read_file_content(file: FileContent) -> HttpxFileContent:
    if isinstance(file, os.PathLike):
        return pathlib.Path(file).read_bytes()
    return file


@overload
async def async_to_httpx_files(files: None) -> None: ...


@overload
async def async_to_httpx_files(files: RequestFiles) -> HttpxRequestFiles: ...


async def async_to_httpx_files(files: RequestFiles | None) -> HttpxRequestFiles | None:
    if files is None:
        return None

    if is_mapping_t(files):
        files = {key: await _async_transform_file(file) for key, file in files.items()}
    elif is_sequence_t(files):
        files = [(key, await _async_transform_file(file)) for key, file in files]
    else:
        raise TypeError(f"Unexpected file type input {type(files)}, expected mapping or sequence")

    return files


async def _async_transform_file(file: FileTypes) -> HttpxFileTypes:
    if is_file_content(file):
        if isinstance(file, os.PathLike):
            path = anyio.Path(file)
            return (path.name, await path.read_bytes())

        return file

    if is_tuple_t(file):
        return (file[0], await async_read_file_content(file[1]), *file[2:])

    raise TypeError(f"Expected file types input to be a FileContent type or to be a tuple")


async def async_read_file_content(file: FileContent) -> HttpxFileContent:
    if isinstance(file, os.PathLike):
        return await anyio.Path(file).read_bytes()

    return file


def _is_form_file(obj: object) -> bool:
    """Whether a value in a form-urlencoded body is a file whose contents the field carries.

    Bytes, a file object and a path are files. A file object is anything with a callable `read`, not
    only an `io.IOBase`: `IO[bytes]` admits wrappers that are not one (`SpooledTemporaryFile` before
    Python 3.11, framework upload objects, whose `read()` may be async), and an unrecognized one
    would reach the query encoder's `str()` and go out as its repr. A tuple is one only in the `(filename, content, ...)` shape
    `FileTypes` allows, so a tuple of strings stays the list the query encoder reads it as.
    """
    if _is_form_file_content(obj):
        return True
    return (
        isinstance(obj, tuple)
        and 2 <= len(cast("tuple[object, ...]", obj)) <= 4
        and (obj[0] is None or isinstance(obj[0], str))
        and _is_form_file_content(obj[1])
    )


def _is_form_file_content(obj: object) -> bool:
    """Whether a value is file content: bytes, a path, or an object with a callable `read`."""
    return isinstance(obj, (bytes, bytearray, os.PathLike)) or callable(getattr(obj, "read", None))


def _form_file_source(obj: object) -> object:
    """The content half of a form file value: the tuple's second item, or the value itself."""
    return cast("tuple[object, ...]", obj)[1] if isinstance(obj, tuple) else obj


def _checked_form_contents(source: object, contents: object) -> object:
    """A file object's `read()` result, refused unless it is bytes or text.

    Anything else would reach the query encoder's `str()` and go out as its repr.
    """
    if isinstance(contents, (bytes, bytearray, str)):
        return contents
    raise TypeError(f"Expected {type(source).__name__}.read() to return bytes or str but got {type(contents)} instead.")


def read_form_files(data: _T) -> _T:
    """Returns a form-urlencoded body with every file value replaced by its contents.

    A form has no file parts, so a file field goes out as its contents, the way a string field would.
    A file object is read whole from its current position and a path from the start, with no size
    bound, which suits form fields but not large files; those belong in a multipart body. It runs
    once per call rather than per attempt, so a retry resends the same bytes instead of an exhausted
    file object's empty read. Every container is copied, so the caller's own body is left as it was.
    """
    if _is_form_file(data):
        source = _form_file_source(data)
        if isinstance(source, os.PathLike):
            return cast(_T, pathlib.Path(cast("os.PathLike[str]", source)).read_bytes())
        if isinstance(source, (bytes, bytearray)):
            return cast(_T, bytes(source))
        contents: object = cast("io.BufferedIOBase", source).read()
        if inspect.isawaitable(contents):
            # an async `read()` (an ASGI upload object) cannot be awaited here; close it unawaited
            # rather than leave a warning, and point the caller at the client that can
            if inspect.iscoroutine(contents):
                contents.close()
            raise TypeError(
                f"{type(source).__name__}.read() is asynchronous; send it through the async client, or pass its bytes"
            )
        return cast(_T, _checked_form_contents(source, contents))
    if is_mapping(data):
        return cast(_T, {key: read_form_files(value) for key, value in data.items()})
    if is_list(data) or isinstance(data, tuple):
        return cast(_T, [read_form_files(item) for item in cast("Sequence[object]", data)])
    return data


async def async_read_form_files(data: _T) -> _T:
    """`read_form_files` for an async client.

    It reads a path without blocking the event loop, and awaits a file object whose `read()` is
    asynchronous, as an ASGI framework's upload object's is.
    """
    if _is_form_file(data):
        source = _form_file_source(data)
        if isinstance(source, os.PathLike):
            return cast(_T, await anyio.Path(cast("os.PathLike[str]", source)).read_bytes())
        if isinstance(source, (bytes, bytearray)):
            return cast(_T, bytes(source))
        contents: object = cast("io.BufferedIOBase", source).read()
        if inspect.isawaitable(contents):
            contents = await contents
        return cast(_T, _checked_form_contents(source, contents))
    if is_mapping(data):
        return cast(_T, {key: await async_read_form_files(value) for key, value in data.items()})
    if is_list(data) or isinstance(data, tuple):
        return cast(_T, [await async_read_form_files(item) for item in cast("Sequence[object]", data)])
    return data


def deepcopy_with_paths(item: _T, paths: Sequence[Sequence[str]]) -> _T:
    """Copy only the containers along the given paths.

    Used to guard against mutation by extract_files without copying the entire structure.
    Only dicts and lists that lie on a path are copied; everything else
    is returned by reference.

    For example, given paths=[["foo", "files", "file"]] and the structure:
        {
            "foo": {
                "bar": {"baz": {}},
                "files": {"file": <content>}
            }
        }
    The root dict, "foo", and "files" are copied (they lie on the path).
    "bar" and "baz" are returned by reference (off the path).
    """
    return _deepcopy_with_paths(item, paths, 0)


def _deepcopy_with_paths(item: _T, paths: Sequence[Sequence[str]], index: int) -> _T:
    if not paths:
        return item
    if is_mapping(item):
        key_to_paths: dict[str, list[Sequence[str]]] = {}
        for path in paths:
            if index < len(path):
                key_to_paths.setdefault(path[index], []).append(path)

        # if no path continues through this mapping, it won't be mutated and copying it is redundant
        if not key_to_paths:
            return item

        result = dict(item)
        for key, subpaths in key_to_paths.items():
            if key in result:
                result[key] = _deepcopy_with_paths(result[key], subpaths, index + 1)
        return cast(_T, result)
    if is_list(item):
        array_paths = [path for path in paths if index < len(path) and path[index] == "<array>"]

        # if no path expects a list here, nothing will be mutated inside it - return by reference
        if not array_paths:
            return cast(_T, item)
        return cast(_T, [_deepcopy_with_paths(entry, array_paths, index + 1) for entry in item])
    return item
