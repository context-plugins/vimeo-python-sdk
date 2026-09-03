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
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.get_vod_season_error import GetVodSeasonErrorBody, get_vod_season_error_mapper
from ..errors.get_vod_seasons_error import GetVodSeasonsErrorBody, get_vod_seasons_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter27 import Filter27OrStr
from ..models.enums.sort43 import Sort43OrStr
from ..models.enums.sort44 import Sort44OrStr
from ..models.on_demand_season import OnDemandSeason
from ..models.on_demand_season_connection import OnDemandSeasonConnection
from ..models.video_connection import VideoConnection
from ..server.server import Server


class OnDemandSeasons:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandSeasonsWithRawResponse(client, server, auth)

    def get_vod_season(
        self, ondemand_id: float, season_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandSeason:
        """This method returns a single season on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            season_id: The ID of the season.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The season was returned.

        Raises:
            ApiError: No such On Demand page or season exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_season(ondemand_id, season_id, request_options=request_options).unwrap()

    def get_vod_season_videos(
        self,
        ondemand_id: float,
        season_id: float,
        *,
        filter: Filter27OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort44OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified season on an On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            season_id: The ID of the season.
            filter: The attribute by which to filter the results. Option descriptions: * ``viewable`` - Filter by
                viewable videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sorting method. * ``manual`` - Sort the results manually. * ``name`` - Sort the
                results by name. * ``purchase_time`` - Sort the results by time of purchase. * ``release_date`` - Sort
                the results by release date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_vod_season_videos(
            ondemand_id,
            season_id,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_vod_seasons(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter27OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort43OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandSeasonConnection:
        """This method returns every season on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``viewable`` - Filter by
                viewable seasons.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``manual``
                - Sort the results manually.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The seasons were returned.

        Raises:
            ApiError: * No such On Demand page exists. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_seasons(
            ondemand_id,
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> OnDemandSeasonsWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandSeasons:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandSeasonsWithRawResponse(client, server, auth)

    async def get_vod_season(
        self, ondemand_id: float, season_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandSeason:
        """This method returns a single season on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            season_id: The ID of the season.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The season was returned.

        Raises:
            ApiError: No such On Demand page or season exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_vod_season(ondemand_id, season_id, request_options=request_options)
        ).unwrap()

    async def get_vod_season_videos(
        self,
        ondemand_id: float,
        season_id: float,
        *,
        filter: Filter27OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort44OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified season on an On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            season_id: The ID of the season.
            filter: The attribute by which to filter the results. Option descriptions: * ``viewable`` - Filter by
                viewable videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sorting method. * ``manual`` - Sort the results manually. * ``name`` - Sort the
                results by name. * ``purchase_time`` - Sort the results by time of purchase. * ``release_date`` - Sort
                the results by release date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_vod_season_videos(
                ondemand_id,
                season_id,
                filter=filter,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_vod_seasons(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter27OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort43OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandSeasonConnection:
        """This method returns every season on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``viewable`` - Filter by
                viewable seasons.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``manual``
                - Sort the results manually.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The seasons were returned.

        Raises:
            ApiError: * No such On Demand page exists. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_vod_seasons(
                ondemand_id,
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOnDemandSeasonsWithRawResponse:
        return self._with_raw_response


class OnDemandSeasonsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_vod_season(
        self, ondemand_id: float, season_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandSeason, GetVodSeasonErrorBody]:
        """This method returns a single season on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            season_id: The ID of the season.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/seasons/{season_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("season_id", season_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandSeason],
            error_mapper=get_vod_season_error_mapper,
            request_options=request_options,
        )

    def get_vod_season_videos(
        self,
        ondemand_id: float,
        season_id: float,
        *,
        filter: Filter27OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort44OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video in the specified season on an On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            season_id: The ID of the season.
            filter: The attribute by which to filter the results. Option descriptions: * ``viewable`` - Filter by
                viewable videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sorting method. * ``manual`` - Sort the results manually. * ``name`` - Sort the
                results by name. * ``purchase_time`` - Sort the results by time of purchase. * ``release_date`` - Sort
                the results by release date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/seasons/{season_id}/videos"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("season_id", season_id)],
            query_params=[
                param[Filter27OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort44OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_vod_seasons(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter27OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort43OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandSeasonConnection, GetVodSeasonsErrorBody]:
        """This method returns every season on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``viewable`` - Filter by
                viewable seasons.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``manual``
                - Sort the results manually.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/seasons"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter27OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort43OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandSeasonConnection],
            error_mapper=get_vod_seasons_error_mapper,
            request_options=request_options,
        )


class AsyncOnDemandSeasonsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_vod_season(
        self, ondemand_id: float, season_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandSeason, GetVodSeasonErrorBody]:
        """This method returns a single season on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            season_id: The ID of the season.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/seasons/{season_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("season_id", season_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandSeason],
            error_mapper=get_vod_season_error_mapper,
            request_options=request_options,
        )

    async def get_vod_season_videos(
        self,
        ondemand_id: float,
        season_id: float,
        *,
        filter: Filter27OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort44OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video in the specified season on an On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            season_id: The ID of the season.
            filter: The attribute by which to filter the results. Option descriptions: * ``viewable`` - Filter by
                viewable videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sorting method. * ``manual`` - Sort the results manually. * ``name`` - Sort the
                results by name. * ``purchase_time`` - Sort the results by time of purchase. * ``release_date`` - Sort
                the results by release date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/seasons/{season_id}/videos"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("season_id", season_id)],
            query_params=[
                param[Filter27OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort44OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_vod_seasons(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter27OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort43OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandSeasonConnection, GetVodSeasonsErrorBody]:
        """This method returns every season on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``viewable`` - Filter by
                viewable seasons.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``manual``
                - Sort the results manually.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/seasons"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter27OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort43OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandSeasonConnection],
            error_mapper=get_vod_seasons_error_mapper,
            request_options=request_options,
        )
