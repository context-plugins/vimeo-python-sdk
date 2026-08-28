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


class AdminUsers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminUsersWithRawResponse(client, server, auth)

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
    def with_raw_response(self) -> AdminUsersWithRawResponse:
        return self._with_raw_response


class AsyncAdminUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminUsersWithRawResponse(client, server, auth)

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
    def with_raw_response(self) -> AsyncAdminUsersWithRawResponse:
        return self._with_raw_response


class AdminUsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAdminUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
