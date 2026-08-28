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


class Admin:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminWithRawResponse(client, server, auth)

    def admin_apps_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Approve an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to approve.
            request_id: The id of the request to approve.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_apps_approve(
            token, content_type, app_id=app_id, request_id=request_id, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_apps_approved_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        enterprise_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List approved apps for an org or workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            enterprise_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_apps_approved_list(
            token,
            content_type,
            limit=limit,
            cursor=cursor,
            team_id=team_id,
            enterprise_id=enterprise_id,
            request_options=request_options,
        ).unwrap()

    def admin_apps_requests_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List app requests for a team/workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_apps_requests_list(
            token, content_type, limit=limit, cursor=cursor, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_apps_restrict(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Restrict an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to restrict.
            request_id: The id of the request to restrict.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_apps_restrict(
            token, content_type, app_id=app_id, request_id=request_id, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_apps_restricted_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        enterprise_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List restricted apps for an org or workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            enterprise_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_apps_restricted_list(
            token,
            content_type,
            limit=limit,
            cursor=cursor,
            team_id=team_id,
            enterprise_id=enterprise_id,
            request_options=request_options,
        ).unwrap()

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

    def admin_conversations_ekm_list_original_connected_channel_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel_ids: str | None = None,
        team_ids: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all disconnected channels—i.e., channels that were once connected to other workspaces and then
        disconnected—and the corresponding original channel IDs for key revocation with EKM.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            channel_ids: A comma-separated list of channels to filter to.
            team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_ekm_list_original_connected_channel_info(
            token,
            content_type,
            channel_ids=channel_ids,
            team_ids=team_ids,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
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

    def admin_conversations_restrict_access_add_group(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        group_id: str,
        channel_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an allowlist of IDP groups for accessing a channel

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.conversations:write``
            group_id: The `IDP Group
                <https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org>`__
                ID to be an allowlist for the private channel.
            channel_id: The channel to link this group to.
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_restrict_access_add_group(
            content_type, token, group_id, channel_id, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_conversations_restrict_access_list_groups(
        self,
        token: str,
        channel_id: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all IDP Groups linked to a channel

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            channel_id: Value sent with the request.
            content_type: Value sent with the request.
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_restrict_access_list_groups(
            token, channel_id, content_type, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_conversations_restrict_access_remove_group(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        team_id: str,
        group_id: str,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove a linked IDP group linked from a private channel

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.conversations:write``
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            group_id: The `IDP Group
                <https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org>`__
                ID to remove from the private channel.
            channel_id: The channel to remove the linked group from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_restrict_access_remove_group(
            content_type, token, team_id, group_id, channel_id, request_options=request_options
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

    def admin_emoji_add(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        url: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent
                backgrounds work best.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_add(
            content_type, token, name, url, request_options=request_options
        ).unwrap()

    def admin_emoji_add_alias(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        alias_for: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an emoji alias.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be aliased. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            alias_for: The alias of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_add_alias(
            content_type, token, name, alias_for, request_options=request_options
        ).unwrap()

    def admin_emoji_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List emoji for an Enterprise Grid organization.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_list(
            token, content_type, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def admin_emoji_remove(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove an emoji across an Enterprise Grid organization

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_remove(
            content_type, token, name, request_options=request_options
        ).unwrap()

    def admin_emoji_rename(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        new_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Rename an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be renamed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            new_name: The new name of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_rename(
            content_type, token, name, new_name, request_options=request_options
        ).unwrap()

    def admin_invite_requests_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        invite_request_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Approve a workspace invite request.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:write``
            content_type: Value sent with the request.
            invite_request_id: ID of the request to invite.
            team_id: ID for the workspace where the invite request was made.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_invite_requests_approve(
            token, content_type, invite_request_id, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_invite_requests_approved_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all approved workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous API response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000,
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_invite_requests_approved_list(
            token, content_type, team_id=team_id, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def admin_invite_requests_denied_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all denied workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous api response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_invite_requests_denied_list(
            token, content_type, team_id=team_id, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def admin_invite_requests_deny(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        invite_request_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Deny a workspace invite request.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:write``
            content_type: Value sent with the request.
            invite_request_id: ID of the request to invite.
            team_id: ID for the workspace where the invite request was made.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_invite_requests_deny(
            token, content_type, invite_request_id, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_invite_requests_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all pending workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous API response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000,
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_invite_requests_list(
            token, content_type, team_id=team_id, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def admin_teams_admins_list(
        self,
        token: str,
        team_id: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all of the admins on a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            team_id: Value sent with the request.
            content_type: Value sent with the request.
            limit: The maximum number of items to return.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_admins_list(
            token, team_id, content_type, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def admin_teams_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_domain: str,
        team_name: str,
        *,
        team_description: str | None = None,
        team_discoverability: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Create an Enterprise team.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_domain: Team domain (for example, slacksoftballteam).
            team_name: Team name (for example, Slack Softball Team).
            team_description: Description for the team.
            team_discoverability: Who can join the team. A team's discoverability can be ``open``, ``closed``,
                ``invite_only``, or ``unlisted``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_create(
            token,
            content_type,
            team_domain,
            team_name,
            team_description=team_description,
            team_discoverability=team_discoverability,
            request_options=request_options,
        ).unwrap()

    def admin_teams_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all teams on an Enterprise organization

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 100 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_list(
            token, content_type, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def admin_teams_owners_list(
        self,
        token: str,
        team_id: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all of the owners on a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            team_id: Value sent with the request.
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_owners_list(
            token, team_id, content_type, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def admin_teams_settings_info(
        self,
        team_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Fetch information about settings in a workspace

        Args:
            team_id: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_settings_info(
            team_id, token, content_type, request_options=request_options
        ).unwrap()

    def admin_teams_settings_set_default_channels(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        team_id: str,
        channel_ids: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set the default channels of a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            team_id: ID for the workspace to set the default channel for.
            channel_ids: An array of channel IDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_settings_set_default_channels(
            content_type, token, team_id, channel_ids, request_options=request_options
        ).unwrap()

    def admin_teams_settings_set_description(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        description: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set the description of a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: ID for the workspace to set the description for.
            description: The new description for the workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_settings_set_description(
            token, content_type, team_id, description, request_options=request_options
        ).unwrap()

    def admin_teams_settings_set_discoverability(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        discoverability: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """An API method that allows admins to set the discoverability of a given workspace

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: The ID of the workspace to set discoverability on.
            discoverability: This workspace's discovery setting. It must be set to one of ``open``, ``invite_only``,
                ``closed``, or ``unlisted``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_settings_set_discoverability(
            token, content_type, team_id, discoverability, request_options=request_options
        ).unwrap()

    def admin_teams_settings_set_icon(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        image_url: str,
        team_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Sets the icon of a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            image_url: Image URL for the icon
            team_id: ID for the workspace to set the icon for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_settings_set_icon(
            content_type, token, image_url, team_id, request_options=request_options
        ).unwrap()

    def admin_teams_settings_set_name(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set the name of a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: ID for the workspace to set the name for.
            name: The new name of the workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_teams_settings_set_name(
            token, content_type, team_id, name, request_options=request_options
        ).unwrap()

    def admin_usergroups_add_channels(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        channel_ids: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add one or more default channels to an IDP group.

        Args:
            token: Authentication token. Requires scope: ``admin.usergroups:write``
            content_type: Value sent with the request.
            usergroup_id: ID of the IDP group to add default channels for.
            channel_ids: Comma separated string of channel IDs.
            team_id: The workspace to add default channels in.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_usergroups_add_channels(
            token, content_type, usergroup_id, channel_ids, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_usergroups_add_teams(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        team_ids: str,
        *,
        auto_provision: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Associate one or more default workspaces with an organization-wide IDP group.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            usergroup_id: An encoded usergroup (IDP Group) ID.
            team_ids: A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the
                organization associated with the token.
            auto_provision: When ``true``, this method automatically creates new workspace accounts for the IDP group
                members.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_usergroups_add_teams(
            token, content_type, usergroup_id, team_ids, auto_provision=auto_provision, request_options=request_options
        ).unwrap()

    def admin_usergroups_list_channels(
        self,
        usergroup_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        include_num_members: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List the channels linked to an org-level IDP group (user group).

        Args:
            usergroup_id: ID of the IDP group to list default channels for.
            token: Authentication token. Requires scope: ``admin.usergroups:read``
            content_type: Value sent with the request.
            team_id: ID of the the workspace.
            include_num_members: Flag to include or exclude the count of members per channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_usergroups_list_channels(
            usergroup_id,
            token,
            content_type,
            team_id=team_id,
            include_num_members=include_num_members,
            request_options=request_options,
        ).unwrap()

    def admin_usergroups_remove_channels(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        channel_ids: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove one or more default channels from an org-level IDP group (user group).

        Args:
            token: Authentication token. Requires scope: ``admin.usergroups:write``
            content_type: Value sent with the request.
            usergroup_id: ID of the IDP Group
            channel_ids: Comma-separated string of channel IDs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_usergroups_remove_channels(
            token, content_type, usergroup_id, channel_ids, request_options=request_options
        ).unwrap()

    def admin_users_assign(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        is_restricted: bool | None = None,
        is_ultra_restricted: bool | None = None,
        channel_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an Enterprise user to a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to add to the workspace.
            is_restricted: True if user should be added to the workspace as a guest.
            is_ultra_restricted: True if user should be added to the workspace as a single-channel guest.
            channel_ids: Comma separated values of channel IDs to add user in the new workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_assign(
            token,
            content_type,
            team_id,
            user_id,
            is_restricted=is_restricted,
            is_ultra_restricted=is_ultra_restricted,
            channel_ids=channel_ids,
            request_options=request_options,
        ).unwrap()

    def admin_users_invite(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        email: str,
        channel_ids: str,
        *,
        custom_message: str | None = None,
        real_name: str | None = None,
        resend: bool | None = None,
        is_restricted: bool | None = None,
        is_ultra_restricted: bool | None = None,
        guest_expiration_ts: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Invite a user to a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            email: The email address of the person to invite.
            channel_ids: A comma-separated list of ``channel_id``s for this user to join. At least one channel is
                required.
            custom_message: An optional message to send to the user in the invite email.
            real_name: Full name of the user.
            resend: Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
            is_restricted: Is this user a multi-channel guest user? (default: false)
            is_ultra_restricted: Is this user a single channel guest user? (default: false)
            guest_expiration_ts: Timestamp when guest account should be disabled. Only include this timestamp if you are
                inviting a guest user and you want their account to expire on a certain date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_invite(
            token,
            content_type,
            team_id,
            email,
            channel_ids,
            custom_message=custom_message,
            real_name=real_name,
            resend=resend,
            is_restricted=is_restricted,
            is_ultra_restricted=is_ultra_restricted,
            guest_expiration_ts=guest_expiration_ts,
            request_options=request_options,
        ).unwrap()

    def admin_users_list(
        self,
        team_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List users on a workspace

        Args:
            team_id: The ID (``T1234``) of the workspace.
            token: Authentication token. Requires scope: ``admin.users:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            limit: Limit for how many users to be retrieved per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_list(
            team_id, token, content_type, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def admin_users_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove a user from a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to remove.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_remove(
            token, content_type, team_id, user_id, request_options=request_options
        ).unwrap()

    def admin_users_session_invalidate(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        session_id: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Invalidate a single session for a user by session_id

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: ID of the team that the session belongs to
            session_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_session_invalidate(
            token, content_type, team_id, session_id, request_options=request_options
        ).unwrap()

    def admin_users_session_reset(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        user_id: str,
        *,
        mobile_only: bool | None = None,
        web_only: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Wipes all valid sessions on all devices for a given user

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            user_id: The ID of the user to wipe sessions for
            mobile_only: Only expire mobile sessions (default: false)
            web_only: Only expire web sessions (default: false)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_session_reset(
            token, content_type, user_id, mobile_only=mobile_only, web_only=web_only, request_options=request_options
        ).unwrap()

    def admin_users_set_admin(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set an existing guest, regular user, or owner to be an admin user.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to designate as an admin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_set_admin(
            token, content_type, team_id, user_id, request_options=request_options
        ).unwrap()

    def admin_users_set_expiration(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        expiration_ts: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set an expiration for a guest user

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to set an expiration for.
            expiration_ts: Timestamp when guest account should be disabled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_set_expiration(
            token, content_type, team_id, user_id, expiration_ts, request_options=request_options
        ).unwrap()

    def admin_users_set_owner(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set an existing guest, regular user, or admin user to be a workspace owner.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: Id of the user to promote to owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_set_owner(
            token, content_type, team_id, user_id, request_options=request_options
        ).unwrap()

    def admin_users_set_regular(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set an existing guest user, admin user, or owner to be a regular user.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to designate as a regular user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_users_set_regular(
            token, content_type, team_id, user_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AdminWithRawResponse:
        return self._with_raw_response


class AsyncAdmin:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminWithRawResponse(client, server, auth)

    async def admin_apps_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Approve an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to approve.
            request_id: The id of the request to approve.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_apps_approve(
                token,
                content_type,
                app_id=app_id,
                request_id=request_id,
                team_id=team_id,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_apps_approved_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        enterprise_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List approved apps for an org or workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            enterprise_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_apps_approved_list(
                token,
                content_type,
                limit=limit,
                cursor=cursor,
                team_id=team_id,
                enterprise_id=enterprise_id,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_apps_requests_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List app requests for a team/workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_apps_requests_list(
                token, content_type, limit=limit, cursor=cursor, team_id=team_id, request_options=request_options
            )
        ).unwrap()

    async def admin_apps_restrict(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Restrict an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to restrict.
            request_id: The id of the request to restrict.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_apps_restrict(
                token,
                content_type,
                app_id=app_id,
                request_id=request_id,
                team_id=team_id,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_apps_restricted_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        enterprise_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List restricted apps for an org or workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            enterprise_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_apps_restricted_list(
                token,
                content_type,
                limit=limit,
                cursor=cursor,
                team_id=team_id,
                enterprise_id=enterprise_id,
                request_options=request_options,
            )
        ).unwrap()

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

    async def admin_conversations_ekm_list_original_connected_channel_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel_ids: str | None = None,
        team_ids: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all disconnected channels—i.e., channels that were once connected to other workspaces and then
        disconnected—and the corresponding original channel IDs for key revocation with EKM.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            channel_ids: A comma-separated list of channels to filter to.
            team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_ekm_list_original_connected_channel_info(
                token,
                content_type,
                channel_ids=channel_ids,
                team_ids=team_ids,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
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

    async def admin_conversations_restrict_access_add_group(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        group_id: str,
        channel_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an allowlist of IDP groups for accessing a channel

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.conversations:write``
            group_id: The `IDP Group
                <https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org>`__
                ID to be an allowlist for the private channel.
            channel_id: The channel to link this group to.
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_restrict_access_add_group(
                content_type, token, group_id, channel_id, team_id=team_id, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_restrict_access_list_groups(
        self,
        token: str,
        channel_id: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all IDP Groups linked to a channel

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            channel_id: Value sent with the request.
            content_type: Value sent with the request.
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_restrict_access_list_groups(
                token, channel_id, content_type, team_id=team_id, request_options=request_options
            )
        ).unwrap()

    async def admin_conversations_restrict_access_remove_group(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        team_id: str,
        group_id: str,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove a linked IDP group linked from a private channel

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.conversations:write``
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            group_id: The `IDP Group
                <https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org>`__
                ID to remove from the private channel.
            channel_id: The channel to remove the linked group from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_restrict_access_remove_group(
                content_type, token, team_id, group_id, channel_id, request_options=request_options
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

    async def admin_emoji_add(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        url: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent
                backgrounds work best.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_add(
                content_type, token, name, url, request_options=request_options
            )
        ).unwrap()

    async def admin_emoji_add_alias(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        alias_for: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an emoji alias.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be aliased. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            alias_for: The alias of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_add_alias(
                content_type, token, name, alias_for, request_options=request_options
            )
        ).unwrap()

    async def admin_emoji_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List emoji for an Enterprise Grid organization.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_list(
                token, content_type, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def admin_emoji_remove(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove an emoji across an Enterprise Grid organization

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_remove(content_type, token, name, request_options=request_options)
        ).unwrap()

    async def admin_emoji_rename(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        new_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Rename an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be renamed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            new_name: The new name of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_rename(
                content_type, token, name, new_name, request_options=request_options
            )
        ).unwrap()

    async def admin_invite_requests_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        invite_request_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Approve a workspace invite request.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:write``
            content_type: Value sent with the request.
            invite_request_id: ID of the request to invite.
            team_id: ID for the workspace where the invite request was made.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_invite_requests_approve(
                token, content_type, invite_request_id, team_id=team_id, request_options=request_options
            )
        ).unwrap()

    async def admin_invite_requests_approved_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all approved workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous API response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000,
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_invite_requests_approved_list(
                token, content_type, team_id=team_id, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def admin_invite_requests_denied_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all denied workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous api response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_invite_requests_denied_list(
                token, content_type, team_id=team_id, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def admin_invite_requests_deny(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        invite_request_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Deny a workspace invite request.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:write``
            content_type: Value sent with the request.
            invite_request_id: ID of the request to invite.
            team_id: ID for the workspace where the invite request was made.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_invite_requests_deny(
                token, content_type, invite_request_id, team_id=team_id, request_options=request_options
            )
        ).unwrap()

    async def admin_invite_requests_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all pending workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous API response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000,
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_invite_requests_list(
                token, content_type, team_id=team_id, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_admins_list(
        self,
        token: str,
        team_id: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all of the admins on a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            team_id: Value sent with the request.
            content_type: Value sent with the request.
            limit: The maximum number of items to return.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_admins_list(
                token, team_id, content_type, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_domain: str,
        team_name: str,
        *,
        team_description: str | None = None,
        team_discoverability: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Create an Enterprise team.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_domain: Team domain (for example, slacksoftballteam).
            team_name: Team name (for example, Slack Softball Team).
            team_description: Description for the team.
            team_discoverability: Who can join the team. A team's discoverability can be ``open``, ``closed``,
                ``invite_only``, or ``unlisted``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_create(
                token,
                content_type,
                team_domain,
                team_name,
                team_description=team_description,
                team_discoverability=team_discoverability,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_teams_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all teams on an Enterprise organization

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 100 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_list(
                token, content_type, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_owners_list(
        self,
        token: str,
        team_id: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all of the owners on a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            team_id: Value sent with the request.
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_owners_list(
                token, team_id, content_type, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_settings_info(
        self,
        team_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Fetch information about settings in a workspace

        Args:
            team_id: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_settings_info(
                team_id, token, content_type, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_settings_set_default_channels(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        team_id: str,
        channel_ids: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set the default channels of a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            team_id: ID for the workspace to set the default channel for.
            channel_ids: An array of channel IDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_settings_set_default_channels(
                content_type, token, team_id, channel_ids, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_settings_set_description(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        description: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set the description of a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: ID for the workspace to set the description for.
            description: The new description for the workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_settings_set_description(
                token, content_type, team_id, description, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_settings_set_discoverability(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        discoverability: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """An API method that allows admins to set the discoverability of a given workspace

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: The ID of the workspace to set discoverability on.
            discoverability: This workspace's discovery setting. It must be set to one of ``open``, ``invite_only``,
                ``closed``, or ``unlisted``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_settings_set_discoverability(
                token, content_type, team_id, discoverability, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_settings_set_icon(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        image_url: str,
        team_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Sets the icon of a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            image_url: Image URL for the icon
            team_id: ID for the workspace to set the icon for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_settings_set_icon(
                content_type, token, image_url, team_id, request_options=request_options
            )
        ).unwrap()

    async def admin_teams_settings_set_name(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set the name of a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: ID for the workspace to set the name for.
            name: The new name of the workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_teams_settings_set_name(
                token, content_type, team_id, name, request_options=request_options
            )
        ).unwrap()

    async def admin_usergroups_add_channels(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        channel_ids: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add one or more default channels to an IDP group.

        Args:
            token: Authentication token. Requires scope: ``admin.usergroups:write``
            content_type: Value sent with the request.
            usergroup_id: ID of the IDP group to add default channels for.
            channel_ids: Comma separated string of channel IDs.
            team_id: The workspace to add default channels in.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_usergroups_add_channels(
                token, content_type, usergroup_id, channel_ids, team_id=team_id, request_options=request_options
            )
        ).unwrap()

    async def admin_usergroups_add_teams(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        team_ids: str,
        *,
        auto_provision: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Associate one or more default workspaces with an organization-wide IDP group.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            usergroup_id: An encoded usergroup (IDP Group) ID.
            team_ids: A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the
                organization associated with the token.
            auto_provision: When ``true``, this method automatically creates new workspace accounts for the IDP group
                members.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_usergroups_add_teams(
                token,
                content_type,
                usergroup_id,
                team_ids,
                auto_provision=auto_provision,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_usergroups_list_channels(
        self,
        usergroup_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        include_num_members: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List the channels linked to an org-level IDP group (user group).

        Args:
            usergroup_id: ID of the IDP group to list default channels for.
            token: Authentication token. Requires scope: ``admin.usergroups:read``
            content_type: Value sent with the request.
            team_id: ID of the the workspace.
            include_num_members: Flag to include or exclude the count of members per channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_usergroups_list_channels(
                usergroup_id,
                token,
                content_type,
                team_id=team_id,
                include_num_members=include_num_members,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_usergroups_remove_channels(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        channel_ids: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove one or more default channels from an org-level IDP group (user group).

        Args:
            token: Authentication token. Requires scope: ``admin.usergroups:write``
            content_type: Value sent with the request.
            usergroup_id: ID of the IDP Group
            channel_ids: Comma-separated string of channel IDs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_usergroups_remove_channels(
                token, content_type, usergroup_id, channel_ids, request_options=request_options
            )
        ).unwrap()

    async def admin_users_assign(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        is_restricted: bool | None = None,
        is_ultra_restricted: bool | None = None,
        channel_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an Enterprise user to a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to add to the workspace.
            is_restricted: True if user should be added to the workspace as a guest.
            is_ultra_restricted: True if user should be added to the workspace as a single-channel guest.
            channel_ids: Comma separated values of channel IDs to add user in the new workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_assign(
                token,
                content_type,
                team_id,
                user_id,
                is_restricted=is_restricted,
                is_ultra_restricted=is_ultra_restricted,
                channel_ids=channel_ids,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_users_invite(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        email: str,
        channel_ids: str,
        *,
        custom_message: str | None = None,
        real_name: str | None = None,
        resend: bool | None = None,
        is_restricted: bool | None = None,
        is_ultra_restricted: bool | None = None,
        guest_expiration_ts: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Invite a user to a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            email: The email address of the person to invite.
            channel_ids: A comma-separated list of ``channel_id``s for this user to join. At least one channel is
                required.
            custom_message: An optional message to send to the user in the invite email.
            real_name: Full name of the user.
            resend: Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
            is_restricted: Is this user a multi-channel guest user? (default: false)
            is_ultra_restricted: Is this user a single channel guest user? (default: false)
            guest_expiration_ts: Timestamp when guest account should be disabled. Only include this timestamp if you are
                inviting a guest user and you want their account to expire on a certain date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_invite(
                token,
                content_type,
                team_id,
                email,
                channel_ids,
                custom_message=custom_message,
                real_name=real_name,
                resend=resend,
                is_restricted=is_restricted,
                is_ultra_restricted=is_ultra_restricted,
                guest_expiration_ts=guest_expiration_ts,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_users_list(
        self,
        team_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List users on a workspace

        Args:
            team_id: The ID (``T1234``) of the workspace.
            token: Authentication token. Requires scope: ``admin.users:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            limit: Limit for how many users to be retrieved per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_list(
                team_id, token, content_type, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def admin_users_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove a user from a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to remove.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_remove(
                token, content_type, team_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def admin_users_session_invalidate(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        session_id: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Invalidate a single session for a user by session_id

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: ID of the team that the session belongs to
            session_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_session_invalidate(
                token, content_type, team_id, session_id, request_options=request_options
            )
        ).unwrap()

    async def admin_users_session_reset(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        user_id: str,
        *,
        mobile_only: bool | None = None,
        web_only: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Wipes all valid sessions on all devices for a given user

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            user_id: The ID of the user to wipe sessions for
            mobile_only: Only expire mobile sessions (default: false)
            web_only: Only expire web sessions (default: false)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_session_reset(
                token,
                content_type,
                user_id,
                mobile_only=mobile_only,
                web_only=web_only,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_users_set_admin(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set an existing guest, regular user, or owner to be an admin user.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to designate as an admin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_set_admin(
                token, content_type, team_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def admin_users_set_expiration(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        expiration_ts: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set an expiration for a guest user

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to set an expiration for.
            expiration_ts: Timestamp when guest account should be disabled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_set_expiration(
                token, content_type, team_id, user_id, expiration_ts, request_options=request_options
            )
        ).unwrap()

    async def admin_users_set_owner(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set an existing guest, regular user, or admin user to be a workspace owner.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: Id of the user to promote to owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_set_owner(
                token, content_type, team_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def admin_users_set_regular(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Set an existing guest user, admin user, or owner to be a regular user.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to designate as a regular user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_users_set_regular(
                token, content_type, team_id, user_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAdminWithRawResponse:
        return self._with_raw_response


class AdminWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def admin_apps_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Approve an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to approve.
            request_id: The id of the request to approve.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.apps.approve"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("app_id", app_id),
                    param[str | None]("request_id", request_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_apps_approved_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        enterprise_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List approved apps for an org or workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            enterprise_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.apps.approved.list"),
            query_params=[
                param[str]("token", token),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("team_id", team_id),
                param[str | None]("enterprise_id", enterprise_id),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_apps_requests_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List app requests for a team/workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.apps.requests.list"),
            query_params=[
                param[str]("token", token),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("team_id", team_id),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_apps_restrict(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Restrict an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to restrict.
            request_id: The id of the request to restrict.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.apps.restrict"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("app_id", app_id),
                    param[str | None]("request_id", request_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_apps_restricted_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        enterprise_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List restricted apps for an org or workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            enterprise_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.apps.restricted.list"),
            query_params=[
                param[str]("token", token),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("team_id", team_id),
                param[str | None]("enterprise_id", enterprise_id),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def admin_conversations_ekm_list_original_connected_channel_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel_ids: str | None = None,
        team_ids: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all disconnected channels—i.e., channels that were once connected to other workspaces and then
        disconnected—and the corresponding original channel IDs for key revocation with EKM.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            channel_ids: A comma-separated list of channels to filter to.
            team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.ekm.listOriginalConnectedChannelInfo"),
            query_params=[
                param[str]("token", token),
                param[str | None]("channel_ids", channel_ids),
                param[str | None]("team_ids", team_ids),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
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

    def admin_conversations_restrict_access_add_group(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        group_id: str,
        channel_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an allowlist of IDP groups for accessing a channel

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.conversations:write``
            group_id: The `IDP Group
                <https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org>`__
                ID to be an allowlist for the private channel.
            channel_id: The channel to link this group to.
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.restrictAccess.addGroup"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("token", token),
                    param[str]("group_id", group_id),
                    param[str]("channel_id", channel_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_restrict_access_list_groups(
        self,
        token: str,
        channel_id: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all IDP Groups linked to a channel

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            channel_id: Value sent with the request.
            content_type: Value sent with the request.
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.restrictAccess.listGroups"),
            query_params=[
                param[str]("token", token), param[str]("channel_id", channel_id), param[str | None]("team_id", team_id)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_conversations_restrict_access_remove_group(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        team_id: str,
        group_id: str,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove a linked IDP group linked from a private channel

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.conversations:write``
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            group_id: The `IDP Group
                <https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org>`__
                ID to remove from the private channel.
            channel_id: The channel to remove the linked group from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.restrictAccess.removeGroup"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("token", token),
                    param[str]("team_id", team_id),
                    param[str]("group_id", group_id),
                    param[str]("channel_id", channel_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
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

    def admin_emoji_add(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        url: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent
                backgrounds work best.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.add"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("url", url)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_emoji_add_alias(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        alias_for: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an emoji alias.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be aliased. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            alias_for: The alias of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.addAlias"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("alias_for", alias_for)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_emoji_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List emoji for an Enterprise Grid organization.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.emoji.list"),
            query_params=[
                param[str]("token", token), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_emoji_remove(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove an emoji across an Enterprise Grid organization

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.remove"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_emoji_rename(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        new_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Rename an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be renamed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            new_name: The new name of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.rename"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("new_name", new_name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_invite_requests_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        invite_request_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Approve a workspace invite request.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:write``
            content_type: Value sent with the request.
            invite_request_id: ID of the request to invite.
            team_id: ID for the workspace where the invite request was made.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.inviteRequests.approve"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("invite_request_id", invite_request_id), param[str | None]("team_id", team_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_invite_requests_approved_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all approved workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous API response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000,
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.inviteRequests.approved.list"),
            query_params=[
                param[str | None]("team_id", team_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_invite_requests_denied_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all denied workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous api response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.inviteRequests.denied.list"),
            query_params=[
                param[str | None]("team_id", team_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_invite_requests_deny(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        invite_request_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Deny a workspace invite request.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:write``
            content_type: Value sent with the request.
            invite_request_id: ID of the request to invite.
            team_id: ID for the workspace where the invite request was made.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.inviteRequests.deny"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("invite_request_id", invite_request_id), param[str | None]("team_id", team_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_invite_requests_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all pending workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous API response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000,
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.inviteRequests.list"),
            query_params=[
                param[str | None]("team_id", team_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_admins_list(
        self,
        token: str,
        team_id: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all of the admins on a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            team_id: Value sent with the request.
            content_type: Value sent with the request.
            limit: The maximum number of items to return.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.teams.admins.list"),
            query_params=[
                param[str]("token", token),
                param[str]("team_id", team_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_domain: str,
        team_name: str,
        *,
        team_description: str | None = None,
        team_discoverability: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Create an Enterprise team.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_domain: Team domain (for example, slacksoftballteam).
            team_name: Team name (for example, Slack Softball Team).
            team_description: Description for the team.
            team_discoverability: Who can join the team. A team's discoverability can be ``open``, ``closed``,
                ``invite_only``, or ``unlisted``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.create"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("team_domain", team_domain),
                    param[str]("team_name", team_name),
                    param[str | None]("team_description", team_description),
                    param[str | None]("team_discoverability", team_discoverability),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all teams on an Enterprise organization

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 100 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.teams.list"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_owners_list(
        self,
        token: str,
        team_id: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all of the owners on a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            team_id: Value sent with the request.
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.teams.owners.list"),
            query_params=[
                param[str]("token", token),
                param[str]("team_id", team_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_settings_info(
        self,
        team_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Fetch information about settings in a workspace

        Args:
            team_id: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.teams.settings.info"),
            query_params=[param[str]("team_id", team_id)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_settings_set_default_channels(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        team_id: str,
        channel_ids: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set the default channels of a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            team_id: ID for the workspace to set the default channel for.
            channel_ids: An array of channel IDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setDefaultChannels"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [param[str]("token", token), param[str]("team_id", team_id), param[str]("channel_ids", channel_ids)]
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_settings_set_description(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        description: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set the description of a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: ID for the workspace to set the description for.
            description: The new description for the workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setDescription"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("description", description)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_settings_set_discoverability(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        discoverability: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """An API method that allows admins to set the discoverability of a given workspace

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: The ID of the workspace to set discoverability on.
            discoverability: This workspace's discovery setting. It must be set to one of ``open``, ``invite_only``,
                ``closed``, or ``unlisted``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setDiscoverability"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("discoverability", discoverability)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_settings_set_icon(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        image_url: str,
        team_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Sets the icon of a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            image_url: Image URL for the icon
            team_id: ID for the workspace to set the icon for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setIcon"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [param[str]("token", token), param[str]("image_url", image_url), param[str]("team_id", team_id)]
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_teams_settings_set_name(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set the name of a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: ID for the workspace to set the name for.
            name: The new name of the workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setName"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_usergroups_add_channels(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        channel_ids: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add one or more default channels to an IDP group.

        Args:
            token: Authentication token. Requires scope: ``admin.usergroups:write``
            content_type: Value sent with the request.
            usergroup_id: ID of the IDP group to add default channels for.
            channel_ids: Comma separated string of channel IDs.
            team_id: The workspace to add default channels in.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.usergroups.addChannels"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("usergroup_id", usergroup_id),
                    param[str]("channel_ids", channel_ids),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_usergroups_add_teams(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        team_ids: str,
        *,
        auto_provision: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Associate one or more default workspaces with an organization-wide IDP group.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            usergroup_id: An encoded usergroup (IDP Group) ID.
            team_ids: A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the
                organization associated with the token.
            auto_provision: When ``true``, this method automatically creates new workspace accounts for the IDP group
                members.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.usergroups.addTeams"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("usergroup_id", usergroup_id),
                    param[str]("team_ids", team_ids),
                    param[bool | None]("auto_provision", auto_provision),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_usergroups_list_channels(
        self,
        usergroup_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        include_num_members: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List the channels linked to an org-level IDP group (user group).

        Args:
            usergroup_id: ID of the IDP group to list default channels for.
            token: Authentication token. Requires scope: ``admin.usergroups:read``
            content_type: Value sent with the request.
            team_id: ID of the the workspace.
            include_num_members: Flag to include or exclude the count of members per channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.usergroups.listChannels"),
            query_params=[
                param[str]("usergroup_id", usergroup_id),
                param[str | None]("team_id", team_id),
                param[bool | None]("include_num_members", include_num_members),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_usergroups_remove_channels(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        channel_ids: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove one or more default channels from an org-level IDP group (user group).

        Args:
            token: Authentication token. Requires scope: ``admin.usergroups:write``
            content_type: Value sent with the request.
            usergroup_id: ID of the IDP Group
            channel_ids: Comma-separated string of channel IDs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.usergroups.removeChannels"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("usergroup_id", usergroup_id), param[str]("channel_ids", channel_ids)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_assign(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        is_restricted: bool | None = None,
        is_ultra_restricted: bool | None = None,
        channel_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an Enterprise user to a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to add to the workspace.
            is_restricted: True if user should be added to the workspace as a guest.
            is_ultra_restricted: True if user should be added to the workspace as a single-channel guest.
            channel_ids: Comma separated values of channel IDs to add user in the new workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.assign"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("team_id", team_id),
                    param[str]("user_id", user_id),
                    param[bool | None]("is_restricted", is_restricted),
                    param[bool | None]("is_ultra_restricted", is_ultra_restricted),
                    param[str | None]("channel_ids", channel_ids),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_invite(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        email: str,
        channel_ids: str,
        *,
        custom_message: str | None = None,
        real_name: str | None = None,
        resend: bool | None = None,
        is_restricted: bool | None = None,
        is_ultra_restricted: bool | None = None,
        guest_expiration_ts: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Invite a user to a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            email: The email address of the person to invite.
            channel_ids: A comma-separated list of ``channel_id``s for this user to join. At least one channel is
                required.
            custom_message: An optional message to send to the user in the invite email.
            real_name: Full name of the user.
            resend: Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
            is_restricted: Is this user a multi-channel guest user? (default: false)
            is_ultra_restricted: Is this user a single channel guest user? (default: false)
            guest_expiration_ts: Timestamp when guest account should be disabled. Only include this timestamp if you are
                inviting a guest user and you want their account to expire on a certain date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.invite"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("team_id", team_id),
                    param[str]("email", email),
                    param[str]("channel_ids", channel_ids),
                    param[str | None]("custom_message", custom_message),
                    param[str | None]("real_name", real_name),
                    param[bool | None]("resend", resend),
                    param[bool | None]("is_restricted", is_restricted),
                    param[bool | None]("is_ultra_restricted", is_ultra_restricted),
                    param[str | None]("guest_expiration_ts", guest_expiration_ts),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_list(
        self,
        team_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List users on a workspace

        Args:
            team_id: The ID (``T1234``) of the workspace.
            token: Authentication token. Requires scope: ``admin.users:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            limit: Limit for how many users to be retrieved per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.users.list"),
            query_params=[
                param[str]("team_id", team_id), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove a user from a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to remove.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("user_id", user_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_session_invalidate(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        session_id: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Invalidate a single session for a user by session_id

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: ID of the team that the session belongs to
            session_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.session.invalidate"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[int]("session_id", session_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_session_reset(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        user_id: str,
        *,
        mobile_only: bool | None = None,
        web_only: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Wipes all valid sessions on all devices for a given user

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            user_id: The ID of the user to wipe sessions for
            mobile_only: Only expire mobile sessions (default: false)
            web_only: Only expire web sessions (default: false)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.session.reset"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("user_id", user_id),
                    param[bool | None]("mobile_only", mobile_only),
                    param[bool | None]("web_only", web_only),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_set_admin(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set an existing guest, regular user, or owner to be an admin user.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to designate as an admin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.setAdmin"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("user_id", user_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_set_expiration(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        expiration_ts: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set an expiration for a guest user

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to set an expiration for.
            expiration_ts: Timestamp when guest account should be disabled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.setExpiration"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("team_id", team_id),
                    param[str]("user_id", user_id),
                    param[int]("expiration_ts", expiration_ts),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_set_owner(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set an existing guest, regular user, or admin user to be a workspace owner.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: Id of the user to promote to owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.setOwner"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("user_id", user_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_users_set_regular(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set an existing guest user, admin user, or owner to be a regular user.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to designate as a regular user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.setRegular"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("user_id", user_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAdminWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def admin_apps_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Approve an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to approve.
            request_id: The id of the request to approve.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.apps.approve"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("app_id", app_id),
                    param[str | None]("request_id", request_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_apps_approved_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        enterprise_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List approved apps for an org or workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            enterprise_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.apps.approved.list"),
            query_params=[
                param[str]("token", token),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("team_id", team_id),
                param[str | None]("enterprise_id", enterprise_id),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_apps_requests_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List app requests for a team/workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.apps.requests.list"),
            query_params=[
                param[str]("token", token),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("team_id", team_id),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_apps_restrict(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Restrict an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to restrict.
            request_id: The id of the request to restrict.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.apps.restrict"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("app_id", app_id),
                    param[str | None]("request_id", request_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_apps_restricted_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        team_id: str | None = None,
        enterprise_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List restricted apps for an org or workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            team_id: Value sent with the request.
            enterprise_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.apps.restricted.list"),
            query_params=[
                param[str]("token", token),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("team_id", team_id),
                param[str | None]("enterprise_id", enterprise_id),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    async def admin_conversations_ekm_list_original_connected_channel_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel_ids: str | None = None,
        team_ids: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all disconnected channels—i.e., channels that were once connected to other workspaces and then
        disconnected—and the corresponding original channel IDs for key revocation with EKM.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            channel_ids: A comma-separated list of channels to filter to.
            team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.ekm.listOriginalConnectedChannelInfo"),
            query_params=[
                param[str]("token", token),
                param[str | None]("channel_ids", channel_ids),
                param[str | None]("team_ids", team_ids),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
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

    async def admin_conversations_restrict_access_add_group(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        group_id: str,
        channel_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an allowlist of IDP groups for accessing a channel

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.conversations:write``
            group_id: The `IDP Group
                <https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org>`__
                ID to be an allowlist for the private channel.
            channel_id: The channel to link this group to.
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.restrictAccess.addGroup"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("token", token),
                    param[str]("group_id", group_id),
                    param[str]("channel_id", channel_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_restrict_access_list_groups(
        self,
        token: str,
        channel_id: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all IDP Groups linked to a channel

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            channel_id: Value sent with the request.
            content_type: Value sent with the request.
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.restrictAccess.listGroups"),
            query_params=[
                param[str]("token", token), param[str]("channel_id", channel_id), param[str | None]("team_id", team_id)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_conversations_restrict_access_remove_group(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        team_id: str,
        group_id: str,
        channel_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove a linked IDP group linked from a private channel

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.conversations:write``
            team_id: The workspace where the channel exists. This argument is required for channels only tied to one
                workspace, and optional for channels that are shared across an organization.
            group_id: The `IDP Group
                <https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org>`__
                ID to remove from the private channel.
            channel_id: The channel to remove the linked group from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.conversations.restrictAccess.removeGroup"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("token", token),
                    param[str]("team_id", team_id),
                    param[str]("group_id", group_id),
                    param[str]("channel_id", channel_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
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

    async def admin_emoji_add(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        url: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent
                backgrounds work best.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.add"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("url", url)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_emoji_add_alias(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        alias_for: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an emoji alias.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be aliased. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            alias_for: The alias of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.addAlias"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("alias_for", alias_for)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_emoji_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List emoji for an Enterprise Grid organization.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.emoji.list"),
            query_params=[
                param[str]("token", token), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_emoji_remove(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove an emoji across an Enterprise Grid organization

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.remove"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_emoji_rename(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        new_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Rename an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be renamed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            new_name: The new name of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.rename"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("new_name", new_name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_invite_requests_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        invite_request_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Approve a workspace invite request.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:write``
            content_type: Value sent with the request.
            invite_request_id: ID of the request to invite.
            team_id: ID for the workspace where the invite request was made.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.inviteRequests.approve"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("invite_request_id", invite_request_id), param[str | None]("team_id", team_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_invite_requests_approved_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all approved workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous API response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000,
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.inviteRequests.approved.list"),
            query_params=[
                param[str | None]("team_id", team_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_invite_requests_denied_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all denied workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous api response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.inviteRequests.denied.list"),
            query_params=[
                param[str | None]("team_id", team_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_invite_requests_deny(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        invite_request_id: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Deny a workspace invite request.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:write``
            content_type: Value sent with the request.
            invite_request_id: ID of the request to invite.
            team_id: ID for the workspace where the invite request was made.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.inviteRequests.deny"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("invite_request_id", invite_request_id), param[str | None]("team_id", team_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_invite_requests_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all pending workspace invite requests.

        Args:
            token: Authentication token. Requires scope: ``admin.invites:read``
            content_type: Value sent with the request.
            team_id: ID for the workspace where the invite requests were made.
            cursor: Value of the ``next_cursor`` field sent as part of the previous API response
            limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000,
                both inclusive
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.inviteRequests.list"),
            query_params=[
                param[str | None]("team_id", team_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_admins_list(
        self,
        token: str,
        team_id: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all of the admins on a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            team_id: Value sent with the request.
            content_type: Value sent with the request.
            limit: The maximum number of items to return.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.teams.admins.list"),
            query_params=[
                param[str]("token", token),
                param[str]("team_id", team_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_domain: str,
        team_name: str,
        *,
        team_description: str | None = None,
        team_discoverability: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Create an Enterprise team.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_domain: Team domain (for example, slacksoftballteam).
            team_name: Team name (for example, Slack Softball Team).
            team_description: Description for the team.
            team_discoverability: Who can join the team. A team's discoverability can be ``open``, ``closed``,
                ``invite_only``, or ``unlisted``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.create"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("team_domain", team_domain),
                    param[str]("team_name", team_name),
                    param[str | None]("team_description", team_description),
                    param[str | None]("team_discoverability", team_discoverability),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all teams on an Enterprise organization

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 100 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.teams.list"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_owners_list(
        self,
        token: str,
        team_id: str,
        content_type: ContentTypeOrStr,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all of the owners on a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            team_id: Value sent with the request.
            content_type: Value sent with the request.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.teams.owners.list"),
            query_params=[
                param[str]("token", token),
                param[str]("team_id", team_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_settings_info(
        self,
        team_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Fetch information about settings in a workspace

        Args:
            team_id: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.teams.settings.info"),
            query_params=[param[str]("team_id", team_id)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_settings_set_default_channels(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        team_id: str,
        channel_ids: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set the default channels of a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            team_id: ID for the workspace to set the default channel for.
            channel_ids: An array of channel IDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setDefaultChannels"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [param[str]("token", token), param[str]("team_id", team_id), param[str]("channel_ids", channel_ids)]
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_settings_set_description(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        description: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set the description of a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: ID for the workspace to set the description for.
            description: The new description for the workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setDescription"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("description", description)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_settings_set_discoverability(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        discoverability: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """An API method that allows admins to set the discoverability of a given workspace

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: The ID of the workspace to set discoverability on.
            discoverability: This workspace's discovery setting. It must be set to one of ``open``, ``invite_only``,
                ``closed``, or ``unlisted``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setDiscoverability"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("discoverability", discoverability)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_settings_set_icon(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        image_url: str,
        team_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Sets the icon of a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            image_url: Image URL for the icon
            team_id: ID for the workspace to set the icon for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setIcon"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [param[str]("token", token), param[str]("image_url", image_url), param[str]("team_id", team_id)]
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_teams_settings_set_name(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set the name of a given workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            team_id: ID for the workspace to set the name for.
            name: The new name of the workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.teams.settings.setName"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_usergroups_add_channels(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        channel_ids: str,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add one or more default channels to an IDP group.

        Args:
            token: Authentication token. Requires scope: ``admin.usergroups:write``
            content_type: Value sent with the request.
            usergroup_id: ID of the IDP group to add default channels for.
            channel_ids: Comma separated string of channel IDs.
            team_id: The workspace to add default channels in.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.usergroups.addChannels"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("usergroup_id", usergroup_id),
                    param[str]("channel_ids", channel_ids),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_usergroups_add_teams(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        team_ids: str,
        *,
        auto_provision: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Associate one or more default workspaces with an organization-wide IDP group.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:write``
            content_type: Value sent with the request.
            usergroup_id: An encoded usergroup (IDP Group) ID.
            team_ids: A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the
                organization associated with the token.
            auto_provision: When ``true``, this method automatically creates new workspace accounts for the IDP group
                members.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.usergroups.addTeams"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("usergroup_id", usergroup_id),
                    param[str]("team_ids", team_ids),
                    param[bool | None]("auto_provision", auto_provision),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_usergroups_list_channels(
        self,
        usergroup_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        include_num_members: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List the channels linked to an org-level IDP group (user group).

        Args:
            usergroup_id: ID of the IDP group to list default channels for.
            token: Authentication token. Requires scope: ``admin.usergroups:read``
            content_type: Value sent with the request.
            team_id: ID of the the workspace.
            include_num_members: Flag to include or exclude the count of members per channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.usergroups.listChannels"),
            query_params=[
                param[str]("usergroup_id", usergroup_id),
                param[str | None]("team_id", team_id),
                param[bool | None]("include_num_members", include_num_members),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_usergroups_remove_channels(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup_id: str,
        channel_ids: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove one or more default channels from an org-level IDP group (user group).

        Args:
            token: Authentication token. Requires scope: ``admin.usergroups:write``
            content_type: Value sent with the request.
            usergroup_id: ID of the IDP Group
            channel_ids: Comma-separated string of channel IDs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.usergroups.removeChannels"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("usergroup_id", usergroup_id), param[str]("channel_ids", channel_ids)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_assign(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        is_restricted: bool | None = None,
        is_ultra_restricted: bool | None = None,
        channel_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an Enterprise user to a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to add to the workspace.
            is_restricted: True if user should be added to the workspace as a guest.
            is_ultra_restricted: True if user should be added to the workspace as a single-channel guest.
            channel_ids: Comma separated values of channel IDs to add user in the new workspace.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.assign"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("team_id", team_id),
                    param[str]("user_id", user_id),
                    param[bool | None]("is_restricted", is_restricted),
                    param[bool | None]("is_ultra_restricted", is_ultra_restricted),
                    param[str | None]("channel_ids", channel_ids),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_invite(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        email: str,
        channel_ids: str,
        *,
        custom_message: str | None = None,
        real_name: str | None = None,
        resend: bool | None = None,
        is_restricted: bool | None = None,
        is_ultra_restricted: bool | None = None,
        guest_expiration_ts: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Invite a user to a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            email: The email address of the person to invite.
            channel_ids: A comma-separated list of ``channel_id``s for this user to join. At least one channel is
                required.
            custom_message: An optional message to send to the user in the invite email.
            real_name: Full name of the user.
            resend: Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
            is_restricted: Is this user a multi-channel guest user? (default: false)
            is_ultra_restricted: Is this user a single channel guest user? (default: false)
            guest_expiration_ts: Timestamp when guest account should be disabled. Only include this timestamp if you are
                inviting a guest user and you want their account to expire on a certain date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.invite"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("team_id", team_id),
                    param[str]("email", email),
                    param[str]("channel_ids", channel_ids),
                    param[str | None]("custom_message", custom_message),
                    param[str | None]("real_name", real_name),
                    param[bool | None]("resend", resend),
                    param[bool | None]("is_restricted", is_restricted),
                    param[bool | None]("is_ultra_restricted", is_ultra_restricted),
                    param[str | None]("guest_expiration_ts", guest_expiration_ts),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_list(
        self,
        team_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List users on a workspace

        Args:
            team_id: The ID (``T1234``) of the workspace.
            token: Authentication token. Requires scope: ``admin.users:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            limit: Limit for how many users to be retrieved per page
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.users.list"),
            query_params=[
                param[str]("team_id", team_id), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove a user from a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to remove.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("user_id", user_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_session_invalidate(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        session_id: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Invalidate a single session for a user by session_id

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: ID of the team that the session belongs to
            session_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.session.invalidate"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[int]("session_id", session_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_session_reset(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        user_id: str,
        *,
        mobile_only: bool | None = None,
        web_only: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Wipes all valid sessions on all devices for a given user

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            user_id: The ID of the user to wipe sessions for
            mobile_only: Only expire mobile sessions (default: false)
            web_only: Only expire web sessions (default: false)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.session.reset"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("user_id", user_id),
                    param[bool | None]("mobile_only", mobile_only),
                    param[bool | None]("web_only", web_only),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_set_admin(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set an existing guest, regular user, or owner to be an admin user.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to designate as an admin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.setAdmin"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("user_id", user_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_set_expiration(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        expiration_ts: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set an expiration for a guest user

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to set an expiration for.
            expiration_ts: Timestamp when guest account should be disabled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.setExpiration"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("team_id", team_id),
                    param[str]("user_id", user_id),
                    param[int]("expiration_ts", expiration_ts),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_set_owner(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set an existing guest, regular user, or admin user to be a workspace owner.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: Id of the user to promote to owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.setOwner"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("user_id", user_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_users_set_regular(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        team_id: str,
        user_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Set an existing guest user, admin user, or owner to be a regular user.

        Args:
            token: Authentication token. Requires scope: ``admin.users:write``
            content_type: Value sent with the request.
            team_id: The ID (``T1234``) of the workspace.
            user_id: The ID of the user to designate as a regular user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.users.setRegular"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("team_id", team_id), param[str]("user_id", user_id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
