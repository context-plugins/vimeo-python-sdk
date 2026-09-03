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
from ..errors.toggle_rle_low_latency_alt1_error import (
    ToggleRleLowLatencyAlt1ErrorBody,
    toggle_rle_low_latency_alt1_error_mapper,
)
from ..errors.toggle_rle_low_latency_alt2_error import (
    ToggleRleLowLatencyAlt2ErrorBody,
    toggle_rle_low_latency_alt2_error_mapper,
)
from ..errors.toggle_rle_low_latency_error import ToggleRleLowLatencyErrorBody, toggle_rle_low_latency_error_mapper
from ..models.live_events_low_latency_request import LiveEventsLowLatencyRequest, LiveEventsLowLatencyRequestDict
from ..models.me_live_events_low_latency_request import MeLiveEventsLowLatencyRequest, MeLiveEventsLowLatencyRequestDict
from ..models.recurring_event_low_latency import RecurringEventLowLatency
from ..models.users_live_events_low_latency_request import (
    UsersLiveEventsLowLatencyRequest,
    UsersLiveEventsLowLatencyRequestDict,
)
from ..server.server import Server


class LiveEventLowLatency:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventLowLatencyWithRawResponse(client, server, auth)

    def toggle_rle_low_latency(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsLowLatencyRequest | UsersLiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEventLowLatency:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The low-latency status of the event was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't toggle the low-latency option of the event. Error
                code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.toggle_rle_low_latency(
            live_event_id, user_id, body=body, request_options=request_options
        ).unwrap()

    def toggle_rle_low_latency_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsLowLatencyRequest | LiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEventLowLatency:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The low-latency status of the event was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't toggle the low-latency option of the event. Error
                code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.toggle_rle_low_latency_alt1(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    def toggle_rle_low_latency_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsLowLatencyRequest | MeLiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEventLowLatency:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The low-latency status of the event was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't toggle the low-latency option of the event. Error
                code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.toggle_rle_low_latency_alt2(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveEventLowLatencyWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventLowLatency:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventLowLatencyWithRawResponse(client, server, auth)

    async def toggle_rle_low_latency(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsLowLatencyRequest | UsersLiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEventLowLatency:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The low-latency status of the event was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't toggle the low-latency option of the event. Error
                code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.toggle_rle_low_latency(
                live_event_id, user_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def toggle_rle_low_latency_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsLowLatencyRequest | LiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEventLowLatency:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The low-latency status of the event was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't toggle the low-latency option of the event. Error
                code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.toggle_rle_low_latency_alt1(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def toggle_rle_low_latency_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsLowLatencyRequest | MeLiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEventLowLatency:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The low-latency status of the event was returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't toggle the low-latency option of the event. Error
                code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.toggle_rle_low_latency_alt2(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveEventLowLatencyWithRawResponse:
        return self._with_raw_response


class LiveEventLowLatencyWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def toggle_rle_low_latency(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsLowLatencyRequest | UsersLiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyErrorBody]:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/low_latency"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsLowLatencyRequest | UsersLiveEventsLowLatencyRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEventLowLatency],
            error_mapper=toggle_rle_low_latency_error_mapper,
            request_options=request_options,
        )

    def toggle_rle_low_latency_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsLowLatencyRequest | LiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyAlt1ErrorBody]:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/low_latency"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsLowLatencyRequest | LiveEventsLowLatencyRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEventLowLatency],
            error_mapper=toggle_rle_low_latency_alt1_error_mapper,
            request_options=request_options,
        )

    def toggle_rle_low_latency_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsLowLatencyRequest | MeLiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyAlt2ErrorBody]:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/live_events/{live_event_id}/low_latency"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsLowLatencyRequest | MeLiveEventsLowLatencyRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEventLowLatency],
            error_mapper=toggle_rle_low_latency_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEventLowLatencyWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def toggle_rle_low_latency(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsLowLatencyRequest | UsersLiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyErrorBody]:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/low_latency"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsLowLatencyRequest | UsersLiveEventsLowLatencyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEventLowLatency],
            error_mapper=toggle_rle_low_latency_error_mapper,
            request_options=request_options,
        )

    async def toggle_rle_low_latency_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsLowLatencyRequest | LiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyAlt1ErrorBody]:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/low_latency"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsLowLatencyRequest | LiveEventsLowLatencyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEventLowLatency],
            error_mapper=toggle_rle_low_latency_alt1_error_mapper,
            request_options=request_options,
        )

    async def toggle_rle_low_latency_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsLowLatencyRequest | MeLiveEventsLowLatencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEventLowLatency, ToggleRleLowLatencyAlt2ErrorBody]:
        """This method toggles the low-latency option of the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/live_events/{live_event_id}/low_latency"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsLowLatencyRequest | MeLiveEventsLowLatencyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEventLowLatency],
            error_mapper=toggle_rle_low_latency_alt2_error_mapper,
            request_options=request_options,
        )
