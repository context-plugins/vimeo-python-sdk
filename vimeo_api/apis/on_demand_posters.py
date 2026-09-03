from __future__ import annotations

from uuid import UUID, uuid4

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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.add_vod_poster_error import AddVodPosterErrorBody, add_vod_poster_error_mapper
from ..errors.get_vod_posters_error import GetVodPostersErrorBody, get_vod_posters_error_mapper
from ..models.ondemand_pages_pictures_request import OndemandPagesPicturesRequest, OndemandPagesPicturesRequestDict
from ..models.picture import Picture
from ..models.picture_connection import PictureConnection
from ..server.server import Server


class OnDemandPosters:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandPostersWithRawResponse(client, server, auth)

    def add_vod_poster(self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method adds a poster image to the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The poster was added.

        Raises:
            ApiError: The authenticated user can't add posters to this On Demand page. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.add_vod_poster(ondemand_id, request_options=request_options).unwrap()

    def edit_vod_poster(
        self,
        ondemand_id: float,
        poster_id: float,
        *,
        body: OndemandPagesPicturesRequest | OndemandPagesPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits a poster image on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            poster_id: The ID of the poster.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The poster was edited.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.edit_vod_poster(
            ondemand_id, poster_id, body=body, request_options=request_options
        ).unwrap()

    def get_vod_poster(
        self, ondemand_id: float, poster_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single poster on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            poster_id: The ID of the poster.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The poster was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_vod_poster(ondemand_id, poster_id, request_options=request_options).unwrap()

    def get_vod_posters(
        self,
        ondemand_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every poster on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The posters were returned.

        Raises:
            ApiError: No such On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_posters(
            ondemand_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> OnDemandPostersWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandPosters:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandPostersWithRawResponse(client, server, auth)

    async def add_vod_poster(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds a poster image to the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The poster was added.

        Raises:
            ApiError: The authenticated user can't add posters to this On Demand page. ``error`` is ``LegacyError |
                RawError``."""
        return (await self._with_raw_response.add_vod_poster(ondemand_id, request_options=request_options)).unwrap()

    async def edit_vod_poster(
        self,
        ondemand_id: float,
        poster_id: float,
        *,
        body: OndemandPagesPicturesRequest | OndemandPagesPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits a poster image on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            poster_id: The ID of the poster.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The poster was edited.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.edit_vod_poster(
                ondemand_id, poster_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_vod_poster(
        self, ondemand_id: float, poster_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single poster on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            poster_id: The ID of the poster.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The poster was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_vod_poster(ondemand_id, poster_id, request_options=request_options)
        ).unwrap()

    async def get_vod_posters(
        self,
        ondemand_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every poster on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The posters were returned.

        Raises:
            ApiError: No such On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_vod_posters(
                ondemand_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOnDemandPostersWithRawResponse:
        return self._with_raw_response


class OnDemandPostersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_vod_poster(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, AddVodPosterErrorBody]:
        """This method adds a poster image to the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/pictures"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=add_vod_poster_error_mapper,
            request_options=request_options,
        )

    def edit_vod_poster(
        self,
        ondemand_id: float,
        poster_id: float,
        *,
        body: OndemandPagesPicturesRequest | OndemandPagesPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method edits a poster image on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            poster_id: The ID of the poster.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/pictures/{poster_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("poster_id", poster_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesPicturesRequest | OndemandPagesPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_vod_poster(
        self, ondemand_id: float, poster_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns a single poster on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            poster_id: The ID of the poster.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/pictures/{poster_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("poster_id", poster_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_vod_posters(
        self,
        ondemand_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetVodPostersErrorBody]:
        """This method returns every poster on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/pictures"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_vod_posters_error_mapper,
            request_options=request_options,
        )


class AsyncOnDemandPostersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_vod_poster(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, AddVodPosterErrorBody]:
        """This method adds a poster image to the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/pictures"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=add_vod_poster_error_mapper,
            request_options=request_options,
        )

    async def edit_vod_poster(
        self,
        ondemand_id: float,
        poster_id: float,
        *,
        body: OndemandPagesPicturesRequest | OndemandPagesPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method edits a poster image on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            poster_id: The ID of the poster.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/pictures/{poster_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("poster_id", poster_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesPicturesRequest | OndemandPagesPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_vod_poster(
        self, ondemand_id: float, poster_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns a single poster on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            poster_id: The ID of the poster.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/pictures/{poster_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("poster_id", poster_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_vod_posters(
        self,
        ondemand_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetVodPostersErrorBody]:
        """This method returns every poster on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/pictures"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_vod_posters_error_mapper,
            request_options=request_options,
        )
