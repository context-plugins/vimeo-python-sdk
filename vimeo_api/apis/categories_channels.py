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
    json_decoder,
    param,
)
from ..errors.get_category_channels_error import GetCategoryChannelsErrorBody, get_category_channels_error_mapper
from ..models.channel_connection import ChannelConnection
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort4 import Sort4OrStr
from ..server.server import Server


class CategoriesChannels:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CategoriesChannelsWithRawResponse(client, server, auth)

    def get_category_channels(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChannelConnection:
        """This method returns every channel that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``followers`` - Sort the results by number of
                followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: No such category exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_category_channels(
            category,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> CategoriesChannelsWithRawResponse:
        return self._with_raw_response


class AsyncCategoriesChannels:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCategoriesChannelsWithRawResponse(client, server, auth)

    async def get_category_channels(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChannelConnection:
        """This method returns every channel that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``followers`` - Sort the results by number of
                followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: No such category exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_category_channels(
                category,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCategoriesChannelsWithRawResponse:
        return self._with_raw_response


class CategoriesChannelsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_category_channels(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChannelConnection, GetCategoryChannelsErrorBody]:
        """This method returns every channel that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``followers`` - Sort the results by number of
                followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}/channels"),
            path_params=[param[str]("category", category)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort4OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_category_channels_error_mapper,
            request_options=request_options,
        )


class AsyncCategoriesChannelsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_category_channels(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChannelConnection, GetCategoryChannelsErrorBody]:
        """This method returns every channel that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``followers`` - Sort the results by number of
                followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}/channels"),
            path_params=[param[str]("category", category)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort4OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_category_channels_error_mapper,
            request_options=request_options,
        )
