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
from ..models.enums.content_type import ContentTypeOrStr
from ..models.usergroups_users_listschema import UsergroupsUsersListschema
from ..models.usergroups_users_updateschema import UsergroupsUsersUpdateschema
from ..server.server import Server


class UsergroupsUsers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsergroupsUsersWithRawResponse(client, server, auth)

    def usergroups_users_list(
        self,
        token: str,
        usergroup: str,
        content_type: ContentTypeOrStr,
        *,
        include_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsUsersListschema:
        """List all users in a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:read``
            usergroup: The encoded ID of the User Group to update.
            content_type: Value sent with the request.
            include_disabled: Allow results that involve disabled User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.usergroups_users_list(
            token, usergroup, content_type, include_disabled=include_disabled, request_options=request_options
        ).unwrap()

    def usergroups_users_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        users: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsUsersUpdateschema:
        """Update the list of users for a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to update.
            users: A comma separated string of encoded user IDs that represent the entire list of users for the User
                Group.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.usergroups_users_update(
            token, content_type, usergroup, users, include_count=include_count, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UsergroupsUsersWithRawResponse:
        return self._with_raw_response


class AsyncUsergroupsUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsergroupsUsersWithRawResponse(client, server, auth)

    async def usergroups_users_list(
        self,
        token: str,
        usergroup: str,
        content_type: ContentTypeOrStr,
        *,
        include_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsUsersListschema:
        """List all users in a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:read``
            usergroup: The encoded ID of the User Group to update.
            content_type: Value sent with the request.
            include_disabled: Allow results that involve disabled User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.usergroups_users_list(
                token, usergroup, content_type, include_disabled=include_disabled, request_options=request_options
            )
        ).unwrap()

    async def usergroups_users_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        users: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsUsersUpdateschema:
        """Update the list of users for a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to update.
            users: A comma separated string of encoded user IDs that represent the entire list of users for the User
                Group.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.usergroups_users_update(
                token, content_type, usergroup, users, include_count=include_count, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsergroupsUsersWithRawResponse:
        return self._with_raw_response


class UsergroupsUsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def usergroups_users_list(
        self,
        token: str,
        usergroup: str,
        content_type: ContentTypeOrStr,
        *,
        include_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsUsersListschema, RawError]:
        """List all users in a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:read``
            usergroup: The encoded ID of the User Group to update.
            content_type: Value sent with the request.
            include_disabled: Allow results that involve disabled User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/usergroups.users.list"),
            query_params=[
                param[str]("token", token),
                param[str]("usergroup", usergroup),
                param[bool | None]("include_disabled", include_disabled),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsUsersListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def usergroups_users_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        users: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsUsersUpdateschema, RawError]:
        """Update the list of users for a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to update.
            users: A comma separated string of encoded user IDs that represent the entire list of users for the User
                Group.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.users.update"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("usergroup", usergroup),
                    param[str]("users", users),
                    param[bool | None]("include_count", include_count),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsUsersUpdateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUsergroupsUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def usergroups_users_list(
        self,
        token: str,
        usergroup: str,
        content_type: ContentTypeOrStr,
        *,
        include_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsUsersListschema, RawError]:
        """List all users in a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:read``
            usergroup: The encoded ID of the User Group to update.
            content_type: Value sent with the request.
            include_disabled: Allow results that involve disabled User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/usergroups.users.list"),
            query_params=[
                param[str]("token", token),
                param[str]("usergroup", usergroup),
                param[bool | None]("include_disabled", include_disabled),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsUsersListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def usergroups_users_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        users: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsUsersUpdateschema, RawError]:
        """Update the list of users for a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to update.
            users: A comma separated string of encoded user IDs that represent the entire list of users for the User
                Group.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.users.update"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("usergroup", usergroup),
                    param[str]("users", users),
                    param[bool | None]("include_count", include_count),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsUsersUpdateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
