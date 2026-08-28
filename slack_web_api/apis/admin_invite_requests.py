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


class AdminInviteRequests:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminInviteRequestsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AdminInviteRequestsWithRawResponse:
        return self._with_raw_response


class AsyncAdminInviteRequests:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminInviteRequestsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAdminInviteRequestsWithRawResponse:
        return self._with_raw_response


class AdminInviteRequestsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminInviteRequestsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
