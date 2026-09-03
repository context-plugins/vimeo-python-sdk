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
    param,
)
from ..errors.get_one_time_event_m3_u8_playback_alt1_error import (
    GetOneTimeEventM3U8PlaybackAlt1ErrorBody,
    get_one_time_event_m3_u8_playback_alt1_error_mapper,
)
from ..errors.get_one_time_event_m3_u8_playback_error import (
    GetOneTimeEventM3U8PlaybackErrorBody,
    get_one_time_event_m3_u8_playback_error_mapper,
)
from ..server.server import Server


class VideosLiveM3U8Playback:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosLiveM3U8PlaybackWithRawResponse(client, server, auth)

    def get_one_time_event_m3u8_playback(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The M3U8 playback URL was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the M3U8 playback URL. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_one_time_event_m3u8_playback(
            user_id, video_id, request_options=request_options
        ).unwrap()

    def get_one_time_event_m3u8_playback_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The M3U8 playback URL was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the M3U8 playback URL. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_one_time_event_m3u8_playback_alt1(
            video_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosLiveM3U8PlaybackWithRawResponse:
        return self._with_raw_response


class AsyncVideosLiveM3U8Playback:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosLiveM3U8PlaybackWithRawResponse(client, server, auth)

    async def get_one_time_event_m3u8_playback(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The M3U8 playback URL was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the M3U8 playback URL. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_one_time_event_m3u8_playback(
                user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_one_time_event_m3u8_playback_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The M3U8 playback URL was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the M3U8 playback URL. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_one_time_event_m3u8_playback_alt1(
                video_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosLiveM3U8PlaybackWithRawResponse:
        return self._with_raw_response


class VideosLiveM3U8PlaybackWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_one_time_event_m3u8_playback(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetOneTimeEventM3U8PlaybackErrorBody]:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/videos/{video_id}/m3u8_playback"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_one_time_event_m3_u8_playback_error_mapper,
            request_options=request_options,
        )

    def get_one_time_event_m3u8_playback_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetOneTimeEventM3U8PlaybackAlt1ErrorBody]:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/videos/{video_id}/m3u8_playback"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_one_time_event_m3_u8_playback_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncVideosLiveM3U8PlaybackWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_one_time_event_m3u8_playback(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetOneTimeEventM3U8PlaybackErrorBody]:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/videos/{video_id}/m3u8_playback"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_one_time_event_m3_u8_playback_error_mapper,
            request_options=request_options,
        )

    async def get_one_time_event_m3u8_playback_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetOneTimeEventM3U8PlaybackAlt1ErrorBody]:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/videos/{video_id}/m3u8_playback"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_one_time_event_m3_u8_playback_alt1_error_mapper,
            request_options=request_options,
        )
