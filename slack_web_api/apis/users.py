from __future__ import annotations

from typing import Any

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
from ..models.apimethodusers_get_presence import ApimethodusersGetPresence
from ..models.enums.content_type import ContentTypeOrStr
from ..models.users_conversationssuccessschema import UsersConversationssuccessschema
from ..models.users_delete_photoschema import UsersDeletePhotoschema
from ..models.users_infosuccessschema import UsersInfosuccessschema
from ..models.users_listschema import UsersListschema
from ..models.users_lookup_by_emailsuccessschema import UsersLookupByEmailsuccessschema
from ..models.users_profile_getschema import UsersProfileGetschema
from ..models.users_profile_setschema import UsersProfileSetschema
from ..models.users_set_activeschema import UsersSetActiveschema
from ..models.users_set_photoschema import UsersSetPhotoschema
from ..models.users_set_presenceschema import UsersSetPresenceschema
from ..server.server import Server


class Users:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersWithRawResponse(client, server, auth)

    def users_conversations(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        types: str | None = None,
        exclude_archived: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersConversationssuccessschema:
        """List conversations the calling user may access.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            user: Browse conversations by a specific user ID's membership. Non-public channels are restricted to those
                where the calling user shares membership.
            types: Mix and match channel types by providing a comma-separated list of any combination of
                ``public_channel``, ``private_channel``, ``mpim``, ``im``
            exclude_archived: Set to ``true`` to exclude archived channels from the list
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached. Must be an integer no larger than 1000.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response with only public channels. Note how ``num_members`` and ``is_member`` are not
            returned like typical ``conversations`` objects.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_conversations(
            content_type,
            token=token,
            user=user,
            types=types,
            exclude_archived=exclude_archived,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def users_delete_photo(
        self, content_type: ContentTypeOrStr, token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UsersDeletePhotoschema:
        """Delete the user profile photo

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users.profile:write``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_delete_photo(content_type, token, request_options=request_options).unwrap()

    def users_get_presence(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApimethodusersGetPresence:
        """Gets user presence information.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            user: User to get presence info on. Defaults to the authed user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            When requesting information for a different user, this method just returns the current presence (either
            ``active`` or ``away``).

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_get_presence(
            token, content_type, user=user, request_options=request_options
        ).unwrap()

    def users_identity(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Get a user's identity.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``identity.basic``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            You will receive at a minimum the following information:

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_identity(
            content_type, token=token, request_options=request_options
        ).unwrap()

    def users_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_locale: bool | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersInfosuccessschema:
        """Gets information about a user.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            include_locale: Set this to ``true`` to receive the locale for this user. Defaults to ``false``
            user: User to get info on
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_info(
            token, content_type, include_locale=include_locale, user=user, request_options=request_options
        ).unwrap()

    def users_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        include_locale: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersListschema:
        """Lists all users in a Slack team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users:read``
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached. Providing no ``limit`` value will result in Slack
                attempting to deliver you the entire result set. If the collection is too large you may experience
                ``limit_required`` or HTTP 500 errors.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            include_locale: Set this to ``true`` to receive the locale for users. Defaults to ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_list(
            content_type,
            token=token,
            limit=limit,
            cursor=cursor,
            include_locale=include_locale,
            request_options=request_options,
        ).unwrap()

    def users_lookup_by_email(
        self,
        token: str,
        email: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersLookupByEmailsuccessschema:
        """Find a user with an email address.

        Args:
            token: Authentication token. Requires scope: ``users:read.email``
            email: An email address belonging to a user in the workspace
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_lookup_by_email(
            token, email, content_type, request_options=request_options
        ).unwrap()

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

    def users_set_active(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> UsersSetActiveschema:
        """Marked a user as active. Deprecated and non-functional.

        Args:
            token: Authentication token. Requires scope: ``users:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_set_active(token, content_type, request_options=request_options).unwrap()

    def users_set_photo(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        *,
        crop_w: str | None = None,
        crop_x: str | None = None,
        crop_y: str | None = None,
        image: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersSetPhotoschema:
        """Set the user profile photo

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users.profile:write``
            crop_w: Width/height of crop box (always square)
            crop_x: X coordinate of top-left corner of crop box
            crop_y: Y coordinate of top-left corner of crop box
            image: File contents via ``multipart/form-data``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_set_photo(
            content_type,
            token,
            crop_w=crop_w,
            crop_x=crop_x,
            crop_y=crop_y,
            image=image,
            request_options=request_options,
        ).unwrap()

    def users_set_presence(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        presence: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersSetPresenceschema:
        """Manually sets user presence.

        Args:
            token: Authentication token. Requires scope: ``users:write``
            content_type: Value sent with the request.
            presence: Either ``auto`` or ``away``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.users_set_presence(
            token, content_type, presence, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UsersWithRawResponse:
        return self._with_raw_response


class AsyncUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersWithRawResponse(client, server, auth)

    async def users_conversations(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        types: str | None = None,
        exclude_archived: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersConversationssuccessschema:
        """List conversations the calling user may access.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            user: Browse conversations by a specific user ID's membership. Non-public channels are restricted to those
                where the calling user shares membership.
            types: Mix and match channel types by providing a comma-separated list of any combination of
                ``public_channel``, ``private_channel``, ``mpim``, ``im``
            exclude_archived: Set to ``true`` to exclude archived channels from the list
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached. Must be an integer no larger than 1000.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response with only public channels. Note how ``num_members`` and ``is_member`` are not
            returned like typical ``conversations`` objects.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_conversations(
                content_type,
                token=token,
                user=user,
                types=types,
                exclude_archived=exclude_archived,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def users_delete_photo(
        self, content_type: ContentTypeOrStr, token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UsersDeletePhotoschema:
        """Delete the user profile photo

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users.profile:write``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_delete_photo(content_type, token, request_options=request_options)
        ).unwrap()

    async def users_get_presence(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApimethodusersGetPresence:
        """Gets user presence information.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            user: User to get presence info on. Defaults to the authed user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            When requesting information for a different user, this method just returns the current presence (either
            ``active`` or ``away``).

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_get_presence(
                token, content_type, user=user, request_options=request_options
            )
        ).unwrap()

    async def users_identity(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Get a user's identity.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``identity.basic``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            You will receive at a minimum the following information:

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_identity(content_type, token=token, request_options=request_options)
        ).unwrap()

    async def users_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_locale: bool | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersInfosuccessschema:
        """Gets information about a user.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            include_locale: Set this to ``true`` to receive the locale for this user. Defaults to ``false``
            user: User to get info on
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_info(
                token, content_type, include_locale=include_locale, user=user, request_options=request_options
            )
        ).unwrap()

    async def users_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        include_locale: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersListschema:
        """Lists all users in a Slack team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users:read``
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached. Providing no ``limit`` value will result in Slack
                attempting to deliver you the entire result set. If the collection is too large you may experience
                ``limit_required`` or HTTP 500 errors.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            include_locale: Set this to ``true`` to receive the locale for users. Defaults to ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_list(
                content_type,
                token=token,
                limit=limit,
                cursor=cursor,
                include_locale=include_locale,
                request_options=request_options,
            )
        ).unwrap()

    async def users_lookup_by_email(
        self,
        token: str,
        email: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersLookupByEmailsuccessschema:
        """Find a user with an email address.

        Args:
            token: Authentication token. Requires scope: ``users:read.email``
            email: An email address belonging to a user in the workspace
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_lookup_by_email(
                token, email, content_type, request_options=request_options
            )
        ).unwrap()

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

    async def users_set_active(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> UsersSetActiveschema:
        """Marked a user as active. Deprecated and non-functional.

        Args:
            token: Authentication token. Requires scope: ``users:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_set_active(token, content_type, request_options=request_options)
        ).unwrap()

    async def users_set_photo(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        *,
        crop_w: str | None = None,
        crop_x: str | None = None,
        crop_y: str | None = None,
        image: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersSetPhotoschema:
        """Set the user profile photo

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users.profile:write``
            crop_w: Width/height of crop box (always square)
            crop_x: X coordinate of top-left corner of crop box
            crop_y: Y coordinate of top-left corner of crop box
            image: File contents via ``multipart/form-data``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_set_photo(
                content_type,
                token,
                crop_w=crop_w,
                crop_x=crop_x,
                crop_y=crop_y,
                image=image,
                request_options=request_options,
            )
        ).unwrap()

    async def users_set_presence(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        presence: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersSetPresenceschema:
        """Manually sets user presence.

        Args:
            token: Authentication token. Requires scope: ``users:write``
            content_type: Value sent with the request.
            presence: Either ``auto`` or ``away``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.users_set_presence(
                token, content_type, presence, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersWithRawResponse:
        return self._with_raw_response


class UsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def users_conversations(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        types: str | None = None,
        exclude_archived: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersConversationssuccessschema, RawError]:
        """List conversations the calling user may access.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            user: Browse conversations by a specific user ID's membership. Non-public channels are restricted to those
                where the calling user shares membership.
            types: Mix and match channel types by providing a comma-separated list of any combination of
                ``public_channel``, ``private_channel``, ``mpim``, ``im``
            exclude_archived: Set to ``true`` to exclude archived channels from the list
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached. Must be an integer no larger than 1000.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.conversations"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("user", user),
                param[str | None]("types", types),
                param[bool | None]("exclude_archived", exclude_archived),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersConversationssuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_delete_photo(
        self, content_type: ContentTypeOrStr, token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UsersDeletePhotoschema, RawError]:
        """Delete the user profile photo

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users.profile:write``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.deletePhoto"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersDeletePhotoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_get_presence(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApimethodusersGetPresence, RawError]:
        """Gets user presence information.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            user: User to get presence info on. Defaults to the authed user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.getPresence"),
            query_params=[param[str]("token", token), param[str | None]("user", user)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ApimethodusersGetPresence],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_identity(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Get a user's identity.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``identity.basic``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.identity"),
            query_params=[param[str | None]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_locale: bool | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersInfosuccessschema, RawError]:
        """Gets information about a user.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            include_locale: Set this to ``true`` to receive the locale for this user. Defaults to ``false``
            user: User to get info on
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.info"),
            query_params=[
                param[str]("token", token),
                param[bool | None]("include_locale", include_locale),
                param[str | None]("user", user),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersInfosuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        include_locale: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersListschema, RawError]:
        """Lists all users in a Slack team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users:read``
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached. Providing no ``limit`` value will result in Slack
                attempting to deliver you the entire result set. If the collection is too large you may experience
                ``limit_required`` or HTTP 500 errors.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            include_locale: Set this to ``true`` to receive the locale for users. Defaults to ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.list"),
            query_params=[
                param[str | None]("token", token),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("include_locale", include_locale),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_lookup_by_email(
        self,
        token: str,
        email: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersLookupByEmailsuccessschema, RawError]:
        """Find a user with an email address.

        Args:
            token: Authentication token. Requires scope: ``users:read.email``
            email: An email address belonging to a user in the workspace
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.lookupByEmail"),
            query_params=[param[str]("token", token), param[str]("email", email)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersLookupByEmailsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def users_set_active(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UsersSetActiveschema, RawError]:
        """Marked a user as active. Deprecated and non-functional.

        Args:
            token: Authentication token. Requires scope: ``users:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.setActive"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersSetActiveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_set_photo(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        *,
        crop_w: str | None = None,
        crop_x: str | None = None,
        crop_y: str | None = None,
        image: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersSetPhotoschema, RawError]:
        """Set the user profile photo

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users.profile:write``
            crop_w: Width/height of crop box (always square)
            crop_x: X coordinate of top-left corner of crop box
            crop_y: Y coordinate of top-left corner of crop box
            image: File contents via ``multipart/form-data``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.setPhoto"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("token", token),
                    param[str | None]("crop_w", crop_w),
                    param[str | None]("crop_x", crop_x),
                    param[str | None]("crop_y", crop_y),
                    param[str | None]("image", image),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersSetPhotoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def users_set_presence(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        presence: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersSetPresenceschema, RawError]:
        """Manually sets user presence.

        Args:
            token: Authentication token. Requires scope: ``users:write``
            content_type: Value sent with the request.
            presence: Either ``auto`` or ``away``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.setPresence"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("presence", presence)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersSetPresenceschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def users_conversations(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        types: str | None = None,
        exclude_archived: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersConversationssuccessschema, RawError]:
        """List conversations the calling user may access.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``conversations:read``
            user: Browse conversations by a specific user ID's membership. Non-public channels are restricted to those
                where the calling user shares membership.
            types: Mix and match channel types by providing a comma-separated list of any combination of
                ``public_channel``, ``private_channel``, ``mpim``, ``im``
            exclude_archived: Set to ``true`` to exclude archived channels from the list
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached. Must be an integer no larger than 1000.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.conversations"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("user", user),
                param[str | None]("types", types),
                param[bool | None]("exclude_archived", exclude_archived),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersConversationssuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_delete_photo(
        self, content_type: ContentTypeOrStr, token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UsersDeletePhotoschema, RawError]:
        """Delete the user profile photo

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users.profile:write``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.deletePhoto"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersDeletePhotoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_get_presence(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApimethodusersGetPresence, RawError]:
        """Gets user presence information.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            user: User to get presence info on. Defaults to the authed user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.getPresence"),
            query_params=[param[str]("token", token), param[str | None]("user", user)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ApimethodusersGetPresence],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_identity(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Get a user's identity.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``identity.basic``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.identity"),
            query_params=[param[str | None]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        include_locale: bool | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersInfosuccessschema, RawError]:
        """Gets information about a user.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            include_locale: Set this to ``true`` to receive the locale for this user. Defaults to ``false``
            user: User to get info on
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.info"),
            query_params=[
                param[str]("token", token),
                param[bool | None]("include_locale", include_locale),
                param[str | None]("user", user),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersInfosuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        include_locale: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersListschema, RawError]:
        """Lists all users in a Slack team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users:read``
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the users list hasn't been reached. Providing no ``limit`` value will result in Slack
                attempting to deliver you the entire result set. If the collection is too large you may experience
                ``limit_required`` or HTTP 500 errors.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            include_locale: Set this to ``true`` to receive the locale for users. Defaults to ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.list"),
            query_params=[
                param[str | None]("token", token),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("include_locale", include_locale),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_lookup_by_email(
        self,
        token: str,
        email: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersLookupByEmailsuccessschema, RawError]:
        """Find a user with an email address.

        Args:
            token: Authentication token. Requires scope: ``users:read.email``
            email: An email address belonging to a user in the workspace
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users.lookupByEmail"),
            query_params=[param[str]("token", token), param[str]("email", email)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersLookupByEmailsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    async def users_set_active(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UsersSetActiveschema, RawError]:
        """Marked a user as active. Deprecated and non-functional.

        Args:
            token: Authentication token. Requires scope: ``users:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.setActive"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersSetActiveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_set_photo(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        *,
        crop_w: str | None = None,
        crop_x: str | None = None,
        crop_y: str | None = None,
        image: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersSetPhotoschema, RawError]:
        """Set the user profile photo

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``users.profile:write``
            crop_w: Width/height of crop box (always square)
            crop_x: X coordinate of top-left corner of crop box
            crop_y: Y coordinate of top-left corner of crop box
            image: File contents via ``multipart/form-data``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.setPhoto"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("token", token),
                    param[str | None]("crop_w", crop_w),
                    param[str | None]("crop_x", crop_x),
                    param[str | None]("crop_y", crop_y),
                    param[str | None]("image", image),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersSetPhotoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def users_set_presence(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        presence: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersSetPresenceschema, RawError]:
        """Manually sets user presence.

        Args:
            token: Authentication token. Requires scope: ``users:write``
            content_type: Value sent with the request.
            presence: Either ``auto`` or ``away``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users.setPresence"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("presence", presence)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[UsersSetPresenceschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
