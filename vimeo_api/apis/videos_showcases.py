from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.add_or_remove_multiple_albums_error import (
    AddOrRemoveMultipleAlbumsErrorBody,
    add_or_remove_multiple_albums_error_mapper,
)
from ..errors.get_video_albums_error import GetVideoAlbumsErrorBody, get_video_albums_error_mapper
from ..models.album import Album
from ..models.album_connection import AlbumConnection
from ..models.videos_albums_request import VideosAlbumsRequest, VideosAlbumsRequestDict
from ..server.server import Server


class VideosShowcases:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosShowcasesWithRawResponse(client, server, auth)

    def add_or_remove_multiple_albums(
        self,
        video_id: float,
        *,
        body: VideosAlbumsRequest | VideosAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Album]:
        """This method adds or removes the specified video to or from multiple showcases.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added or removed.

        Raises:
            ApiError: Error code 3433: No such video exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_or_remove_multiple_albums(
            video_id, body=body, request_options=request_options
        ).unwrap()

    def get_video_albums(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlbumConnection:
        """This method returns all the showcases that contain the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcases were returned.

        Raises:
            ApiError: * Error code 3433: No such video exists. * Error code 5451: This resource is restricted in your
                region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_video_albums(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosShowcasesWithRawResponse:
        return self._with_raw_response


class AsyncVideosShowcases:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosShowcasesWithRawResponse(client, server, auth)

    async def add_or_remove_multiple_albums(
        self,
        video_id: float,
        *,
        body: VideosAlbumsRequest | VideosAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Album]:
        """This method adds or removes the specified video to or from multiple showcases.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added or removed.

        Raises:
            ApiError: Error code 3433: No such video exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_or_remove_multiple_albums(
                video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_video_albums(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlbumConnection:
        """This method returns all the showcases that contain the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcases were returned.

        Raises:
            ApiError: * Error code 3433: No such video exists. * Error code 5451: This resource is restricted in your
                region. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_video_albums(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosShowcasesWithRawResponse:
        return self._with_raw_response


class VideosShowcasesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_or_remove_multiple_albums(
        self,
        video_id: float,
        *,
        body: VideosAlbumsRequest | VideosAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Album], AddOrRemoveMultipleAlbumsErrorBody]:
        """This method adds or removes the specified video to or from multiple showcases.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/albums"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosAlbumsRequest | VideosAlbumsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[Album]],
            error_mapper=add_or_remove_multiple_albums_error_mapper,
            request_options=request_options,
        )

    def get_video_albums(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlbumConnection, GetVideoAlbumsErrorBody]:
        """This method returns all the showcases that contain the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/albums"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlbumConnection],
            error_mapper=get_video_albums_error_mapper,
            request_options=request_options,
        )


class AsyncVideosShowcasesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_or_remove_multiple_albums(
        self,
        video_id: float,
        *,
        body: VideosAlbumsRequest | VideosAlbumsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Album], AddOrRemoveMultipleAlbumsErrorBody]:
        """This method adds or removes the specified video to or from multiple showcases.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/albums"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosAlbumsRequest | VideosAlbumsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[Album]],
            error_mapper=add_or_remove_multiple_albums_error_mapper,
            request_options=request_options,
        )

    async def get_video_albums(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlbumConnection, GetVideoAlbumsErrorBody]:
        """This method returns all the showcases that contain the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/albums"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlbumConnection],
            error_mapper=get_video_albums_error_mapper,
            request_options=request_options,
        )
