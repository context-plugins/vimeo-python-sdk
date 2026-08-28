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
from ..errors.create_audio_track_error import CreateAudioTrackErrorBody, create_audio_track_error_mapper
from ..errors.create_video_version_error import CreateVideoVersionErrorBody, create_video_version_error_mapper
from ..errors.delete_audio_track_error import DeleteAudioTrackErrorBody, delete_audio_track_error_mapper
from ..errors.delete_video_version_error import DeleteVideoVersionErrorBody, delete_video_version_error_mapper
from ..errors.edit_audio_track_error import EditAudioTrackErrorBody, edit_audio_track_error_mapper
from ..errors.edit_video_version_error import EditVideoVersionErrorBody, edit_video_version_error_mapper
from ..errors.get_audio_track_error import GetAudioTrackErrorBody, get_audio_track_error_mapper
from ..errors.get_audio_tracks_error import GetAudioTracksErrorBody, get_audio_tracks_error_mapper
from ..errors.get_video_version_error import GetVideoVersionErrorBody, get_video_version_error_mapper
from ..errors.get_video_versions_alt1_error import GetVideoVersionsAlt1ErrorBody, get_video_versions_alt1_error_mapper
from ..errors.get_video_versions_error import GetVideoVersionsErrorBody, get_video_versions_error_mapper
from ..models.alternate_audio_track import AlternateAudioTrack
from ..models.alternate_audio_track_connection import AlternateAudioTrackConnection
from ..models.picture import Picture
from ..models.video_version import VideoVersion
from ..models.video_version_connection import VideoVersionConnection
from ..models.videos_versions_audiotracks_audiotrack_id_request import (
    VideosVersionsAudiotracksAudiotrackIdRequest,
    VideosVersionsAudiotracksAudiotrackIdRequestDict,
)
from ..models.videos_versions_audiotracks_request import (
    VideosVersionsAudiotracksRequest,
    VideosVersionsAudiotracksRequestDict,
)
from ..models.videos_versions_request import VideosVersionsRequest, VideosVersionsRequestDict
from ..models.videos_versions_request1 import VideosVersionsRequest1, VideosVersionsRequest1Dict
from ..server.server import Server


class VideosVersions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosVersionsWithRawResponse(client, server, auth)

    def create_audio_track(
        self,
        version_id: float,
        video_id: float,
        body: VideosVersionsAudiotracksRequest | VideosVersionsAudiotracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlternateAudioTrack:
        """This method creates a new audio track for a video version.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio track was created.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_audio_track(
            version_id, video_id, body, request_options=request_options
        ).unwrap()

    def create_video_version(
        self,
        video_id: float,
        body: VideosVersionsRequest | VideosVersionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoVersion:
        """This method adds a version to the specified video. The authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The version was added.

        Raises:
            ApiError: Error code 2204: The request input contains invalid version data. * Error code 3427: The
                authenticated user can't edit the video. * Error code 4104: The authenticated user's allotted daily
                quota has been reached. * Error code 5011: An upload isn't associated with this version. * Error code
                5012: A video isn't associated with this upload. * Error code 5013: The endpoint isn't available,
                because the specified version of the API is less than 3.4 and **upload.approach** isn't ``tus``.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.create_video_version(video_id, body, request_options=request_options).unwrap()

    def delete_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes an audio track from the specified video version.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio track was deleted.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_audio_track(
            audiotrack_id, version_id, video_id, request_options=request_options
        ).unwrap()

    def delete_video_version(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified version from a video. The authenticated user must be the owner of the
        video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video version was deleted.

        Raises:
            ApiError: * No such video exists. * Error code 2523: The version isn't associated with the video. * Error
                code 2538: The specified version is the video's current version and can't be deleted. * Error code 3200:
                The authenticated user can't access the versions of this video. * Error code 8003: The user credentials
                are invalid. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_video_version(
            version_id, video_id, request_options=request_options
        ).unwrap()

    def edit_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        body: (
            VideosVersionsAudiotracksAudiotrackIdRequest | VideosVersionsAudiotracksAudiotrackIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlternateAudioTrack:
        """This method edits the metadata for the specified audio track.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio track was edited.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.edit_audio_track(
            audiotrack_id, version_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def edit_video_version(
        self,
        version_id: float,
        video_id: float,
        *,
        body: VideosVersionsRequest1 | VideosVersionsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoVersion:
        """This method edits the specified version of a video. The authenticated user must be the owner of the video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The version was edited.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. * No such video exists. * Error code 2205: A
                parameter is invalid. * Error code 3200: The authenticated user can't access the versions of this video.
                ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.edit_video_version(
            version_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def get_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlternateAudioTrack:
        """This method returns the specified audio track that is associated with a video version.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio track was returned.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_audio_track(
            audiotrack_id, version_id, video_id, request_options=request_options
        ).unwrap()

    def get_audio_tracks(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> AlternateAudioTrackConnection:
        """This method returns all audio tracks that are associated with the specified video version.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio tracks were returned.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_audio_tracks(version_id, video_id, request_options=request_options).unwrap()

    def get_audiotrack_downloads(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns a list of downloadable file links for a version of a video that contains the specified
        alternate audio track.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of downloadable file links was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_audiotrack_downloads(
            version_id, video_id, request_options=request_options
        ).unwrap()

    def get_version_thumbnail(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns the thumbnail associated with the specified version of a video.

        Args:
            version_id: The ID of the version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The version thumbnail was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_version_thumbnail(
            version_id, video_id, request_options=request_options
        ).unwrap()

    def get_video_version(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoVersion:
        """This method returns a single version of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video version was returned.

        Raises:
            ApiError: * No such video exists. * Error code 3200: The authenticated user can't access the versions of
                this video. * Error code 8003: The user credentials are invalid. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.get_video_version(version_id, video_id, request_options=request_options).unwrap()

    def get_video_versions(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoVersionConnection:
        """This method returns every version of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The versions were returned.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. No such video exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.get_video_versions(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_video_versions_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoVersionConnection:
        """This method returns every version of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The versions were returned.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. No such video exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.get_video_versions_alt1(
            channel_id, video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosVersionsWithRawResponse:
        return self._with_raw_response


class AsyncVideosVersions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosVersionsWithRawResponse(client, server, auth)

    async def create_audio_track(
        self,
        version_id: float,
        video_id: float,
        body: VideosVersionsAudiotracksRequest | VideosVersionsAudiotracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlternateAudioTrack:
        """This method creates a new audio track for a video version.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio track was created.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.create_audio_track(
                version_id, video_id, body, request_options=request_options
            )
        ).unwrap()

    async def create_video_version(
        self,
        video_id: float,
        body: VideosVersionsRequest | VideosVersionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoVersion:
        """This method adds a version to the specified video. The authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The version was added.

        Raises:
            ApiError: Error code 2204: The request input contains invalid version data. * Error code 3427: The
                authenticated user can't edit the video. * Error code 4104: The authenticated user's allotted daily
                quota has been reached. * Error code 5011: An upload isn't associated with this version. * Error code
                5012: A video isn't associated with this upload. * Error code 5013: The endpoint isn't available,
                because the specified version of the API is less than 3.4 and **upload.approach** isn't ``tus``.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.create_video_version(video_id, body, request_options=request_options)
        ).unwrap()

    async def delete_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes an audio track from the specified video version.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio track was deleted.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_audio_track(
                audiotrack_id, version_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def delete_video_version(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified version from a video. The authenticated user must be the owner of the
        video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video version was deleted.

        Raises:
            ApiError: * No such video exists. * Error code 2523: The version isn't associated with the video. * Error
                code 2538: The specified version is the video's current version and can't be deleted. * Error code 3200:
                The authenticated user can't access the versions of this video. * Error code 8003: The user credentials
                are invalid. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_video_version(version_id, video_id, request_options=request_options)
        ).unwrap()

    async def edit_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        body: (
            VideosVersionsAudiotracksAudiotrackIdRequest | VideosVersionsAudiotracksAudiotrackIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlternateAudioTrack:
        """This method edits the metadata for the specified audio track.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio track was edited.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_audio_track(
                audiotrack_id, version_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def edit_video_version(
        self,
        version_id: float,
        video_id: float,
        *,
        body: VideosVersionsRequest1 | VideosVersionsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoVersion:
        """This method edits the specified version of a video. The authenticated user must be the owner of the video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The version was edited.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. * No such video exists. * Error code 2205: A
                parameter is invalid. * Error code 3200: The authenticated user can't access the versions of this video.
                ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_video_version(
                version_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlternateAudioTrack:
        """This method returns the specified audio track that is associated with a video version.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio track was returned.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_audio_track(
                audiotrack_id, version_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_audio_tracks(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> AlternateAudioTrackConnection:
        """This method returns all audio tracks that are associated with the specified video version.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The audio tracks were returned.

        Raises:
            ApiError: No such audio track exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_audio_tracks(version_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_audiotrack_downloads(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns a list of downloadable file links for a version of a video that contains the specified
        alternate audio track.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of downloadable file links was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_audiotrack_downloads(
                version_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_version_thumbnail(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns the thumbnail associated with the specified version of a video.

        Args:
            version_id: The ID of the version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The version thumbnail was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_version_thumbnail(version_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_video_version(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoVersion:
        """This method returns a single version of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video version was returned.

        Raises:
            ApiError: * No such video exists. * Error code 3200: The authenticated user can't access the versions of
                this video. * Error code 8003: The user credentials are invalid. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.get_video_version(version_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_video_versions(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoVersionConnection:
        """This method returns every version of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The versions were returned.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. No such video exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_video_versions(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_video_versions_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoVersionConnection:
        """This method returns every version of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The versions were returned.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. No such video exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_video_versions_alt1(
                channel_id, video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosVersionsWithRawResponse:
        return self._with_raw_response


class VideosVersionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_audio_track(
        self,
        version_id: float,
        video_id: float,
        body: VideosVersionsAudiotracksRequest | VideosVersionsAudiotracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlternateAudioTrack, CreateAudioTrackErrorBody]:
        """This method creates a new audio track for a video version.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            body=json_body[VideosVersionsAudiotracksRequest | VideosVersionsAudiotracksRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlternateAudioTrack],
            error_mapper=create_audio_track_error_mapper,
            request_options=request_options,
        )

    def create_video_version(
        self,
        video_id: float,
        body: VideosVersionsRequest | VideosVersionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoVersion, CreateVideoVersionErrorBody]:
        """This method adds a version to the specified video. The authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/versions"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosVersionsRequest | VideosVersionsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersion],
            error_mapper=create_video_version_error_mapper,
            request_options=request_options,
        )

    def delete_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteAudioTrackErrorBody]:
        """This method deletes an audio track from the specified video version.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}"),
            path_params=[
                param[str]("audiotrack_id", audiotrack_id),
                param[float]("version_id", version_id),
                param[float]("video_id", video_id),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_audio_track_error_mapper,
            request_options=request_options,
        )

    def delete_video_version(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoVersionErrorBody]:
        """This method deletes the specified version from a video. The authenticated user must be the owner of the
        video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_version_error_mapper,
            request_options=request_options,
        )

    def edit_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        body: (
            VideosVersionsAudiotracksAudiotrackIdRequest | VideosVersionsAudiotracksAudiotrackIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlternateAudioTrack, EditAudioTrackErrorBody]:
        """This method edits the metadata for the specified audio track.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}"),
            path_params=[
                param[str]("audiotrack_id", audiotrack_id),
                param[float]("version_id", version_id),
                param[float]("video_id", video_id),
            ],
            body=json_body[
                VideosVersionsAudiotracksAudiotrackIdRequest | VideosVersionsAudiotracksAudiotrackIdRequestDict | None
            ](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlternateAudioTrack],
            error_mapper=edit_audio_track_error_mapper,
            request_options=request_options,
        )

    def edit_video_version(
        self,
        version_id: float,
        video_id: float,
        *,
        body: VideosVersionsRequest1 | VideosVersionsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoVersion, EditVideoVersionErrorBody]:
        """This method edits the specified version of a video. The authenticated user must be the owner of the video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            body=json_body[VideosVersionsRequest1 | VideosVersionsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersion],
            error_mapper=edit_video_version_error_mapper,
            request_options=request_options,
        )

    def get_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlternateAudioTrack, GetAudioTrackErrorBody]:
        """This method returns the specified audio track that is associated with a video version.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}"),
            path_params=[
                param[str]("audiotrack_id", audiotrack_id),
                param[float]("version_id", version_id),
                param[float]("video_id", video_id),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlternateAudioTrack],
            error_mapper=get_audio_track_error_mapper,
            request_options=request_options,
        )

    def get_audio_tracks(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AlternateAudioTrackConnection, GetAudioTracksErrorBody]:
        """This method returns all audio tracks that are associated with the specified video version.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlternateAudioTrackConnection],
            error_mapper=get_audio_tracks_error_mapper,
            request_options=request_options,
        )

    def get_audiotrack_downloads(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns a list of downloadable file links for a version of a video that contains the specified
        alternate audio track.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/downloads"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_version_thumbnail(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns the thumbnail associated with the specified version of a video.

        Args:
            version_id: The ID of the version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/picture"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_video_version(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoVersion, GetVideoVersionErrorBody]:
        """This method returns a single version of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersion],
            error_mapper=get_video_version_error_mapper,
            request_options=request_options,
        )

    def get_video_versions(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoVersionConnection, GetVideoVersionsErrorBody]:
        """This method returns every version of the specified video. The authenticated user must be the owner of the
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
            url_template=self._server.default("/videos/{video_id}/versions"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersionConnection],
            error_mapper=get_video_versions_error_mapper,
            request_options=request_options,
        )

    def get_video_versions_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoVersionConnection, GetVideoVersionsAlt1ErrorBody]:
        """This method returns every version of the specified video. The authenticated user must be the owner of the
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
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/versions"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersionConnection],
            error_mapper=get_video_versions_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncVideosVersionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_audio_track(
        self,
        version_id: float,
        video_id: float,
        body: VideosVersionsAudiotracksRequest | VideosVersionsAudiotracksRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlternateAudioTrack, CreateAudioTrackErrorBody]:
        """This method creates a new audio track for a video version.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            body=json_body[VideosVersionsAudiotracksRequest | VideosVersionsAudiotracksRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlternateAudioTrack],
            error_mapper=create_audio_track_error_mapper,
            request_options=request_options,
        )

    async def create_video_version(
        self,
        video_id: float,
        body: VideosVersionsRequest | VideosVersionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoVersion, CreateVideoVersionErrorBody]:
        """This method adds a version to the specified video. The authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/versions"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosVersionsRequest | VideosVersionsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersion],
            error_mapper=create_video_version_error_mapper,
            request_options=request_options,
        )

    async def delete_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteAudioTrackErrorBody]:
        """This method deletes an audio track from the specified video version.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}"),
            path_params=[
                param[str]("audiotrack_id", audiotrack_id),
                param[float]("version_id", version_id),
                param[float]("video_id", video_id),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_audio_track_error_mapper,
            request_options=request_options,
        )

    async def delete_video_version(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoVersionErrorBody]:
        """This method deletes the specified version from a video. The authenticated user must be the owner of the
        video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_version_error_mapper,
            request_options=request_options,
        )

    async def edit_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        body: (
            VideosVersionsAudiotracksAudiotrackIdRequest | VideosVersionsAudiotracksAudiotrackIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlternateAudioTrack, EditAudioTrackErrorBody]:
        """This method edits the metadata for the specified audio track.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}"),
            path_params=[
                param[str]("audiotrack_id", audiotrack_id),
                param[float]("version_id", version_id),
                param[float]("video_id", video_id),
            ],
            body=json_body[
                VideosVersionsAudiotracksAudiotrackIdRequest | VideosVersionsAudiotracksAudiotrackIdRequestDict | None
            ](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlternateAudioTrack],
            error_mapper=edit_audio_track_error_mapper,
            request_options=request_options,
        )

    async def edit_video_version(
        self,
        version_id: float,
        video_id: float,
        *,
        body: VideosVersionsRequest1 | VideosVersionsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoVersion, EditVideoVersionErrorBody]:
        """This method edits the specified version of a video. The authenticated user must be the owner of the video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            body=json_body[VideosVersionsRequest1 | VideosVersionsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersion],
            error_mapper=edit_video_version_error_mapper,
            request_options=request_options,
        )

    async def get_audio_track(
        self,
        audiotrack_id: str,
        version_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlternateAudioTrack, GetAudioTrackErrorBody]:
        """This method returns the specified audio track that is associated with a video version.

        Args:
            audiotrack_id: The ID of the audio track.
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}"),
            path_params=[
                param[str]("audiotrack_id", audiotrack_id),
                param[float]("version_id", version_id),
                param[float]("video_id", video_id),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlternateAudioTrack],
            error_mapper=get_audio_track_error_mapper,
            request_options=request_options,
        )

    async def get_audio_tracks(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AlternateAudioTrackConnection, GetAudioTracksErrorBody]:
        """This method returns all audio tracks that are associated with the specified video version.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/audiotracks"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlternateAudioTrackConnection],
            error_mapper=get_audio_tracks_error_mapper,
            request_options=request_options,
        )

    async def get_audiotrack_downloads(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns a list of downloadable file links for a version of a video that contains the specified
        alternate audio track.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/downloads"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_version_thumbnail(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns the thumbnail associated with the specified version of a video.

        Args:
            version_id: The ID of the version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}/picture"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_video_version(
        self, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoVersion, GetVideoVersionErrorBody]:
        """This method returns a single version of the specified video. The authenticated user must be the owner of the
        video.

        Args:
            version_id: The ID of the video version.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/versions/{version_id}"),
            path_params=[param[float]("version_id", version_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersion],
            error_mapper=get_video_version_error_mapper,
            request_options=request_options,
        )

    async def get_video_versions(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoVersionConnection, GetVideoVersionsErrorBody]:
        """This method returns every version of the specified video. The authenticated user must be the owner of the
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
            url_template=self._server.default("/videos/{video_id}/versions"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersionConnection],
            error_mapper=get_video_versions_error_mapper,
            request_options=request_options,
        )

    async def get_video_versions_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoVersionConnection, GetVideoVersionsAlt1ErrorBody]:
        """This method returns every version of the specified video. The authenticated user must be the owner of the
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
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/versions"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoVersionConnection],
            error_mapper=get_video_versions_alt1_error_mapper,
            request_options=request_options,
        )
