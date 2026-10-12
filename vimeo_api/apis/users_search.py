from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.search_users_error import SearchUsersErrorBody, search_users_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort13 import Sort13OrStr
from ..models.user_connection import UserConnection
from ..server.server import Server


class UsersSearch:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersSearchWithRawResponse(client, server, auth)

    def search_users(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort13OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns user search results.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``relevant`` - Sort the results by relevance. * ``videos`` - Sort the results by
                number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The search results were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. There was an internal search error.
                Search is disabled. ``error`` is ``Error | LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.search_users(
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> UsersSearchWithRawResponse:
        return self._with_raw_response


class AsyncUsersSearch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersSearchWithRawResponse(client, server, auth)

    async def search_users(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort13OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns user search results.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``relevant`` - Sort the results by relevance. * ``videos`` - Sort the results by
                number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The search results were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. There was an internal search error.
                Search is disabled. ``error`` is ``Error | LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.search_users(
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncUsersSearchWithRawResponse:
        return self._with_raw_response


class UsersSearchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def search_users(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort13OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, SearchUsersErrorBody]:
        """This method returns user search results.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``relevant`` - Sort the results by relevance. * ``videos`` - Sort the results by
                number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort13OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=search_users_error_mapper,
            request_options=request_options,
        )


class AsyncUsersSearchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def search_users(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort13OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, SearchUsersErrorBody]:
        """This method returns user search results.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``relevant`` - Sort the results by relevance. * ``videos`` - Sort the results by
                number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort13OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[UserConnection],
            error_mapper=search_users_error_mapper,
            request_options=request_options,
        )
