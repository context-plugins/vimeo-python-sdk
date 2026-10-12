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
from ..errors.get_category_groups_error import GetCategoryGroupsErrorBody, get_category_groups_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.group_connection import GroupConnection
from ..server.server import Server


class CategoriesGroups:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CategoriesGroupsWithRawResponse(client, server, auth)

    def get_category_groups(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupConnection:
        """This method returns every group that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``members`` - Sort the results by number of
                members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The groups were returned.

        Raises:
            ApiError: No such category exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_category_groups(
                category,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> CategoriesGroupsWithRawResponse:
        return self._with_raw_response


class AsyncCategoriesGroups:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCategoriesGroupsWithRawResponse(client, server, auth)

    async def get_category_groups(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupConnection:
        """This method returns every group that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``members`` - Sort the results by number of
                members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The groups were returned.

        Raises:
            ApiError: No such category exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_category_groups(
                category,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCategoriesGroupsWithRawResponse:
        return self._with_raw_response


class CategoriesGroupsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_category_groups(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupConnection, GetCategoryGroupsErrorBody]:
        """This method returns every group that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``members`` - Sort the results by number of
                members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}/groups"),
            path_params=[param[str]("category", category)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[GroupConnection],
            error_mapper=get_category_groups_error_mapper,
            request_options=request_options,
        )


class AsyncCategoriesGroupsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_category_groups(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupConnection, GetCategoryGroupsErrorBody]:
        """This method returns every group that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``members`` - Sort the results by number of
                members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}/groups"),
            path_params=[param[str]("category", category)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[GroupConnection],
            error_mapper=get_category_groups_error_mapper,
            request_options=request_options,
        )
