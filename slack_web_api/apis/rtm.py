from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.content_type import ContentTypeOrStr
from ..models.rtm_connectschema import RtmConnectschema
from ..server.server import Server


class Rtm:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RtmWithRawResponse(client, server, auth)

    def rtm_connect(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        batch_presence_aware: bool | None = None,
        presence_sub: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RtmConnectschema:
        """Starts a Real Time Messaging session.

        Args:
            token: Authentication token. Requires scope: ``rtm:stream``
            content_type: Value sent with the request.
            batch_presence_aware: Batch presence deliveries via subscription. Enabling changes the shape of
                ``presence_change`` events.
            presence_sub: Only deliver presence events when requested by subscription
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.rtm_connect(
            token,
            content_type,
            batch_presence_aware=batch_presence_aware,
            presence_sub=presence_sub,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> RtmWithRawResponse:
        return self._with_raw_response


class AsyncRtm:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRtmWithRawResponse(client, server, auth)

    async def rtm_connect(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        batch_presence_aware: bool | None = None,
        presence_sub: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RtmConnectschema:
        """Starts a Real Time Messaging session.

        Args:
            token: Authentication token. Requires scope: ``rtm:stream``
            content_type: Value sent with the request.
            batch_presence_aware: Batch presence deliveries via subscription. Enabling changes the shape of
                ``presence_change`` events.
            presence_sub: Only deliver presence events when requested by subscription
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.rtm_connect(
                token,
                content_type,
                batch_presence_aware=batch_presence_aware,
                presence_sub=presence_sub,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncRtmWithRawResponse:
        return self._with_raw_response


class RtmWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def rtm_connect(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        batch_presence_aware: bool | None = None,
        presence_sub: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RtmConnectschema, RawError]:
        """Starts a Real Time Messaging session.

        Args:
            token: Authentication token. Requires scope: ``rtm:stream``
            content_type: Value sent with the request.
            batch_presence_aware: Batch presence deliveries via subscription. Enabling changes the shape of
                ``presence_change`` events.
            presence_sub: Only deliver presence events when requested by subscription
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/rtm.connect"),
            query_params=[
                param[str]("token", token),
                param[bool | None]("batch_presence_aware", batch_presence_aware),
                param[bool | None]("presence_sub", presence_sub),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RtmConnectschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncRtmWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def rtm_connect(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        batch_presence_aware: bool | None = None,
        presence_sub: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RtmConnectschema, RawError]:
        """Starts a Real Time Messaging session.

        Args:
            token: Authentication token. Requires scope: ``rtm:stream``
            content_type: Value sent with the request.
            batch_presence_aware: Batch presence deliveries via subscription. Enabling changes the shape of
                ``presence_change`` events.
            presence_sub: Only deliver presence events when requested by subscription
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/rtm.connect"),
            query_params=[
                param[str]("token", token),
                param[bool | None]("batch_presence_aware", batch_presence_aware),
                param[bool | None]("presence_sub", presence_sub),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RtmConnectschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
