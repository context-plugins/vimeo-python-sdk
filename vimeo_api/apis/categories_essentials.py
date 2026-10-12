from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.get_category_error import GetCategoryErrorBody, get_category_error_mapper
from ..models.category import Category
from ..models.category_connection import CategoryConnection
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort3 import Sort3OrStr
from ..server.server import Server


class CategoriesEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CategoriesEssentialsWithRawResponse(client, server, auth)

    def get_categories(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoryConnection:
        """This method returns every available category.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``last_video_featured_time`` - Sort the results by
                most recently featured. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The categories were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_categories(
                direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
            ),
        )

    def get_category(self, category: str, *, request_options: RequestOptionsOrDict | None = None) -> Category:
        """This method returns the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The category was returned.

        Raises:
            ApiError: No such category exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.get_category(category, request_options=request_options))

    @property
    def with_raw_response(self) -> CategoriesEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncCategoriesEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCategoriesEssentialsWithRawResponse(client, server, auth)

    async def get_categories(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoryConnection:
        """This method returns every available category.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``last_video_featured_time`` - Sort the results by
                most recently featured. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The categories were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_categories(
                direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
            ),
        )

    async def get_category(self, category: str, *, request_options: RequestOptionsOrDict | None = None) -> Category:
        """This method returns the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The category was returned.

        Raises:
            ApiError: No such category exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.get_category(category, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncCategoriesEssentialsWithRawResponse:
        return self._with_raw_response


class CategoriesEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_categories(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoryConnection, RawError]:
        """This method returns every available category.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``last_video_featured_time`` - Sort the results by
                most recently featured. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort3OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_category(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Category, GetCategoryErrorBody]:
        """This method returns the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}"),
            path_params=[param[str]("category", category)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Category],
            error_mapper=get_category_error_mapper,
            request_options=request_options,
        )


class AsyncCategoriesEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_categories(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoryConnection, RawError]:
        """This method returns every available category.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``last_video_featured_time`` - Sort the results by
                most recently featured. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort3OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[CategoryConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_category(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Category, GetCategoryErrorBody]:
        """This method returns the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}"),
            path_params=[param[str]("category", category)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Category],
            error_mapper=get_category_error_mapper,
            request_options=request_options,
        )
