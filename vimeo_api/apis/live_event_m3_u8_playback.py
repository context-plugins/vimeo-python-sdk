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
from ..errors.get_live_event_m3_u8_playback_alt1_error import (
    GetLiveEventM3U8PlaybackAlt1ErrorBody,
    get_live_event_m3_u8_playback_alt1_error_mapper,
)
from ..errors.get_live_event_m3_u8_playback_error import (
    GetLiveEventM3U8PlaybackErrorBody,
    get_live_event_m3_u8_playback_error_mapper,
)
from ..server.server import Server


class LiveEventM3U8Playback:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventM3U8PlaybackWithRawResponse(client, server, auth)

    def get_live_event_m3u8_playback(
        self,
        live_event_id: float,
        user_id: float,
        *,
        dvr: float | None = None,
        max_fps_fhd: float | None = None,
        ttl: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            dvr: When set to ``1``, returns an fMP4 stream URL if DVR is enabled on the event. If DVR is not enabled,
                the standard stream URL is returned.
            max_fps_fhd: The requested maximum frames per second.
            ttl: The time to live of the playlist link in seconds. This value must be between ``10`` and ``60``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The M3U8 playback URL was returned.

        Raises:
            ApiError: Error code 10008: The event hasn't started. Error code 8000: The user credentials are invalid.
                Error code 3200: The authenticated user can't access the M3U8 playback URL. Error code 5000: No such
                event or user exists. * Error code 4020: No streamable video was found. * Error code 4021: No video was
                found. Error code 7900: The streamable video in progress will be available soon. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_live_event_m3u8_playback(
            live_event_id, user_id, dvr=dvr, max_fps_fhd=max_fps_fhd, ttl=ttl, request_options=request_options
        ).unwrap()

    def get_live_event_m3u8_playback_alt1(
        self,
        live_event_id: float,
        *,
        dvr: float | None = None,
        max_fps_fhd: float | None = None,
        ttl: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            live_event_id: The ID of the event.
            dvr: When set to ``1``, returns an fMP4 stream URL if DVR is enabled on the event. If DVR is not enabled,
                the standard stream URL is returned.
            max_fps_fhd: The requested maximum frames per second.
            ttl: The time to live of the playlist link in seconds. This value must be between ``10`` and ``60``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The M3U8 playback URL was returned.

        Raises:
            ApiError: Error code 10008: The event hasn't started. Error code 8000: The user credentials are invalid.
                Error code 3200: The authenticated user can't access the M3U8 playback URL. Error code 5000: No such
                event or user exists. * Error code 4020: No streamable video was found. * Error code 4021: No video was
                found. Error code 7900: The streamable video in progress will be available soon. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_live_event_m3u8_playback_alt1(
            live_event_id, dvr=dvr, max_fps_fhd=max_fps_fhd, ttl=ttl, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveEventM3U8PlaybackWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventM3U8Playback:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventM3U8PlaybackWithRawResponse(client, server, auth)

    async def get_live_event_m3u8_playback(
        self,
        live_event_id: float,
        user_id: float,
        *,
        dvr: float | None = None,
        max_fps_fhd: float | None = None,
        ttl: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            dvr: When set to ``1``, returns an fMP4 stream URL if DVR is enabled on the event. If DVR is not enabled,
                the standard stream URL is returned.
            max_fps_fhd: The requested maximum frames per second.
            ttl: The time to live of the playlist link in seconds. This value must be between ``10`` and ``60``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The M3U8 playback URL was returned.

        Raises:
            ApiError: Error code 10008: The event hasn't started. Error code 8000: The user credentials are invalid.
                Error code 3200: The authenticated user can't access the M3U8 playback URL. Error code 5000: No such
                event or user exists. * Error code 4020: No streamable video was found. * Error code 4021: No video was
                found. Error code 7900: The streamable video in progress will be available soon. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_live_event_m3u8_playback(
                live_event_id, user_id, dvr=dvr, max_fps_fhd=max_fps_fhd, ttl=ttl, request_options=request_options
            )
        ).unwrap()

    async def get_live_event_m3u8_playback_alt1(
        self,
        live_event_id: float,
        *,
        dvr: float | None = None,
        max_fps_fhd: float | None = None,
        ttl: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            live_event_id: The ID of the event.
            dvr: When set to ``1``, returns an fMP4 stream URL if DVR is enabled on the event. If DVR is not enabled,
                the standard stream URL is returned.
            max_fps_fhd: The requested maximum frames per second.
            ttl: The time to live of the playlist link in seconds. This value must be between ``10`` and ``60``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The M3U8 playback URL was returned.

        Raises:
            ApiError: Error code 10008: The event hasn't started. Error code 8000: The user credentials are invalid.
                Error code 3200: The authenticated user can't access the M3U8 playback URL. Error code 5000: No such
                event or user exists. * Error code 4020: No streamable video was found. * Error code 4021: No video was
                found. Error code 7900: The streamable video in progress will be available soon. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_live_event_m3u8_playback_alt1(
                live_event_id, dvr=dvr, max_fps_fhd=max_fps_fhd, ttl=ttl, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveEventM3U8PlaybackWithRawResponse:
        return self._with_raw_response


class LiveEventM3U8PlaybackWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_live_event_m3u8_playback(
        self,
        live_event_id: float,
        user_id: float,
        *,
        dvr: float | None = None,
        max_fps_fhd: float | None = None,
        ttl: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, GetLiveEventM3U8PlaybackErrorBody]:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            dvr: When set to ``1``, returns an fMP4 stream URL if DVR is enabled on the event. If DVR is not enabled,
                the standard stream URL is returned.
            max_fps_fhd: The requested maximum frames per second.
            ttl: The time to live of the playlist link in seconds. This value must be between ``10`` and ``60``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/m3u8_playback"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            query_params=[
                param[float | None]("dvr", dvr),
                param[float | None]("max_fps_fhd", max_fps_fhd),
                param[float | None]("ttl", ttl),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_live_event_m3_u8_playback_error_mapper,
            request_options=request_options,
        )

    def get_live_event_m3u8_playback_alt1(
        self,
        live_event_id: float,
        *,
        dvr: float | None = None,
        max_fps_fhd: float | None = None,
        ttl: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, GetLiveEventM3U8PlaybackAlt1ErrorBody]:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            live_event_id: The ID of the event.
            dvr: When set to ``1``, returns an fMP4 stream URL if DVR is enabled on the event. If DVR is not enabled,
                the standard stream URL is returned.
            max_fps_fhd: The requested maximum frames per second.
            ttl: The time to live of the playlist link in seconds. This value must be between ``10`` and ``60``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/m3u8_playback"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[
                param[float | None]("dvr", dvr),
                param[float | None]("max_fps_fhd", max_fps_fhd),
                param[float | None]("ttl", ttl),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_live_event_m3_u8_playback_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEventM3U8PlaybackWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_live_event_m3u8_playback(
        self,
        live_event_id: float,
        user_id: float,
        *,
        dvr: float | None = None,
        max_fps_fhd: float | None = None,
        ttl: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, GetLiveEventM3U8PlaybackErrorBody]:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            dvr: When set to ``1``, returns an fMP4 stream URL if DVR is enabled on the event. If DVR is not enabled,
                the standard stream URL is returned.
            max_fps_fhd: The requested maximum frames per second.
            ttl: The time to live of the playlist link in seconds. This value must be between ``10`` and ``60``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/m3u8_playback"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            query_params=[
                param[float | None]("dvr", dvr),
                param[float | None]("max_fps_fhd", max_fps_fhd),
                param[float | None]("ttl", ttl),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_live_event_m3_u8_playback_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_m3u8_playback_alt1(
        self,
        live_event_id: float,
        *,
        dvr: float | None = None,
        max_fps_fhd: float | None = None,
        ttl: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, GetLiveEventM3U8PlaybackAlt1ErrorBody]:
        """This method returns an M3U8 playback URL for the specified event stream. You should use this endpoint only in
        conjunction with our recommended procedure for playing events via HLS. For more information, see our `HLS guide
        <https://developer.vimeo.com/api/live/playback>`__.

        Args:
            live_event_id: The ID of the event.
            dvr: When set to ``1``, returns an fMP4 stream URL if DVR is enabled on the event. If DVR is not enabled,
                the standard stream URL is returned.
            max_fps_fhd: The requested maximum frames per second.
            ttl: The time to live of the playlist link in seconds. This value must be between ``10`` and ``60``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/m3u8_playback"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[
                param[float | None]("dvr", dvr),
                param[float | None]("max_fps_fhd", max_fps_fhd),
                param[float | None]("ttl", ttl),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_live_event_m3_u8_playback_alt1_error_mapper,
            request_options=request_options,
        )
