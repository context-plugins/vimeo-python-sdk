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
from ..models.enums.content_type import ContentTypeOrStr
from ..models.reactions_addschema import ReactionsAddschema
from ..models.reactions_listschema import ReactionsListschema
from ..models.reactions_removeschema import ReactionsRemoveschema
from ..server.server import Server


class Reactions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReactionsWithRawResponse(client, server, auth)

    def reactions_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        name: str,
        timestamp: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReactionsAddschema:
        """Adds a reaction to an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:write``
            content_type: Value sent with the request.
            channel: Channel where the message to add reaction to was posted.
            name: Reaction (emoji) name.
            timestamp: Timestamp of the message to add reaction to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reactions_add(
            token, content_type, channel, name, timestamp, request_options=request_options
        ).unwrap()

    def reactions_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        full: bool | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Gets reactions for an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:read``
            content_type: Value sent with the request.
            channel: Channel where the message to get reactions for was posted.
            file: File to get reactions for.
            file_comment: File comment to get reactions for.
            full: If true always return the complete reaction list.
            timestamp: Timestamp of the message to get reactions for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reactions_get(
            token,
            content_type,
            channel=channel,
            file=file,
            file_comment=file_comment,
            full=full,
            timestamp=timestamp,
            request_options=request_options,
        ).unwrap()

    def reactions_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        full: bool | None = None,
        count: int | None = None,
        page: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReactionsListschema:
        """Lists reactions made by a user.

        Args:
            token: Authentication token. Requires scope: ``reactions:read``
            content_type: Value sent with the request.
            user: Show reactions made by this user. Defaults to the authed user.
            full: If true always return the complete reaction list.
            count: Value sent with the request.
            page: Value sent with the request.
            cursor: Parameter for pagination. Set ``cursor`` equal to the ``next_cursor`` attribute returned by the
                previous request's ``response_metadata``. This parameter is optional, but pagination is mandatory: the
                default value simply fetches the first "page" of the collection.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reactions_list(
            token,
            content_type,
            user=user,
            full=full,
            count=count,
            page=page,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def reactions_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        *,
        file: str | None = None,
        file_comment: str | None = None,
        channel: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReactionsRemoveschema:
        """Removes a reaction from an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:write``
            content_type: Value sent with the request.
            name: Reaction (emoji) name.
            file: File to remove reaction from.
            file_comment: File comment to remove reaction from.
            channel: Channel where the message to remove reaction from was posted.
            timestamp: Timestamp of the message to remove reaction from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reactions_remove(
            token,
            content_type,
            name,
            file=file,
            file_comment=file_comment,
            channel=channel,
            timestamp=timestamp,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ReactionsWithRawResponse:
        return self._with_raw_response


class AsyncReactions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReactionsWithRawResponse(client, server, auth)

    async def reactions_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        name: str,
        timestamp: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReactionsAddschema:
        """Adds a reaction to an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:write``
            content_type: Value sent with the request.
            channel: Channel where the message to add reaction to was posted.
            name: Reaction (emoji) name.
            timestamp: Timestamp of the message to add reaction to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reactions_add(
                token, content_type, channel, name, timestamp, request_options=request_options
            )
        ).unwrap()

    async def reactions_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        full: bool | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Gets reactions for an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:read``
            content_type: Value sent with the request.
            channel: Channel where the message to get reactions for was posted.
            file: File to get reactions for.
            file_comment: File comment to get reactions for.
            full: If true always return the complete reaction list.
            timestamp: Timestamp of the message to get reactions for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reactions_get(
                token,
                content_type,
                channel=channel,
                file=file,
                file_comment=file_comment,
                full=full,
                timestamp=timestamp,
                request_options=request_options,
            )
        ).unwrap()

    async def reactions_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        full: bool | None = None,
        count: int | None = None,
        page: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReactionsListschema:
        """Lists reactions made by a user.

        Args:
            token: Authentication token. Requires scope: ``reactions:read``
            content_type: Value sent with the request.
            user: Show reactions made by this user. Defaults to the authed user.
            full: If true always return the complete reaction list.
            count: Value sent with the request.
            page: Value sent with the request.
            cursor: Parameter for pagination. Set ``cursor`` equal to the ``next_cursor`` attribute returned by the
                previous request's ``response_metadata``. This parameter is optional, but pagination is mandatory: the
                default value simply fetches the first "page" of the collection.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reactions_list(
                token,
                content_type,
                user=user,
                full=full,
                count=count,
                page=page,
                cursor=cursor,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def reactions_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        *,
        file: str | None = None,
        file_comment: str | None = None,
        channel: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReactionsRemoveschema:
        """Removes a reaction from an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:write``
            content_type: Value sent with the request.
            name: Reaction (emoji) name.
            file: File to remove reaction from.
            file_comment: File comment to remove reaction from.
            channel: Channel where the message to remove reaction from was posted.
            timestamp: Timestamp of the message to remove reaction from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reactions_remove(
                token,
                content_type,
                name,
                file=file,
                file_comment=file_comment,
                channel=channel,
                timestamp=timestamp,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncReactionsWithRawResponse:
        return self._with_raw_response


class ReactionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def reactions_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        name: str,
        timestamp: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReactionsAddschema, RawError]:
        """Adds a reaction to an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:write``
            content_type: Value sent with the request.
            channel: Channel where the message to add reaction to was posted.
            name: Reaction (emoji) name.
            timestamp: Timestamp of the message to add reaction to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reactions.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [param[str]("channel", channel), param[str]("name", name), param[str]("timestamp", timestamp)]
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ReactionsAddschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reactions_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        full: bool | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Gets reactions for an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:read``
            content_type: Value sent with the request.
            channel: Channel where the message to get reactions for was posted.
            file: File to get reactions for.
            file_comment: File comment to get reactions for.
            full: If true always return the complete reaction list.
            timestamp: Timestamp of the message to get reactions for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/reactions.get"),
            query_params=[
                param[str]("token", token),
                param[str | None]("channel", channel),
                param[str | None]("file", file),
                param[str | None]("file_comment", file_comment),
                param[bool | None]("full", full),
                param[str | None]("timestamp", timestamp),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reactions_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        full: bool | None = None,
        count: int | None = None,
        page: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReactionsListschema, RawError]:
        """Lists reactions made by a user.

        Args:
            token: Authentication token. Requires scope: ``reactions:read``
            content_type: Value sent with the request.
            user: Show reactions made by this user. Defaults to the authed user.
            full: If true always return the complete reaction list.
            count: Value sent with the request.
            page: Value sent with the request.
            cursor: Parameter for pagination. Set ``cursor`` equal to the ``next_cursor`` attribute returned by the
                previous request's ``response_metadata``. This parameter is optional, but pagination is mandatory: the
                default value simply fetches the first "page" of the collection.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/reactions.list"),
            query_params=[
                param[str]("token", token),
                param[str | None]("user", user),
                param[bool | None]("full", full),
                param[int | None]("count", count),
                param[int | None]("page", page),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ReactionsListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reactions_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        *,
        file: str | None = None,
        file_comment: str | None = None,
        channel: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReactionsRemoveschema, RawError]:
        """Removes a reaction from an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:write``
            content_type: Value sent with the request.
            name: Reaction (emoji) name.
            file: File to remove reaction from.
            file_comment: File comment to remove reaction from.
            channel: Channel where the message to remove reaction from was posted.
            timestamp: Timestamp of the message to remove reaction from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reactions.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("name", name),
                    param[str | None]("file", file),
                    param[str | None]("file_comment", file_comment),
                    param[str | None]("channel", channel),
                    param[str | None]("timestamp", timestamp),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ReactionsRemoveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncReactionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def reactions_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        name: str,
        timestamp: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReactionsAddschema, RawError]:
        """Adds a reaction to an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:write``
            content_type: Value sent with the request.
            channel: Channel where the message to add reaction to was posted.
            name: Reaction (emoji) name.
            timestamp: Timestamp of the message to add reaction to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reactions.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [param[str]("channel", channel), param[str]("name", name), param[str]("timestamp", timestamp)]
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ReactionsAddschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reactions_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        full: bool | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Gets reactions for an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:read``
            content_type: Value sent with the request.
            channel: Channel where the message to get reactions for was posted.
            file: File to get reactions for.
            file_comment: File comment to get reactions for.
            full: If true always return the complete reaction list.
            timestamp: Timestamp of the message to get reactions for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/reactions.get"),
            query_params=[
                param[str]("token", token),
                param[str | None]("channel", channel),
                param[str | None]("file", file),
                param[str | None]("file_comment", file_comment),
                param[bool | None]("full", full),
                param[str | None]("timestamp", timestamp),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reactions_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        full: bool | None = None,
        count: int | None = None,
        page: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReactionsListschema, RawError]:
        """Lists reactions made by a user.

        Args:
            token: Authentication token. Requires scope: ``reactions:read``
            content_type: Value sent with the request.
            user: Show reactions made by this user. Defaults to the authed user.
            full: If true always return the complete reaction list.
            count: Value sent with the request.
            page: Value sent with the request.
            cursor: Parameter for pagination. Set ``cursor`` equal to the ``next_cursor`` attribute returned by the
                previous request's ``response_metadata``. This parameter is optional, but pagination is mandatory: the
                default value simply fetches the first "page" of the collection.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/reactions.list"),
            query_params=[
                param[str]("token", token),
                param[str | None]("user", user),
                param[bool | None]("full", full),
                param[int | None]("count", count),
                param[int | None]("page", page),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ReactionsListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reactions_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        name: str,
        *,
        file: str | None = None,
        file_comment: str | None = None,
        channel: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReactionsRemoveschema, RawError]:
        """Removes a reaction from an item.

        Args:
            token: Authentication token. Requires scope: ``reactions:write``
            content_type: Value sent with the request.
            name: Reaction (emoji) name.
            file: File to remove reaction from.
            file_comment: File comment to remove reaction from.
            channel: Channel where the message to remove reaction from was posted.
            timestamp: Timestamp of the message to remove reaction from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reactions.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("name", name),
                    param[str | None]("file", file),
                    param[str | None]("file_comment", file_comment),
                    param[str | None]("channel", channel),
                    param[str | None]("timestamp", timestamp),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ReactionsRemoveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
