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
    param,
    raw_error_response,
)
from ..models.event_session_status import EventSessionStatus
from ..server.server import Server


class LiveEventSessions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventSessionsWithRawResponse(client, server, auth)

    def get_live_clip_ingest_status(
        self, live_event_id: str, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EventSessionStatus:
        """This method returns the ingest status of the specified event and associated video.

        Args:
            live_event_id: Value sent with the request.
            clip_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The ingest status was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_live_clip_ingest_status(
            live_event_id, clip_id=clip_id, request_options=request_options
        ).unwrap()

    def get_live_ingest_status(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventSessionStatus:
        """This method returns the ingest status of the specified event.

        Args:
            video_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The ingest status was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_live_ingest_status(video_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> LiveEventSessionsWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventSessions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventSessionsWithRawResponse(client, server, auth)

    async def get_live_clip_ingest_status(
        self, live_event_id: str, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EventSessionStatus:
        """This method returns the ingest status of the specified event and associated video.

        Args:
            live_event_id: Value sent with the request.
            clip_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The ingest status was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_live_clip_ingest_status(
                live_event_id, clip_id=clip_id, request_options=request_options
            )
        ).unwrap()

    async def get_live_ingest_status(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventSessionStatus:
        """This method returns the ingest status of the specified event.

        Args:
            video_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The ingest status was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_live_ingest_status(video_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveEventSessionsWithRawResponse:
        return self._with_raw_response


class LiveEventSessionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_live_clip_ingest_status(
        self, live_event_id: str, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventSessionStatus, RawError]:
        """This method returns the ingest status of the specified event and associated video.

        Args:
            live_event_id: Value sent with the request.
            clip_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/session_status"),
            path_params=[param[str]("live_event_id", live_event_id)],
            query_params=[param[float | None]("clip_id", clip_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventSessionStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_live_ingest_status(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventSessionStatus, RawError]:
        """This method returns the ingest status of the specified event.

        Args:
            video_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/sessions/status"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventSessionStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLiveEventSessionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_live_clip_ingest_status(
        self, live_event_id: str, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventSessionStatus, RawError]:
        """This method returns the ingest status of the specified event and associated video.

        Args:
            live_event_id: Value sent with the request.
            clip_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/session_status"),
            path_params=[param[str]("live_event_id", live_event_id)],
            query_params=[param[float | None]("clip_id", clip_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventSessionStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_live_ingest_status(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventSessionStatus, RawError]:
        """This method returns the ingest status of the specified event.

        Args:
            video_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/sessions/status"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventSessionStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
