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
    json_decoder,
    param,
)
from ..errors.end_live_event_alt1_error import EndLiveEventAlt1ErrorBody, end_live_event_alt1_error_mapper
from ..errors.end_live_event_alt2_error import EndLiveEventAlt2ErrorBody, end_live_event_alt2_error_mapper
from ..errors.end_live_event_error import EndLiveEventErrorBody, end_live_event_error_mapper
from ..models.video import Video
from ..server.server import Server


class LiveEventEnd:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventEndWithRawResponse(client, server, auth)

    def end_live_event(
        self,
        live_event_id: float,
        user_id: str,
        *,
        clip_id: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: Value sent with the request.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was ended.

        Raises:
            ApiError: Error code 10004: The event isn't being streamed. * Error code 3200: The user can't end the
                session. * Error code 3422: The authenticated user can't end the event. Error code 5000: No such event
                or user exists. Error code 4021: There is no video for the event. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.end_live_event(
            live_event_id, user_id, clip_id=clip_id, request_options=request_options
        ).unwrap()

    def end_live_event_alt1(
        self, live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was ended.

        Raises:
            ApiError: Error code 10004: The event isn't being streamed. * Error code 3200: The user can't end the
                session. * Error code 3422: The authenticated user can't end the event. Error code 5000: No such event
                or user exists. Error code 4021: There is no video for the event. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.end_live_event_alt1(
            live_event_id, clip_id=clip_id, request_options=request_options
        ).unwrap()

    def end_live_event_alt2(
        self, live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was ended.

        Raises:
            ApiError: Error code 10004: The event isn't being streamed. * Error code 3200: The user can't end the
                session. * Error code 3422: The authenticated user can't end the event. Error code 5000: No such event
                or user exists. Error code 4021: There is no video for the event. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.end_live_event_alt2(
            live_event_id, clip_id=clip_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveEventEndWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventEnd:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventEndWithRawResponse(client, server, auth)

    async def end_live_event(
        self,
        live_event_id: float,
        user_id: str,
        *,
        clip_id: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: Value sent with the request.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was ended.

        Raises:
            ApiError: Error code 10004: The event isn't being streamed. * Error code 3200: The user can't end the
                session. * Error code 3422: The authenticated user can't end the event. Error code 5000: No such event
                or user exists. Error code 4021: There is no video for the event. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.end_live_event(
                live_event_id, user_id, clip_id=clip_id, request_options=request_options
            )
        ).unwrap()

    async def end_live_event_alt1(
        self, live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was ended.

        Raises:
            ApiError: Error code 10004: The event isn't being streamed. * Error code 3200: The user can't end the
                session. * Error code 3422: The authenticated user can't end the event. Error code 5000: No such event
                or user exists. Error code 4021: There is no video for the event. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.end_live_event_alt1(
                live_event_id, clip_id=clip_id, request_options=request_options
            )
        ).unwrap()

    async def end_live_event_alt2(
        self, live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was ended.

        Raises:
            ApiError: Error code 10004: The event isn't being streamed. * Error code 3200: The user can't end the
                session. * Error code 3422: The authenticated user can't end the event. Error code 5000: No such event
                or user exists. Error code 4021: There is no video for the event. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.end_live_event_alt2(
                live_event_id, clip_id=clip_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveEventEndWithRawResponse:
        return self._with_raw_response


class LiveEventEndWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def end_live_event(
        self,
        live_event_id: float,
        user_id: str,
        *,
        clip_id: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, EndLiveEventErrorBody]:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: Value sent with the request.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/end"),
            path_params=[param[float]("live_event_id", live_event_id), param[str]("user_id", user_id)],
            query_params=[param[float | None]("clip_id", clip_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=end_live_event_error_mapper,
            request_options=request_options,
        )

    def end_live_event_alt1(
        self, live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, EndLiveEventAlt1ErrorBody]:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/end"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[param[float | None]("clip_id", clip_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=end_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    def end_live_event_alt2(
        self, live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, EndLiveEventAlt2ErrorBody]:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/end"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[param[float | None]("clip_id", clip_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=end_live_event_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEventEndWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def end_live_event(
        self,
        live_event_id: float,
        user_id: str,
        *,
        clip_id: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, EndLiveEventErrorBody]:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: Value sent with the request.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/end"),
            path_params=[param[float]("live_event_id", live_event_id), param[str]("user_id", user_id)],
            query_params=[param[float | None]("clip_id", clip_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=end_live_event_error_mapper,
            request_options=request_options,
        )

    async def end_live_event_alt1(
        self, live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, EndLiveEventAlt1ErrorBody]:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/end"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[param[float | None]("clip_id", clip_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=end_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    async def end_live_event_alt2(
        self, live_event_id: float, *, clip_id: float | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, EndLiveEventAlt2ErrorBody]:
        """This method ends the specified event. The authenticated user must be the owner of the event.

        Args:
            live_event_id: The ID of the event.
            clip_id: The ID of the streamable video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/end"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[param[float | None]("clip_id", clip_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=end_live_event_alt2_error_mapper,
            request_options=request_options,
        )
