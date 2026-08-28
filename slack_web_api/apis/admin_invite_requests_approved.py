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


class AdminInviteRequestsApproved:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminInviteRequestsApprovedWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AdminInviteRequestsApprovedWithRawResponse:
        return self._with_raw_response


class AsyncAdminInviteRequestsApproved:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminInviteRequestsApprovedWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAdminInviteRequestsApprovedWithRawResponse:
        return self._with_raw_response


class AdminInviteRequestsApprovedWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminInviteRequestsApprovedWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
