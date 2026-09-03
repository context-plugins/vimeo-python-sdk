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
    json_decoder,
    raw_error_response,
)
from ..models.content_rating_connection import ContentRatingConnection
from ..server.server import Server


class VideosContentRatings:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosContentRatingsWithRawResponse(client, server, auth)

    def get_content_ratings(self, *, request_options: RequestOptionsOrDict | None = None) -> ContentRatingConnection:
        """This method returns all available content ratings.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The content ratings were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_content_ratings(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VideosContentRatingsWithRawResponse:
        return self._with_raw_response


class AsyncVideosContentRatings:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosContentRatingsWithRawResponse(client, server, auth)

    async def get_content_ratings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ContentRatingConnection:
        """This method returns all available content ratings.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The content ratings were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_content_ratings(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosContentRatingsWithRawResponse:
        return self._with_raw_response


class VideosContentRatingsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_content_ratings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContentRatingConnection, RawError]:
        """This method returns all available content ratings.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/contentratings"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ContentRatingConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideosContentRatingsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_content_ratings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ContentRatingConnection, RawError]:
        """This method returns all available content ratings.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/contentratings"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ContentRatingConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
