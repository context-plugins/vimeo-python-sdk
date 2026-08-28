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


class AdminConversationsRestrictAccess:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminConversationsRestrictAccessWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AdminConversationsRestrictAccessWithRawResponse:
        return self._with_raw_response


class AsyncAdminConversationsRestrictAccess:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminConversationsRestrictAccessWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAdminConversationsRestrictAccessWithRawResponse:
        return self._with_raw_response


class AdminConversationsRestrictAccessWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminConversationsRestrictAccessWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
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
