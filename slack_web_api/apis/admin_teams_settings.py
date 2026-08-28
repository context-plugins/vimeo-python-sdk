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


class AdminTeamsSettings:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminTeamsSettingsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AdminTeamsSettingsWithRawResponse:
        return self._with_raw_response


class AsyncAdminTeamsSettings:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminTeamsSettingsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAdminTeamsSettingsWithRawResponse:
        return self._with_raw_response


class AdminTeamsSettingsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminTeamsSettingsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
