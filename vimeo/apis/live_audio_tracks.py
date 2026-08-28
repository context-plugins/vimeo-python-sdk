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
from ..errors.get_event_audio_tracks_error import GetEventAudioTracksErrorBody, get_event_audio_tracks_error_mapper
from ..errors.update_event_audio_tracks_error import (
    UpdateEventAudioTracksErrorBody,
    update_event_audio_tracks_error_mapper,
)
from ..models.event_audio_tracks import EventAudioTracks
from ..models.live_events_audio_tracks_request import LiveEventsAudioTracksRequest, LiveEventsAudioTracksRequestDict
from ..server.server import Server


class LiveAudioTracks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveAudioTracksWithRawResponse(client, server, auth)

    def get_event_audio_tracks(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventAudioTracks:
        """This method returns audio tracks settings for the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event audio track settings were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such event or user exists.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_event_audio_tracks(live_event_id, request_options=request_options).unwrap()

    def update_event_audio_tracks(
        self,
        live_event_id: float,
        *,
        body: LiveEventsAudioTracksRequest | LiveEventsAudioTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventAudioTracks:
        """This method updates audio tracks settings on the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event audio tracks settings were updated.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such event or user exists.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.update_event_audio_tracks(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveAudioTracksWithRawResponse:
        return self._with_raw_response


class AsyncLiveAudioTracks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveAudioTracksWithRawResponse(client, server, auth)

    async def get_event_audio_tracks(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventAudioTracks:
        """This method returns audio tracks settings for the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event audio track settings were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such event or user exists.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_event_audio_tracks(live_event_id, request_options=request_options)
        ).unwrap()

    async def update_event_audio_tracks(
        self,
        live_event_id: float,
        *,
        body: LiveEventsAudioTracksRequest | LiveEventsAudioTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventAudioTracks:
        """This method updates audio tracks settings on the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event audio tracks settings were updated.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such event or user exists.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.update_event_audio_tracks(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveAudioTracksWithRawResponse:
        return self._with_raw_response


class LiveAudioTracksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_event_audio_tracks(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventAudioTracks, GetEventAudioTracksErrorBody]:
        """This method returns audio tracks settings for the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/audio_tracks"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventAudioTracks],
            error_mapper=get_event_audio_tracks_error_mapper,
            request_options=request_options,
        )

    def update_event_audio_tracks(
        self,
        live_event_id: float,
        *,
        body: LiveEventsAudioTracksRequest | LiveEventsAudioTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventAudioTracks, UpdateEventAudioTracksErrorBody]:
        """This method updates audio tracks settings on the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/audio_tracks"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[LiveEventsAudioTracksRequest | LiveEventsAudioTracksRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventAudioTracks],
            error_mapper=update_event_audio_tracks_error_mapper,
            request_options=request_options,
        )


class AsyncLiveAudioTracksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_event_audio_tracks(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventAudioTracks, GetEventAudioTracksErrorBody]:
        """This method returns audio tracks settings for the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/audio_tracks"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventAudioTracks],
            error_mapper=get_event_audio_tracks_error_mapper,
            request_options=request_options,
        )

    async def update_event_audio_tracks(
        self,
        live_event_id: float,
        *,
        body: LiveEventsAudioTracksRequest | LiveEventsAudioTracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventAudioTracks, UpdateEventAudioTracksErrorBody]:
        """This method updates audio tracks settings on the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/audio_tracks"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[LiveEventsAudioTracksRequest | LiveEventsAudioTracksRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventAudioTracks],
            error_mapper=update_event_audio_tracks_error_mapper,
            request_options=request_options,
        )
