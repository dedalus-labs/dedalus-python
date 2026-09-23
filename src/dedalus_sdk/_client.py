# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
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
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import machines, organization
    from .resources.machines import MachinesResource, AsyncMachinesResource
    from .resources.organization import OrganizationResource, AsyncOrganizationResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

__all__ = ["Dedalus", "AsyncDedalus", "Client", "AsyncClient", "Timeout", "Transport", "ProxiesTypes", "RequestOptions"]


class Dedalus(SyncAPIClient):
    # client options
    api_key: str | None
    x_api_key: str | None
    as_base_url: str | None
    dedalus_org_id: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        x_api_key: str | None = None,
        as_base_url: str | None = None,
        dedalus_org_id: str | None = None,
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `DEDALUS_API_KEY`
        - `x_api_key` from `DEDALUS_X_API_KEY`
        - `as_base_url` from `DEDALUS_AS_URL`
        - `dedalus_org_id` from `DEDALUS_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("DEDALUS_API_KEY")
        self.api_key = api_key
        if x_api_key is None:
            x_api_key = os.environ.get("DEDALUS_X_API_KEY")
        self.x_api_key = x_api_key
        if as_base_url is None:
            as_base_url = os.environ.get("DEDALUS_AS_URL", "").strip() or None
        if as_base_url is None:
            as_base_url = "https://as.dedaluslabs.ai"
        self.as_base_url = as_base_url
        if dedalus_org_id is None:
            dedalus_org_id = os.environ.get("DEDALUS_ORG_ID")
        self.dedalus_org_id = dedalus_org_id
        if base_url is None:
            base_url = os.environ.get("DEDALUS_BASE_URL")
        if base_url is None:
            base_url = "https://dcs.dedaluslabs.ai"
        custom_headers_env = os.environ.get("DEDALUS_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
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
    def machines(self) -> "MachinesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.machines import MachinesResource
        return MachinesResource(self)

    @cached_property
    def organization(self) -> "OrganizationResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization import OrganizationResource
        return OrganizationResource(self)

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
        return {
            **self._api_key_header_auth,
            **self._x_api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _x_api_key_header_auth(self) -> dict[str, str]:
        value = self.x_api_key
        if value is None:
            return {}
        return {"x-api-key": value}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            "User-Agent": "Dedalus-SDK",
            "X-SDK-Version": "1.0.0",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        if headers.get("x-api-key"):
            return
        if isinstance(custom_headers.get("x-api-key"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or x_api_key to be set. Or for one of the `Authorization` or `x-api-key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        x_api_key: str | None = None,
        as_base_url: str | None = None,
        dedalus_org_id: str | None = None,
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
        """Create a new client reusing this client's options with optional overrides."""
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
            as_base_url=as_base_url or self.as_base_url,
            dedalus_org_id=dedalus_org_id or self.dedalus_org_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
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
    as_base_url: str | None
    dedalus_org_id: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        x_api_key: str | None = None,
        as_base_url: str | None = None,
        dedalus_org_id: str | None = None,
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `DEDALUS_API_KEY`
        - `x_api_key` from `DEDALUS_X_API_KEY`
        - `as_base_url` from `DEDALUS_AS_URL`
        - `dedalus_org_id` from `DEDALUS_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("DEDALUS_API_KEY")
        self.api_key = api_key
        if x_api_key is None:
            x_api_key = os.environ.get("DEDALUS_X_API_KEY")
        self.x_api_key = x_api_key
        if as_base_url is None:
            as_base_url = os.environ.get("DEDALUS_AS_URL", "").strip() or None
        if as_base_url is None:
            as_base_url = "https://as.dedaluslabs.ai"
        self.as_base_url = as_base_url
        if dedalus_org_id is None:
            dedalus_org_id = os.environ.get("DEDALUS_ORG_ID")
        self.dedalus_org_id = dedalus_org_id
        if base_url is None:
            base_url = os.environ.get("DEDALUS_BASE_URL")
        if base_url is None:
            base_url = "https://dcs.dedaluslabs.ai"
        custom_headers_env = os.environ.get("DEDALUS_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
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
    def machines(self) -> "AsyncMachinesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.machines import AsyncMachinesResource
        return AsyncMachinesResource(self)

    @cached_property
    def organization(self) -> "AsyncOrganizationResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization import AsyncOrganizationResource
        return AsyncOrganizationResource(self)

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
        return {
            **self._api_key_header_auth,
            **self._x_api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _x_api_key_header_auth(self) -> dict[str, str]:
        value = self.x_api_key
        if value is None:
            return {}
        return {"x-api-key": value}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            "User-Agent": "Dedalus-SDK",
            "X-SDK-Version": "1.0.0",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        if headers.get("x-api-key"):
            return
        if isinstance(custom_headers.get("x-api-key"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or x_api_key to be set. Or for one of the `Authorization` or `x-api-key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        x_api_key: str | None = None,
        as_base_url: str | None = None,
        dedalus_org_id: str | None = None,
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
        """Create a new client reusing this client's options with optional overrides."""
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
            as_base_url=as_base_url or self.as_base_url,
            dedalus_org_id=dedalus_org_id or self.dedalus_org_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
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
        with _RESOURCE_IMPORT_LOCK:
            from .resources.machines import MachinesResourceWithRawResponse
        return MachinesResourceWithRawResponse(self._client.machines)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization import OrganizationResourceWithRawResponse
        return OrganizationResourceWithRawResponse(self._client.organization)


class AsyncDedalusWithRawResponse:
    _client: AsyncDedalus

    def __init__(self, client: AsyncDedalus) -> None:
        self._client = client

    @cached_property
    def machines(self) -> machines.AsyncMachinesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.machines import AsyncMachinesResourceWithRawResponse
        return AsyncMachinesResourceWithRawResponse(self._client.machines)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization import AsyncOrganizationResourceWithRawResponse
        return AsyncOrganizationResourceWithRawResponse(self._client.organization)


class DedalusWithStreamedResponse:
    _client: Dedalus

    def __init__(self, client: Dedalus) -> None:
        self._client = client

    @cached_property
    def machines(self) -> machines.MachinesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.machines import MachinesResourceWithStreamingResponse
        return MachinesResourceWithStreamingResponse(self._client.machines)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization import OrganizationResourceWithStreamingResponse
        return OrganizationResourceWithStreamingResponse(self._client.organization)


class AsyncDedalusWithStreamedResponse:
    _client: AsyncDedalus

    def __init__(self, client: AsyncDedalus) -> None:
        self._client = client

    @cached_property
    def machines(self) -> machines.AsyncMachinesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.machines import AsyncMachinesResourceWithStreamingResponse
        return AsyncMachinesResourceWithStreamingResponse(self._client.machines)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization import AsyncOrganizationResourceWithStreamingResponse
        return AsyncOrganizationResourceWithStreamingResponse(self._client.organization)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = Dedalus
AsyncClient = AsyncDedalus
