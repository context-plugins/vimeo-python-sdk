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
from ..models.enums.content_type import ContentTypeOrStr
from ..models.migration_exchangesuccessschema import MigrationExchangesuccessschema
from ..server.server import Server


class Migration:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MigrationWithRawResponse(client, server, auth)

    def migration_exchange(
        self,
        token: str,
        users: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        to_old: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MigrationExchangesuccessschema:
        """For Enterprise Grid workspaces, map local user IDs to global user IDs

        Args:
            token: Authentication token. Requires scope: ``tokens.basic``
            users: A comma-separated list of user ids, up to 400 per request
            content_type: Value sent with the request.
            team_id: Specify team_id starts with ``T`` in case of Org Token
            to_old: Specify ``true`` to convert ``W`` global user IDs to workspace-specific ``U`` IDs. Defaults to
                ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response when mappings exist for the specified user IDs

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.migration_exchange(
            token, users, content_type, team_id=team_id, to_old=to_old, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MigrationWithRawResponse:
        return self._with_raw_response


class AsyncMigration:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMigrationWithRawResponse(client, server, auth)

    async def migration_exchange(
        self,
        token: str,
        users: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        to_old: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MigrationExchangesuccessschema:
        """For Enterprise Grid workspaces, map local user IDs to global user IDs

        Args:
            token: Authentication token. Requires scope: ``tokens.basic``
            users: A comma-separated list of user ids, up to 400 per request
            content_type: Value sent with the request.
            team_id: Specify team_id starts with ``T`` in case of Org Token
            to_old: Specify ``true`` to convert ``W`` global user IDs to workspace-specific ``U`` IDs. Defaults to
                ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response when mappings exist for the specified user IDs

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.migration_exchange(
                token, users, content_type, team_id=team_id, to_old=to_old, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMigrationWithRawResponse:
        return self._with_raw_response


class MigrationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def migration_exchange(
        self,
        token: str,
        users: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        to_old: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MigrationExchangesuccessschema, RawError]:
        """For Enterprise Grid workspaces, map local user IDs to global user IDs

        Args:
            token: Authentication token. Requires scope: ``tokens.basic``
            users: A comma-separated list of user ids, up to 400 per request
            content_type: Value sent with the request.
            team_id: Specify team_id starts with ``T`` in case of Org Token
            to_old: Specify ``true`` to convert ``W`` global user IDs to workspace-specific ``U`` IDs. Defaults to
                ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/migration.exchange"),
            query_params=[
                param[str]("token", token),
                param[str]("users", users),
                param[str | None]("team_id", team_id),
                param[bool | None]("to_old", to_old),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[MigrationExchangesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMigrationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def migration_exchange(
        self,
        token: str,
        users: str,
        content_type: ContentTypeOrStr,
        *,
        team_id: str | None = None,
        to_old: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MigrationExchangesuccessschema, RawError]:
        """For Enterprise Grid workspaces, map local user IDs to global user IDs

        Args:
            token: Authentication token. Requires scope: ``tokens.basic``
            users: A comma-separated list of user ids, up to 400 per request
            content_type: Value sent with the request.
            team_id: Specify team_id starts with ``T`` in case of Org Token
            to_old: Specify ``true`` to convert ``W`` global user IDs to workspace-specific ``U`` IDs. Defaults to
                ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/migration.exchange"),
            query_params=[
                param[str]("token", token),
                param[str]("users", users),
                param[str | None]("team_id", team_id),
                param[bool | None]("to_old", to_old),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[MigrationExchangesuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
