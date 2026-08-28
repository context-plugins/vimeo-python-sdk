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
from ..models.chat_scheduled_messages_listschema import ChatScheduledMessagesListschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class ChatScheduledMessages:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChatScheduledMessagesWithRawResponse(client, server, auth)

    def chat_scheduled_messages_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatScheduledMessagesListschema:
        """Returns a list of scheduled messages.

        Args:
            content_type: Value sent with the request.
            channel: The channel of the scheduled messages
            latest: A UNIX timestamp of the latest value in the time range
            oldest: A UNIX timestamp of the oldest value in the time range
            limit: Maximum number of original entries to return.
            cursor: For pagination purposes, this is the ``cursor`` value returned from a previous call to
                ``chat.scheduledmessages.list`` indicating where you want to start this call from.
            token: Authentication token. Requires scope: ``none``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_scheduled_messages_list(
            content_type,
            channel=channel,
            latest=latest,
            oldest=oldest,
            limit=limit,
            cursor=cursor,
            token=token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ChatScheduledMessagesWithRawResponse:
        return self._with_raw_response


class AsyncChatScheduledMessages:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChatScheduledMessagesWithRawResponse(client, server, auth)

    async def chat_scheduled_messages_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatScheduledMessagesListschema:
        """Returns a list of scheduled messages.

        Args:
            content_type: Value sent with the request.
            channel: The channel of the scheduled messages
            latest: A UNIX timestamp of the latest value in the time range
            oldest: A UNIX timestamp of the oldest value in the time range
            limit: Maximum number of original entries to return.
            cursor: For pagination purposes, this is the ``cursor`` value returned from a previous call to
                ``chat.scheduledmessages.list`` indicating where you want to start this call from.
            token: Authentication token. Requires scope: ``none``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_scheduled_messages_list(
                content_type,
                channel=channel,
                latest=latest,
                oldest=oldest,
                limit=limit,
                cursor=cursor,
                token=token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncChatScheduledMessagesWithRawResponse:
        return self._with_raw_response


class ChatScheduledMessagesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def chat_scheduled_messages_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatScheduledMessagesListschema, RawError]:
        """Returns a list of scheduled messages.

        Args:
            content_type: Value sent with the request.
            channel: The channel of the scheduled messages
            latest: A UNIX timestamp of the latest value in the time range
            oldest: A UNIX timestamp of the oldest value in the time range
            limit: Maximum number of original entries to return.
            cursor: For pagination purposes, this is the ``cursor`` value returned from a previous call to
                ``chat.scheduledmessages.list`` indicating where you want to start this call from.
            token: Authentication token. Requires scope: ``none``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/chat.scheduledMessages.list"),
            query_params=[
                param[str | None]("channel", channel),
                param[float | None]("latest", latest),
                param[float | None]("oldest", oldest),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatScheduledMessagesListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncChatScheduledMessagesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def chat_scheduled_messages_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatScheduledMessagesListschema, RawError]:
        """Returns a list of scheduled messages.

        Args:
            content_type: Value sent with the request.
            channel: The channel of the scheduled messages
            latest: A UNIX timestamp of the latest value in the time range
            oldest: A UNIX timestamp of the oldest value in the time range
            limit: Maximum number of original entries to return.
            cursor: For pagination purposes, this is the ``cursor`` value returned from a previous call to
                ``chat.scheduledmessages.list`` indicating where you want to start this call from.
            token: Authentication token. Requires scope: ``none``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/chat.scheduledMessages.list"),
            query_params=[
                param[str | None]("channel", channel),
                param[float | None]("latest", latest),
                param[float | None]("oldest", oldest),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatScheduledMessagesListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
