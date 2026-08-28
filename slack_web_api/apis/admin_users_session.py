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


class AdminUsersSession:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminUsersSessionWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AdminUsersSessionWithRawResponse:
        return self._with_raw_response


class AsyncAdminUsersSession:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminUsersSessionWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAdminUsersSessionWithRawResponse:
        return self._with_raw_response


class AdminUsersSessionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminUsersSessionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
