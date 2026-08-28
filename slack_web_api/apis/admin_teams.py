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


class AdminTeams:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminTeamsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AdminTeamsWithRawResponse:
        return self._with_raw_response


class AsyncAdminTeams:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminTeamsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAdminTeamsWithRawResponse:
        return self._with_raw_response


class AdminTeamsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminTeamsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
