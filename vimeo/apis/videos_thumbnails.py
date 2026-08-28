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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.channels_videos_pictures_request import ChannelsVideosPicturesRequest, ChannelsVideosPicturesRequestDict
from ..models.picture import Picture
from ..models.picture_connection import PictureConnection
from ..models.videos_pictures_request import VideosPicturesRequest, VideosPicturesRequestDict
from ..models.videos_pictures_request1 import VideosPicturesRequest1, VideosPicturesRequest1Dict
from ..server.server import Server


class VideosThumbnails:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosThumbnailsWithRawResponse(client, server, auth)

    def create_video_thumbnail(
        self,
        video_id: float,
        *,
        body: VideosPicturesRequest | VideosPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method adds a thumbnail image to the specified video. The authenticated user must have team permissions
        for the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail image was added to the video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_video_thumbnail(
            video_id, body=body, request_options=request_options
        ).unwrap()

    def create_video_thumbnail_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        body: ChannelsVideosPicturesRequest | ChannelsVideosPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method adds a thumbnail image to the specified video. The authenticated user must have team permissions
        for the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail image was added to the video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_video_thumbnail_alt1(
            channel_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def delete_video_thumbnail(
        self, picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified thumbnail image from a video. The authenticated user must have team
        permissions for the video.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail was deleted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_video_thumbnail(
            picture_id, video_id, request_options=request_options
        ).unwrap()

    def edit_video_thumbnail(
        self,
        picture_id: float,
        video_id: float,
        *,
        body: VideosPicturesRequest1 | VideosPicturesRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits the specified video thumbnail image. The authenticated user must be the owner of the
        thumbnail.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail was edited.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.edit_video_thumbnail(
            picture_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def get_video_thumbnail(
        self, picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single thumbnail image from the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_thumbnail(
            picture_id, video_id, request_options=request_options
        ).unwrap()

    def get_video_thumbnails(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns all thumbnail images of the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_thumbnails(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_video_thumbnails_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns all thumbnail images of the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_thumbnails_alt1(
            channel_id, video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosThumbnailsWithRawResponse:
        return self._with_raw_response


class AsyncVideosThumbnails:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosThumbnailsWithRawResponse(client, server, auth)

    async def create_video_thumbnail(
        self,
        video_id: float,
        *,
        body: VideosPicturesRequest | VideosPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method adds a thumbnail image to the specified video. The authenticated user must have team permissions
        for the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail image was added to the video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_video_thumbnail(video_id, body=body, request_options=request_options)
        ).unwrap()

    async def create_video_thumbnail_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        body: ChannelsVideosPicturesRequest | ChannelsVideosPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method adds a thumbnail image to the specified video. The authenticated user must have team permissions
        for the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail image was added to the video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_video_thumbnail_alt1(
                channel_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def delete_video_thumbnail(
        self, picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified thumbnail image from a video. The authenticated user must have team
        permissions for the video.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail was deleted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_video_thumbnail(picture_id, video_id, request_options=request_options)
        ).unwrap()

    async def edit_video_thumbnail(
        self,
        picture_id: float,
        video_id: float,
        *,
        body: VideosPicturesRequest1 | VideosPicturesRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits the specified video thumbnail image. The authenticated user must be the owner of the
        thumbnail.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail was edited.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.edit_video_thumbnail(
                picture_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_video_thumbnail(
        self, picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single thumbnail image from the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnail was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_thumbnail(picture_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_video_thumbnails(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns all thumbnail images of the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_thumbnails(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_video_thumbnails_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns all thumbnail images of the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The thumbnails were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_thumbnails_alt1(
                channel_id, video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosThumbnailsWithRawResponse:
        return self._with_raw_response


class VideosThumbnailsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_video_thumbnail(
        self,
        video_id: float,
        *,
        body: VideosPicturesRequest | VideosPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method adds a thumbnail image to the specified video. The authenticated user must have team permissions
        for the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/pictures"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosPicturesRequest | VideosPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_video_thumbnail_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        body: ChannelsVideosPicturesRequest | ChannelsVideosPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method adds a thumbnail image to the specified video. The authenticated user must have team permissions
        for the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/pictures"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            body=json_body[ChannelsVideosPicturesRequest | ChannelsVideosPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_video_thumbnail(
        self, picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method deletes the specified thumbnail image from a video. The authenticated user must have team
        permissions for the video.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/pictures/{picture_id}"),
            path_params=[param[float]("picture_id", picture_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def edit_video_thumbnail(
        self,
        picture_id: float,
        video_id: float,
        *,
        body: VideosPicturesRequest1 | VideosPicturesRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method edits the specified video thumbnail image. The authenticated user must be the owner of the
        thumbnail.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/pictures/{picture_id}"),
            path_params=[param[float]("picture_id", picture_id), param[float]("video_id", video_id)],
            body=json_body[VideosPicturesRequest1 | VideosPicturesRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_video_thumbnail(
        self, picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns a single thumbnail image from the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/pictures/{picture_id}"),
            path_params=[param[float]("picture_id", picture_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_video_thumbnails(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, RawError]:
        """This method returns all thumbnail images of the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/pictures"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_video_thumbnails_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, RawError]:
        """This method returns all thumbnail images of the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/pictures"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideosThumbnailsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_video_thumbnail(
        self,
        video_id: float,
        *,
        body: VideosPicturesRequest | VideosPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method adds a thumbnail image to the specified video. The authenticated user must have team permissions
        for the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/pictures"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosPicturesRequest | VideosPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_video_thumbnail_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        body: ChannelsVideosPicturesRequest | ChannelsVideosPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method adds a thumbnail image to the specified video. The authenticated user must have team permissions
        for the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/pictures"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            body=json_body[ChannelsVideosPicturesRequest | ChannelsVideosPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_video_thumbnail(
        self, picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method deletes the specified thumbnail image from a video. The authenticated user must have team
        permissions for the video.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/pictures/{picture_id}"),
            path_params=[param[float]("picture_id", picture_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def edit_video_thumbnail(
        self,
        picture_id: float,
        video_id: float,
        *,
        body: VideosPicturesRequest1 | VideosPicturesRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method edits the specified video thumbnail image. The authenticated user must be the owner of the
        thumbnail.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/pictures/{picture_id}"),
            path_params=[param[float]("picture_id", picture_id), param[float]("video_id", video_id)],
            body=json_body[VideosPicturesRequest1 | VideosPicturesRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_video_thumbnail(
        self, picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns a single thumbnail image from the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            picture_id: The ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/pictures/{picture_id}"),
            path_params=[param[float]("picture_id", picture_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_video_thumbnails(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, RawError]:
        """This method returns all thumbnail images of the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/pictures"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_video_thumbnails_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, RawError]:
        """This method returns all thumbnail images of the specified video. The authenticated user must have team
        permissions for the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/pictures"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
