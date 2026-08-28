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
    empty_response,
    json_decoder,
    param,
)
from ..errors.add_vod_genre_error import AddVodGenreErrorBody, add_vod_genre_error_mapper
from ..errors.delete_vod_genre_error import DeleteVodGenreErrorBody, delete_vod_genre_error_mapper
from ..errors.get_genre_vod_error import GetGenreVodErrorBody, get_genre_vod_error_mapper
from ..errors.get_genre_vods_error import GetGenreVodsErrorBody, get_genre_vods_error_mapper
from ..errors.get_vod_genre_by_ondemand_id_error import (
    GetVodGenreByOndemandIdErrorBody,
    get_vod_genre_by_ondemand_id_error_mapper,
)
from ..errors.get_vod_genre_error import GetVodGenreErrorBody, get_vod_genre_error_mapper
from ..errors.get_vod_genres_by_ondemand_id_error import (
    GetVodGenresByOndemandIdErrorBody,
    get_vod_genres_by_ondemand_id_error_mapper,
)
from ..errors.get_vod_genres_error import GetVodGenresErrorBody, get_vod_genres_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter24 import Filter24OrStr
from ..models.enums.sort41 import Sort41OrStr
from ..models.on_demand_genre import OnDemandGenre
from ..models.on_demand_genre_connection import OnDemandGenreConnection
from ..models.on_demand_page import OnDemandPage
from ..models.on_demand_page_connection import OnDemandPageConnection
from ..server.server import Server


class OnDemandGenres:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandGenresWithRawResponse(client, server, auth)

    def add_vod_genre(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandGenre:
        """This method adds the specified genre designation to an On Demand page. A page can be associated with a
        maximum of two genres. The authenticated user must be the owner of the page.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genre was added.

        Raises:
            ApiError: The On Demand page already has two genres. The authenticated user can't add a genre to this On
                Demand page. No such On Demand page or genre exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_vod_genre(genre_id, ondemand_id, request_options=request_options).unwrap()

    def delete_vod_genre(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a genre association from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genre was removed.

        Raises:
            ApiError: The On Demand page must belong to at least one genre. The authenticated user can't remove a genre
                from this On Demand page. No such On Demand page or genre exists. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.delete_vod_genre(genre_id, ondemand_id, request_options=request_options).unwrap()

    def get_genre_vod(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandPage:
        """This method returns a single On Demand page that belongs to the specified genre.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The On Demand page in the genre was returned.

        Raises:
            ApiError: No such On Demand page or genre exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_genre_vod(genre_id, ondemand_id, request_options=request_options).unwrap()

    def get_genre_vods(
        self,
        genre_id: str,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter24OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort41OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every On Demand page that belongs to the specified genre.

        Args:
            genre_id: The ID of the genre.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``country`` - Sort the results
                by country. * ``my_region`` - Sort the results by user's region.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name. *
                ``publish.time`` - Sort the results by time of publishing. * ``videos`` - Sort the results by video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The On Demand pages in the genre were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_genre_vods(
            genre_id,
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_vod_genre(self, genre_id: str, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandGenre:
        """This method returns a single On Demand genre.

        Args:
            genre_id: The ID of the genre.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genre was returned.

        Raises:
            ApiError: No such genre exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_genre(genre_id, request_options=request_options).unwrap()

    def get_vod_genre_by_ondemand_id(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandGenre:
        """This method determines whether an On Demand page is associated with the specified genre.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The On Demand page is in this genre.

        Raises:
            ApiError: No such On Demand page or genre exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_genre_by_ondemand_id(
            genre_id, ondemand_id, request_options=request_options
        ).unwrap()

    def get_vod_genres(self, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandGenreConnection:
        """This method returns every existing On Demand genre.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genres were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_vod_genres(request_options=request_options).unwrap()

    def get_vod_genres_by_ondemand_id(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandGenreConnection:
        """This method returns every genre associated with the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genres were returned.

        Raises:
            ApiError: * No such On Demand page exists. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_genres_by_ondemand_id(
            ondemand_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> OnDemandGenresWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandGenres:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandGenresWithRawResponse(client, server, auth)

    async def add_vod_genre(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandGenre:
        """This method adds the specified genre designation to an On Demand page. A page can be associated with a
        maximum of two genres. The authenticated user must be the owner of the page.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genre was added.

        Raises:
            ApiError: The On Demand page already has two genres. The authenticated user can't add a genre to this On
                Demand page. No such On Demand page or genre exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_vod_genre(genre_id, ondemand_id, request_options=request_options)
        ).unwrap()

    async def delete_vod_genre(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a genre association from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genre was removed.

        Raises:
            ApiError: The On Demand page must belong to at least one genre. The authenticated user can't remove a genre
                from this On Demand page. No such On Demand page or genre exists. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.delete_vod_genre(genre_id, ondemand_id, request_options=request_options)
        ).unwrap()

    async def get_genre_vod(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandPage:
        """This method returns a single On Demand page that belongs to the specified genre.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The On Demand page in the genre was returned.

        Raises:
            ApiError: No such On Demand page or genre exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_genre_vod(genre_id, ondemand_id, request_options=request_options)
        ).unwrap()

    async def get_genre_vods(
        self,
        genre_id: str,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter24OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort41OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPageConnection:
        """This method returns every On Demand page that belongs to the specified genre.

        Args:
            genre_id: The ID of the genre.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``country`` - Sort the results
                by country. * ``my_region`` - Sort the results by user's region.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name. *
                ``publish.time`` - Sort the results by time of publishing. * ``videos`` - Sort the results by video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The On Demand pages in the genre were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_genre_vods(
                genre_id,
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_vod_genre(
        self, genre_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandGenre:
        """This method returns a single On Demand genre.

        Args:
            genre_id: The ID of the genre.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genre was returned.

        Raises:
            ApiError: No such genre exists. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.get_vod_genre(genre_id, request_options=request_options)).unwrap()

    async def get_vod_genre_by_ondemand_id(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandGenre:
        """This method determines whether an On Demand page is associated with the specified genre.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The On Demand page is in this genre.

        Raises:
            ApiError: No such On Demand page or genre exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_vod_genre_by_ondemand_id(
                genre_id, ondemand_id, request_options=request_options
            )
        ).unwrap()

    async def get_vod_genres(self, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandGenreConnection:
        """This method returns every existing On Demand genre.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genres were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.get_vod_genres(request_options=request_options)).unwrap()

    async def get_vod_genres_by_ondemand_id(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandGenreConnection:
        """This method returns every genre associated with the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The genres were returned.

        Raises:
            ApiError: * No such On Demand page exists. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_vod_genres_by_ondemand_id(ondemand_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOnDemandGenresWithRawResponse:
        return self._with_raw_response


class OnDemandGenresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_vod_genre(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenre, AddVodGenreErrorBody]:
        """This method adds the specified genre designation to an On Demand page. A page can be associated with a
        maximum of two genres. The authenticated user must be the owner of the page.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/genres/{genre_id}"),
            path_params=[param[str]("genre_id", genre_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenre],
            error_mapper=add_vod_genre_error_mapper,
            request_options=request_options,
        )

    def delete_vod_genre(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodGenreErrorBody]:
        """This method removes a genre association from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/genres/{genre_id}"),
            path_params=[param[str]("genre_id", genre_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_vod_genre_error_mapper,
            request_options=request_options,
        )

    def get_genre_vod(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandPage, GetGenreVodErrorBody]:
        """This method returns a single On Demand page that belongs to the specified genre.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/genres/{genre_id}/pages/{ondemand_id}"),
            path_params=[param[str]("genre_id", genre_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPage],
            error_mapper=get_genre_vod_error_mapper,
            request_options=request_options,
        )

    def get_genre_vods(
        self,
        genre_id: str,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter24OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort41OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetGenreVodsErrorBody]:
        """This method returns every On Demand page that belongs to the specified genre.

        Args:
            genre_id: The ID of the genre.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``country`` - Sort the results
                by country. * ``my_region`` - Sort the results by user's region.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name. *
                ``publish.time`` - Sort the results by time of publishing. * ``videos`` - Sort the results by video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/genres/{genre_id}/pages"),
            path_params=[param[str]("genre_id", genre_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter24OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort41OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPageConnection],
            error_mapper=get_genre_vods_error_mapper,
            request_options=request_options,
        )

    def get_vod_genre(
        self, genre_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenre, GetVodGenreErrorBody]:
        """This method returns a single On Demand genre.

        Args:
            genre_id: The ID of the genre.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/genres/{genre_id}"),
            path_params=[param[str]("genre_id", genre_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenre],
            error_mapper=get_vod_genre_error_mapper,
            request_options=request_options,
        )

    def get_vod_genre_by_ondemand_id(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenre, GetVodGenreByOndemandIdErrorBody]:
        """This method determines whether an On Demand page is associated with the specified genre.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/genres/{genre_id}"),
            path_params=[param[str]("genre_id", genre_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenre],
            error_mapper=get_vod_genre_by_ondemand_id_error_mapper,
            request_options=request_options,
        )

    def get_vod_genres(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenreConnection, GetVodGenresErrorBody]:
        """This method returns every existing On Demand genre.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/genres"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenreConnection],
            error_mapper=get_vod_genres_error_mapper,
            request_options=request_options,
        )

    def get_vod_genres_by_ondemand_id(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenreConnection, GetVodGenresByOndemandIdErrorBody]:
        """This method returns every genre associated with the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/genres"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenreConnection],
            error_mapper=get_vod_genres_by_ondemand_id_error_mapper,
            request_options=request_options,
        )


class AsyncOnDemandGenresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_vod_genre(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenre, AddVodGenreErrorBody]:
        """This method adds the specified genre designation to an On Demand page. A page can be associated with a
        maximum of two genres. The authenticated user must be the owner of the page.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/genres/{genre_id}"),
            path_params=[param[str]("genre_id", genre_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenre],
            error_mapper=add_vod_genre_error_mapper,
            request_options=request_options,
        )

    async def delete_vod_genre(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodGenreErrorBody]:
        """This method removes a genre association from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/genres/{genre_id}"),
            path_params=[param[str]("genre_id", genre_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_vod_genre_error_mapper,
            request_options=request_options,
        )

    async def get_genre_vod(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandPage, GetGenreVodErrorBody]:
        """This method returns a single On Demand page that belongs to the specified genre.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/genres/{genre_id}/pages/{ondemand_id}"),
            path_params=[param[str]("genre_id", genre_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPage],
            error_mapper=get_genre_vod_error_mapper,
            request_options=request_options,
        )

    async def get_genre_vods(
        self,
        genre_id: str,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter24OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort41OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPageConnection, GetGenreVodsErrorBody]:
        """This method returns every On Demand page that belongs to the specified genre.

        Args:
            genre_id: The ID of the genre.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``country`` - Sort the results
                by country. * ``my_region`` - Sort the results by user's region.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name. *
                ``publish.time`` - Sort the results by time of publishing. * ``videos`` - Sort the results by video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/genres/{genre_id}/pages"),
            path_params=[param[str]("genre_id", genre_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter24OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort41OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPageConnection],
            error_mapper=get_genre_vods_error_mapper,
            request_options=request_options,
        )

    async def get_vod_genre(
        self, genre_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenre, GetVodGenreErrorBody]:
        """This method returns a single On Demand genre.

        Args:
            genre_id: The ID of the genre.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/genres/{genre_id}"),
            path_params=[param[str]("genre_id", genre_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenre],
            error_mapper=get_vod_genre_error_mapper,
            request_options=request_options,
        )

    async def get_vod_genre_by_ondemand_id(
        self, genre_id: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenre, GetVodGenreByOndemandIdErrorBody]:
        """This method determines whether an On Demand page is associated with the specified genre.

        Args:
            genre_id: The ID of the genre.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/genres/{genre_id}"),
            path_params=[param[str]("genre_id", genre_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenre],
            error_mapper=get_vod_genre_by_ondemand_id_error_mapper,
            request_options=request_options,
        )

    async def get_vod_genres(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenreConnection, GetVodGenresErrorBody]:
        """This method returns every existing On Demand genre.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/genres"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenreConnection],
            error_mapper=get_vod_genres_error_mapper,
            request_options=request_options,
        )

    async def get_vod_genres_by_ondemand_id(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandGenreConnection, GetVodGenresByOndemandIdErrorBody]:
        """This method returns every genre associated with the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/genres"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandGenreConnection],
            error_mapper=get_vod_genres_by_ondemand_id_error_mapper,
            request_options=request_options,
        )
