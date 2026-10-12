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
from ..errors.check_if_vod_was_purchased_alt1_error import (
    CheckIfVodWasPurchasedAlt1ErrorBody,
    check_if_vod_was_purchased_alt1_error_mapper,
)
from ..errors.get_vod_purchases_alt1_error import GetVodPurchasesAlt1ErrorBody, get_vod_purchases_alt1_error_mapper
from ..errors.get_vod_purchases_error import GetVodPurchasesErrorBody, get_vod_purchases_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter19 import Filter19OrStr
from ..models.enums.sort33 import Sort33OrStr
from ..models.on_demand_page import OnDemandPage
from ..models.on_demand_page_connection import OnDemandPageConnection
from ..server.server import Server


class OnDemandPurchasesAndRentals:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandPurchasesAndRentalsWithRawResponse(client, server, auth)

    def check_if_vod_was_purchased_alt1(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandPage:
        """This method determines whether the authenticated user has made a purchase or rental from the specified On
        Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The authenticated user has made this purchase.

        Raises:
            ApiError: The authenticated user can't make purchases for another user's account. No such user or On Demand
                page exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.check_if_vod_was_purchased_alt1(ondemand_id, request_options=request_options)
        )

    def get_vod_purchases(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter19OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every purchase and rental that the authenticated user has made across all On Demand
        pages.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the On Demand video to filter on. Option descriptions: * ``all`` - Filter by all video
                types. * ``expiring_soon`` - Filter by videos that expire soon. * ``film`` - Filter by film. *
                ``important`` - Filter by pages that are about to expire. * ``purchased`` - Filter by purchased videos.
                * ``rented`` - Filter by rented videos. * ``series`` - Filter by series. * ``subscription`` - Filter by
                video subscription. * ``unwatched`` - Filter by unwatched videos. * ``watched`` - Filter by watched
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added video. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by
                date. * ``name`` - Sort the results by video name. * ``purchase_time`` - Sort the results by time of
                video purchase. * ``rating`` - Sort the results by content rating. * ``release_date`` - Sort the results
                by video release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The purchases and rentals were returned.

        Raises:
            ApiError: The authenticated user can't get purchases and rentals for another user's account. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_vod_purchases(
                user_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_vod_purchases_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter19OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every purchase and rental that the authenticated user has made across all On Demand
        pages.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the On Demand video to filter on. Option descriptions: * ``all`` - Filter by all video
                types. * ``expiring_soon`` - Filter by videos that expire soon. * ``film`` - Filter by film. *
                ``important`` - Filter by pages that are about to expire. * ``purchased`` - Filter by purchased videos.
                * ``rented`` - Filter by rented videos. * ``series`` - Filter by series. * ``subscription`` - Filter by
                video subscription. * ``unwatched`` - Filter by unwatched videos. * ``watched`` - Filter by watched
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added video. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by
                date. * ``name`` - Sort the results by video name. * ``purchase_time`` - Sort the results by time of
                video purchase. * ``rating`` - Sort the results by content rating. * ``release_date`` - Sort the results
                by video release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The purchases and rentals were returned.

        Raises:
            ApiError: The authenticated user can't get purchases and rentals for another user's account. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_vod_purchases_alt1(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> OnDemandPurchasesAndRentalsWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandPurchasesAndRentals:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandPurchasesAndRentalsWithRawResponse(client, server, auth)

    async def check_if_vod_was_purchased_alt1(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandPage:
        """This method determines whether the authenticated user has made a purchase or rental from the specified On
        Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The authenticated user has made this purchase.

        Raises:
            ApiError: The authenticated user can't make purchases for another user's account. No such user or On Demand
                page exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_if_vod_was_purchased_alt1(ondemand_id, request_options=request_options)
        )

    async def get_vod_purchases(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter19OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every purchase and rental that the authenticated user has made across all On Demand
        pages.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the On Demand video to filter on. Option descriptions: * ``all`` - Filter by all video
                types. * ``expiring_soon`` - Filter by videos that expire soon. * ``film`` - Filter by film. *
                ``important`` - Filter by pages that are about to expire. * ``purchased`` - Filter by purchased videos.
                * ``rented`` - Filter by rented videos. * ``series`` - Filter by series. * ``subscription`` - Filter by
                video subscription. * ``unwatched`` - Filter by unwatched videos. * ``watched`` - Filter by watched
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added video. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by
                date. * ``name`` - Sort the results by video name. * ``purchase_time`` - Sort the results by time of
                video purchase. * ``rating`` - Sort the results by content rating. * ``release_date`` - Sort the results
                by video release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The purchases and rentals were returned.

        Raises:
            ApiError: The authenticated user can't get purchases and rentals for another user's account. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_vod_purchases(
                user_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_vod_purchases_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter19OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every purchase and rental that the authenticated user has made across all On Demand
        pages.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the On Demand video to filter on. Option descriptions: * ``all`` - Filter by all video
                types. * ``expiring_soon`` - Filter by videos that expire soon. * ``film`` - Filter by film. *
                ``important`` - Filter by pages that are about to expire. * ``purchased`` - Filter by purchased videos.
                * ``rented`` - Filter by rented videos. * ``series`` - Filter by series. * ``subscription`` - Filter by
                video subscription. * ``unwatched`` - Filter by unwatched videos. * ``watched`` - Filter by watched
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added video. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by
                date. * ``name`` - Sort the results by video name. * ``purchase_time`` - Sort the results by time of
                video purchase. * ``rating`` - Sort the results by content rating. * ``release_date`` - Sort the results
                by video release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The purchases and rentals were returned.

        Raises:
            ApiError: The authenticated user can't get purchases and rentals for another user's account. ``error`` is
                ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_vod_purchases_alt1(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncOnDemandPurchasesAndRentalsWithRawResponse:
        return self._with_raw_response


class OnDemandPurchasesAndRentalsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_if_vod_was_purchased_alt1(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandPage, CheckIfVodWasPurchasedAlt1ErrorBody]:
        """This method determines whether the authenticated user has made a purchase or rental from the specified On
        Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/ondemand/purchases/{ondemand_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPage],
            error_mapper=check_if_vod_was_purchased_alt1_error_mapper,
            request_options=request_options,
        )

    def get_vod_purchases(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter19OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetVodPurchasesErrorBody]:
        """This method returns every purchase and rental that the authenticated user has made across all On Demand
        pages.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the On Demand video to filter on. Option descriptions: * ``all`` - Filter by all video
                types. * ``expiring_soon`` - Filter by videos that expire soon. * ``film`` - Filter by film. *
                ``important`` - Filter by pages that are about to expire. * ``purchased`` - Filter by purchased videos.
                * ``rented`` - Filter by rented videos. * ``series`` - Filter by series. * ``subscription`` - Filter by
                video subscription. * ``unwatched`` - Filter by unwatched videos. * ``watched`` - Filter by watched
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added video. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by
                date. * ``name`` - Sort the results by video name. * ``purchase_time`` - Sort the results by time of
                video purchase. * ``rating`` - Sort the results by content rating. * ``release_date`` - Sort the results
                by video release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/ondemand/purchases"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter19OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort33OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPageConnection],
            error_mapper=get_vod_purchases_error_mapper,
            request_options=request_options,
        )

    def get_vod_purchases_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter19OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetVodPurchasesAlt1ErrorBody]:
        """This method returns every purchase and rental that the authenticated user has made across all On Demand
        pages.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the On Demand video to filter on. Option descriptions: * ``all`` - Filter by all video
                types. * ``expiring_soon`` - Filter by videos that expire soon. * ``film`` - Filter by film. *
                ``important`` - Filter by pages that are about to expire. * ``purchased`` - Filter by purchased videos.
                * ``rented`` - Filter by rented videos. * ``series`` - Filter by series. * ``subscription`` - Filter by
                video subscription. * ``unwatched`` - Filter by unwatched videos. * ``watched`` - Filter by watched
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added video. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by
                date. * ``name`` - Sort the results by video name. * ``purchase_time`` - Sort the results by time of
                video purchase. * ``rating`` - Sort the results by content rating. * ``release_date`` - Sort the results
                by video release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/ondemand/purchases"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter19OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort33OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPageConnection],
            error_mapper=get_vod_purchases_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncOnDemandPurchasesAndRentalsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_if_vod_was_purchased_alt1(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandPage, CheckIfVodWasPurchasedAlt1ErrorBody]:
        """This method determines whether the authenticated user has made a purchase or rental from the specified On
        Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/ondemand/purchases/{ondemand_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPage],
            error_mapper=check_if_vod_was_purchased_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_vod_purchases(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter19OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetVodPurchasesErrorBody]:
        """This method returns every purchase and rental that the authenticated user has made across all On Demand
        pages.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the On Demand video to filter on. Option descriptions: * ``all`` - Filter by all video
                types. * ``expiring_soon`` - Filter by videos that expire soon. * ``film`` - Filter by film. *
                ``important`` - Filter by pages that are about to expire. * ``purchased`` - Filter by purchased videos.
                * ``rented`` - Filter by rented videos. * ``series`` - Filter by series. * ``subscription`` - Filter by
                video subscription. * ``unwatched`` - Filter by unwatched videos. * ``watched`` - Filter by watched
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added video. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by
                date. * ``name`` - Sort the results by video name. * ``purchase_time`` - Sort the results by time of
                video purchase. * ``rating`` - Sort the results by content rating. * ``release_date`` - Sort the results
                by video release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/ondemand/purchases"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter19OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort33OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPageConnection],
            error_mapper=get_vod_purchases_error_mapper,
            request_options=request_options,
        )

    async def get_vod_purchases_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter19OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetVodPurchasesAlt1ErrorBody]:
        """This method returns every purchase and rental that the authenticated user has made across all On Demand
        pages.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The type of the On Demand video to filter on. Option descriptions: * ``all`` - Filter by all video
                types. * ``expiring_soon`` - Filter by videos that expire soon. * ``film`` - Filter by film. *
                ``important`` - Filter by pages that are about to expire. * ``purchased`` - Filter by purchased videos.
                * ``rented`` - Filter by rented videos. * ``series`` - Filter by series. * ``subscription`` - Filter by
                video subscription. * ``unwatched`` - Filter by unwatched videos. * ``watched`` - Filter by watched
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added video. * ``alphabetical`` - Sort the results alphabetically. * ``date`` - Sort the results by
                date. * ``name`` - Sort the results by video name. * ``purchase_time`` - Sort the results by time of
                video purchase. * ``rating`` - Sort the results by content rating. * ``release_date`` - Sort the results
                by video release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/ondemand/purchases"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter19OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort33OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandPageConnection],
            error_mapper=get_vod_purchases_alt1_error_mapper,
            request_options=request_options,
        )
