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
from ..models.conversations_archivesuccessschema import ConversationsArchivesuccessschema
from ..models.conversations_closesuccessschema import ConversationsClosesuccessschema
from ..models.conversations_createsuccessschema import ConversationsCreatesuccessschema
from ..models.conversations_historysuccessschema import ConversationsHistorysuccessschema
from ..models.conversations_infosuccessschema import ConversationsInfosuccessschema
from ..models.conversations_inviteerrorschema import ConversationsInviteerrorschema
from ..models.conversations_joinsuccessschema import ConversationsJoinsuccessschema
from ..models.conversations_kicksuccessschema import ConversationsKicksuccessschema
from ..models.conversations_leavesuccessschema import ConversationsLeavesuccessschema
from ..models.conversations_listsuccessschema import ConversationsListsuccessschema
from ..models.conversations_marksuccessschema import ConversationsMarksuccessschema
from ..models.conversations_memberssuccessschema import ConversationsMemberssuccessschema
from ..models.conversations_opensuccessschema import ConversationsOpensuccessschema
from ..models.conversations_renamesuccessschema import ConversationsRenamesuccessschema
from ..models.conversations_repliessuccessschema import ConversationsRepliessuccessschema
from ..models.conversations_set_purposesuccessschema import ConversationsSetPurposesuccessschema
from ..models.conversations_set_topicsuccessschema import ConversationsSetTopicsuccessschema
from ..models.conversations_unarchivesuccessschema import ConversationsUnarchivesuccessschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Conversations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsWithRawResponse(client, server, auth)

    def conversations_archive(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsArchivesuccessschema:
        """Archives a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to archive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_archive(
            content_type, token=token, channel=channel, request_options=request_options
        ).unwrap()

    def conversations_close(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsClosesuccessschema:
        """Closes a direct message or multi-person direct message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to close.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_close(
            content_type, token=token, channel=channel, request_options=request_options
        ).unwrap()

    def conversations_create(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        name: str | None = None,
        is_private: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsCreatesuccessschema:
        """Initiates a public or private channel-based conversation

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            name: Name of the public or private channel to create
            is_private: Create a private channel instead of a public one
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            If successful, the command returns a rather stark `conversation object </types/conversation>`__

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_create(
            content_type, token=token, name=name, is_private=is_private, request_options=request_options
        ).unwrap()

    def conversations_history(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsHistorysuccessschema:
        """Fetches a conversation's history of messages and events.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:history``
            channel: Conversation ID to fetch history for.
            latest: End of time range of messages to include in results.
            oldest: Start of time range of messages to include in results.
            inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is
                specified.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response containing a channel's messages

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_history(
            content_type,
            token=token,
            channel=channel,
            latest=latest,
            oldest=oldest,
            inclusive=inclusive,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def conversations_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        include_locale: bool | None = None,
        include_num_members: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsInfosuccessschema:
        """Retrieve information about a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            channel: Conversation ID to learn more about
            include_locale: Set this to ``true`` to receive the locale for this conversation. Defaults to ``false``
            include_num_members: Set to ``true`` to include the member count for the specified conversation. Defaults to
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response for a public channel. (Also, a response from a private channel and a multi-party IM
            is very similar to this example.)

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_info(
            content_type,
            token=token,
            channel=channel,
            include_locale=include_locale,
            include_num_members=include_num_members,
            request_options=request_options,
        ).unwrap()

    def conversations_invite(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsInviteerrorschema:
        """Invites users to a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: The ID of the public or private channel to invite user(s) to.
            users: A comma separated list of user IDs. Up to 1000 users may be listed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response when an invitation is extended

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_invite(
            content_type, token=token, channel=channel, users=users, request_options=request_options
        ).unwrap()

    def conversations_join(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsJoinsuccessschema:
        """Joins an existing conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``channels:write``
            channel: ID of conversation to join
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_join(
            content_type, token=token, channel=channel, request_options=request_options
        ).unwrap()

    def conversations_kick(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsKicksuccessschema:
        """Removes a user from a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to remove user from.
            user: User ID to be removed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_kick(
            content_type, token=token, channel=channel, user=user, request_options=request_options
        ).unwrap()

    def conversations_leave(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsLeavesuccessschema:
        """Leaves a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to leave
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_leave(
            content_type, token=token, channel=channel, request_options=request_options
        ).unwrap()

    def conversations_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        exclude_archived: bool | None = None,
        types: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsListsuccessschema:
        """Lists all channels in a Slack team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            exclude_archived: Set to ``true`` to exclude archived channels from the list
            types: Mix and match channel types by providing a comma-separated list of any combination of
                ``public_channel``, ``private_channel``, ``mpim``, ``im``
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached. Must be an integer no larger than 1000.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response with only public channels

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_list(
            content_type,
            token=token,
            exclude_archived=exclude_archived,
            types=types,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def conversations_mark(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsMarksuccessschema:
        """Sets the read cursor in a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Channel or conversation to set the read cursor for.
            ts: Unique identifier of message you want marked as most recently seen in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_mark(
            content_type, token=token, channel=channel, ts=ts, request_options=request_options
        ).unwrap()

    def conversations_members(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsMemberssuccessschema:
        """Retrieve members of a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            channel: ID of the conversation to retrieve members for
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical paginated success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_members(
            content_type, token=token, channel=channel, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def conversations_open(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        users: str | None = None,
        return_im: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsOpensuccessschema:
        """Opens or resumes a direct message or multi-person direct message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Resume a conversation by supplying an ``im`` or ``mpim``'s ID. Or provide the ``users`` field
                instead.
            users: Comma separated lists of users. If only one user is included, this creates a 1:1 DM. The ordering of
                the users is preserved whenever a multi-person direct message is returned. Supply a ``channel`` when not
                supplying ``users``.
            return_im: Boolean, indicates you want the full IM channel definition in the response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_open(
            content_type,
            token=token,
            channel=channel,
            users=users,
            return_im=return_im,
            request_options=request_options,
        ).unwrap()

    def conversations_rename(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsRenamesuccessschema:
        """Renames a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to rename
            name: New name for conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_rename(
            content_type, token=token, channel=channel, name=name, request_options=request_options
        ).unwrap()

    def conversations_replies(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts: float | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsRepliessuccessschema:
        """Retrieve a thread of messages posted to a conversation

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:history``
            channel: Conversation ID to fetch thread from.
            ts: Unique identifier of a thread's parent message. ``ts`` must be the timestamp of an existing message with
                0 or more replies. If there are no replies then just the single message referenced by ``ts`` will return
                - it is just an ordinary, unthreaded message.
            latest: End of time range of messages to include in results.
            oldest: Start of time range of messages to include in results.
            inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is
                specified.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_replies(
            content_type,
            token=token,
            channel=channel,
            ts=ts,
            latest=latest,
            oldest=oldest,
            inclusive=inclusive,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def conversations_set_purpose(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        purpose: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsSetPurposesuccessschema:
        """Sets the purpose for a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to set the purpose of
            purpose: A new, specialer purpose
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_set_purpose(
            content_type, token=token, channel=channel, purpose=purpose, request_options=request_options
        ).unwrap()

    def conversations_set_topic(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        topic: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsSetTopicsuccessschema:
        """Sets the topic for a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to set the topic of
            topic: The new topic string. Does not support formatting or linkification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_set_topic(
            content_type, token=token, channel=channel, topic=topic, request_options=request_options
        ).unwrap()

    def conversations_unarchive(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsUnarchivesuccessschema:
        """Reverses conversation archival.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to unarchive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.conversations_unarchive(
            content_type, token=token, channel=channel, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsWithRawResponse:
        return self._with_raw_response


class AsyncConversations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsWithRawResponse(client, server, auth)

    async def conversations_archive(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsArchivesuccessschema:
        """Archives a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to archive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_archive(
                content_type, token=token, channel=channel, request_options=request_options
            )
        ).unwrap()

    async def conversations_close(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsClosesuccessschema:
        """Closes a direct message or multi-person direct message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to close.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_close(
                content_type, token=token, channel=channel, request_options=request_options
            )
        ).unwrap()

    async def conversations_create(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        name: str | None = None,
        is_private: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsCreatesuccessschema:
        """Initiates a public or private channel-based conversation

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            name: Name of the public or private channel to create
            is_private: Create a private channel instead of a public one
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            If successful, the command returns a rather stark `conversation object </types/conversation>`__

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_create(
                content_type, token=token, name=name, is_private=is_private, request_options=request_options
            )
        ).unwrap()

    async def conversations_history(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsHistorysuccessschema:
        """Fetches a conversation's history of messages and events.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:history``
            channel: Conversation ID to fetch history for.
            latest: End of time range of messages to include in results.
            oldest: Start of time range of messages to include in results.
            inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is
                specified.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response containing a channel's messages

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_history(
                content_type,
                token=token,
                channel=channel,
                latest=latest,
                oldest=oldest,
                inclusive=inclusive,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def conversations_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        include_locale: bool | None = None,
        include_num_members: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsInfosuccessschema:
        """Retrieve information about a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            channel: Conversation ID to learn more about
            include_locale: Set this to ``true`` to receive the locale for this conversation. Defaults to ``false``
            include_num_members: Set to ``true`` to include the member count for the specified conversation. Defaults to
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response for a public channel. (Also, a response from a private channel and a multi-party IM
            is very similar to this example.)

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_info(
                content_type,
                token=token,
                channel=channel,
                include_locale=include_locale,
                include_num_members=include_num_members,
                request_options=request_options,
            )
        ).unwrap()

    async def conversations_invite(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsInviteerrorschema:
        """Invites users to a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: The ID of the public or private channel to invite user(s) to.
            users: A comma separated list of user IDs. Up to 1000 users may be listed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response when an invitation is extended

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_invite(
                content_type, token=token, channel=channel, users=users, request_options=request_options
            )
        ).unwrap()

    async def conversations_join(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsJoinsuccessschema:
        """Joins an existing conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``channels:write``
            channel: ID of conversation to join
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_join(
                content_type, token=token, channel=channel, request_options=request_options
            )
        ).unwrap()

    async def conversations_kick(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsKicksuccessschema:
        """Removes a user from a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to remove user from.
            user: User ID to be removed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_kick(
                content_type, token=token, channel=channel, user=user, request_options=request_options
            )
        ).unwrap()

    async def conversations_leave(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsLeavesuccessschema:
        """Leaves a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to leave
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_leave(
                content_type, token=token, channel=channel, request_options=request_options
            )
        ).unwrap()

    async def conversations_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        exclude_archived: bool | None = None,
        types: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsListsuccessschema:
        """Lists all channels in a Slack team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            exclude_archived: Set to ``true`` to exclude archived channels from the list
            types: Mix and match channel types by providing a comma-separated list of any combination of
                ``public_channel``, ``private_channel``, ``mpim``, ``im``
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached. Must be an integer no larger than 1000.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response with only public channels

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_list(
                content_type,
                token=token,
                exclude_archived=exclude_archived,
                types=types,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def conversations_mark(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsMarksuccessschema:
        """Sets the read cursor in a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Channel or conversation to set the read cursor for.
            ts: Unique identifier of message you want marked as most recently seen in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_mark(
                content_type, token=token, channel=channel, ts=ts, request_options=request_options
            )
        ).unwrap()

    async def conversations_members(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsMemberssuccessschema:
        """Retrieve members of a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            channel: ID of the conversation to retrieve members for
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical paginated success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_members(
                content_type, token=token, channel=channel, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def conversations_open(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        users: str | None = None,
        return_im: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsOpensuccessschema:
        """Opens or resumes a direct message or multi-person direct message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Resume a conversation by supplying an ``im`` or ``mpim``'s ID. Or provide the ``users`` field
                instead.
            users: Comma separated lists of users. If only one user is included, this creates a 1:1 DM. The ordering of
                the users is preserved whenever a multi-person direct message is returned. Supply a ``channel`` when not
                supplying ``users``.
            return_im: Boolean, indicates you want the full IM channel definition in the response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_open(
                content_type,
                token=token,
                channel=channel,
                users=users,
                return_im=return_im,
                request_options=request_options,
            )
        ).unwrap()

    async def conversations_rename(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsRenamesuccessschema:
        """Renames a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to rename
            name: New name for conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_rename(
                content_type, token=token, channel=channel, name=name, request_options=request_options
            )
        ).unwrap()

    async def conversations_replies(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts: float | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsRepliessuccessschema:
        """Retrieve a thread of messages posted to a conversation

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:history``
            channel: Conversation ID to fetch thread from.
            ts: Unique identifier of a thread's parent message. ``ts`` must be the timestamp of an existing message with
                0 or more replies. If there are no replies then just the single message referenced by ``ts`` will return
                - it is just an ordinary, unthreaded message.
            latest: End of time range of messages to include in results.
            oldest: Start of time range of messages to include in results.
            inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is
                specified.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_replies(
                content_type,
                token=token,
                channel=channel,
                ts=ts,
                latest=latest,
                oldest=oldest,
                inclusive=inclusive,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def conversations_set_purpose(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        purpose: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsSetPurposesuccessschema:
        """Sets the purpose for a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to set the purpose of
            purpose: A new, specialer purpose
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_set_purpose(
                content_type, token=token, channel=channel, purpose=purpose, request_options=request_options
            )
        ).unwrap()

    async def conversations_set_topic(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        topic: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsSetTopicsuccessschema:
        """Sets the topic for a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to set the topic of
            topic: The new topic string. Does not support formatting or linkification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_set_topic(
                content_type, token=token, channel=channel, topic=topic, request_options=request_options
            )
        ).unwrap()

    async def conversations_unarchive(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsUnarchivesuccessschema:
        """Reverses conversation archival.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to unarchive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.conversations_unarchive(
                content_type, token=token, channel=channel, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsWithRawResponse:
        return self._with_raw_response


class ConversationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def conversations_archive(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsArchivesuccessschema, RawError]:
        """Archives a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to archive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.archive"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsArchivesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_close(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsClosesuccessschema, RawError]:
        """Closes a direct message or multi-person direct message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to close.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.close"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsClosesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_create(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        name: str | None = None,
        is_private: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsCreatesuccessschema, RawError]:
        """Initiates a public or private channel-based conversation

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            name: Name of the public or private channel to create
            is_private: Create a private channel instead of a public one
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.create"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("name", name), param[bool | None]("is_private", is_private)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsCreatesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_history(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsHistorysuccessschema, RawError]:
        """Fetches a conversation's history of messages and events.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:history``
            channel: Conversation ID to fetch history for.
            latest: End of time range of messages to include in results.
            oldest: Start of time range of messages to include in results.
            inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is
                specified.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.history"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[float | None]("latest", latest),
                param[float | None]("oldest", oldest),
                param[bool | None]("inclusive", inclusive),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsHistorysuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        include_locale: bool | None = None,
        include_num_members: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsInfosuccessschema, RawError]:
        """Retrieve information about a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            channel: Conversation ID to learn more about
            include_locale: Set this to ``true`` to receive the locale for this conversation. Defaults to ``false``
            include_num_members: Set to ``true`` to include the member count for the specified conversation. Defaults to
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.info"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[bool | None]("include_locale", include_locale),
                param[bool | None]("include_num_members", include_num_members),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsInfosuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_invite(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsInviteerrorschema, RawError]:
        """Invites users to a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: The ID of the public or private channel to invite user(s) to.
            users: A comma separated list of user IDs. Up to 1000 users may be listed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.invite"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("users", users)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsInviteerrorschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_join(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsJoinsuccessschema, RawError]:
        """Joins an existing conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``channels:write``
            channel: ID of conversation to join
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.join"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsJoinsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_kick(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsKicksuccessschema, RawError]:
        """Removes a user from a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to remove user from.
            user: User ID to be removed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.kick"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("user", user)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsKicksuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_leave(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsLeavesuccessschema, RawError]:
        """Leaves a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to leave
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.leave"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsLeavesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        exclude_archived: bool | None = None,
        types: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsListsuccessschema, RawError]:
        """Lists all channels in a Slack team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            exclude_archived: Set to ``true`` to exclude archived channels from the list
            types: Mix and match channel types by providing a comma-separated list of any combination of
                ``public_channel``, ``private_channel``, ``mpim``, ``im``
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached. Must be an integer no larger than 1000.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.list"),
            query_params=[
                param[str | None]("token", token),
                param[bool | None]("exclude_archived", exclude_archived),
                param[str | None]("types", types),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsListsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_mark(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsMarksuccessschema, RawError]:
        """Sets the read cursor in a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Channel or conversation to set the read cursor for.
            ts: Unique identifier of message you want marked as most recently seen in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.mark"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[float | None]("ts", ts)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsMarksuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_members(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsMemberssuccessschema, RawError]:
        """Retrieve members of a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            channel: ID of the conversation to retrieve members for
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.members"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsMemberssuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_open(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        users: str | None = None,
        return_im: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsOpensuccessschema, RawError]:
        """Opens or resumes a direct message or multi-person direct message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Resume a conversation by supplying an ``im`` or ``mpim``'s ID. Or provide the ``users`` field
                instead.
            users: Comma separated lists of users. If only one user is included, this creates a 1:1 DM. The ordering of
                the users is preserved whenever a multi-person direct message is returned. Supply a ``channel`` when not
                supplying ``users``.
            return_im: Boolean, indicates you want the full IM channel definition in the response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.open"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body(
                [
                    param[str | None]("channel", channel),
                    param[str | None]("users", users),
                    param[bool | None]("return_im", return_im),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsOpensuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_rename(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsRenamesuccessschema, RawError]:
        """Renames a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to rename
            name: New name for conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.rename"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsRenamesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_replies(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts: float | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsRepliessuccessschema, RawError]:
        """Retrieve a thread of messages posted to a conversation

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:history``
            channel: Conversation ID to fetch thread from.
            ts: Unique identifier of a thread's parent message. ``ts`` must be the timestamp of an existing message with
                0 or more replies. If there are no replies then just the single message referenced by ``ts`` will return
                - it is just an ordinary, unthreaded message.
            latest: End of time range of messages to include in results.
            oldest: Start of time range of messages to include in results.
            inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is
                specified.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.replies"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[float | None]("ts", ts),
                param[float | None]("latest", latest),
                param[float | None]("oldest", oldest),
                param[bool | None]("inclusive", inclusive),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsRepliessuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_set_purpose(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        purpose: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsSetPurposesuccessschema, RawError]:
        """Sets the purpose for a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to set the purpose of
            purpose: A new, specialer purpose
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.setPurpose"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("purpose", purpose)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsSetPurposesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_set_topic(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        topic: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsSetTopicsuccessschema, RawError]:
        """Sets the topic for a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to set the topic of
            topic: The new topic string. Does not support formatting or linkification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.setTopic"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("topic", topic)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsSetTopicsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def conversations_unarchive(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsUnarchivesuccessschema, RawError]:
        """Reverses conversation archival.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to unarchive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.unarchive"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsUnarchivesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def conversations_archive(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsArchivesuccessschema, RawError]:
        """Archives a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to archive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.archive"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsArchivesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_close(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsClosesuccessschema, RawError]:
        """Closes a direct message or multi-person direct message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to close.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.close"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsClosesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_create(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        name: str | None = None,
        is_private: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsCreatesuccessschema, RawError]:
        """Initiates a public or private channel-based conversation

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            name: Name of the public or private channel to create
            is_private: Create a private channel instead of a public one
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.create"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("name", name), param[bool | None]("is_private", is_private)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsCreatesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_history(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsHistorysuccessschema, RawError]:
        """Fetches a conversation's history of messages and events.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:history``
            channel: Conversation ID to fetch history for.
            latest: End of time range of messages to include in results.
            oldest: Start of time range of messages to include in results.
            inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is
                specified.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.history"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[float | None]("latest", latest),
                param[float | None]("oldest", oldest),
                param[bool | None]("inclusive", inclusive),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsHistorysuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        include_locale: bool | None = None,
        include_num_members: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsInfosuccessschema, RawError]:
        """Retrieve information about a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            channel: Conversation ID to learn more about
            include_locale: Set this to ``true`` to receive the locale for this conversation. Defaults to ``false``
            include_num_members: Set to ``true`` to include the member count for the specified conversation. Defaults to
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.info"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[bool | None]("include_locale", include_locale),
                param[bool | None]("include_num_members", include_num_members),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsInfosuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_invite(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsInviteerrorschema, RawError]:
        """Invites users to a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: The ID of the public or private channel to invite user(s) to.
            users: A comma separated list of user IDs. Up to 1000 users may be listed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.invite"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("users", users)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsInviteerrorschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_join(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsJoinsuccessschema, RawError]:
        """Joins an existing conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``channels:write``
            channel: ID of conversation to join
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.join"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsJoinsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_kick(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsKicksuccessschema, RawError]:
        """Removes a user from a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to remove user from.
            user: User ID to be removed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.kick"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("user", user)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsKicksuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_leave(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsLeavesuccessschema, RawError]:
        """Leaves a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to leave
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.leave"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsLeavesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        exclude_archived: bool | None = None,
        types: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsListsuccessschema, RawError]:
        """Lists all channels in a Slack team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            exclude_archived: Set to ``true`` to exclude archived channels from the list
            types: Mix and match channel types by providing a comma-separated list of any combination of
                ``public_channel``, ``private_channel``, ``mpim``, ``im``
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached. Must be an integer no larger than 1000.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.list"),
            query_params=[
                param[str | None]("token", token),
                param[bool | None]("exclude_archived", exclude_archived),
                param[str | None]("types", types),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsListsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_mark(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsMarksuccessschema, RawError]:
        """Sets the read cursor in a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Channel or conversation to set the read cursor for.
            ts: Unique identifier of message you want marked as most recently seen in this conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.mark"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[float | None]("ts", ts)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsMarksuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_members(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsMemberssuccessschema, RawError]:
        """Retrieve members of a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            channel: ID of the conversation to retrieve members for
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.members"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsMemberssuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_open(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        users: str | None = None,
        return_im: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsOpensuccessschema, RawError]:
        """Opens or resumes a direct message or multi-person direct message.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Resume a conversation by supplying an ``im`` or ``mpim``'s ID. Or provide the ``users`` field
                instead.
            users: Comma separated lists of users. If only one user is included, this creates a 1:1 DM. The ordering of
                the users is preserved whenever a multi-person direct message is returned. Supply a ``channel`` when not
                supplying ``users``.
            return_im: Boolean, indicates you want the full IM channel definition in the response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.open"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body(
                [
                    param[str | None]("channel", channel),
                    param[str | None]("users", users),
                    param[bool | None]("return_im", return_im),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsOpensuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_rename(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsRenamesuccessschema, RawError]:
        """Renames a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to rename
            name: New name for conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.rename"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsRenamesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_replies(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts: float | None = None,
        latest: float | None = None,
        oldest: float | None = None,
        inclusive: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsRepliessuccessschema, RawError]:
        """Retrieve a thread of messages posted to a conversation

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:history``
            channel: Conversation ID to fetch thread from.
            ts: Unique identifier of a thread's parent message. ``ts`` must be the timestamp of an existing message with
                0 or more replies. If there are no replies then just the single message referenced by ``ts`` will return
                - it is just an ordinary, unthreaded message.
            latest: End of time range of messages to include in results.
            oldest: Start of time range of messages to include in results.
            inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is
                specified.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/conversations.replies"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[float | None]("ts", ts),
                param[float | None]("latest", latest),
                param[float | None]("oldest", oldest),
                param[bool | None]("inclusive", inclusive),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsRepliessuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_set_purpose(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        purpose: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsSetPurposesuccessschema, RawError]:
        """Sets the purpose for a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to set the purpose of
            purpose: A new, specialer purpose
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.setPurpose"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("purpose", purpose)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsSetPurposesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_set_topic(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        topic: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsSetTopicsuccessschema, RawError]:
        """Sets the topic for a conversation.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: Conversation to set the topic of
            topic: The new topic string. Does not support formatting or linkification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.setTopic"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel), param[str | None]("topic", topic)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsSetTopicsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def conversations_unarchive(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsUnarchivesuccessschema, RawError]:
        """Reverses conversation archival.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:write``
            channel: ID of conversation to unarchive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/conversations.unarchive"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("channel", channel)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ConversationsUnarchivesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
