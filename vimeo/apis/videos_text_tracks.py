from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_text_track_alt1_error import CreateTextTrackAlt1ErrorBody, create_text_track_alt1_error_mapper
from ..errors.create_text_track_error import CreateTextTrackErrorBody, create_text_track_error_mapper
from ..errors.delete_text_track_error import DeleteTextTrackErrorBody, delete_text_track_error_mapper
from ..errors.edit_text_track_error import EditTextTrackErrorBody, edit_text_track_error_mapper
from ..errors.get_text_track_error import GetTextTrackErrorBody, get_text_track_error_mapper
from ..errors.get_text_tracks_alt1_error import GetTextTracksAlt1ErrorBody, get_text_tracks_alt1_error_mapper
from ..errors.get_text_tracks_alt2_error import GetTextTracksAlt2ErrorBody, get_text_tracks_alt2_error_mapper
from ..errors.get_text_tracks_alt3_error import GetTextTracksAlt3ErrorBody, get_text_tracks_alt3_error_mapper
from ..errors.get_text_tracks_error import GetTextTracksErrorBody, get_text_tracks_error_mapper
from ..models.channels_videos_texttracks_request import (
    ChannelsVideosTexttracksRequest,
    ChannelsVideosTexttracksRequestDict,
)
from ..models.text_track import TextTrack
from ..models.text_track_connection import TextTrackConnection
from ..models.videos_texttracks_request import VideosTexttracksRequest, VideosTexttracksRequestDict
from ..models.videos_texttracks_request1 import VideosTexttracksRequest1, VideosTexttracksRequest1Dict
from ..server.server import Server


class VideosTextTracks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosTextTracksWithRawResponse(client, server, auth)

    def create_text_track(
        self,
        video_id: float,
        body: VideosTexttracksRequest | VideosTexttracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrack:
        """This method adds a text track to the specified video. For more information, see `Working with Text Track
        Uploads <https://developer.vimeo.com/api/upload/texttracks>`__.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was added.

        Raises:
            ApiError: * The authenticated user can't add the text track. * Error code 2204: The request contains errors.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_text_track(video_id, body, request_options=request_options).unwrap()

    def create_text_track_alt1(
        self,
        channel_id: float,
        video_id: float,
        body: ChannelsVideosTexttracksRequest | ChannelsVideosTexttracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrack:
        """This method adds a text track to the specified video. For more information, see `Working with Text Track
        Uploads <https://developer.vimeo.com/api/upload/texttracks>`__.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was added.

        Raises:
            ApiError: * The authenticated user can't add the text track. * Error code 2204: The request contains errors.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_text_track_alt1(
            channel_id, video_id, body, request_options=request_options
        ).unwrap()

    def delete_text_track(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified text track from a video. The authenticated user must be the owner of the
        video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was deleted.

        Raises:
            ApiError: * Error code 3430: The authenticated user doesn't have permission to access the text track. *
                Error code 3431: This text track is disabled. * No such video or text track exists. * The authenticated
                user can't delete the text track. * Error code 5014: The specified text track doesn't exist. * Error
                code 5015: The specified text track belongs to a different video. ``error`` is ``Error | LegacyError |
                RawError``."""
        return self._with_raw_response.delete_text_track(
            texttrack_id, video_id, request_options=request_options
        ).unwrap()

    def edit_text_track(
        self,
        texttrack_id: float,
        video_id: float,
        *,
        body: VideosTexttracksRequest1 | VideosTexttracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrack:
        """This method edits the specified text track of a video. The authenticated user must be the owner of the video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was edited.

        Raises:
            ApiError: * The authenticated user can't edit the text track. * Error code 2204: There are errors in the
                request. * Error code 3430: The authenticated user doesn't have permission to access the text track. *
                Error code 3431: This text track is disabled. * No such video or text track exists. * Error code 5014:
                The specified text track doesn't exist. * Error code 5015: The specified text track belongs to a
                different video. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.edit_text_track(
            texttrack_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def get_text_track(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> TextTrack:
        """This method returns a single text track of the specified video. The authenticated user must be the owner of
        the video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was returned.

        Raises:
            ApiError: * Error code 3430: The authenticated user doesn't have permission to access the text track. *
                Error code 3431: This text track is disabled. * No such video or text track exists. * Error code 5014:
                The specified text track doesn't exist. * Error code 5015: The specified text track belongs to a
                different video. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.get_text_track(texttrack_id, video_id, request_options=request_options).unwrap()

    def get_text_tracks(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrackConnection:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text tracks were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_text_tracks(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_text_tracks_alt1(
        self,
        video_id: float,
        version_id: str,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrackConnection:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            version_id: Value sent with the request.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text tracks were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_text_tracks_alt1(
            video_id, version_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_text_tracks_alt2(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrackConnection:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text tracks were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_text_tracks_alt2(
            channel_id, video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_text_tracks_alt3(
        self,
        album_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrackConnection:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text tracks were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_text_tracks_alt3(
            album_id, video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosTextTracksWithRawResponse:
        return self._with_raw_response


class AsyncVideosTextTracks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosTextTracksWithRawResponse(client, server, auth)

    async def create_text_track(
        self,
        video_id: float,
        body: VideosTexttracksRequest | VideosTexttracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrack:
        """This method adds a text track to the specified video. For more information, see `Working with Text Track
        Uploads <https://developer.vimeo.com/api/upload/texttracks>`__.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was added.

        Raises:
            ApiError: * The authenticated user can't add the text track. * Error code 2204: The request contains errors.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.create_text_track(video_id, body, request_options=request_options)
        ).unwrap()

    async def create_text_track_alt1(
        self,
        channel_id: float,
        video_id: float,
        body: ChannelsVideosTexttracksRequest | ChannelsVideosTexttracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrack:
        """This method adds a text track to the specified video. For more information, see `Working with Text Track
        Uploads <https://developer.vimeo.com/api/upload/texttracks>`__.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was added.

        Raises:
            ApiError: * The authenticated user can't add the text track. * Error code 2204: The request contains errors.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.create_text_track_alt1(
                channel_id, video_id, body, request_options=request_options
            )
        ).unwrap()

    async def delete_text_track(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified text track from a video. The authenticated user must be the owner of the
        video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was deleted.

        Raises:
            ApiError: * Error code 3430: The authenticated user doesn't have permission to access the text track. *
                Error code 3431: This text track is disabled. * No such video or text track exists. * The authenticated
                user can't delete the text track. * Error code 5014: The specified text track doesn't exist. * Error
                code 5015: The specified text track belongs to a different video. ``error`` is ``Error | LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.delete_text_track(texttrack_id, video_id, request_options=request_options)
        ).unwrap()

    async def edit_text_track(
        self,
        texttrack_id: float,
        video_id: float,
        *,
        body: VideosTexttracksRequest1 | VideosTexttracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrack:
        """This method edits the specified text track of a video. The authenticated user must be the owner of the video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was edited.

        Raises:
            ApiError: * The authenticated user can't edit the text track. * Error code 2204: There are errors in the
                request. * Error code 3430: The authenticated user doesn't have permission to access the text track. *
                Error code 3431: This text track is disabled. * No such video or text track exists. * Error code 5014:
                The specified text track doesn't exist. * Error code 5015: The specified text track belongs to a
                different video. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_text_track(
                texttrack_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_text_track(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> TextTrack:
        """This method returns a single text track of the specified video. The authenticated user must be the owner of
        the video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text track was returned.

        Raises:
            ApiError: * Error code 3430: The authenticated user doesn't have permission to access the text track. *
                Error code 3431: This text track is disabled. * No such video or text track exists. * Error code 5014:
                The specified text track doesn't exist. * Error code 5015: The specified text track belongs to a
                different video. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_text_track(texttrack_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_text_tracks(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrackConnection:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text tracks were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_text_tracks(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_text_tracks_alt1(
        self,
        video_id: float,
        version_id: str,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrackConnection:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            version_id: Value sent with the request.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text tracks were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_text_tracks_alt1(
                video_id, version_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_text_tracks_alt2(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrackConnection:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text tracks were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_text_tracks_alt2(
                channel_id, video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_text_tracks_alt3(
        self,
        album_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TextTrackConnection:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The text tracks were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_text_tracks_alt3(
                album_id, video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosTextTracksWithRawResponse:
        return self._with_raw_response


class VideosTextTracksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_text_track(
        self,
        video_id: float,
        body: VideosTexttracksRequest | VideosTexttracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrack, CreateTextTrackErrorBody]:
        """This method adds a text track to the specified video. For more information, see `Working with Text Track
        Uploads <https://developer.vimeo.com/api/upload/texttracks>`__.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/texttracks"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosTexttracksRequest | VideosTexttracksRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrack],
            error_mapper=create_text_track_error_mapper,
            request_options=request_options,
        )

    def create_text_track_alt1(
        self,
        channel_id: float,
        video_id: float,
        body: ChannelsVideosTexttracksRequest | ChannelsVideosTexttracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrack, CreateTextTrackAlt1ErrorBody]:
        """This method adds a text track to the specified video. For more information, see `Working with Text Track
        Uploads <https://developer.vimeo.com/api/upload/texttracks>`__.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/texttracks"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            body=json_body[ChannelsVideosTexttracksRequest | ChannelsVideosTexttracksRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrack],
            error_mapper=create_text_track_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_text_track(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTextTrackErrorBody]:
        """This method deletes the specified text track from a video. The authenticated user must be the owner of the
        video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/texttracks/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_text_track_error_mapper,
            request_options=request_options,
        )

    def edit_text_track(
        self,
        texttrack_id: float,
        video_id: float,
        *,
        body: VideosTexttracksRequest1 | VideosTexttracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrack, EditTextTrackErrorBody]:
        """This method edits the specified text track of a video. The authenticated user must be the owner of the video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/texttracks/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            body=json_body[VideosTexttracksRequest1 | VideosTexttracksRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrack],
            error_mapper=edit_text_track_error_mapper,
            request_options=request_options,
        )

    def get_text_track(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TextTrack, GetTextTrackErrorBody]:
        """This method returns a single text track of the specified video. The authenticated user must be the owner of
        the video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/texttracks/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrack],
            error_mapper=get_text_track_error_mapper,
            request_options=request_options,
        )

    def get_text_tracks(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrackConnection, GetTextTracksErrorBody]:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/texttracks"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrackConnection],
            error_mapper=get_text_tracks_error_mapper,
            request_options=request_options,
        )

    def get_text_tracks_alt1(
        self,
        video_id: float,
        version_id: str,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrackConnection, GetTextTracksAlt1ErrorBody]:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            version_id: Value sent with the request.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/texttracks"),
            path_params=[param[float]("video_id", video_id), param[str]("version_id", version_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrackConnection],
            error_mapper=get_text_tracks_alt1_error_mapper,
            request_options=request_options,
        )

    def get_text_tracks_alt2(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrackConnection, GetTextTracksAlt2ErrorBody]:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

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
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/texttracks"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrackConnection],
            error_mapper=get_text_tracks_alt2_error_mapper,
            request_options=request_options,
        )

    def get_text_tracks_alt3(
        self,
        album_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrackConnection, GetTextTracksAlt3ErrorBody]:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{album_id}/videos/{video_id}/texttracks"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrackConnection],
            error_mapper=get_text_tracks_alt3_error_mapper,
            request_options=request_options,
        )


class AsyncVideosTextTracksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_text_track(
        self,
        video_id: float,
        body: VideosTexttracksRequest | VideosTexttracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrack, CreateTextTrackErrorBody]:
        """This method adds a text track to the specified video. For more information, see `Working with Text Track
        Uploads <https://developer.vimeo.com/api/upload/texttracks>`__.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/texttracks"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosTexttracksRequest | VideosTexttracksRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrack],
            error_mapper=create_text_track_error_mapper,
            request_options=request_options,
        )

    async def create_text_track_alt1(
        self,
        channel_id: float,
        video_id: float,
        body: ChannelsVideosTexttracksRequest | ChannelsVideosTexttracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrack, CreateTextTrackAlt1ErrorBody]:
        """This method adds a text track to the specified video. For more information, see `Working with Text Track
        Uploads <https://developer.vimeo.com/api/upload/texttracks>`__.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/texttracks"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            body=json_body[ChannelsVideosTexttracksRequest | ChannelsVideosTexttracksRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrack],
            error_mapper=create_text_track_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_text_track(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTextTrackErrorBody]:
        """This method deletes the specified text track from a video. The authenticated user must be the owner of the
        video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/texttracks/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_text_track_error_mapper,
            request_options=request_options,
        )

    async def edit_text_track(
        self,
        texttrack_id: float,
        video_id: float,
        *,
        body: VideosTexttracksRequest1 | VideosTexttracksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrack, EditTextTrackErrorBody]:
        """This method edits the specified text track of a video. The authenticated user must be the owner of the video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/texttracks/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            body=json_body[VideosTexttracksRequest1 | VideosTexttracksRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrack],
            error_mapper=edit_text_track_error_mapper,
            request_options=request_options,
        )

    async def get_text_track(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TextTrack, GetTextTrackErrorBody]:
        """This method returns a single text track of the specified video. The authenticated user must be the owner of
        the video.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/texttracks/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrack],
            error_mapper=get_text_track_error_mapper,
            request_options=request_options,
        )

    async def get_text_tracks(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrackConnection, GetTextTracksErrorBody]:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/texttracks"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrackConnection],
            error_mapper=get_text_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_text_tracks_alt1(
        self,
        video_id: float,
        version_id: str,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrackConnection, GetTextTracksAlt1ErrorBody]:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            version_id: Value sent with the request.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/texttracks"),
            path_params=[param[float]("video_id", video_id), param[str]("version_id", version_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrackConnection],
            error_mapper=get_text_tracks_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_text_tracks_alt2(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrackConnection, GetTextTracksAlt2ErrorBody]:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

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
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/texttracks"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrackConnection],
            error_mapper=get_text_tracks_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_text_tracks_alt3(
        self,
        album_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TextTrackConnection, GetTextTracksAlt3ErrorBody]:
        """This method returns every text track of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{album_id}/videos/{video_id}/texttracks"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TextTrackConnection],
            error_mapper=get_text_tracks_alt3_error_mapper,
            request_options=request_options,
        )
