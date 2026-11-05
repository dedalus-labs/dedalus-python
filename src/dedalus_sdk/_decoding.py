"""Bounded decoding of a response's content codings.

httpx inflates a whole network read in one call, so with stacked codings (`gzip, gzip`) a few KiB read
can expand to gigabytes before any size limit sees a byte. Buffered bodies and streamed ones (SSE,
JSON Lines) read their bytes through `BoundedDecoder` instead, which inflates gzip and deflate in
steps of at most `INFLATE_STEP` bytes, so every reader can stop at its own limit after each step.
"""

from __future__ import annotations

import zlib
from typing import Dict, List, Mapping, Iterator, AsyncIterator, cast

import httpx

from ._exceptions import APIError

# The most bytes one inflate step produces.
INFLATE_STEP = 64 * 1024

# The content codings `BoundedDecoder` undoes itself, with the zlib window bits that read each one.
ZLIB_CODINGS: Dict[str, int] = {
    "gzip": zlib.MAX_WBITS | 16,
    "x-gzip": zlib.MAX_WBITS | 16,
    "deflate": zlib.MAX_WBITS,
}

# Codings only httpx can undo, each through an optional package and without bounding the output, so a
# body that uses one is refused. httpx skips one whose package is missing, and so does `BoundedDecoder`.
HTTPX_ONLY_CODINGS = frozenset({"br", "zstd"})


class CodingRefused(Exception):
    """A success body coded br or zstd, which no limit could bound; the caller reports it as an SDK error."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class Inflater:
    """One gzip or deflate layer, inflated at most `INFLATE_STEP` bytes per step.

    A deflate body should be zlib-wrapped, but some servers send it raw; as httpx does, a stream whose
    first bytes are not a zlib header is read again as raw deflate.
    """

    def __init__(self, wbits: int) -> None:
        self._wbits = wbits
        self._decompressor = zlib.decompressobj(wbits)
        self._started = False

    def feed(self, data: bytes) -> Iterator[bytes]:
        """Inflates `data`, yielding the output in pieces of at most `INFLATE_STEP` bytes."""
        while not self._decompressor.eof:
            try:
                out = self._decompressor.decompress(data, INFLATE_STEP)
            except zlib.error:
                if self._started or self._wbits != zlib.MAX_WBITS:
                    raise
                self._wbits = -zlib.MAX_WBITS
                self._decompressor = zlib.decompressobj(self._wbits)
                continue
            self._started = True
            # Input past the step stays in `unconsumed_tail`; an empty step with nothing left means
            # zlib needs more input.
            data = self._decompressor.unconsumed_tail
            if out:
                yield out
            elif not data:
                break

    def flush(self) -> Iterator[bytes]:
        """Whatever the layer still holds once the body has ended; `feed` has drained it to a few bytes."""
        out = self._decompressor.flush()
        if out:
            yield out


def httpx_decoders() -> Mapping[str, object]:
    """The content codings the installed httpx decodes; br and zstd appear only with their optional packages."""
    try:
        from httpx._decoders import SUPPORTED_DECODERS  # pyright: ignore[reportPrivateUsage]
    except ImportError:
        return {}
    return cast("Mapping[str, object]", SUPPORTED_DECODERS)


class BoundedDecoder:
    """Undoes a response's gzip and deflate content codings, stacked ones included, in bounded steps.

    Each layer hands the next a piece of at most `INFLATE_STEP` bytes, so a reader can stop at its
    limit after every step instead of after httpx has inflated a whole network read at once.
    """

    def __init__(self, layers: List[Inflater]) -> None:
        self._layers = layers

    @classmethod
    def for_response(cls, response: httpx.Response, *, capped: bool) -> BoundedDecoder | None:
        """The decoder for `response`'s `Content-Encoding`, or None when httpx must decode it.

        httpx decodes a body read uncapped and a body it already holds (a transport may hand back a
        response read in full): that one has no raw stream left and is served from memory. Codings
        are undone last-applied first. `identity` and codings httpx does not know pass through
        unchanged, as they do in httpx. A br or zstd coding httpx would decode raises `CodingRefused`
        on a success; an error body with one is read raw.
        """
        if hasattr(response, "_content") or not capped:
            # An uncapped body (a successful binary download) is the caller's to bound, so httpx
            # decodes it as it would.
            return None
        codings = [coding.strip().lower() for coding in response.headers.get("content-encoding", "").split(",")]
        if any(coding in HTTPX_ONLY_CODINGS and coding in httpx_decoders() for coding in codings):
            # httpx inflates br and zstd a whole network read per call, which no limit can stop, and the
            # SDK never asks for them (`Accept-Encoding: gzip, deflate`).
            if not response.is_success:
                # An error body is read for its message only: keep its raw bytes, so the status error
                # (and its retry) still stands.
                return cls([])
            raise CodingRefused(
                "A br or zstd content coding is not decoded for a buffered or streamed response; "
                "the SDK accepts gzip and deflate"
            )
        return cls([Inflater(ZLIB_CODINGS[coding]) for coding in reversed(codings) if coding in ZLIB_CODINGS])

    def decode(self, data: bytes) -> Iterator[bytes]:
        """Decodes one network read, yielding the body in bounded pieces."""
        return self._push(0, data)

    def flush(self) -> Iterator[bytes]:
        """Decodes what the layers still hold once the body has ended."""
        for index, layer in enumerate(self._layers):
            for piece in layer.flush():
                yield from self._push(index + 1, piece)

    def _push(self, index: int, data: bytes) -> Iterator[bytes]:
        """Runs `data` through the layers from `index` on."""
        if index == len(self._layers):
            yield data
            return
        for piece in self._layers[index].feed(data):
            yield from self._push(index + 1, piece)


def decoding_error(response: httpx.Response, exc: zlib.error) -> httpx.DecodingError:
    """The error for a body that is not valid for its `Content-Encoding`, as httpx raises it."""
    return httpx.DecodingError(f"Error decoding the response body: {exc}", request=response.request)


def _stream_decoder(response: httpx.Response) -> BoundedDecoder | None:
    """The bounded decoder for a streamed body, reporting a br or zstd one as an `APIError`."""
    try:
        return BoundedDecoder.for_response(response, capped=True)
    except CodingRefused as exc:
        raise APIError(exc.message, response.request, body=None) from None


def iter_decoded(response: httpx.Response) -> Iterator[bytes]:
    """A streamed body's bytes, decoded in bounded pieces as they arrive (SSE and JSON Lines read this)."""
    decoder = _stream_decoder(response)
    if decoder is None:
        yield from response.iter_bytes()
        return
    try:
        for raw in response.iter_raw():
            yield from decoder.decode(raw)
        yield from decoder.flush()
    except zlib.error as exc:
        raise decoding_error(response, exc) from exc


async def aiter_decoded(response: httpx.Response) -> AsyncIterator[bytes]:
    """The async twin of `iter_decoded`."""
    decoder = _stream_decoder(response)
    if decoder is None:
        async for chunk in response.aiter_bytes():
            yield chunk
        return
    try:
        async for raw in response.aiter_raw():
            for piece in decoder.decode(raw):
                yield piece
        for piece in decoder.flush():
            yield piece
    except zlib.error as exc:
        raise decoding_error(response, exc) from exc
