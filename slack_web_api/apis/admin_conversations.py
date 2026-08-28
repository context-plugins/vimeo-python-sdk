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
from ..models.admin_conversations_archiveschema import AdminConversationsArchiveschema
from ..models.admin_conversations_convert_to_privateschema import AdminConversationsConvertToPrivateschema
from ..models.admin_conversations_createschema import AdminConversationsCreateschema
from ..models.admin_conversations_deleteschema import AdminConversationsDeleteschema
from ..models.admin_conversations_get_conversation_prefsschema import AdminConversationsGetConversationPrefsschema
from ..models.admin_conversations_get_teamsschema import AdminConversationsGetTeamsschema
from ..models.admin_conversations_inviteschema import AdminConversationsInviteschema
from ..models.admin_conversations_renameschema import AdminConversationsRenameschema
from ..models.admin_conversations_renameschema1 import AdminConversationsRenameschema1
from ..models.admin_conversations_searchschema import AdminConversationsSearchschema
from ..models.admin_conversations_set_conversation_prefsschema import AdminConversationsSetConversationPrefsschema
from ..models.admin_conversations_unarchiveschema import AdminConversationsUnarchiveschema
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class AdminConversations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminConversationsWithRawResponse(client, server, auth)

    def admin_conversations_archive(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsArchiveschema:
        """Archive a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to archive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_archive(
            token, content_type, channel_id, request_options=request_options
        ).unwrap()

    def admin_conversations_convert_to_private(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsConvertToPrivateschema:
        """Convert a public channel to a private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to convert to private.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_convert_to_private(
            token, content_type, channel_id, request_options=request_options
        ).unwrap()

    def admin_conversations_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        is_private: bool,
        *,
        description: str | None = None,
        org_wide: bool | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsCreateschema:
        """Create a public or private channel-based conversation.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            name: Name of the public or private channel to create.
            is_private: When ``true``, creates a private channel instead of a public channel
            description: Description of the public or private channel to create.
            org_wide: When ``true``, the channel will be available org-wide. Note: if the channel is not
                ``org_wide=true``, you must specify a ``team_id`` for this channel
            team_id: The workspace to create the channel in. Note: this argument is required unless you set
                ``org_wide=true``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_create(
            token,
            content_type,
            name,
            is_private,
            description=description,
            org_wide=org_wide,
            team_id=team_id,
            request_options=request_options,
        ).unwrap()

    def admin_conversations_delete(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsDeleteschema:
        """Delete a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_delete(
            token, content_type, channel_id, request_options=request_options
        ).unwrap()

    def admin_conversations_disconnect_shared(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        leaving_team_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsRenameschema:
        """Disconnect a connected channel from one or more workspaces.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to be disconnected from some workspaces.
            leaving_team_ids: The team to be removed from the channel. Currently only a single team id can be specified.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_disconnect_shared(
            token, content_type, channel_id, leaving_team_ids=leaving_team_ids, request_options=request_options
        ).unwrap()

    def admin_conversations_get_conversation_prefs(
        self,
        channel_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsGetConversationPrefsschema:
        """Get conversation preferences for a public or private channel.

        Args:
            channel_id: The channel to get preferences for.
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_get_conversation_prefs(
            channel_id, token, content_type, request_options=request_options
        ).unwrap()

    def admin_conversations_get_teams(
        self,
        channel_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsGetTeamsschema:
        """Get all the workspaces a given public or private channel is connected to within this Enterprise org.

        Args:
            channel_id: The channel to determine connected workspaces within the organization for.
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_get_teams(
            channel_id, token, content_type, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def admin_conversations_invite(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        user_ids: str,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsInviteschema:
        """Invite a user to a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            user_ids: The users to invite.
            channel_id: The channel that the users will be invited to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_invite(
            token, content_type, user_ids, channel_id, request_options=request_options
        ).unwrap()

    def admin_conversations_rename(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsRenameschema1:
        """Rename a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to rename.
            name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_rename(
            token, content_type, channel_id, name, request_options=request_options
        ).unwrap()

    def admin_conversations_search(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_ids: str | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        search_channel_types: str | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsSearchschema:
        """Search for public or private channels in an Enterprise organization.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            team_ids: Comma separated string of team IDs, signifying the workspaces to search through.
            query: Name of the the channel to query by.
            limit: Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            search_channel_types: The type of channel to include or exclude in the search. For example ``private`` will
                search private channels, while ``private_exclude`` will exclude them. For a full list of types, check
                the `Types section <#types>`__.
            sort: Possible values are ``relevant`` (search ranking based on what we think is closest), ``name``
                (alphabetical), ``member_count`` (number of users in the channel), and ``created`` (date channel was
                created). You can optionally pair this with the ``sort_dir`` arg to change how it is sorted
            sort_dir: Sort direction. Possible values are ``asc`` for ascending order like (1, 2, 3) or (a, b, c), and
                ``desc`` for descending order like (3, 2, 1) or (c, b, a)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_search(
            token,
            content_type,
            team_ids=team_ids,
            query=query,
            limit=limit,
            cursor=cursor,
            search_channel_types=search_channel_types,
            sort=sort,
            sort_dir=sort_dir,
            request_options=request_options,
        ).unwrap()

    def admin_conversations_set_conversation_prefs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        prefs: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsSetConversationPrefsschema:
        """Set the posting permissions for a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to set the prefs for
            prefs: The prefs for this channel in a stringified JSON format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_set_conversation_prefs(
            token, content_type, channel_id, prefs, request_options=request_options
        ).unwrap()

    def admin_conversations_set_teams(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        team_id: str | None = None,
        target_team_ids: str | None = None,
        org_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set the workspaces in an Enterprise grid org that connect to a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The encoded ``channel_id`` to add or remove to workspaces.
            team_id: The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace
                shared channel.
            target_team_ids: A comma-separated list of workspaces to which the channel should be shared. Not required if
                the channel is being shared org-wide.
            org_channel: True if channel has to be converted to an org channel
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_set_teams(
            token,
            content_type,
            channel_id,
            team_id=team_id,
            target_team_ids=target_team_ids,
            org_channel=org_channel,
            request_options=request_options,
        ).unwrap()

    def admin_conversations_unarchive(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsUnarchiveschema:
        """Unarchive a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to unarchive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_unarchive(
            token, content_type, channel_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AdminConversationsWithRawResponse:
        return self._with_raw_response


class AsyncAdminConversations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminConversationsWithRawResponse(client, server, auth)

    async def admin_conversations_archive(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsArchiveschema:
        """Archive a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to archive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_archive(
                token, content_type, channel_id, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_convert_to_private(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsConvertToPrivateschema:
        """Convert a public channel to a private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to convert to private.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_convert_to_private(
                token, content_type, channel_id, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        is_private: bool,
        *,
        description: str | None = None,
        org_wide: bool | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsCreateschema:
        """Create a public or private channel-based conversation.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            name: Name of the public or private channel to create.
            is_private: When ``true``, creates a private channel instead of a public channel
            description: Description of the public or private channel to create.
            org_wide: When ``true``, the channel will be available org-wide. Note: if the channel is not
                ``org_wide=true``, you must specify a ``team_id`` for this channel
            team_id: The workspace to create the channel in. Note: this argument is required unless you set
                ``org_wide=true``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_create(
                token,
                content_type,
                name,
                is_private,
                description=description,
                org_wide=org_wide,
                team_id=team_id,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_conversations_delete(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsDeleteschema:
        """Delete a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_delete(
                token, content_type, channel_id, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_disconnect_shared(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        leaving_team_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsRenameschema:
        """Disconnect a connected channel from one or more workspaces.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to be disconnected from some workspaces.
            leaving_team_ids: The team to be removed from the channel. Currently only a single team id can be specified.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_disconnect_shared(
                token, content_type, channel_id, leaving_team_ids=leaving_team_ids, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_get_conversation_prefs(
        self,
        channel_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsGetConversationPrefsschema:
        """Get conversation preferences for a public or private channel.

        Args:
            channel_id: The channel to get preferences for.
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_get_conversation_prefs(
                channel_id, token, content_type, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_get_teams(
        self,
        channel_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsGetTeamsschema:
        """Get all the workspaces a given public or private channel is connected to within this Enterprise org.

        Args:
            channel_id: The channel to determine connected workspaces within the organization for.
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_get_teams(
                channel_id, token, content_type, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_invite(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        user_ids: str,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsInviteschema:
        """Invite a user to a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            user_ids: The users to invite.
            channel_id: The channel that the users will be invited to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_invite(
                token, content_type, user_ids, channel_id, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_rename(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsRenameschema1:
        """Rename a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to rename.
            name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_rename(
                token, content_type, channel_id, name, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_search(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_ids: str | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        search_channel_types: str | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsSearchschema:
        """Search for public or private channels in an Enterprise organization.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            team_ids: Comma separated string of team IDs, signifying the workspaces to search through.
            query: Name of the the channel to query by.
            limit: Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            search_channel_types: The type of channel to include or exclude in the search. For example ``private`` will
                search private channels, while ``private_exclude`` will exclude them. For a full list of types, check
                the `Types section <#types>`__.
            sort: Possible values are ``relevant`` (search ranking based on what we think is closest), ``name``
                (alphabetical), ``member_count`` (number of users in the channel), and ``created`` (date channel was
                created). You can optionally pair this with the ``sort_dir`` arg to change how it is sorted
            sort_dir: Sort direction. Possible values are ``asc`` for ascending order like (1, 2, 3) or (a, b, c), and
                ``desc`` for descending order like (3, 2, 1) or (c, b, a)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_search(
                token,
                content_type,
                team_ids=team_ids,
                query=query,
                limit=limit,
                cursor=cursor,
                search_channel_types=search_channel_types,
                sort=sort,
                sort_dir=sort_dir,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_conversations_set_conversation_prefs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        prefs: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsSetConversationPrefsschema:
        """Set the posting permissions for a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to set the prefs for
            prefs: The prefs for this channel in a stringified JSON format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_set_conversation_prefs(
                token, content_type, channel_id, prefs, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_set_teams(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        team_id: str | None = None,
        target_team_ids: str | None = None,
        org_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set the workspaces in an Enterprise grid org that connect to a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The encoded ``channel_id`` to add or remove to workspaces.
            team_id: The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace
                shared channel.
            target_team_ids: A comma-separated list of workspaces to which the channel should be shared. Not required if
                the channel is being shared org-wide.
            org_channel: True if channel has to be converted to an org channel
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_set_teams(
                token,
                content_type,
                channel_id,
                team_id=team_id,
                target_team_ids=target_team_ids,
                org_channel=org_channel,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_conversations_unarchive(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminConversationsUnarchiveschema:
        """Unarchive a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to unarchive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_unarchive(
                token, content_type, channel_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAdminConversationsWithRawResponse:
        return self._with_raw_response


class AdminConversationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def admin_conversations_archive(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsArchiveschema, RawError]:
        """Archive a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to archive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.archive"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsArchiveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_convert_to_private(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsConvertToPrivateschema, RawError]:
        """Convert a public channel to a private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to convert to private.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.convertToPrivate"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsConvertToPrivateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        is_private: bool,
        *,
        description: str | None = None,
        org_wide: bool | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsCreateschema, RawError]:
        """Create a public or private channel-based conversation.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            name: Name of the public or private channel to create.
            is_private: When ``true``, creates a private channel instead of a public channel
            description: Description of the public or private channel to create.
            org_wide: When ``true``, the channel will be available org-wide. Note: if the channel is not
                ``org_wide=true``, you must specify a ``team_id`` for this channel
            team_id: The workspace to create the channel in. Note: this argument is required unless you set
                ``org_wide=true``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.create"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("name", name),
                    param[bool]("is_private", is_private),
                    param[str | None]("description", description),
                    param[bool | None]("org_wide", org_wide),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsCreateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_delete(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsDeleteschema, RawError]:
        """Delete a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.delete"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsDeleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_disconnect_shared(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        leaving_team_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsRenameschema, RawError]:
        """Disconnect a connected channel from one or more workspaces.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to be disconnected from some workspaces.
            leaving_team_ids: The team to be removed from the channel. Currently only a single team id can be specified.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.disconnectShared"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [param[str]("channel_id", channel_id), param[str | None]("leaving_team_ids", leaving_team_ids)]
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsRenameschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_get_conversation_prefs(
        self,
        channel_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsGetConversationPrefsschema, RawError]:
        """Get conversation preferences for a public or private channel.

        Args:
            channel_id: The channel to get preferences for.
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.getConversationPrefs"),
            query_params=[param[str]("channel_id", channel_id)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsGetConversationPrefsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_get_teams(
        self,
        channel_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsGetTeamsschema, RawError]:
        """Get all the workspaces a given public or private channel is connected to within this Enterprise org.

        Args:
            channel_id: The channel to determine connected workspaces within the organization for.
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.getTeams"),
            query_params=[
                param[str]("channel_id", channel_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsGetTeamsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_invite(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        user_ids: str,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsInviteschema, RawError]:
        """Invite a user to a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            user_ids: The users to invite.
            channel_id: The channel that the users will be invited to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.invite"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("user_ids", user_ids), param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsInviteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_rename(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsRenameschema1, RawError]:
        """Rename a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to rename.
            name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.rename"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id), param[str]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsRenameschema1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_search(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_ids: str | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        search_channel_types: str | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsSearchschema, RawError]:
        """Search for public or private channels in an Enterprise organization.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            team_ids: Comma separated string of team IDs, signifying the workspaces to search through.
            query: Name of the the channel to query by.
            limit: Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            search_channel_types: The type of channel to include or exclude in the search. For example ``private`` will
                search private channels, while ``private_exclude`` will exclude them. For a full list of types, check
                the `Types section <#types>`__.
            sort: Possible values are ``relevant`` (search ranking based on what we think is closest), ``name``
                (alphabetical), ``member_count`` (number of users in the channel), and ``created`` (date channel was
                created). You can optionally pair this with the ``sort_dir`` arg to change how it is sorted
            sort_dir: Sort direction. Possible values are ``asc`` for ascending order like (1, 2, 3) or (a, b, c), and
                ``desc`` for descending order like (3, 2, 1) or (c, b, a)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.search"),
            query_params=[
                param[str | None]("team_ids", team_ids),
                param[str | None]("query", query),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("search_channel_types", search_channel_types),
                param[str | None]("sort", sort),
                param[str | None]("sort_dir", sort_dir),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsSearchschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_set_conversation_prefs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        prefs: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsSetConversationPrefsschema, RawError]:
        """Set the posting permissions for a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to set the prefs for
            prefs: The prefs for this channel in a stringified JSON format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.setConversationPrefs"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id), param[str]("prefs", prefs)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsSetConversationPrefsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_set_teams(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        team_id: str | None = None,
        target_team_ids: str | None = None,
        org_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set the workspaces in an Enterprise grid org that connect to a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The encoded ``channel_id`` to add or remove to workspaces.
            team_id: The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace
                shared channel.
            target_team_ids: A comma-separated list of workspaces to which the channel should be shared. Not required if
                the channel is being shared org-wide.
            org_channel: True if channel has to be converted to an org channel
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.setTeams"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel_id", channel_id),
                    param[str | None]("team_id", team_id),
                    param[str | None]("target_team_ids", target_team_ids),
                    param[bool | None]("org_channel", org_channel),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_unarchive(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsUnarchiveschema, RawError]:
        """Unarchive a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to unarchive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.unarchive"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsUnarchiveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAdminConversationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def admin_conversations_archive(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsArchiveschema, RawError]:
        """Archive a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to archive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.archive"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsArchiveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_convert_to_private(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsConvertToPrivateschema, RawError]:
        """Convert a public channel to a private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to convert to private.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.convertToPrivate"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsConvertToPrivateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        is_private: bool,
        *,
        description: str | None = None,
        org_wide: bool | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsCreateschema, RawError]:
        """Create a public or private channel-based conversation.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            name: Name of the public or private channel to create.
            is_private: When ``true``, creates a private channel instead of a public channel
            description: Description of the public or private channel to create.
            org_wide: When ``true``, the channel will be available org-wide. Note: if the channel is not
                ``org_wide=true``, you must specify a ``team_id`` for this channel
            team_id: The workspace to create the channel in. Note: this argument is required unless you set
                ``org_wide=true``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.create"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("name", name),
                    param[bool]("is_private", is_private),
                    param[str | None]("description", description),
                    param[bool | None]("org_wide", org_wide),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsCreateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_delete(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsDeleteschema, RawError]:
        """Delete a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.delete"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsDeleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_disconnect_shared(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        leaving_team_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsRenameschema, RawError]:
        """Disconnect a connected channel from one or more workspaces.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to be disconnected from some workspaces.
            leaving_team_ids: The team to be removed from the channel. Currently only a single team id can be specified.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.disconnectShared"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [param[str]("channel_id", channel_id), param[str | None]("leaving_team_ids", leaving_team_ids)]
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsRenameschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_get_conversation_prefs(
        self,
        channel_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsGetConversationPrefsschema, RawError]:
        """Get conversation preferences for a public or private channel.

        Args:
            channel_id: The channel to get preferences for.
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.getConversationPrefs"),
            query_params=[param[str]("channel_id", channel_id)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsGetConversationPrefsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_get_teams(
        self,
        channel_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsGetTeamsschema, RawError]:
        """Get all the workspaces a given public or private channel is connected to within this Enterprise org.

        Args:
            channel_id: The channel to determine connected workspaces within the organization for.
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.getTeams"),
            query_params=[
                param[str]("channel_id", channel_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsGetTeamsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_invite(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        user_ids: str,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsInviteschema, RawError]:
        """Invite a user to a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            user_ids: The users to invite.
            channel_id: The channel that the users will be invited to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.invite"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("user_ids", user_ids), param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsInviteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_rename(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsRenameschema1, RawError]:
        """Rename a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to rename.
            name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.rename"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id), param[str]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsRenameschema1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_search(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_ids: str | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        search_channel_types: str | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsSearchschema, RawError]:
        """Search for public or private channels in an Enterprise organization.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            team_ids: Comma separated string of team IDs, signifying the workspaces to search through.
            query: Name of the the channel to query by.
            limit: Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            search_channel_types: The type of channel to include or exclude in the search. For example ``private`` will
                search private channels, while ``private_exclude`` will exclude them. For a full list of types, check
                the `Types section <#types>`__.
            sort: Possible values are ``relevant`` (search ranking based on what we think is closest), ``name``
                (alphabetical), ``member_count`` (number of users in the channel), and ``created`` (date channel was
                created). You can optionally pair this with the ``sort_dir`` arg to change how it is sorted
            sort_dir: Sort direction. Possible values are ``asc`` for ascending order like (1, 2, 3) or (a, b, c), and
                ``desc`` for descending order like (3, 2, 1) or (c, b, a)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.search"),
            query_params=[
                param[str | None]("team_ids", team_ids),
                param[str | None]("query", query),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("search_channel_types", search_channel_types),
                param[str | None]("sort", sort),
                param[str | None]("sort_dir", sort_dir),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsSearchschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_set_conversation_prefs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        prefs: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsSetConversationPrefsschema, RawError]:
        """Set the posting permissions for a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to set the prefs for
            prefs: The prefs for this channel in a stringified JSON format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.setConversationPrefs"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id), param[str]("prefs", prefs)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsSetConversationPrefsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_set_teams(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        team_id: str | None = None,
        target_team_ids: str | None = None,
        org_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set the workspaces in an Enterprise grid org that connect to a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The encoded ``channel_id`` to add or remove to workspaces.
            team_id: The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace
                shared channel.
            target_team_ids: A comma-separated list of workspaces to which the channel should be shared. Not required if
                the channel is being shared org-wide.
            org_channel: True if channel has to be converted to an org channel
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.setTeams"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("channel_id", channel_id),
                    param[str | None]("team_id", team_id),
                    param[str | None]("target_team_ids", target_team_ids),
                    param[bool | None]("org_channel", org_channel),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_unarchive(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminConversationsUnarchiveschema, RawError]:
        """Unarchive a public or private channel.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:write``
            content_type: Value sent with the request.
            channel_id: The channel to unarchive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.unarchive"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel_id", channel_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AdminConversationsUnarchiveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
