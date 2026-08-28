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
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class AdminTeamsOwners:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminTeamsOwnersWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AdminTeamsOwnersWithRawResponse:
        return self._with_raw_response


class AsyncAdminTeamsOwners:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminTeamsOwnersWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAdminTeamsOwnersWithRawResponse:
        return self._with_raw_response


class AdminTeamsOwnersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminTeamsOwnersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
