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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.activate_live_event_alt1_error import (
    ActivateLiveEventAlt1ErrorBody,
    activate_live_event_alt1_error_mapper,
)
from ..errors.activate_live_event_alt2_error import (
    ActivateLiveEventAlt2ErrorBody,
    activate_live_event_alt2_error_mapper,
)
from ..errors.activate_live_event_error import ActivateLiveEventErrorBody, activate_live_event_error_mapper
from ..models.live_events_activate_request import LiveEventsActivateRequest, LiveEventsActivateRequestDict
from ..models.me_live_events_activate_request import MeLiveEventsActivateRequest, MeLiveEventsActivateRequestDict
from ..models.users_live_events_activate_request import (
    UsersLiveEventsActivateRequest,
    UsersLiveEventsActivateRequestDict,
)
from ..models.video import Video
from ..server.server import Server


class LiveEventActivation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventActivationWithRawResponse(client, server, auth)

    def activate_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsActivateRequest | UsersLiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was activated.

        Raises:
            ApiError: * Error code 2428: The event has already been activated. * Error code 2551: The session can't be
                activated when the scheduled media playback feature is enabled. Error code 8000: The user credentials
                are invalid. * Error code 3200: The authenticated user doesn't have the necessary permissions to stream
                to the event. * Error code 3422: The authenticated user can't activate the event. Error code 5000: No
                such event or user exists. Error code 4017: An unexpected error occurred. Error code 7701: The service
                is unavailable. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.activate_live_event(
                live_event_id, user_id, body=body, request_options=request_options
            ),
        )

    def activate_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsActivateRequest | LiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was activated.

        Raises:
            ApiError: * Error code 2428: The event has already been activated. * Error code 2551: The session can't be
                activated when the scheduled media playback feature is enabled. Error code 8000: The user credentials
                are invalid. * Error code 3200: The authenticated user doesn't have the necessary permissions to stream
                to the event. * Error code 3422: The authenticated user can't activate the event. Error code 5000: No
                such event or user exists. Error code 4017: An unexpected error occurred. Error code 7701: The service
                is unavailable. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.activate_live_event_alt1(live_event_id, body=body, request_options=request_options)
        )

    def activate_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsActivateRequest | MeLiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was activated.

        Raises:
            ApiError: * Error code 2428: The event has already been activated. * Error code 2551: The session can't be
                activated when the scheduled media playback feature is enabled. Error code 8000: The user credentials
                are invalid. * Error code 3200: The authenticated user doesn't have the necessary permissions to stream
                to the event. * Error code 3422: The authenticated user can't activate the event. Error code 5000: No
                such event or user exists. Error code 4017: An unexpected error occurred. Error code 7701: The service
                is unavailable. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.activate_live_event_alt2(live_event_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> LiveEventActivationWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventActivation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventActivationWithRawResponse(client, server, auth)

    async def activate_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsActivateRequest | UsersLiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was activated.

        Raises:
            ApiError: * Error code 2428: The event has already been activated. * Error code 2551: The session can't be
                activated when the scheduled media playback feature is enabled. Error code 8000: The user credentials
                are invalid. * Error code 3200: The authenticated user doesn't have the necessary permissions to stream
                to the event. * Error code 3422: The authenticated user can't activate the event. Error code 5000: No
                such event or user exists. Error code 4017: An unexpected error occurred. Error code 7701: The service
                is unavailable. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.activate_live_event(
                live_event_id, user_id, body=body, request_options=request_options
            ),
        )

    async def activate_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsActivateRequest | LiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was activated.

        Raises:
            ApiError: * Error code 2428: The event has already been activated. * Error code 2551: The session can't be
                activated when the scheduled media playback feature is enabled. Error code 8000: The user credentials
                are invalid. * Error code 3200: The authenticated user doesn't have the necessary permissions to stream
                to the event. * Error code 3422: The authenticated user can't activate the event. Error code 5000: No
                such event or user exists. Error code 4017: An unexpected error occurred. Error code 7701: The service
                is unavailable. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.activate_live_event_alt1(
                live_event_id, body=body, request_options=request_options
            ),
        )

    async def activate_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsActivateRequest | MeLiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was activated.

        Raises:
            ApiError: * Error code 2428: The event has already been activated. * Error code 2551: The session can't be
                activated when the scheduled media playback feature is enabled. Error code 8000: The user credentials
                are invalid. * Error code 3200: The authenticated user doesn't have the necessary permissions to stream
                to the event. * Error code 3422: The authenticated user can't activate the event. Error code 5000: No
                such event or user exists. Error code 4017: An unexpected error occurred. Error code 7701: The service
                is unavailable. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.activate_live_event_alt2(
                live_event_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncLiveEventActivationWithRawResponse:
        return self._with_raw_response


class LiveEventActivationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activate_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsActivateRequest | UsersLiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, ActivateLiveEventErrorBody]:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/activate"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsActivateRequest | UsersLiveEventsActivateRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=activate_live_event_error_mapper,
            request_options=request_options,
        )

    def activate_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsActivateRequest | LiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, ActivateLiveEventAlt1ErrorBody]:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/activate"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsActivateRequest | LiveEventsActivateRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=activate_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    def activate_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsActivateRequest | MeLiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, ActivateLiveEventAlt2ErrorBody]:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/activate"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsActivateRequest | MeLiveEventsActivateRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=activate_live_event_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEventActivationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activate_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsActivateRequest | UsersLiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, ActivateLiveEventErrorBody]:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/activate"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsActivateRequest | UsersLiveEventsActivateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=activate_live_event_error_mapper,
            request_options=request_options,
        )

    async def activate_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsActivateRequest | LiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, ActivateLiveEventAlt1ErrorBody]:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/activate"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsActivateRequest | LiveEventsActivateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=activate_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    async def activate_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsActivateRequest | MeLiveEventsActivateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, ActivateLiveEventAlt2ErrorBody]:
        """This method creates the necessary RTMP links for the specified event. Begin streaming to these links to
        trigger the event on Vimeo. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/activate"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsActivateRequest | MeLiveEventsActivateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=activate_live_event_alt2_error_mapper,
            request_options=request_options,
        )
