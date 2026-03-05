# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import DedalusError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import pets, store, users
    from .resources.pets import PetsResource, AsyncPetsResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.store.store import StoreResource, AsyncStoreResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Dedalus", "AsyncDedalus", "Client", "AsyncClient"]


class Dedalus(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Dedalus client instance.

        This automatically infers the `api_key` argument from the `PETSTORE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PETSTORE_API_KEY")
        if api_key is None:
            raise DedalusError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PETSTORE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("DEDALUS_BASE_URL")
        if base_url is None:
            base_url = f"https://petstore3.swagger.io/api/v3"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def pets(self) -> PetsResource:
        """Everything about your Pets"""
        from .resources.pets import PetsResource

        return PetsResource(self)

    @cached_property
    def store(self) -> StoreResource:
        """Access to Petstore orders"""
        from .resources.store import StoreResource

        return StoreResource(self)

    @cached_property
    def users(self) -> UsersResource:
        """Operations about user"""
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def with_raw_response(self) -> DedalusWithRawResponse:
        return DedalusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DedalusWithStreamedResponse:
        return DedalusWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"api_key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncDedalus(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncDedalus client instance.

        This automatically infers the `api_key` argument from the `PETSTORE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PETSTORE_API_KEY")
        if api_key is None:
            raise DedalusError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PETSTORE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("DEDALUS_BASE_URL")
        if base_url is None:
            base_url = f"https://petstore3.swagger.io/api/v3"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def pets(self) -> AsyncPetsResource:
        """Everything about your Pets"""
        from .resources.pets import AsyncPetsResource

        return AsyncPetsResource(self)

    @cached_property
    def store(self) -> AsyncStoreResource:
        """Access to Petstore orders"""
        from .resources.store import AsyncStoreResource

        return AsyncStoreResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """Operations about user"""
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncDedalusWithRawResponse:
        return AsyncDedalusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDedalusWithStreamedResponse:
        return AsyncDedalusWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"api_key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class DedalusWithRawResponse:
    _client: Dedalus

    def __init__(self, client: Dedalus) -> None:
        self._client = client

    @cached_property
    def pets(self) -> pets.PetsResourceWithRawResponse:
        """Everything about your Pets"""
        from .resources.pets import PetsResourceWithRawResponse

        return PetsResourceWithRawResponse(self._client.pets)

    @cached_property
    def store(self) -> store.StoreResourceWithRawResponse:
        """Access to Petstore orders"""
        from .resources.store import StoreResourceWithRawResponse

        return StoreResourceWithRawResponse(self._client.store)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """Operations about user"""
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)


class AsyncDedalusWithRawResponse:
    _client: AsyncDedalus

    def __init__(self, client: AsyncDedalus) -> None:
        self._client = client

    @cached_property
    def pets(self) -> pets.AsyncPetsResourceWithRawResponse:
        """Everything about your Pets"""
        from .resources.pets import AsyncPetsResourceWithRawResponse

        return AsyncPetsResourceWithRawResponse(self._client.pets)

    @cached_property
    def store(self) -> store.AsyncStoreResourceWithRawResponse:
        """Access to Petstore orders"""
        from .resources.store import AsyncStoreResourceWithRawResponse

        return AsyncStoreResourceWithRawResponse(self._client.store)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """Operations about user"""
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)


class DedalusWithStreamedResponse:
    _client: Dedalus

    def __init__(self, client: Dedalus) -> None:
        self._client = client

    @cached_property
    def pets(self) -> pets.PetsResourceWithStreamingResponse:
        """Everything about your Pets"""
        from .resources.pets import PetsResourceWithStreamingResponse

        return PetsResourceWithStreamingResponse(self._client.pets)

    @cached_property
    def store(self) -> store.StoreResourceWithStreamingResponse:
        """Access to Petstore orders"""
        from .resources.store import StoreResourceWithStreamingResponse

        return StoreResourceWithStreamingResponse(self._client.store)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """Operations about user"""
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)


class AsyncDedalusWithStreamedResponse:
    _client: AsyncDedalus

    def __init__(self, client: AsyncDedalus) -> None:
        self._client = client

    @cached_property
    def pets(self) -> pets.AsyncPetsResourceWithStreamingResponse:
        """Everything about your Pets"""
        from .resources.pets import AsyncPetsResourceWithStreamingResponse

        return AsyncPetsResourceWithStreamingResponse(self._client.pets)

    @cached_property
    def store(self) -> store.AsyncStoreResourceWithStreamingResponse:
        """Access to Petstore orders"""
        from .resources.store import AsyncStoreResourceWithStreamingResponse

        return AsyncStoreResourceWithStreamingResponse(self._client.store)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """Operations about user"""
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)


Client = Dedalus

AsyncClient = AsyncDedalus
