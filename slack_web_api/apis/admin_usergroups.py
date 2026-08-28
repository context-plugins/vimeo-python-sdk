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
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class AdminUsergroups:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminUsergroupsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AdminUsergroupsWithRawResponse:
        return self._with_raw_response


class AsyncAdminUsergroups:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminUsergroupsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAdminUsergroupsWithRawResponse:
        return self._with_raw_response


class AdminUsergroupsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminUsergroupsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
