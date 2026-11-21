# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.machines.ports.access_key_list_response import AccessKeyListResponse
from ....types.machines.ports import access_key_list_params, access_key_mint_params, access_key_rotate_params
from ....types.machines.ports.access_key_mint_response import AccessKeyMintResponse
from ....types.machines.ports.access_key_revoke_response import AccessKeyRevokeResponse
from ....types.machines.ports.access_key_rotate_response import AccessKeyRotateResponse

__all__ = ["AccessKeysResource", "AsyncAccessKeysResource"]


class AccessKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessKeysResourceWithRawResponse:
        return AccessKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessKeysResourceWithStreamingResponse:
        return AccessKeysResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        machine_id: str,
        port_id: str,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessKeyListResponse:
        """
        List port access keys

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessKeyListResponse: OK

        Example:
            ```python
            access_key = client.machines.ports.access_keys.list(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}/access-keys",
                **{"machine_id": machine_id, "port_id": port_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, access_key_list_params.AccessKeyListParams),
            ),
            cast_to=AccessKeyListResponse,
        )

    def mint(
        self,
        *,
        machine_id: str,
        port_id: str,
        expires_in: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AccessKeyMintResponse:
        """
        Mint port access key

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            expires_in: Lifetime in integer seconds.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            AccessKeyMintResponse: OK

        Example:
            ```python
            access_key = client.machines.ports.access_keys.mint(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                expires_in=1,
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._post(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}/access-keys",
                **{"machine_id": machine_id, "port_id": port_id},
            ),
            body=maybe_transform(
                {"expires_in": expires_in},
                access_key_mint_params.AccessKeyMintParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccessKeyMintResponse,
        )

    def revoke(
        self,
        *,
        machine_id: str,
        port_id: str,
        access_key_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AccessKeyRevokeResponse:
        """
        Revoke port access key

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            access_key_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            AccessKeyRevokeResponse: OK

        Example:
            ```python
            access_key = client.machines.ports.access_keys.revoke(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                access_key_id="accessKeyID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        if access_key_id is None or (isinstance(access_key_id, str) and not access_key_id):
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        return self._delete(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}/access-keys/{access_key_id}",
                **{"machine_id": machine_id, "port_id": port_id, "access_key_id": access_key_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccessKeyRevokeResponse,
        )

    def rotate(
        self,
        *,
        machine_id: str,
        port_id: str,
        access_key_id: str,
        expires_in: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AccessKeyRotateResponse:
        """
        Rotate port access key

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            access_key_id: Path parameter.
            expires_in: Lifetime in integer seconds.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            AccessKeyRotateResponse: OK

        Example:
            ```python
            access_key = client.machines.ports.access_keys.rotate(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                access_key_id="accessKeyID",
                expires_in=1,
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        if access_key_id is None or (isinstance(access_key_id, str) and not access_key_id):
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        return self._post(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}/access-keys/{access_key_id}/rotate",
                **{"machine_id": machine_id, "port_id": port_id, "access_key_id": access_key_id},
            ),
            body=maybe_transform(
                {"expires_in": expires_in},
                access_key_rotate_params.AccessKeyRotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccessKeyRotateResponse,
        )


class AsyncAccessKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessKeysResourceWithRawResponse:
        return AsyncAccessKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessKeysResourceWithStreamingResponse:
        return AsyncAccessKeysResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        machine_id: str,
        port_id: str,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessKeyListResponse:
        """
        List port access keys

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessKeyListResponse: OK

        Example:
            ```python
            access_key = await client.machines.ports.access_keys.list(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}/access-keys",
                **{"machine_id": machine_id, "port_id": port_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor}, access_key_list_params.AccessKeyListParams
                ),
            ),
            cast_to=AccessKeyListResponse,
        )

    async def mint(
        self,
        *,
        machine_id: str,
        port_id: str,
        expires_in: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AccessKeyMintResponse:
        """
        Mint port access key

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            expires_in: Lifetime in integer seconds.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            AccessKeyMintResponse: OK

        Example:
            ```python
            access_key = await client.machines.ports.access_keys.mint(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                expires_in=1,
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._post(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}/access-keys",
                **{"machine_id": machine_id, "port_id": port_id},
            ),
            body=await async_maybe_transform(
                {"expires_in": expires_in},
                access_key_mint_params.AccessKeyMintParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccessKeyMintResponse,
        )

    async def revoke(
        self,
        *,
        machine_id: str,
        port_id: str,
        access_key_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AccessKeyRevokeResponse:
        """
        Revoke port access key

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            access_key_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            AccessKeyRevokeResponse: OK

        Example:
            ```python
            access_key = await client.machines.ports.access_keys.revoke(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                access_key_id="accessKeyID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        if access_key_id is None or (isinstance(access_key_id, str) and not access_key_id):
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        return await self._delete(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}/access-keys/{access_key_id}",
                **{"machine_id": machine_id, "port_id": port_id, "access_key_id": access_key_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccessKeyRevokeResponse,
        )

    async def rotate(
        self,
        *,
        machine_id: str,
        port_id: str,
        access_key_id: str,
        expires_in: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AccessKeyRotateResponse:
        """
        Rotate port access key

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            access_key_id: Path parameter.
            expires_in: Lifetime in integer seconds.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            AccessKeyRotateResponse: OK

        Example:
            ```python
            access_key = await client.machines.ports.access_keys.rotate(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                access_key_id="accessKeyID",
                expires_in=1,
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        if access_key_id is None or (isinstance(access_key_id, str) and not access_key_id):
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        return await self._post(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}/access-keys/{access_key_id}/rotate",
                **{"machine_id": machine_id, "port_id": port_id, "access_key_id": access_key_id},
            ),
            body=await async_maybe_transform(
                {"expires_in": expires_in},
                access_key_rotate_params.AccessKeyRotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccessKeyRotateResponse,
        )


class AccessKeysResourceWithRawResponse:
    def __init__(self, access_keys: AccessKeysResource) -> None:
        self._access_keys = access_keys

        self.list = to_raw_response_wrapper(
            access_keys.list,
        )
        self.mint = to_raw_response_wrapper(
            access_keys.mint,
        )
        self.revoke = to_raw_response_wrapper(
            access_keys.revoke,
        )
        self.rotate = to_raw_response_wrapper(
            access_keys.rotate,
        )


class AsyncAccessKeysResourceWithRawResponse:
    def __init__(self, access_keys: AsyncAccessKeysResource) -> None:
        self._access_keys = access_keys

        self.list = async_to_raw_response_wrapper(
            access_keys.list,
        )
        self.mint = async_to_raw_response_wrapper(
            access_keys.mint,
        )
        self.revoke = async_to_raw_response_wrapper(
            access_keys.revoke,
        )
        self.rotate = async_to_raw_response_wrapper(
            access_keys.rotate,
        )


class AccessKeysResourceWithStreamingResponse:
    def __init__(self, access_keys: AccessKeysResource) -> None:
        self._access_keys = access_keys

        self.list = to_streamed_response_wrapper(
            access_keys.list,
        )
        self.mint = to_streamed_response_wrapper(
            access_keys.mint,
        )
        self.revoke = to_streamed_response_wrapper(
            access_keys.revoke,
        )
        self.rotate = to_streamed_response_wrapper(
            access_keys.rotate,
        )


class AsyncAccessKeysResourceWithStreamingResponse:
    def __init__(self, access_keys: AsyncAccessKeysResource) -> None:
        self._access_keys = access_keys

        self.list = async_to_streamed_response_wrapper(
            access_keys.list,
        )
        self.mint = async_to_streamed_response_wrapper(
            access_keys.mint,
        )
        self.revoke = async_to_streamed_response_wrapper(
            access_keys.revoke,
        )
        self.rotate = async_to_streamed_response_wrapper(
            access_keys.rotate,
        )
