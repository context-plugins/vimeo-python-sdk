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
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort8 import Sort8OrStr
from ..models.portfolio import Portfolio
from ..models.portfolio_connection import PortfolioConnection
from ..server.server import Server


class PortfoliosEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PortfoliosEssentialsWithRawResponse(client, server, auth)

    def get_portfolio(
        self, portfolio_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Portfolio:
        """This method returns a single portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portfolio was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_portfolio(portfolio_id, user_id, request_options=request_options))

    def get_portfolio_alt1(
        self, portfolio_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Portfolio:
        """This method returns a single portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portfolio was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_portfolio_alt1(portfolio_id, request_options=request_options))

    def get_portfolios(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PortfolioConnection:
        """This method returns every portfolio belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portfolios were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_portfolios(
                user_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_portfolios_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PortfolioConnection:
        """This method returns every portfolio belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portfolios were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_portfolios_alt1(
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> PortfoliosEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncPortfoliosEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPortfoliosEssentialsWithRawResponse(client, server, auth)

    async def get_portfolio(
        self, portfolio_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Portfolio:
        """This method returns a single portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portfolio was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_portfolio(portfolio_id, user_id, request_options=request_options)
        )

    async def get_portfolio_alt1(
        self, portfolio_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Portfolio:
        """This method returns a single portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portfolio was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_portfolio_alt1(portfolio_id, request_options=request_options))

    async def get_portfolios(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PortfolioConnection:
        """This method returns every portfolio belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portfolios were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_portfolios(
                user_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_portfolios_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PortfolioConnection:
        """This method returns every portfolio belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portfolios were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_portfolios_alt1(
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncPortfoliosEssentialsWithRawResponse:
        return self._with_raw_response


class PortfoliosEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_portfolio(
        self, portfolio_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Portfolio, RawError]:
        """This method returns a single portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Portfolio],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_portfolio_alt1(
        self, portfolio_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Portfolio, RawError]:
        """This method returns a single portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/portfolios/{portfolio_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Portfolio],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_portfolios(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PortfolioConnection, RawError]:
        """This method returns every portfolio belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/portfolios"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PortfolioConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_portfolios_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PortfolioConnection, RawError]:
        """This method returns every portfolio belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/portfolios"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PortfolioConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPortfoliosEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_portfolio(
        self, portfolio_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Portfolio, RawError]:
        """This method returns a single portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Portfolio],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_portfolio_alt1(
        self, portfolio_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Portfolio, RawError]:
        """This method returns a single portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/portfolios/{portfolio_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Portfolio],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_portfolios(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PortfolioConnection, RawError]:
        """This method returns every portfolio belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/portfolios"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PortfolioConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_portfolios_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PortfolioConnection, RawError]:
        """This method returns every portfolio belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/portfolios"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PortfolioConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
