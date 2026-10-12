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
from ..errors.edit_live_event_auto_cc_alt1_error import (
    EditLiveEventAutoCcAlt1ErrorBody,
    edit_live_event_auto_cc_alt1_error_mapper,
)
from ..errors.edit_live_event_auto_cc_alt2_error import (
    EditLiveEventAutoCcAlt2ErrorBody,
    edit_live_event_auto_cc_alt2_error_mapper,
)
from ..errors.edit_live_event_auto_cc_error import EditLiveEventAutoCcErrorBody, edit_live_event_auto_cc_error_mapper
from ..models.event_automated_closed_captions import EventAutomatedClosedCaptions
from ..models.live_events_auto_cc_request import LiveEventsAutoCcRequest, LiveEventsAutoCcRequestDict
from ..models.me_live_events_auto_cc_request import MeLiveEventsAutoCcRequest, MeLiveEventsAutoCcRequestDict
from ..models.users_live_events_auto_cc_request import UsersLiveEventsAutoCcRequest, UsersLiveEventsAutoCcRequestDict
from ..server.server import Server


class LiveEventAutomatedClosedCaptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventAutomatedClosedCaptionsWithRawResponse(client, server, auth)

    def edit_live_event_auto_cc(
        self,
        live_event_id: float,
        user_id: float,
        body: UsersLiveEventsAutoCcRequest | UsersLiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventAutomatedClosedCaptions:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The automated closed captions preference was edited.

        Raises:
            ApiError: Error code 2204: The payload is invalid. * Error code 3200: The user doesn't have permission to
                edit the closed captions preference for the specified event. * Error code 3422: The authenticated user
                can't edit the closed captions preference for the specified event. * Error code 3439: The authenticated
                user has reached the automated closed captions usage limit, or they can't use the automated closed
                captions feature at all. * Error code 3459: The authenticated user can't use the automated closed
                captions translation feature. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            self._with_raw_response.edit_live_event_auto_cc(
                live_event_id, user_id, body, request_options=request_options
            ),
        )

    def edit_live_event_auto_cc_alt1(
        self,
        live_event_id: float,
        body: LiveEventsAutoCcRequest | LiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventAutomatedClosedCaptions:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The automated closed captions preference was edited.

        Raises:
            ApiError: Error code 2204: The payload is invalid. * Error code 3200: The user doesn't have permission to
                edit the closed captions preference for the specified event. * Error code 3422: The authenticated user
                can't edit the closed captions preference for the specified event. * Error code 3439: The authenticated
                user has reached the automated closed captions usage limit, or they can't use the automated closed
                captions feature at all. * Error code 3459: The authenticated user can't use the automated closed
                captions translation feature. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            self._with_raw_response.edit_live_event_auto_cc_alt1(live_event_id, body, request_options=request_options)
        )

    def edit_live_event_auto_cc_alt2(
        self,
        live_event_id: float,
        body: MeLiveEventsAutoCcRequest | MeLiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventAutomatedClosedCaptions:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The automated closed captions preference was edited.

        Raises:
            ApiError: Error code 2204: The payload is invalid. * Error code 3200: The user doesn't have permission to
                edit the closed captions preference for the specified event. * Error code 3422: The authenticated user
                can't edit the closed captions preference for the specified event. * Error code 3439: The authenticated
                user has reached the automated closed captions usage limit, or they can't use the automated closed
                captions feature at all. * Error code 3459: The authenticated user can't use the automated closed
                captions translation feature. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            self._with_raw_response.edit_live_event_auto_cc_alt2(live_event_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> LiveEventAutomatedClosedCaptionsWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventAutomatedClosedCaptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventAutomatedClosedCaptionsWithRawResponse(client, server, auth)

    async def edit_live_event_auto_cc(
        self,
        live_event_id: float,
        user_id: float,
        body: UsersLiveEventsAutoCcRequest | UsersLiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventAutomatedClosedCaptions:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The automated closed captions preference was edited.

        Raises:
            ApiError: Error code 2204: The payload is invalid. * Error code 3200: The user doesn't have permission to
                edit the closed captions preference for the specified event. * Error code 3422: The authenticated user
                can't edit the closed captions preference for the specified event. * Error code 3439: The authenticated
                user has reached the automated closed captions usage limit, or they can't use the automated closed
                captions feature at all. * Error code 3459: The authenticated user can't use the automated closed
                captions translation feature. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            await self._with_raw_response.edit_live_event_auto_cc(
                live_event_id, user_id, body, request_options=request_options
            ),
        )

    async def edit_live_event_auto_cc_alt1(
        self,
        live_event_id: float,
        body: LiveEventsAutoCcRequest | LiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventAutomatedClosedCaptions:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The automated closed captions preference was edited.

        Raises:
            ApiError: Error code 2204: The payload is invalid. * Error code 3200: The user doesn't have permission to
                edit the closed captions preference for the specified event. * Error code 3422: The authenticated user
                can't edit the closed captions preference for the specified event. * Error code 3439: The authenticated
                user has reached the automated closed captions usage limit, or they can't use the automated closed
                captions feature at all. * Error code 3459: The authenticated user can't use the automated closed
                captions translation feature. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            await self._with_raw_response.edit_live_event_auto_cc_alt1(
                live_event_id, body, request_options=request_options
            ),
        )

    async def edit_live_event_auto_cc_alt2(
        self,
        live_event_id: float,
        body: MeLiveEventsAutoCcRequest | MeLiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventAutomatedClosedCaptions:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The automated closed captions preference was edited.

        Raises:
            ApiError: Error code 2204: The payload is invalid. * Error code 3200: The user doesn't have permission to
                edit the closed captions preference for the specified event. * Error code 3422: The authenticated user
                can't edit the closed captions preference for the specified event. * Error code 3439: The authenticated
                user has reached the automated closed captions usage limit, or they can't use the automated closed
                captions feature at all. * Error code 3459: The authenticated user can't use the automated closed
                captions translation feature. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            await self._with_raw_response.edit_live_event_auto_cc_alt2(
                live_event_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncLiveEventAutomatedClosedCaptionsWithRawResponse:
        return self._with_raw_response


class LiveEventAutomatedClosedCaptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def edit_live_event_auto_cc(
        self,
        live_event_id: float,
        user_id: float,
        body: UsersLiveEventsAutoCcRequest | UsersLiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcErrorBody]:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/auto_cc"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsAutoCcRequest | UsersLiveEventsAutoCcRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventAutomatedClosedCaptions],
            error_mapper=edit_live_event_auto_cc_error_mapper,
            request_options=request_options,
        )

    def edit_live_event_auto_cc_alt1(
        self,
        live_event_id: float,
        body: LiveEventsAutoCcRequest | LiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcAlt1ErrorBody]:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/auto_cc"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsAutoCcRequest | LiveEventsAutoCcRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventAutomatedClosedCaptions],
            error_mapper=edit_live_event_auto_cc_alt1_error_mapper,
            request_options=request_options,
        )

    def edit_live_event_auto_cc_alt2(
        self,
        live_event_id: float,
        body: MeLiveEventsAutoCcRequest | MeLiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcAlt2ErrorBody]:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/live_events/{live_event_id}/auto_cc"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsAutoCcRequest | MeLiveEventsAutoCcRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventAutomatedClosedCaptions],
            error_mapper=edit_live_event_auto_cc_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEventAutomatedClosedCaptionsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def edit_live_event_auto_cc(
        self,
        live_event_id: float,
        user_id: float,
        body: UsersLiveEventsAutoCcRequest | UsersLiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcErrorBody]:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/auto_cc"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsAutoCcRequest | UsersLiveEventsAutoCcRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[EventAutomatedClosedCaptions],
            error_mapper=edit_live_event_auto_cc_error_mapper,
            request_options=request_options,
        )

    async def edit_live_event_auto_cc_alt1(
        self,
        live_event_id: float,
        body: LiveEventsAutoCcRequest | LiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcAlt1ErrorBody]:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/auto_cc"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsAutoCcRequest | LiveEventsAutoCcRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[EventAutomatedClosedCaptions],
            error_mapper=edit_live_event_auto_cc_alt1_error_mapper,
            request_options=request_options,
        )

    async def edit_live_event_auto_cc_alt2(
        self,
        live_event_id: float,
        body: MeLiveEventsAutoCcRequest | MeLiveEventsAutoCcRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventAutomatedClosedCaptions, EditLiveEventAutoCcAlt2ErrorBody]:
        """This method edits the automated closed captions preference for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/live_events/{live_event_id}/auto_cc"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsAutoCcRequest | MeLiveEventsAutoCcRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[EventAutomatedClosedCaptions],
            error_mapper=edit_live_event_auto_cc_alt2_error_mapper,
            request_options=request_options,
        )
