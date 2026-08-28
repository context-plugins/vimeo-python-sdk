from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.chat_delete_scheduled_messageschema import ChatDeleteScheduledMessageschema
from ..models.chat_deletesuccessschema import ChatDeletesuccessschema
from ..models.chat_get_permalinksuccessschema import ChatGetPermalinksuccessschema
from ..models.chat_me_messageschema import ChatMeMessageschema
from ..models.chat_post_ephemeralsuccessschema import ChatPostEphemeralsuccessschema
from ..models.chat_post_messagesuccessschema import ChatPostMessagesuccessschema
from ..models.chat_schedule_messagesuccessschema import ChatScheduleMessagesuccessschema
from ..models.chat_scheduled_messages_listschema import ChatScheduledMessagesListschema
from ..models.chat_unfurlsuccessschema import ChatUnfurlsuccessschema
from ..models.chat_updatesuccessschema import ChatUpdatesuccessschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Chat:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChatWithRawResponse(client, server, auth)

    def chat_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        ts: float | None = None,
        channel: str | None = None,
        as_user: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatDeletesuccessschema:
        """Deletes a message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            ts: Timestamp of the message to be deleted.
            channel: Channel containing the message to be deleted.
            as_user: Pass true to delete the message as the authed user with ``chat:write:user`` scope. `Bot users
                </bot-users>`__ in this context are considered authed users. If unused or false, the message will be
                deleted with ``chat:write:bot`` scope.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_delete(
            content_type, token=token, ts=ts, channel=channel, as_user=as_user, request_options=request_options
        ).unwrap()

    def chat_delete_scheduled_message(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        scheduled_message_id: str,
        *,
        as_user: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatDeleteScheduledMessageschema:
        """Deletes a pending scheduled message from the queue.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: The channel the scheduled_message is posting to
            scheduled_message_id: ``scheduled_message_id`` returned from call to chat.scheduleMessage
            as_user: Pass true to delete the message as the authed user with ``chat:write:user`` scope. `Bot users
                </bot-users>`__ in this context are considered authed users. If unused or false, the message will be
                deleted with ``chat:write:bot`` scope.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_delete_scheduled_message(
            token, content_type, channel, scheduled_message_id, as_user=as_user, request_options=request_options
        ).unwrap()

    def chat_get_permalink(
        self,
        token: str,
        channel: str,
        message_ts: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatGetPermalinksuccessschema:
        """Retrieve a permalink URL for a specific extant message

        Args:
            token: Authentication token. Requires scope: ``none``
            channel: The ID of the conversation or channel containing the message
            message_ts: A message's ``ts`` value, uniquely identifying it within a channel
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_get_permalink(
            token, channel, message_ts, content_type, request_options=request_options
        ).unwrap()

    def chat_me_message(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        text: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatMeMessageschema:
        """Share a me message into a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            channel: Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded
                ID, or a name.
            text: Text of the message to send.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_me_message(
            content_type, token=token, channel=channel, text=text, request_options=request_options
        ).unwrap()

    def chat_post_ephemeral(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        user: str,
        *,
        as_user: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        parse: str | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatPostEphemeralsuccessschema:
        """Sends an ephemeral message to a user in a channel.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
            user: ``id`` of the user who will receive the ephemeral message. The user should be in the channel specified
                by the ``channel`` argument.
            as_user: Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is
                not included. Otherwise, defaults to false.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji: Emoji to use as the icon for this message. Overrides ``icon_url``. Must be used in conjunction
                with ``as_user`` set to ``false``, otherwise ignored. See `authorship <#authorship>`__ below.
            icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with ``as_user``
                set to false, otherwise ignored. See `authorship <#authorship>`__ below.
            link_names: Find and link channel names and usernames.
            parse: Change how messages are treated. Defaults to ``none``. See `below <#formatting>`__.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            thread_ts: Provide another message's ``ts`` value to post this message in a thread. Avoid using a reply's
                ``ts`` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is
                already an active thread.
            username: Set your bot's user name. Must be used in conjunction with ``as_user`` set to false, otherwise
                ignored. See `authorship <#authorship>`__ below.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_post_ephemeral(
            token,
            content_type,
            channel,
            user,
            as_user=as_user,
            attachments=attachments,
            blocks=blocks,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            link_names=link_names,
            parse=parse,
            text=text,
            thread_ts=thread_ts,
            username=username,
            request_options=request_options,
        ).unwrap()

    def chat_post_message(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        mrkdwn: bool | None = None,
        parse: str | None = None,
        reply_broadcast: bool | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatPostMessagesuccessschema:
        """Sends a message to a channel.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See
                `below <#channels>`__ for more details.
            as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See
                `authorship <#authorship>`__ below.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji: Emoji to use as the icon for this message. Overrides ``icon_url``. Must be used in conjunction
                with ``as_user`` set to ``false``, otherwise ignored. See `authorship <#authorship>`__ below.
            icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with ``as_user``
                set to false, otherwise ignored. See `authorship <#authorship>`__ below.
            link_names: Find and link channel names and usernames.
            mrkdwn: Disable Slack markup parsing by setting to ``false``. Enabled by default.
            parse: Change how messages are treated. Defaults to ``none``. See `below <#formatting>`__.
            reply_broadcast: Used in conjunction with ``thread_ts`` and indicates whether reply should be made visible
                to everyone in the channel or conversation. Defaults to ``false``.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            thread_ts: Provide another message's ``ts`` value to make this message a reply. Avoid using a reply's ``ts``
                value; use its parent instead.
            unfurl_links: Pass true to enable unfurling of primarily text-based content.
            unfurl_media: Pass false to disable unfurling of media content.
            username: Set your bot's user name. Must be used in conjunction with ``as_user`` set to false, otherwise
                ignored. See `authorship <#authorship>`__ below.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_post_message(
            token,
            content_type,
            channel,
            as_user=as_user,
            attachments=attachments,
            blocks=blocks,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            link_names=link_names,
            mrkdwn=mrkdwn,
            parse=parse,
            reply_broadcast=reply_broadcast,
            text=text,
            thread_ts=thread_ts,
            unfurl_links=unfurl_links,
            unfurl_media=unfurl_media,
            username=username,
            request_options=request_options,
        ).unwrap()

    def chat_schedule_message(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        text: str | None = None,
        post_at: str | None = None,
        parse: str | None = None,
        as_user: bool | None = None,
        link_names: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        thread_ts: float | None = None,
        reply_broadcast: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatScheduleMessagesuccessschema:
        """Schedules a message to be sent to a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            channel: Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See
                `below <#channels>`__ for more details.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            post_at: Unix EPOCH timestamp of time in future to send the message.
            parse: Change how messages are treated. Defaults to ``none``. See `chat.postMessage
                <chat.postMessage#formatting>`__.
            as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See
                `chat.postMessage <chat.postMessage#authorship>`__.
            link_names: Find and link channel names and usernames.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            unfurl_links: Pass true to enable unfurling of primarily text-based content.
            unfurl_media: Pass false to disable unfurling of media content.
            thread_ts: Provide another message's ``ts`` value to make this message a reply. Avoid using a reply's ``ts``
                value; use its parent instead.
            reply_broadcast: Used in conjunction with ``thread_ts`` and indicates whether reply should be made visible
                to everyone in the channel or conversation. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_schedule_message(
            content_type,
            token=token,
            channel=channel,
            text=text,
            post_at=post_at,
            parse=parse,
            as_user=as_user,
            link_names=link_names,
            attachments=attachments,
            blocks=blocks,
            unfurl_links=unfurl_links,
            unfurl_media=unfurl_media,
            thread_ts=thread_ts,
            reply_broadcast=reply_broadcast,
            request_options=request_options,
        ).unwrap()

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

    def chat_unfurl(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        ts: str,
        *,
        unfurls: str | None = None,
        user_auth_message: str | None = None,
        user_auth_required: bool | None = None,
        user_auth_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatUnfurlsuccessschema:
        """Provide custom unfurl behavior for user-posted URLs

        Args:
            token: Authentication token. Requires scope: ``links:write``
            content_type: Value sent with the request.
            channel: Channel ID of the message
            ts: Timestamp of the message to add unfurl behavior to.
            unfurls: URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl
                blocks or message attachments.
            user_auth_message: Provide a simply-formatted string to send as an ephemeral message to the user as
                invitation to authenticate further and enable full unfurling behavior
            user_auth_required: Set to ``true`` or ``1`` to indicate the user must install your Slack app to trigger
                unfurls for this domain
            user_auth_url: Send users to this custom URL where they will complete authentication in your app to fully
                trigger unfurling. Value should be properly URL-encoded.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical, minimal success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_unfurl(
            token,
            content_type,
            channel,
            ts,
            unfurls=unfurls,
            user_auth_message=user_auth_message,
            user_auth_required=user_auth_required,
            user_auth_url=user_auth_url,
            request_options=request_options,
        ).unwrap()

    def chat_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        ts: str,
        *,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        link_names: str | None = None,
        parse: str | None = None,
        text: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatUpdatesuccessschema:
        """Updates a message.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel containing the message to be updated.
            ts: Timestamp of the message to be updated.
            as_user: Pass true to update the message as the authed user. `Bot users </bot-users>`__ in this context are
                considered authed users.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string. This field is
                required when not presenting ``text``. If you don't include this field, the message's previous
                ``attachments`` will be retained. To remove previous ``attachments``, include an empty array for this
                field.
            blocks: A JSON-based array of `structured blocks </block-kit/building>`__, presented as a URL-encoded
                string. If you don't include this field, the message's previous ``blocks`` will be retained. To remove
                previous ``blocks``, include an empty array for this field.
            link_names: Find and link channel names and usernames. Defaults to ``none``. If you do not specify a value
                for this field, the original value set for the message will be overwritten with the default, ``none``.
            parse: Change how messages are treated. Defaults to ``client``, unlike ``chat.postMessage``. Accepts either
                ``none`` or ``full``. If you do not specify a value for this field, the original value set for the
                message will be overwritten with the default, ``client``.
            text: New text for the message, using the `default formatting rules </reference/surfaces/formatting>`__.
                It's not required when presenting ``blocks`` or ``attachments``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chat_update(
            token,
            content_type,
            channel,
            ts,
            as_user=as_user,
            attachments=attachments,
            blocks=blocks,
            link_names=link_names,
            parse=parse,
            text=text,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ChatWithRawResponse:
        return self._with_raw_response


class AsyncChat:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChatWithRawResponse(client, server, auth)

    async def chat_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        ts: float | None = None,
        channel: str | None = None,
        as_user: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatDeletesuccessschema:
        """Deletes a message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            ts: Timestamp of the message to be deleted.
            channel: Channel containing the message to be deleted.
            as_user: Pass true to delete the message as the authed user with ``chat:write:user`` scope. `Bot users
                </bot-users>`__ in this context are considered authed users. If unused or false, the message will be
                deleted with ``chat:write:bot`` scope.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_delete(
                content_type, token=token, ts=ts, channel=channel, as_user=as_user, request_options=request_options
            )
        ).unwrap()

    async def chat_delete_scheduled_message(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        scheduled_message_id: str,
        *,
        as_user: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatDeleteScheduledMessageschema:
        """Deletes a pending scheduled message from the queue.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: The channel the scheduled_message is posting to
            scheduled_message_id: ``scheduled_message_id`` returned from call to chat.scheduleMessage
            as_user: Pass true to delete the message as the authed user with ``chat:write:user`` scope. `Bot users
                </bot-users>`__ in this context are considered authed users. If unused or false, the message will be
                deleted with ``chat:write:bot`` scope.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_delete_scheduled_message(
                token, content_type, channel, scheduled_message_id, as_user=as_user, request_options=request_options
            )
        ).unwrap()

    async def chat_get_permalink(
        self,
        token: str,
        channel: str,
        message_ts: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatGetPermalinksuccessschema:
        """Retrieve a permalink URL for a specific extant message

        Args:
            token: Authentication token. Requires scope: ``none``
            channel: The ID of the conversation or channel containing the message
            message_ts: A message's ``ts`` value, uniquely identifying it within a channel
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_get_permalink(
                token, channel, message_ts, content_type, request_options=request_options
            )
        ).unwrap()

    async def chat_me_message(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        text: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatMeMessageschema:
        """Share a me message into a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            channel: Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded
                ID, or a name.
            text: Text of the message to send.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_me_message(
                content_type, token=token, channel=channel, text=text, request_options=request_options
            )
        ).unwrap()

    async def chat_post_ephemeral(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        user: str,
        *,
        as_user: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        parse: str | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatPostEphemeralsuccessschema:
        """Sends an ephemeral message to a user in a channel.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
            user: ``id`` of the user who will receive the ephemeral message. The user should be in the channel specified
                by the ``channel`` argument.
            as_user: Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is
                not included. Otherwise, defaults to false.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji: Emoji to use as the icon for this message. Overrides ``icon_url``. Must be used in conjunction
                with ``as_user`` set to ``false``, otherwise ignored. See `authorship <#authorship>`__ below.
            icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with ``as_user``
                set to false, otherwise ignored. See `authorship <#authorship>`__ below.
            link_names: Find and link channel names and usernames.
            parse: Change how messages are treated. Defaults to ``none``. See `below <#formatting>`__.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            thread_ts: Provide another message's ``ts`` value to post this message in a thread. Avoid using a reply's
                ``ts`` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is
                already an active thread.
            username: Set your bot's user name. Must be used in conjunction with ``as_user`` set to false, otherwise
                ignored. See `authorship <#authorship>`__ below.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_post_ephemeral(
                token,
                content_type,
                channel,
                user,
                as_user=as_user,
                attachments=attachments,
                blocks=blocks,
                icon_emoji=icon_emoji,
                icon_url=icon_url,
                link_names=link_names,
                parse=parse,
                text=text,
                thread_ts=thread_ts,
                username=username,
                request_options=request_options,
            )
        ).unwrap()

    async def chat_post_message(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        mrkdwn: bool | None = None,
        parse: str | None = None,
        reply_broadcast: bool | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatPostMessagesuccessschema:
        """Sends a message to a channel.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See
                `below <#channels>`__ for more details.
            as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See
                `authorship <#authorship>`__ below.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji: Emoji to use as the icon for this message. Overrides ``icon_url``. Must be used in conjunction
                with ``as_user`` set to ``false``, otherwise ignored. See `authorship <#authorship>`__ below.
            icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with ``as_user``
                set to false, otherwise ignored. See `authorship <#authorship>`__ below.
            link_names: Find and link channel names and usernames.
            mrkdwn: Disable Slack markup parsing by setting to ``false``. Enabled by default.
            parse: Change how messages are treated. Defaults to ``none``. See `below <#formatting>`__.
            reply_broadcast: Used in conjunction with ``thread_ts`` and indicates whether reply should be made visible
                to everyone in the channel or conversation. Defaults to ``false``.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            thread_ts: Provide another message's ``ts`` value to make this message a reply. Avoid using a reply's ``ts``
                value; use its parent instead.
            unfurl_links: Pass true to enable unfurling of primarily text-based content.
            unfurl_media: Pass false to disable unfurling of media content.
            username: Set your bot's user name. Must be used in conjunction with ``as_user`` set to false, otherwise
                ignored. See `authorship <#authorship>`__ below.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_post_message(
                token,
                content_type,
                channel,
                as_user=as_user,
                attachments=attachments,
                blocks=blocks,
                icon_emoji=icon_emoji,
                icon_url=icon_url,
                link_names=link_names,
                mrkdwn=mrkdwn,
                parse=parse,
                reply_broadcast=reply_broadcast,
                text=text,
                thread_ts=thread_ts,
                unfurl_links=unfurl_links,
                unfurl_media=unfurl_media,
                username=username,
                request_options=request_options,
            )
        ).unwrap()

    async def chat_schedule_message(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        text: str | None = None,
        post_at: str | None = None,
        parse: str | None = None,
        as_user: bool | None = None,
        link_names: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        thread_ts: float | None = None,
        reply_broadcast: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatScheduleMessagesuccessschema:
        """Schedules a message to be sent to a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            channel: Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See
                `below <#channels>`__ for more details.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            post_at: Unix EPOCH timestamp of time in future to send the message.
            parse: Change how messages are treated. Defaults to ``none``. See `chat.postMessage
                <chat.postMessage#formatting>`__.
            as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See
                `chat.postMessage <chat.postMessage#authorship>`__.
            link_names: Find and link channel names and usernames.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            unfurl_links: Pass true to enable unfurling of primarily text-based content.
            unfurl_media: Pass false to disable unfurling of media content.
            thread_ts: Provide another message's ``ts`` value to make this message a reply. Avoid using a reply's ``ts``
                value; use its parent instead.
            reply_broadcast: Used in conjunction with ``thread_ts`` and indicates whether reply should be made visible
                to everyone in the channel or conversation. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_schedule_message(
                content_type,
                token=token,
                channel=channel,
                text=text,
                post_at=post_at,
                parse=parse,
                as_user=as_user,
                link_names=link_names,
                attachments=attachments,
                blocks=blocks,
                unfurl_links=unfurl_links,
                unfurl_media=unfurl_media,
                thread_ts=thread_ts,
                reply_broadcast=reply_broadcast,
                request_options=request_options,
            )
        ).unwrap()

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

    async def chat_unfurl(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        ts: str,
        *,
        unfurls: str | None = None,
        user_auth_message: str | None = None,
        user_auth_required: bool | None = None,
        user_auth_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatUnfurlsuccessschema:
        """Provide custom unfurl behavior for user-posted URLs

        Args:
            token: Authentication token. Requires scope: ``links:write``
            content_type: Value sent with the request.
            channel: Channel ID of the message
            ts: Timestamp of the message to add unfurl behavior to.
            unfurls: URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl
                blocks or message attachments.
            user_auth_message: Provide a simply-formatted string to send as an ephemeral message to the user as
                invitation to authenticate further and enable full unfurling behavior
            user_auth_required: Set to ``true`` or ``1`` to indicate the user must install your Slack app to trigger
                unfurls for this domain
            user_auth_url: Send users to this custom URL where they will complete authentication in your app to fully
                trigger unfurling. Value should be properly URL-encoded.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical, minimal success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_unfurl(
                token,
                content_type,
                channel,
                ts,
                unfurls=unfurls,
                user_auth_message=user_auth_message,
                user_auth_required=user_auth_required,
                user_auth_url=user_auth_url,
                request_options=request_options,
            )
        ).unwrap()

    async def chat_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        ts: str,
        *,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        link_names: str | None = None,
        parse: str | None = None,
        text: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChatUpdatesuccessschema:
        """Updates a message.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel containing the message to be updated.
            ts: Timestamp of the message to be updated.
            as_user: Pass true to update the message as the authed user. `Bot users </bot-users>`__ in this context are
                considered authed users.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string. This field is
                required when not presenting ``text``. If you don't include this field, the message's previous
                ``attachments`` will be retained. To remove previous ``attachments``, include an empty array for this
                field.
            blocks: A JSON-based array of `structured blocks </block-kit/building>`__, presented as a URL-encoded
                string. If you don't include this field, the message's previous ``blocks`` will be retained. To remove
                previous ``blocks``, include an empty array for this field.
            link_names: Find and link channel names and usernames. Defaults to ``none``. If you do not specify a value
                for this field, the original value set for the message will be overwritten with the default, ``none``.
            parse: Change how messages are treated. Defaults to ``client``, unlike ``chat.postMessage``. Accepts either
                ``none`` or ``full``. If you do not specify a value for this field, the original value set for the
                message will be overwritten with the default, ``client``.
            text: New text for the message, using the `default formatting rules </reference/surfaces/formatting>`__.
                It's not required when presenting ``blocks`` or ``attachments``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.chat_update(
                token,
                content_type,
                channel,
                ts,
                as_user=as_user,
                attachments=attachments,
                blocks=blocks,
                link_names=link_names,
                parse=parse,
                text=text,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncChatWithRawResponse:
        return self._with_raw_response


class ChatWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def chat_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        ts: float | None = None,
        channel: str | None = None,
        as_user: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatDeletesuccessschema, RawError]:
        """Deletes a message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            ts: Timestamp of the message to be deleted.
            channel: Channel containing the message to be deleted.
            as_user: Pass true to delete the message as the authed user with ``chat:write:user`` scope. `Bot users
                </bot-users>`__ in this context are considered authed users. If unused or false, the message will be
                deleted with ``chat:write:bot`` scope.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.delete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body(
                [
                    param[float | None]("ts", ts),
                    param[str | None]("channel", channel),
                    param[bool | None]("as_user", as_user),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatDeletesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chat_delete_scheduled_message(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        scheduled_message_id: str,
        *,
        as_user: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatDeleteScheduledMessageschema, RawError]:
        """Deletes a pending scheduled message from the queue.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: The channel the scheduled_message is posting to
            scheduled_message_id: ``scheduled_message_id`` returned from call to chat.scheduleMessage
            as_user: Pass true to delete the message as the authed user with ``chat:write:user`` scope. `Bot users
                </bot-users>`__ in this context are considered authed users. If unused or false, the message will be
                deleted with ``chat:write:bot`` scope.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.deleteScheduledMessage"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str]("scheduled_message_id", scheduled_message_id),
                    param[bool | None]("as_user", as_user),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatDeleteScheduledMessageschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chat_get_permalink(
        self,
        token: str,
        channel: str,
        message_ts: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatGetPermalinksuccessschema, RawError]:
        """Retrieve a permalink URL for a specific extant message

        Args:
            token: Authentication token. Requires scope: ``none``
            channel: The ID of the conversation or channel containing the message
            message_ts: A message's ``ts`` value, uniquely identifying it within a channel
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/chat.getPermalink"),
            query_params=[
                param[str]("token", token), param[str]("channel", channel), param[str]("message_ts", message_ts)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatGetPermalinksuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chat_me_message(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        text: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatMeMessageschema, RawError]:
        """Share a me message into a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            channel: Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded
                ID, or a name.
            text: Text of the message to send.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.meMessage"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("text", text)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatMeMessageschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chat_post_ephemeral(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        user: str,
        *,
        as_user: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        parse: str | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatPostEphemeralsuccessschema, RawError]:
        """Sends an ephemeral message to a user in a channel.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
            user: ``id`` of the user who will receive the ephemeral message. The user should be in the channel specified
                by the ``channel`` argument.
            as_user: Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is
                not included. Otherwise, defaults to false.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji: Emoji to use as the icon for this message. Overrides ``icon_url``. Must be used in conjunction
                with ``as_user`` set to ``false``, otherwise ignored. See `authorship <#authorship>`__ below.
            icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with ``as_user``
                set to false, otherwise ignored. See `authorship <#authorship>`__ below.
            link_names: Find and link channel names and usernames.
            parse: Change how messages are treated. Defaults to ``none``. See `below <#formatting>`__.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            thread_ts: Provide another message's ``ts`` value to post this message in a thread. Avoid using a reply's
                ``ts`` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is
                already an active thread.
            username: Set your bot's user name. Must be used in conjunction with ``as_user`` set to false, otherwise
                ignored. See `authorship <#authorship>`__ below.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.postEphemeral"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str]("user", user),
                    param[bool | None]("as_user", as_user),
                    param[str | None]("attachments", attachments),
                    param[str | None]("blocks", blocks),
                    param[str | None]("icon_emoji", icon_emoji),
                    param[str | None]("icon_url", icon_url),
                    param[bool | None]("link_names", link_names),
                    param[str | None]("parse", parse),
                    param[str | None]("text", text),
                    param[str | None]("thread_ts", thread_ts),
                    param[str | None]("username", username),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatPostEphemeralsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chat_post_message(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        mrkdwn: bool | None = None,
        parse: str | None = None,
        reply_broadcast: bool | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatPostMessagesuccessschema, RawError]:
        """Sends a message to a channel.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See
                `below <#channels>`__ for more details.
            as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See
                `authorship <#authorship>`__ below.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji: Emoji to use as the icon for this message. Overrides ``icon_url``. Must be used in conjunction
                with ``as_user`` set to ``false``, otherwise ignored. See `authorship <#authorship>`__ below.
            icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with ``as_user``
                set to false, otherwise ignored. See `authorship <#authorship>`__ below.
            link_names: Find and link channel names and usernames.
            mrkdwn: Disable Slack markup parsing by setting to ``false``. Enabled by default.
            parse: Change how messages are treated. Defaults to ``none``. See `below <#formatting>`__.
            reply_broadcast: Used in conjunction with ``thread_ts`` and indicates whether reply should be made visible
                to everyone in the channel or conversation. Defaults to ``false``.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            thread_ts: Provide another message's ``ts`` value to make this message a reply. Avoid using a reply's ``ts``
                value; use its parent instead.
            unfurl_links: Pass true to enable unfurling of primarily text-based content.
            unfurl_media: Pass false to disable unfurling of media content.
            username: Set your bot's user name. Must be used in conjunction with ``as_user`` set to false, otherwise
                ignored. See `authorship <#authorship>`__ below.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.postMessage"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str | None]("as_user", as_user),
                    param[str | None]("attachments", attachments),
                    param[str | None]("blocks", blocks),
                    param[str | None]("icon_emoji", icon_emoji),
                    param[str | None]("icon_url", icon_url),
                    param[bool | None]("link_names", link_names),
                    param[bool | None]("mrkdwn", mrkdwn),
                    param[str | None]("parse", parse),
                    param[bool | None]("reply_broadcast", reply_broadcast),
                    param[str | None]("text", text),
                    param[str | None]("thread_ts", thread_ts),
                    param[bool | None]("unfurl_links", unfurl_links),
                    param[bool | None]("unfurl_media", unfurl_media),
                    param[str | None]("username", username),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatPostMessagesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chat_schedule_message(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        text: str | None = None,
        post_at: str | None = None,
        parse: str | None = None,
        as_user: bool | None = None,
        link_names: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        thread_ts: float | None = None,
        reply_broadcast: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatScheduleMessagesuccessschema, RawError]:
        """Schedules a message to be sent to a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            channel: Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See
                `below <#channels>`__ for more details.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            post_at: Unix EPOCH timestamp of time in future to send the message.
            parse: Change how messages are treated. Defaults to ``none``. See `chat.postMessage
                <chat.postMessage#formatting>`__.
            as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See
                `chat.postMessage <chat.postMessage#authorship>`__.
            link_names: Find and link channel names and usernames.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            unfurl_links: Pass true to enable unfurling of primarily text-based content.
            unfurl_media: Pass false to disable unfurling of media content.
            thread_ts: Provide another message's ``ts`` value to make this message a reply. Avoid using a reply's ``ts``
                value; use its parent instead.
            reply_broadcast: Used in conjunction with ``thread_ts`` and indicates whether reply should be made visible
                to everyone in the channel or conversation. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.scheduleMessage"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body(
                [
                    param[str | None]("channel", channel),
                    param[str | None]("text", text),
                    param[str | None]("post_at", post_at),
                    param[str | None]("parse", parse),
                    param[bool | None]("as_user", as_user),
                    param[bool | None]("link_names", link_names),
                    param[str | None]("attachments", attachments),
                    param[str | None]("blocks", blocks),
                    param[bool | None]("unfurl_links", unfurl_links),
                    param[bool | None]("unfurl_media", unfurl_media),
                    param[float | None]("thread_ts", thread_ts),
                    param[bool | None]("reply_broadcast", reply_broadcast),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatScheduleMessagesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def chat_unfurl(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        ts: str,
        *,
        unfurls: str | None = None,
        user_auth_message: str | None = None,
        user_auth_required: bool | None = None,
        user_auth_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatUnfurlsuccessschema, RawError]:
        """Provide custom unfurl behavior for user-posted URLs

        Args:
            token: Authentication token. Requires scope: ``links:write``
            content_type: Value sent with the request.
            channel: Channel ID of the message
            ts: Timestamp of the message to add unfurl behavior to.
            unfurls: URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl
                blocks or message attachments.
            user_auth_message: Provide a simply-formatted string to send as an ephemeral message to the user as
                invitation to authenticate further and enable full unfurling behavior
            user_auth_required: Set to ``true`` or ``1`` to indicate the user must install your Slack app to trigger
                unfurls for this domain
            user_auth_url: Send users to this custom URL where they will complete authentication in your app to fully
                trigger unfurling. Value should be properly URL-encoded.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.unfurl"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str]("ts", ts),
                    param[str | None]("unfurls", unfurls),
                    param[str | None]("user_auth_message", user_auth_message),
                    param[bool | None]("user_auth_required", user_auth_required),
                    param[str | None]("user_auth_url", user_auth_url),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatUnfurlsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chat_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        ts: str,
        *,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        link_names: str | None = None,
        parse: str | None = None,
        text: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatUpdatesuccessschema, RawError]:
        """Updates a message.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel containing the message to be updated.
            ts: Timestamp of the message to be updated.
            as_user: Pass true to update the message as the authed user. `Bot users </bot-users>`__ in this context are
                considered authed users.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string. This field is
                required when not presenting ``text``. If you don't include this field, the message's previous
                ``attachments`` will be retained. To remove previous ``attachments``, include an empty array for this
                field.
            blocks: A JSON-based array of `structured blocks </block-kit/building>`__, presented as a URL-encoded
                string. If you don't include this field, the message's previous ``blocks`` will be retained. To remove
                previous ``blocks``, include an empty array for this field.
            link_names: Find and link channel names and usernames. Defaults to ``none``. If you do not specify a value
                for this field, the original value set for the message will be overwritten with the default, ``none``.
            parse: Change how messages are treated. Defaults to ``client``, unlike ``chat.postMessage``. Accepts either
                ``none`` or ``full``. If you do not specify a value for this field, the original value set for the
                message will be overwritten with the default, ``client``.
            text: New text for the message, using the `default formatting rules </reference/surfaces/formatting>`__.
                It's not required when presenting ``blocks`` or ``attachments``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.update"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str]("ts", ts),
                    param[str | None]("as_user", as_user),
                    param[str | None]("attachments", attachments),
                    param[str | None]("blocks", blocks),
                    param[str | None]("link_names", link_names),
                    param[str | None]("parse", parse),
                    param[str | None]("text", text),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatUpdatesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncChatWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def chat_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        ts: float | None = None,
        channel: str | None = None,
        as_user: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatDeletesuccessschema, RawError]:
        """Deletes a message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            ts: Timestamp of the message to be deleted.
            channel: Channel containing the message to be deleted.
            as_user: Pass true to delete the message as the authed user with ``chat:write:user`` scope. `Bot users
                </bot-users>`__ in this context are considered authed users. If unused or false, the message will be
                deleted with ``chat:write:bot`` scope.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.delete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body(
                [
                    param[float | None]("ts", ts),
                    param[str | None]("channel", channel),
                    param[bool | None]("as_user", as_user),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatDeletesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chat_delete_scheduled_message(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        scheduled_message_id: str,
        *,
        as_user: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatDeleteScheduledMessageschema, RawError]:
        """Deletes a pending scheduled message from the queue.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: The channel the scheduled_message is posting to
            scheduled_message_id: ``scheduled_message_id`` returned from call to chat.scheduleMessage
            as_user: Pass true to delete the message as the authed user with ``chat:write:user`` scope. `Bot users
                </bot-users>`__ in this context are considered authed users. If unused or false, the message will be
                deleted with ``chat:write:bot`` scope.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.deleteScheduledMessage"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str]("scheduled_message_id", scheduled_message_id),
                    param[bool | None]("as_user", as_user),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatDeleteScheduledMessageschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chat_get_permalink(
        self,
        token: str,
        channel: str,
        message_ts: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatGetPermalinksuccessschema, RawError]:
        """Retrieve a permalink URL for a specific extant message

        Args:
            token: Authentication token. Requires scope: ``none``
            channel: The ID of the conversation or channel containing the message
            message_ts: A message's ``ts`` value, uniquely identifying it within a channel
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/chat.getPermalink"),
            query_params=[
                param[str]("token", token), param[str]("channel", channel), param[str]("message_ts", message_ts)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatGetPermalinksuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chat_me_message(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        text: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatMeMessageschema, RawError]:
        """Share a me message into a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            channel: Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded
                ID, or a name.
            text: Text of the message to send.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.meMessage"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("text", text)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatMeMessageschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chat_post_ephemeral(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        user: str,
        *,
        as_user: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        parse: str | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatPostEphemeralsuccessschema, RawError]:
        """Sends an ephemeral message to a user in a channel.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
            user: ``id`` of the user who will receive the ephemeral message. The user should be in the channel specified
                by the ``channel`` argument.
            as_user: Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is
                not included. Otherwise, defaults to false.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji: Emoji to use as the icon for this message. Overrides ``icon_url``. Must be used in conjunction
                with ``as_user`` set to ``false``, otherwise ignored. See `authorship <#authorship>`__ below.
            icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with ``as_user``
                set to false, otherwise ignored. See `authorship <#authorship>`__ below.
            link_names: Find and link channel names and usernames.
            parse: Change how messages are treated. Defaults to ``none``. See `below <#formatting>`__.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            thread_ts: Provide another message's ``ts`` value to post this message in a thread. Avoid using a reply's
                ``ts`` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is
                already an active thread.
            username: Set your bot's user name. Must be used in conjunction with ``as_user`` set to false, otherwise
                ignored. See `authorship <#authorship>`__ below.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.postEphemeral"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str]("user", user),
                    param[bool | None]("as_user", as_user),
                    param[str | None]("attachments", attachments),
                    param[str | None]("blocks", blocks),
                    param[str | None]("icon_emoji", icon_emoji),
                    param[str | None]("icon_url", icon_url),
                    param[bool | None]("link_names", link_names),
                    param[str | None]("parse", parse),
                    param[str | None]("text", text),
                    param[str | None]("thread_ts", thread_ts),
                    param[str | None]("username", username),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatPostEphemeralsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chat_post_message(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        icon_emoji: str | None = None,
        icon_url: str | None = None,
        link_names: bool | None = None,
        mrkdwn: bool | None = None,
        parse: str | None = None,
        reply_broadcast: bool | None = None,
        text: str | None = None,
        thread_ts: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatPostMessagesuccessschema, RawError]:
        """Sends a message to a channel.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See
                `below <#channels>`__ for more details.
            as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See
                `authorship <#authorship>`__ below.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            icon_emoji: Emoji to use as the icon for this message. Overrides ``icon_url``. Must be used in conjunction
                with ``as_user`` set to ``false``, otherwise ignored. See `authorship <#authorship>`__ below.
            icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with ``as_user``
                set to false, otherwise ignored. See `authorship <#authorship>`__ below.
            link_names: Find and link channel names and usernames.
            mrkdwn: Disable Slack markup parsing by setting to ``false``. Enabled by default.
            parse: Change how messages are treated. Defaults to ``none``. See `below <#formatting>`__.
            reply_broadcast: Used in conjunction with ``thread_ts`` and indicates whether reply should be made visible
                to everyone in the channel or conversation. Defaults to ``false``.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            thread_ts: Provide another message's ``ts`` value to make this message a reply. Avoid using a reply's ``ts``
                value; use its parent instead.
            unfurl_links: Pass true to enable unfurling of primarily text-based content.
            unfurl_media: Pass false to disable unfurling of media content.
            username: Set your bot's user name. Must be used in conjunction with ``as_user`` set to false, otherwise
                ignored. See `authorship <#authorship>`__ below.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.postMessage"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str | None]("as_user", as_user),
                    param[str | None]("attachments", attachments),
                    param[str | None]("blocks", blocks),
                    param[str | None]("icon_emoji", icon_emoji),
                    param[str | None]("icon_url", icon_url),
                    param[bool | None]("link_names", link_names),
                    param[bool | None]("mrkdwn", mrkdwn),
                    param[str | None]("parse", parse),
                    param[bool | None]("reply_broadcast", reply_broadcast),
                    param[str | None]("text", text),
                    param[str | None]("thread_ts", thread_ts),
                    param[bool | None]("unfurl_links", unfurl_links),
                    param[bool | None]("unfurl_media", unfurl_media),
                    param[str | None]("username", username),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatPostMessagesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chat_schedule_message(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        text: str | None = None,
        post_at: str | None = None,
        parse: str | None = None,
        as_user: bool | None = None,
        link_names: bool | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        thread_ts: float | None = None,
        reply_broadcast: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatScheduleMessagesuccessschema, RawError]:
        """Schedules a message to be sent to a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``chat:write``
            channel: Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See
                `below <#channels>`__ for more details.
            text: How this field works and whether it is required depends on other fields you use in your API call. `See
                below <#text_usage>`__ for more detail.
            post_at: Unix EPOCH timestamp of time in future to send the message.
            parse: Change how messages are treated. Defaults to ``none``. See `chat.postMessage
                <chat.postMessage#formatting>`__.
            as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See
                `chat.postMessage <chat.postMessage#authorship>`__.
            link_names: Find and link channel names and usernames.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
            blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
            unfurl_links: Pass true to enable unfurling of primarily text-based content.
            unfurl_media: Pass false to disable unfurling of media content.
            thread_ts: Provide another message's ``ts`` value to make this message a reply. Avoid using a reply's ``ts``
                value; use its parent instead.
            reply_broadcast: Used in conjunction with ``thread_ts`` and indicates whether reply should be made visible
                to everyone in the channel or conversation. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.scheduleMessage"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body(
                [
                    param[str | None]("channel", channel),
                    param[str | None]("text", text),
                    param[str | None]("post_at", post_at),
                    param[str | None]("parse", parse),
                    param[bool | None]("as_user", as_user),
                    param[bool | None]("link_names", link_names),
                    param[str | None]("attachments", attachments),
                    param[str | None]("blocks", blocks),
                    param[bool | None]("unfurl_links", unfurl_links),
                    param[bool | None]("unfurl_media", unfurl_media),
                    param[float | None]("thread_ts", thread_ts),
                    param[bool | None]("reply_broadcast", reply_broadcast),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatScheduleMessagesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    async def chat_unfurl(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        ts: str,
        *,
        unfurls: str | None = None,
        user_auth_message: str | None = None,
        user_auth_required: bool | None = None,
        user_auth_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatUnfurlsuccessschema, RawError]:
        """Provide custom unfurl behavior for user-posted URLs

        Args:
            token: Authentication token. Requires scope: ``links:write``
            content_type: Value sent with the request.
            channel: Channel ID of the message
            ts: Timestamp of the message to add unfurl behavior to.
            unfurls: URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl
                blocks or message attachments.
            user_auth_message: Provide a simply-formatted string to send as an ephemeral message to the user as
                invitation to authenticate further and enable full unfurling behavior
            user_auth_required: Set to ``true`` or ``1`` to indicate the user must install your Slack app to trigger
                unfurls for this domain
            user_auth_url: Send users to this custom URL where they will complete authentication in your app to fully
                trigger unfurling. Value should be properly URL-encoded.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.unfurl"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str]("ts", ts),
                    param[str | None]("unfurls", unfurls),
                    param[str | None]("user_auth_message", user_auth_message),
                    param[bool | None]("user_auth_required", user_auth_required),
                    param[str | None]("user_auth_url", user_auth_url),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatUnfurlsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chat_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        ts: str,
        *,
        as_user: str | None = None,
        attachments: str | None = None,
        blocks: str | None = None,
        link_names: str | None = None,
        parse: str | None = None,
        text: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChatUpdatesuccessschema, RawError]:
        """Updates a message.

        Args:
            token: Authentication token. Requires scope: ``chat:write``
            content_type: Value sent with the request.
            channel: Channel containing the message to be updated.
            ts: Timestamp of the message to be updated.
            as_user: Pass true to update the message as the authed user. `Bot users </bot-users>`__ in this context are
                considered authed users.
            attachments: A JSON-based array of structured attachments, presented as a URL-encoded string. This field is
                required when not presenting ``text``. If you don't include this field, the message's previous
                ``attachments`` will be retained. To remove previous ``attachments``, include an empty array for this
                field.
            blocks: A JSON-based array of `structured blocks </block-kit/building>`__, presented as a URL-encoded
                string. If you don't include this field, the message's previous ``blocks`` will be retained. To remove
                previous ``blocks``, include an empty array for this field.
            link_names: Find and link channel names and usernames. Defaults to ``none``. If you do not specify a value
                for this field, the original value set for the message will be overwritten with the default, ``none``.
            parse: Change how messages are treated. Defaults to ``client``, unlike ``chat.postMessage``. Accepts either
                ``none`` or ``full``. If you do not specify a value for this field, the original value set for the
                message will be overwritten with the default, ``client``.
            text: New text for the message, using the `default formatting rules </reference/surfaces/formatting>`__.
                It's not required when presenting ``blocks`` or ``attachments``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/chat.update"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel", channel),
                    param[str]("ts", ts),
                    param[str | None]("as_user", as_user),
                    param[str | None]("attachments", attachments),
                    param[str | None]("blocks", blocks),
                    param[str | None]("link_names", link_names),
                    param[str | None]("parse", parse),
                    param[str | None]("text", text),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ChatUpdatesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
