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
from ..models.stars_addschema import StarsAddschema
from ..models.stars_listschema import StarsListschema
from ..models.stars_removeschema import StarsRemoveschema
from ..server.server import Server


class Stars:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StarsWithRawResponse(client, server, auth)

    def stars_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StarsAddschema:
        """Adds a star to an item.

        Args:
            token: Authentication token. Requires scope: ``stars:write``
            content_type: Value sent with the request.
            channel: Channel to add star to, or channel where the message to add star to was posted (used with
                ``timestamp``).
            file: File to add star to.
            file_comment: File comment to add star to.
            timestamp: Timestamp of the message to add star to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stars_add(
            token,
            content_type,
            channel=channel,
            file=file,
            file_comment=file_comment,
            timestamp=timestamp,
            request_options=request_options,
        ).unwrap()

    def stars_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        count: str | None = None,
        page: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StarsListschema:
        """Lists stars for a user.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``stars:read``
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
        return self._with_raw_response.stars_list(
            content_type,
            token=token,
            count=count,
            page=page,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def stars_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StarsRemoveschema:
        """Removes a star from an item.

        Args:
            token: Authentication token. Requires scope: ``stars:write``
            content_type: Value sent with the request.
            channel: Channel to remove star from, or channel where the message to remove star from was posted (used with
                ``timestamp``).
            file: File to remove star from.
            file_comment: File comment to remove star from.
            timestamp: Timestamp of the message to remove star from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stars_remove(
            token,
            content_type,
            channel=channel,
            file=file,
            file_comment=file_comment,
            timestamp=timestamp,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> StarsWithRawResponse:
        return self._with_raw_response


class AsyncStars:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStarsWithRawResponse(client, server, auth)

    async def stars_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StarsAddschema:
        """Adds a star to an item.

        Args:
            token: Authentication token. Requires scope: ``stars:write``
            content_type: Value sent with the request.
            channel: Channel to add star to, or channel where the message to add star to was posted (used with
                ``timestamp``).
            file: File to add star to.
            file_comment: File comment to add star to.
            timestamp: Timestamp of the message to add star to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stars_add(
                token,
                content_type,
                channel=channel,
                file=file,
                file_comment=file_comment,
                timestamp=timestamp,
                request_options=request_options,
            )
        ).unwrap()

    async def stars_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        count: str | None = None,
        page: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StarsListschema:
        """Lists stars for a user.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``stars:read``
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
            await self._with_raw_response.stars_list(
                content_type,
                token=token,
                count=count,
                page=page,
                cursor=cursor,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def stars_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StarsRemoveschema:
        """Removes a star from an item.

        Args:
            token: Authentication token. Requires scope: ``stars:write``
            content_type: Value sent with the request.
            channel: Channel to remove star from, or channel where the message to remove star from was posted (used with
                ``timestamp``).
            file: File to remove star from.
            file_comment: File comment to remove star from.
            timestamp: Timestamp of the message to remove star from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stars_remove(
                token,
                content_type,
                channel=channel,
                file=file,
                file_comment=file_comment,
                timestamp=timestamp,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStarsWithRawResponse:
        return self._with_raw_response


class StarsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def stars_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StarsAddschema, RawError]:
        """Adds a star to an item.

        Args:
            token: Authentication token. Requires scope: ``stars:write``
            content_type: Value sent with the request.
            channel: Channel to add star to, or channel where the message to add star to was posted (used with
                ``timestamp``).
            file: File to add star to.
            file_comment: File comment to add star to.
            timestamp: Timestamp of the message to add star to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/stars.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("channel", channel),
                    param[str | None]("file", file),
                    param[str | None]("file_comment", file_comment),
                    param[str | None]("timestamp", timestamp),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[StarsAddschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stars_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        count: str | None = None,
        page: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StarsListschema, RawError]:
        """Lists stars for a user.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``stars:read``
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
            url_template=self._server.default("/stars.list"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("count", count),
                param[str | None]("page", page),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[StarsListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stars_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StarsRemoveschema, RawError]:
        """Removes a star from an item.

        Args:
            token: Authentication token. Requires scope: ``stars:write``
            content_type: Value sent with the request.
            channel: Channel to remove star from, or channel where the message to remove star from was posted (used with
                ``timestamp``).
            file: File to remove star from.
            file_comment: File comment to remove star from.
            timestamp: Timestamp of the message to remove star from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/stars.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("channel", channel),
                    param[str | None]("file", file),
                    param[str | None]("file_comment", file_comment),
                    param[str | None]("timestamp", timestamp),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[StarsRemoveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStarsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def stars_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StarsAddschema, RawError]:
        """Adds a star to an item.

        Args:
            token: Authentication token. Requires scope: ``stars:write``
            content_type: Value sent with the request.
            channel: Channel to add star to, or channel where the message to add star to was posted (used with
                ``timestamp``).
            file: File to add star to.
            file_comment: File comment to add star to.
            timestamp: Timestamp of the message to add star to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/stars.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("channel", channel),
                    param[str | None]("file", file),
                    param[str | None]("file_comment", file_comment),
                    param[str | None]("timestamp", timestamp),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[StarsAddschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stars_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        count: str | None = None,
        page: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StarsListschema, RawError]:
        """Lists stars for a user.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``stars:read``
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
            url_template=self._server.default("/stars.list"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("count", count),
                param[str | None]("page", page),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[StarsListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stars_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel: str | None = None,
        file: str | None = None,
        file_comment: str | None = None,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StarsRemoveschema, RawError]:
        """Removes a star from an item.

        Args:
            token: Authentication token. Requires scope: ``stars:write``
            content_type: Value sent with the request.
            channel: Channel to remove star from, or channel where the message to remove star from was posted (used with
                ``timestamp``).
            file: File to remove star from.
            file_comment: File comment to remove star from.
            timestamp: Timestamp of the message to remove star from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/stars.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("channel", channel),
                    param[str | None]("file", file),
                    param[str | None]("file_comment", file_comment),
                    param[str | None]("timestamp", timestamp),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[StarsRemoveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
