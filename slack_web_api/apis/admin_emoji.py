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


class AdminEmoji:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminEmojiWithRawResponse(client, server, auth)

    def admin_emoji_add(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        url: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent
                backgrounds work best.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_add(
            content_type, token, name, url, request_options=request_options
        ).unwrap()

    def admin_emoji_add_alias(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        alias_for: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an emoji alias.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be aliased. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            alias_for: The alias of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_add_alias(
            content_type, token, name, alias_for, request_options=request_options
        ).unwrap()

    def admin_emoji_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List emoji for an Enterprise Grid organization.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_list(
            token, content_type, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def admin_emoji_remove(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove an emoji across an Enterprise Grid organization

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_remove(
            content_type, token, name, request_options=request_options
        ).unwrap()

    def admin_emoji_rename(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        new_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Rename an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be renamed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            new_name: The new name of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_emoji_rename(
            content_type, token, name, new_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AdminEmojiWithRawResponse:
        return self._with_raw_response


class AsyncAdminEmoji:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminEmojiWithRawResponse(client, server, auth)

    async def admin_emoji_add(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        url: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent
                backgrounds work best.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_add(
                content_type, token, name, url, request_options=request_options
            )
        ).unwrap()

    async def admin_emoji_add_alias(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        alias_for: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Add an emoji alias.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be aliased. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            alias_for: The alias of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_add_alias(
                content_type, token, name, alias_for, request_options=request_options
            )
        ).unwrap()

    async def admin_emoji_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List emoji for an Enterprise Grid organization.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_list(
                token, content_type, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def admin_emoji_remove(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove an emoji across an Enterprise Grid organization

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_remove(content_type, token, name, request_options=request_options)
        ).unwrap()

    async def admin_emoji_rename(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        new_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Rename an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be renamed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            new_name: The new name of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_emoji_rename(
                content_type, token, name, new_name, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAdminEmojiWithRawResponse:
        return self._with_raw_response


class AdminEmojiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def admin_emoji_add(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        url: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent
                backgrounds work best.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.add"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("url", url)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_emoji_add_alias(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        alias_for: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an emoji alias.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be aliased. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            alias_for: The alias of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.addAlias"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("alias_for", alias_for)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_emoji_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List emoji for an Enterprise Grid organization.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.emoji.list"),
            query_params=[
                param[str]("token", token), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_emoji_remove(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove an emoji across an Enterprise Grid organization

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.remove"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_emoji_rename(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        new_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Rename an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be renamed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            new_name: The new name of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.rename"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("new_name", new_name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAdminEmojiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def admin_emoji_add(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        url: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent
                backgrounds work best.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.add"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("url", url)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_emoji_add_alias(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        alias_for: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Add an emoji alias.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be aliased. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            alias_for: The alias of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.addAlias"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("alias_for", alias_for)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_emoji_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List emoji for an Enterprise Grid organization.

        Args:
            token: Authentication token. Requires scope: ``admin.teams:read``
            content_type: Value sent with the request.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.emoji.list"),
            query_params=[
                param[str]("token", token), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_emoji_remove(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove an emoji across an Enterprise Grid organization

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be removed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.remove"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_emoji_rename(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        name: str,
        new_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Rename an emoji.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``admin.teams:write``
            name: The name of the emoji to be renamed. Colons (``:myemoji:``) around the value are not required,
                although they may be included.
            new_name: The new name of the emoji.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.emoji.rename"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("name", name), param[str]("new_name", new_name)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
