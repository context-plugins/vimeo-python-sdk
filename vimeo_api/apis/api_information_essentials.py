from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    empty_response,
    raw_error_response,
    unwrap,
)
from ..server.server import Server


class ApiInformationEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApiInformationEssentialsWithRawResponse(client, server, auth)

    def get_endpoints(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns the full OpenAPI specification for the Vimeo API.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The OpenAPI specification was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_endpoints(request_options=request_options))

    @property
    def with_raw_response(self) -> ApiInformationEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncApiInformationEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApiInformationEssentialsWithRawResponse(client, server, auth)

    async def get_endpoints(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns the full OpenAPI specification for the Vimeo API.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The OpenAPI specification was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_endpoints(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncApiInformationEssentialsWithRawResponse:
        return self._with_raw_response


class ApiInformationEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_endpoints(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]:
        """This method returns the full OpenAPI specification for the Vimeo API.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApiInformationEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_endpoints(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]:
        """This method returns the full OpenAPI specification for the Vimeo API.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
