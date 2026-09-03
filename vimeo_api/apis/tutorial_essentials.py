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
    empty_response,
    raw_error_response,
)
from ..server.server import Server


class TutorialEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TutorialEssentialsWithRawResponse(client, server, auth)

    def developer_tutorial(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method tests whether users who are working through the `Getting Started
        <https://developer.vimeo.com/api/guides/start>`__ guides have set up their configurations correctly.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.developer_tutorial(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TutorialEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncTutorialEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTutorialEssentialsWithRawResponse(client, server, auth)

    async def developer_tutorial(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method tests whether users who are working through the `Getting Started
        <https://developer.vimeo.com/api/guides/start>`__ guides have set up their configurations correctly.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.developer_tutorial(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTutorialEssentialsWithRawResponse:
        return self._with_raw_response


class TutorialEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def developer_tutorial(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]:
        """This method tests whether users who are working through the `Getting Started
        <https://developer.vimeo.com/api/guides/start>`__ guides have set up their configurations correctly.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tutorial"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTutorialEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def developer_tutorial(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method tests whether users who are working through the `Getting Started
        <https://developer.vimeo.com/api/guides/start>`__ guides have set up their configurations correctly.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tutorial"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
