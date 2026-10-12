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
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.creative_commons_connection import CreativeCommonsConnection
from ..server.server import Server


class VideosCreativeCommons:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosCreativeCommonsWithRawResponse(client, server, auth)

    def get_cc_licenses(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreativeCommonsConnection:
        """This method returns all available Creative Commons licenses.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The Creative Commons licenses were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_cc_licenses(page=page, per_page=per_page, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> VideosCreativeCommonsWithRawResponse:
        return self._with_raw_response


class AsyncVideosCreativeCommons:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosCreativeCommonsWithRawResponse(client, server, auth)

    async def get_cc_licenses(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreativeCommonsConnection:
        """This method returns all available Creative Commons licenses.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The Creative Commons licenses were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_cc_licenses(page=page, per_page=per_page, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncVideosCreativeCommonsWithRawResponse:
        return self._with_raw_response


class VideosCreativeCommonsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_cc_licenses(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreativeCommonsConnection, RawError]:
        """This method returns all available Creative Commons licenses.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/creativecommons"),
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CreativeCommonsConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideosCreativeCommonsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_cc_licenses(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreativeCommonsConnection, RawError]:
        """This method returns all available Creative Commons licenses.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/creativecommons"),
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[CreativeCommonsConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
