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
    json_decoder,
    param,
)
from ..errors.get_transcript_error import GetTranscriptErrorBody, get_transcript_error_mapper
from ..errors.get_transcript_metadata_error import GetTranscriptMetadataErrorBody, get_transcript_metadata_error_mapper
from ..models.segment_connection import SegmentConnection
from ..models.transcript_metadata import TranscriptMetadata
from ..server.server import Server


class VideosTranscripts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosTranscriptsWithRawResponse(client, server, auth)

    def get_transcript(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> SegmentConnection:
        """This method returns the transcript segments of the specified text track.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The transcript segments were returned.

        Raises:
            ApiError: * Error code 2: The specified video doesn't exist. * Error code 5014: The specified text track
                doesn't exist. * Error code 5022: The specified transcript doesn't exist. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_transcript(texttrack_id, video_id, request_options=request_options).unwrap()

    def get_transcript_metadata(
        self, container_uuid: str, texttrack_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> TranscriptMetadata:
        """This method returns the transcript metadata of the specified text track.

        Args:
            container_uuid: The UUID of the video container.
            texttrack_id: The ID of the text track.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The transcript metadata of the text track was returned.

        Raises:
            ApiError: Error code 5022: No such transcript exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_transcript_metadata(
            container_uuid, texttrack_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosTranscriptsWithRawResponse:
        return self._with_raw_response


class AsyncVideosTranscripts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosTranscriptsWithRawResponse(client, server, auth)

    async def get_transcript(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> SegmentConnection:
        """This method returns the transcript segments of the specified text track.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The transcript segments were returned.

        Raises:
            ApiError: * Error code 2: The specified video doesn't exist. * Error code 5014: The specified text track
                doesn't exist. * Error code 5022: The specified transcript doesn't exist. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_transcript(texttrack_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_transcript_metadata(
        self, container_uuid: str, texttrack_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> TranscriptMetadata:
        """This method returns the transcript metadata of the specified text track.

        Args:
            container_uuid: The UUID of the video container.
            texttrack_id: The ID of the text track.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The transcript metadata of the text track was returned.

        Raises:
            ApiError: Error code 5022: No such transcript exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_transcript_metadata(
                container_uuid, texttrack_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosTranscriptsWithRawResponse:
        return self._with_raw_response


class VideosTranscriptsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_transcript(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SegmentConnection, GetTranscriptErrorBody]:
        """This method returns the transcript segments of the specified text track.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/transcripts/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[SegmentConnection],
            error_mapper=get_transcript_error_mapper,
            request_options=request_options,
        )

    def get_transcript_metadata(
        self, container_uuid: str, texttrack_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TranscriptMetadata, GetTranscriptMetadataErrorBody]:
        """This method returns the transcript metadata of the specified text track.

        Args:
            container_uuid: The UUID of the video container.
            texttrack_id: The ID of the text track.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{container_uuid}/transcript/{texttrack_id}/metadata"),
            path_params=[param[str]("container_uuid", container_uuid), param[float]("texttrack_id", texttrack_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TranscriptMetadata],
            error_mapper=get_transcript_metadata_error_mapper,
            request_options=request_options,
        )


class AsyncVideosTranscriptsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_transcript(
        self, texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SegmentConnection, GetTranscriptErrorBody]:
        """This method returns the transcript segments of the specified text track.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/transcripts/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[SegmentConnection],
            error_mapper=get_transcript_error_mapper,
            request_options=request_options,
        )

    async def get_transcript_metadata(
        self, container_uuid: str, texttrack_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TranscriptMetadata, GetTranscriptMetadataErrorBody]:
        """This method returns the transcript metadata of the specified text track.

        Args:
            container_uuid: The UUID of the video container.
            texttrack_id: The ID of the text track.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{container_uuid}/transcript/{texttrack_id}/metadata"),
            path_params=[param[str]("container_uuid", container_uuid), param[float]("texttrack_id", texttrack_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TranscriptMetadata],
            error_mapper=get_transcript_metadata_error_mapper,
            request_options=request_options,
        )
