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
from ..models.users_profile_getschema import UsersProfileGetschema
from ..models.users_profile_setschema import UsersProfileSetschema
from ..server.server import Server


class UsersProfile:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersProfileWithRawResponse(client, server, auth)

    def users_profile_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_labels: bool | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersProfileGetschema:
        """Retrieves a user's profile information.

        Args:
            token: Authentication token. Requires scope: ``users.profile:read``
            content_type: Value sent with the request.
            include_labels: Include labels for each ID in custom profile fields
            user: User to retrieve profile info for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_profile_get(
            token, content_type, include_labels=include_labels, user=user, request_options=request_options
        ).unwrap()

    def users_profile_set(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        name: str | None = None,
        profile: str | None = None,
        user: str | None = None,
        value: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersProfileSetschema:
        """Set the profile information for a user.

        Args:
            token: Authentication token. Requires scope: ``users.profile:write``
            content_type: Value sent with the request.
            name: Name of a single key to set. Usable only if ``profile`` is not passed.
            profile: Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set.
                Each field name is limited to 255 characters.
            user: ID of user to change. This argument may only be specified by team admins on paid teams.
            value: Value to set a single key to. Usable only if ``profile`` is not passed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_profile_set(
            token, content_type, name=name, profile=profile, user=user, value=value, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UsersProfileWithRawResponse:
        return self._with_raw_response


class AsyncUsersProfile:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersProfileWithRawResponse(client, server, auth)

    async def users_profile_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_labels: bool | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersProfileGetschema:
        """Retrieves a user's profile information.

        Args:
            token: Authentication token. Requires scope: ``users.profile:read``
            content_type: Value sent with the request.
            include_labels: Include labels for each ID in custom profile fields
            user: User to retrieve profile info for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_profile_get(
                token, content_type, include_labels=include_labels, user=user, request_options=request_options
            )
        ).unwrap()

    async def users_profile_set(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        name: str | None = None,
        profile: str | None = None,
        user: str | None = None,
        value: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersProfileSetschema:
        """Set the profile information for a user.

        Args:
            token: Authentication token. Requires scope: ``users.profile:write``
            content_type: Value sent with the request.
            name: Name of a single key to set. Usable only if ``profile`` is not passed.
            profile: Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set.
                Each field name is limited to 255 characters.
            user: ID of user to change. This argument may only be specified by team admins on paid teams.
            value: Value to set a single key to. Usable only if ``profile`` is not passed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_profile_set(
                token, content_type, name=name, profile=profile, user=user, value=value, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersProfileWithRawResponse:
        return self._with_raw_response


class UsersProfileWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def users_profile_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_labels: bool | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersProfileGetschema, RawError]:
        """Retrieves a user's profile information.

        Args:
            token: Authentication token. Requires scope: ``users.profile:read``
            content_type: Value sent with the request.
            include_labels: Include labels for each ID in custom profile fields
            user: User to retrieve profile info for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.profile.get"),
            query_params=[
                param[str]("token", token),
                param[bool | None]("include_labels", include_labels),
                param[str | None]("user", user),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersProfileGetschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_profile_set(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        name: str | None = None,
        profile: str | None = None,
        user: str | None = None,
        value: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersProfileSetschema, RawError]:
        """Set the profile information for a user.

        Args:
            token: Authentication token. Requires scope: ``users.profile:write``
            content_type: Value sent with the request.
            name: Name of a single key to set. Usable only if ``profile`` is not passed.
            profile: Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set.
                Each field name is limited to 255 characters.
            user: ID of user to change. This argument may only be specified by team admins on paid teams.
            value: Value to set a single key to. Usable only if ``profile`` is not passed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.profile.set"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("name", name),
                    param[str | None]("profile", profile),
                    param[str | None]("user", user),
                    param[str | None]("value", value),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersProfileSetschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUsersProfileWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def users_profile_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_labels: bool | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersProfileGetschema, RawError]:
        """Retrieves a user's profile information.

        Args:
            token: Authentication token. Requires scope: ``users.profile:read``
            content_type: Value sent with the request.
            include_labels: Include labels for each ID in custom profile fields
            user: User to retrieve profile info for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.profile.get"),
            query_params=[
                param[str]("token", token),
                param[bool | None]("include_labels", include_labels),
                param[str | None]("user", user),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersProfileGetschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_profile_set(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        name: str | None = None,
        profile: str | None = None,
        user: str | None = None,
        value: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersProfileSetschema, RawError]:
        """Set the profile information for a user.

        Args:
            token: Authentication token. Requires scope: ``users.profile:write``
            content_type: Value sent with the request.
            name: Name of a single key to set. Usable only if ``profile`` is not passed.
            profile: Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set.
                Each field name is limited to 255 characters.
            user: ID of user to change. This argument may only be specified by team admins on paid teams.
            value: Value to set a single key to. Usable only if ``profile`` is not passed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.profile.set"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("name", name),
                    param[str | None]("profile", profile),
                    param[str | None]("user", user),
                    param[str | None]("value", value),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersProfileSetschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
