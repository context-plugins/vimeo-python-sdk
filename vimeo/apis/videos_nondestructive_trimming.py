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
    json_body,
    json_decoder,
    param,
)
from ..errors.clip_trim_error import ClipTrimErrorBody, clip_trim_error_mapper
from ..models.trimmed_video import TrimmedVideo
from ..models.videos_trim_request import VideosTrimRequest, VideosTrimRequestDict
from ..server.server import Server


class VideosNondestructiveTrimming:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosNondestructiveTrimmingWithRawResponse(client, server, auth)

    def clip_trim(
        self,
        video_id: float,
        *,
        body: VideosTrimRequest | VideosTrimRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrimmedVideo:
        """This method starts a trim operation for the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The trim operation was started.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3411: The authenticated user is
                unverified. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.clip_trim(video_id, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VideosNondestructiveTrimmingWithRawResponse:
        return self._with_raw_response


class AsyncVideosNondestructiveTrimming:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosNondestructiveTrimmingWithRawResponse(client, server, auth)

    async def clip_trim(
        self,
        video_id: float,
        *,
        body: VideosTrimRequest | VideosTrimRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TrimmedVideo:
        """This method starts a trim operation for the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The trim operation was started.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3411: The authenticated user is
                unverified. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.clip_trim(video_id, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosNondestructiveTrimmingWithRawResponse:
        return self._with_raw_response


class VideosNondestructiveTrimmingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def clip_trim(
        self,
        video_id: float,
        *,
        body: VideosTrimRequest | VideosTrimRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrimmedVideo, ClipTrimErrorBody]:
        """This method starts a trim operation for the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/trim"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosTrimRequest | VideosTrimRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TrimmedVideo],
            error_mapper=clip_trim_error_mapper,
            request_options=request_options,
        )


class AsyncVideosNondestructiveTrimmingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def clip_trim(
        self,
        video_id: float,
        *,
        body: VideosTrimRequest | VideosTrimRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TrimmedVideo, ClipTrimErrorBody]:
        """This method starts a trim operation for the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/trim"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosTrimRequest | VideosTrimRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TrimmedVideo],
            error_mapper=clip_trim_error_mapper,
            request_options=request_options,
        )
