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
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import machines
    from .resources.machines.machines import MachinesResource, AsyncMachinesResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Dedalus", "AsyncDedalus", "Client", "AsyncClient"]


class Dedalus(SyncAPIClient):
    # client options
    api_key: str | None
    x_api_key: str | None
    dedalus_org_id: str | None

    websocket_base_url: str | httpx.URL | None
    """Base URL for WebSocket connections.

    If not specified, the default base URL will be used, with 'wss://' replacing the
    'http://' or 'https://' scheme. For example: 'http://example.com' becomes
    'wss://example.com'
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        x_api_key: str | None = None,
        dedalus_org_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        websocket_base_url: str | httpx.URL | None = None,
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `DEDALUS_API_KEY`
        - `x_api_key` from `DEDALUS_X_API_KEY`
        - `dedalus_org_id` from `DEDALUS_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("DEDALUS_API_KEY")
        self.api_key = api_key

        if x_api_key is None:
            x_api_key = os.environ.get("DEDALUS_X_API_KEY")
        self.x_api_key = x_api_key

        if dedalus_org_id is None:
            dedalus_org_id = os.environ.get("DEDALUS_ORG_ID")
        self.dedalus_org_id = dedalus_org_id

        self.websocket_base_url = websocket_base_url

        if base_url is None:
            base_url = os.environ.get("DEDALUS_BASE_URL")
        if base_url is None:
            base_url = f"https://dcs.dedaluslabs.ai"

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

        self._idempotency_header = "Idempotency-Key"

        self._default_stream_cls = Stream

    @cached_property
    def machines(self) -> MachinesResource:
        from .resources.machines import MachinesResource

        return MachinesResource(self)

    @cached_property
    def with_raw_response(self) -> DedalusWithRawResponse:
        return DedalusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DedalusWithStreamedResponse:
        return DedalusWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key_auth if security.get("api_key_auth", False) else {}),
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _api_key_auth(self) -> dict[str, str]:
        x_api_key = self.x_api_key
        if x_api_key is None:
            return {}
        return {"x-api-key": x_api_key}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Dedalus-Org-Id": self.dedalus_org_id if self.dedalus_org_id is not None else Omit(),
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("x-api-key") or isinstance(custom_headers.get("x-api-key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either x_api_key or api_key to be set. Or for one of the `x-api-key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        x_api_key: str | None = None,
        dedalus_org_id: str | None = None,
        websocket_base_url: str | httpx.URL | None = None,
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
            x_api_key=x_api_key or self.x_api_key,
            dedalus_org_id=dedalus_org_id or self.dedalus_org_id,
            websocket_base_url=websocket_base_url or self.websocket_base_url,
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
    api_key: str | None
    x_api_key: str | None
    dedalus_org_id: str | None

    websocket_base_url: str | httpx.URL | None
    """Base URL for WebSocket connections.

    If not specified, the default base URL will be used, with 'wss://' replacing the
    'http://' or 'https://' scheme. For example: 'http://example.com' becomes
    'wss://example.com'
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        x_api_key: str | None = None,
        dedalus_org_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        websocket_base_url: str | httpx.URL | None = None,
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `DEDALUS_API_KEY`
        - `x_api_key` from `DEDALUS_X_API_KEY`
        - `dedalus_org_id` from `DEDALUS_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("DEDALUS_API_KEY")
        self.api_key = api_key

        if x_api_key is None:
            x_api_key = os.environ.get("DEDALUS_X_API_KEY")
        self.x_api_key = x_api_key

        if dedalus_org_id is None:
            dedalus_org_id = os.environ.get("DEDALUS_ORG_ID")
        self.dedalus_org_id = dedalus_org_id

        self.websocket_base_url = websocket_base_url

        if base_url is None:
            base_url = os.environ.get("DEDALUS_BASE_URL")
        if base_url is None:
            base_url = f"https://dcs.dedaluslabs.ai"

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

        self._idempotency_header = "Idempotency-Key"

        self._default_stream_cls = AsyncStream

    @cached_property
    def machines(self) -> AsyncMachinesResource:
        from .resources.machines import AsyncMachinesResource

        return AsyncMachinesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncDedalusWithRawResponse:
        return AsyncDedalusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDedalusWithStreamedResponse:
        return AsyncDedalusWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key_auth if security.get("api_key_auth", False) else {}),
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _api_key_auth(self) -> dict[str, str]:
        x_api_key = self.x_api_key
        if x_api_key is None:
            return {}
        return {"x-api-key": x_api_key}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Dedalus-Org-Id": self.dedalus_org_id if self.dedalus_org_id is not None else Omit(),
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("x-api-key") or isinstance(custom_headers.get("x-api-key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either x_api_key or api_key to be set. Or for one of the `x-api-key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        x_api_key: str | None = None,
        dedalus_org_id: str | None = None,
        websocket_base_url: str | httpx.URL | None = None,
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
            x_api_key=x_api_key or self.x_api_key,
            dedalus_org_id=dedalus_org_id or self.dedalus_org_id,
            websocket_base_url=websocket_base_url or self.websocket_base_url,
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
    def machines(self) -> machines.MachinesResourceWithRawResponse:
        from .resources.machines import MachinesResourceWithRawResponse

        return MachinesResourceWithRawResponse(self._client.machines)


class AsyncDedalusWithRawResponse:
    _client: AsyncDedalus

    def __init__(self, client: AsyncDedalus) -> None:
        self._client = client

    @cached_property
    def machines(self) -> machines.AsyncMachinesResourceWithRawResponse:
        from .resources.machines import AsyncMachinesResourceWithRawResponse

        return AsyncMachinesResourceWithRawResponse(self._client.machines)


class DedalusWithStreamedResponse:
    _client: Dedalus

    def __init__(self, client: Dedalus) -> None:
        self._client = client

    @cached_property
    def machines(self) -> machines.MachinesResourceWithStreamingResponse:
        from .resources.machines import MachinesResourceWithStreamingResponse

        return MachinesResourceWithStreamingResponse(self._client.machines)


class AsyncDedalusWithStreamedResponse:
    _client: AsyncDedalus

    def __init__(self, client: AsyncDedalus) -> None:
        self._client = client

    @cached_property
    def machines(self) -> machines.AsyncMachinesResourceWithStreamingResponse:
        from .resources.machines import AsyncMachinesResourceWithStreamingResponse

        return AsyncMachinesResourceWithStreamingResponse(self._client.machines)


Client = Dedalus

AsyncClient = AsyncDedalus
