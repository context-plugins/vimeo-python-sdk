from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Search:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SearchWithRawResponse(client, server, auth)

    def search_messages(
        self,
        token: str,
        query: str,
        content_type: ContentTypeOrStr,
        *,
        count: int | None = None,
        highlight: bool | None = None,
        page: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Searches for messages matching a query.

        Args:
            token: Authentication token. Requires scope: ``search:read``
            query: Search query.
            content_type: Value sent with the request.
            count: Pass the number of results you want per "page". Maximum of ``100``.
            highlight: Pass a value of ``true`` to enable query highlight markers (see below).
            page: Value sent with the request.
            sort: Return matches sorted by either ``score`` or ``timestamp``.
            sort_dir: Change sort direction to ascending (``asc``) or descending (``desc``).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_messages(
            token,
            query,
            content_type,
            count=count,
            highlight=highlight,
            page=page,
            sort=sort,
            sort_dir=sort_dir,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SearchWithRawResponse:
        return self._with_raw_response


class AsyncSearch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSearchWithRawResponse(client, server, auth)

    async def search_messages(
        self,
        token: str,
        query: str,
        content_type: ContentTypeOrStr,
        *,
        count: int | None = None,
        highlight: bool | None = None,
        page: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Searches for messages matching a query.

        Args:
            token: Authentication token. Requires scope: ``search:read``
            query: Search query.
            content_type: Value sent with the request.
            count: Pass the number of results you want per "page". Maximum of ``100``.
            highlight: Pass a value of ``true`` to enable query highlight markers (see below).
            page: Value sent with the request.
            sort: Return matches sorted by either ``score`` or ``timestamp``.
            sort_dir: Change sort direction to ascending (``asc``) or descending (``desc``).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_messages(
                token,
                query,
                content_type,
                count=count,
                highlight=highlight,
                page=page,
                sort=sort,
                sort_dir=sort_dir,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSearchWithRawResponse:
        return self._with_raw_response


class SearchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def search_messages(
        self,
        token: str,
        query: str,
        content_type: ContentTypeOrStr,
        *,
        count: int | None = None,
        highlight: bool | None = None,
        page: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Searches for messages matching a query.

        Args:
            token: Authentication token. Requires scope: ``search:read``
            query: Search query.
            content_type: Value sent with the request.
            count: Pass the number of results you want per "page". Maximum of ``100``.
            highlight: Pass a value of ``true`` to enable query highlight markers (see below).
            page: Value sent with the request.
            sort: Return matches sorted by either ``score`` or ``timestamp``.
            sort_dir: Change sort direction to ascending (``asc``) or descending (``desc``).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search.messages"),
            query_params=[
                param[str]("token", token),
                param[str]("query", query),
                param[int | None]("count", count),
                param[bool | None]("highlight", highlight),
                param[int | None]("page", page),
                param[str | None]("sort", sort),
                param[str | None]("sort_dir", sort_dir),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSearchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def search_messages(
        self,
        token: str,
        query: str,
        content_type: ContentTypeOrStr,
        *,
        count: int | None = None,
        highlight: bool | None = None,
        page: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Searches for messages matching a query.

        Args:
            token: Authentication token. Requires scope: ``search:read``
            query: Search query.
            content_type: Value sent with the request.
            count: Pass the number of results you want per "page". Maximum of ``100``.
            highlight: Pass a value of ``true`` to enable query highlight markers (see below).
            page: Value sent with the request.
            sort: Return matches sorted by either ``score`` or ``timestamp``.
            sort_dir: Change sort direction to ascending (``asc``) or descending (``desc``).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search.messages"),
            query_params=[
                param[str]("token", token),
                param[str]("query", query),
                param[int | None]("count", count),
                param[bool | None]("highlight", highlight),
                param[int | None]("page", page),
                param[str | None]("sort", sort),
                param[str | None]("sort_dir", sort_dir),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
