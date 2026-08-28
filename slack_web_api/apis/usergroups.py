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
from ..models.usergroups_createschema import UsergroupsCreateschema
from ..models.usergroups_disableschema import UsergroupsDisableschema
from ..models.usergroups_enableschema import UsergroupsEnableschema
from ..models.usergroups_listschema import UsergroupsListschema
from ..models.usergroups_updateschema import UsergroupsUpdateschema
from ..models.usergroups_users_listschema import UsergroupsUsersListschema
from ..models.usergroups_users_updateschema import UsergroupsUsersUpdateschema
from ..server.server import Server


class Usergroups:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsergroupsWithRawResponse(client, server, auth)

    def usergroups_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        *,
        channels: str | None = None,
        description: str | None = None,
        handle: str | None = None,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsCreateschema:
        """Create a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            name: A name for the User Group. Must be unique among User Groups.
            channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
            description: A short description of the User Group.
            handle: A mention handle. Must be unique among channels, users and User Groups.
            include_count: Include the number of users in each User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.usergroups_create(
            token,
            content_type,
            name,
            channels=channels,
            description=description,
            handle=handle,
            include_count=include_count,
            request_options=request_options,
        ).unwrap()

    def usergroups_disable(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsDisableschema:
        """Disable an existing User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to disable.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.usergroups_disable(
            token, content_type, usergroup, include_count=include_count, request_options=request_options
        ).unwrap()

    def usergroups_enable(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsEnableschema:
        """Enable a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to enable.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.usergroups_enable(
            token, content_type, usergroup, include_count=include_count, request_options=request_options
        ).unwrap()

    def usergroups_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_users: bool | None = None,
        include_count: bool | None = None,
        include_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsListschema:
        """List all User Groups for a team

        Args:
            token: Authentication token. Requires scope: ``usergroups:read``
            content_type: Value sent with the request.
            include_users: Include the list of users for each User Group.
            include_count: Include the number of users in each User Group.
            include_disabled: Include disabled User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.usergroups_list(
            token,
            content_type,
            include_users=include_users,
            include_count=include_count,
            include_disabled=include_disabled,
            request_options=request_options,
        ).unwrap()

    def usergroups_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        handle: str | None = None,
        description: str | None = None,
        channels: str | None = None,
        include_count: bool | None = None,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsUpdateschema:
        """Update an existing User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to update.
            handle: A mention handle. Must be unique among channels, users and User Groups.
            description: A short description of the User Group.
            channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
            include_count: Include the number of users in the User Group.
            name: A name for the User Group. Must be unique among User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.usergroups_update(
            token,
            content_type,
            usergroup,
            handle=handle,
            description=description,
            channels=channels,
            include_count=include_count,
            name=name,
            request_options=request_options,
        ).unwrap()

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
    def with_raw_response(self) -> UsergroupsWithRawResponse:
        return self._with_raw_response


class AsyncUsergroups:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsergroupsWithRawResponse(client, server, auth)

    async def usergroups_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        *,
        channels: str | None = None,
        description: str | None = None,
        handle: str | None = None,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsCreateschema:
        """Create a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            name: A name for the User Group. Must be unique among User Groups.
            channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
            description: A short description of the User Group.
            handle: A mention handle. Must be unique among channels, users and User Groups.
            include_count: Include the number of users in each User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.usergroups_create(
                token,
                content_type,
                name,
                channels=channels,
                description=description,
                handle=handle,
                include_count=include_count,
                request_options=request_options,
            )
        ).unwrap()

    async def usergroups_disable(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsDisableschema:
        """Disable an existing User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to disable.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.usergroups_disable(
                token, content_type, usergroup, include_count=include_count, request_options=request_options
            )
        ).unwrap()

    async def usergroups_enable(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsEnableschema:
        """Enable a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to enable.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.usergroups_enable(
                token, content_type, usergroup, include_count=include_count, request_options=request_options
            )
        ).unwrap()

    async def usergroups_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_users: bool | None = None,
        include_count: bool | None = None,
        include_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsListschema:
        """List all User Groups for a team

        Args:
            token: Authentication token. Requires scope: ``usergroups:read``
            content_type: Value sent with the request.
            include_users: Include the list of users for each User Group.
            include_count: Include the number of users in each User Group.
            include_disabled: Include disabled User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.usergroups_list(
                token,
                content_type,
                include_users=include_users,
                include_count=include_count,
                include_disabled=include_disabled,
                request_options=request_options,
            )
        ).unwrap()

    async def usergroups_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        handle: str | None = None,
        description: str | None = None,
        channels: str | None = None,
        include_count: bool | None = None,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsergroupsUpdateschema:
        """Update an existing User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to update.
            handle: A mention handle. Must be unique among channels, users and User Groups.
            description: A short description of the User Group.
            channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
            include_count: Include the number of users in the User Group.
            name: A name for the User Group. Must be unique among User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.usergroups_update(
                token,
                content_type,
                usergroup,
                handle=handle,
                description=description,
                channels=channels,
                include_count=include_count,
                name=name,
                request_options=request_options,
            )
        ).unwrap()

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
    def with_raw_response(self) -> AsyncUsergroupsWithRawResponse:
        return self._with_raw_response


class UsergroupsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def usergroups_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        *,
        channels: str | None = None,
        description: str | None = None,
        handle: str | None = None,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsCreateschema, RawError]:
        """Create a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            name: A name for the User Group. Must be unique among User Groups.
            channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
            description: A short description of the User Group.
            handle: A mention handle. Must be unique among channels, users and User Groups.
            include_count: Include the number of users in each User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.create"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("name", name),
                    param[str | None]("channels", channels),
                    param[str | None]("description", description),
                    param[str | None]("handle", handle),
                    param[bool | None]("include_count", include_count),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsCreateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def usergroups_disable(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsDisableschema, RawError]:
        """Disable an existing User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to disable.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.disable"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("usergroup", usergroup), param[bool | None]("include_count", include_count)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsDisableschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def usergroups_enable(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsEnableschema, RawError]:
        """Enable a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to enable.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.enable"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("usergroup", usergroup), param[bool | None]("include_count", include_count)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsEnableschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def usergroups_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_users: bool | None = None,
        include_count: bool | None = None,
        include_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsListschema, RawError]:
        """List all User Groups for a team

        Args:
            token: Authentication token. Requires scope: ``usergroups:read``
            content_type: Value sent with the request.
            include_users: Include the list of users for each User Group.
            include_count: Include the number of users in each User Group.
            include_disabled: Include disabled User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/usergroups.list"),
            query_params=[
                param[str]("token", token),
                param[bool | None]("include_users", include_users),
                param[bool | None]("include_count", include_count),
                param[bool | None]("include_disabled", include_disabled),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def usergroups_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        handle: str | None = None,
        description: str | None = None,
        channels: str | None = None,
        include_count: bool | None = None,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsUpdateschema, RawError]:
        """Update an existing User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to update.
            handle: A mention handle. Must be unique among channels, users and User Groups.
            description: A short description of the User Group.
            channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
            include_count: Include the number of users in the User Group.
            name: A name for the User Group. Must be unique among User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.update"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("usergroup", usergroup),
                    param[str | None]("handle", handle),
                    param[str | None]("description", description),
                    param[str | None]("channels", channels),
                    param[bool | None]("include_count", include_count),
                    param[str | None]("name", name),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsUpdateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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


class AsyncUsergroupsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def usergroups_create(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        *,
        channels: str | None = None,
        description: str | None = None,
        handle: str | None = None,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsCreateschema, RawError]:
        """Create a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            name: A name for the User Group. Must be unique among User Groups.
            channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
            description: A short description of the User Group.
            handle: A mention handle. Must be unique among channels, users and User Groups.
            include_count: Include the number of users in each User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.create"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("name", name),
                    param[str | None]("channels", channels),
                    param[str | None]("description", description),
                    param[str | None]("handle", handle),
                    param[bool | None]("include_count", include_count),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsCreateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def usergroups_disable(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsDisableschema, RawError]:
        """Disable an existing User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to disable.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.disable"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("usergroup", usergroup), param[bool | None]("include_count", include_count)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsDisableschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def usergroups_enable(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        include_count: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsEnableschema, RawError]:
        """Enable a User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to enable.
            include_count: Include the number of users in the User Group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.enable"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("usergroup", usergroup), param[bool | None]("include_count", include_count)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsEnableschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def usergroups_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_users: bool | None = None,
        include_count: bool | None = None,
        include_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsListschema, RawError]:
        """List all User Groups for a team

        Args:
            token: Authentication token. Requires scope: ``usergroups:read``
            content_type: Value sent with the request.
            include_users: Include the list of users for each User Group.
            include_count: Include the number of users in each User Group.
            include_disabled: Include disabled User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/usergroups.list"),
            query_params=[
                param[str]("token", token),
                param[bool | None]("include_users", include_users),
                param[bool | None]("include_count", include_count),
                param[bool | None]("include_disabled", include_disabled),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def usergroups_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        usergroup: str,
        *,
        handle: str | None = None,
        description: str | None = None,
        channels: str | None = None,
        include_count: bool | None = None,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsergroupsUpdateschema, RawError]:
        """Update an existing User Group

        Args:
            token: Authentication token. Requires scope: ``usergroups:write``
            content_type: Value sent with the request.
            usergroup: The encoded ID of the User Group to update.
            handle: A mention handle. Must be unique among channels, users and User Groups.
            description: A short description of the User Group.
            channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
            include_count: Include the number of users in the User Group.
            name: A name for the User Group. Must be unique among User Groups.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/usergroups.update"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("usergroup", usergroup),
                    param[str | None]("handle", handle),
                    param[str | None]("description", description),
                    param[str | None]("channels", channels),
                    param[bool | None]("include_count", include_count),
                    param[str | None]("name", name),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsergroupsUpdateschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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
