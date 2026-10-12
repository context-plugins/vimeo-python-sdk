from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_vod_background_error import CreateVodBackgroundErrorBody, create_vod_background_error_mapper
from ..errors.delete_vod_background_error import DeleteVodBackgroundErrorBody, delete_vod_background_error_mapper
from ..errors.edit_vod_background_error import EditVodBackgroundErrorBody, edit_vod_background_error_mapper
from ..errors.get_vod_background_error import GetVodBackgroundErrorBody, get_vod_background_error_mapper
from ..errors.get_vod_backgrounds_error import GetVodBackgroundsErrorBody, get_vod_backgrounds_error_mapper
from ..models.ondemand_pages_backgrounds_request import (
    OndemandPagesBackgroundsRequest,
    OndemandPagesBackgroundsRequestDict,
)
from ..models.picture import Picture
from ..models.picture_connection import PictureConnection
from ..server.server import Server


class OnDemandBackgrounds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandBackgroundsWithRawResponse(client, server, auth)

    def create_vod_background(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds a background image to the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background image was added.

        Raises:
            ApiError: The authenticated user can't add a background image to this On Demand page. No such On Demand page
                exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.create_vod_background(ondemand_id, request_options=request_options))

    def delete_vod_background(
        self, background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified background image on an On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background image was deleted.

        Raises:
            ApiError: The authenticated user can't delete this background image. No such On Demand page or background
                image exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.delete_vod_background(background_id, ondemand_id, request_options=request_options)
        )

    def edit_vod_background(
        self,
        background_id: float,
        ondemand_id: float,
        *,
        body: OndemandPagesBackgroundsRequest | OndemandPagesBackgroundsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits the specified background image on an On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background image was edited.

        Raises:
            ApiError: The authenticated user can't edit this background image. No such On Demand page or background
                image exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.edit_vod_background(
                background_id, ondemand_id, body=body, request_options=request_options
            ),
        )

    def get_vod_background(
        self, background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single background image on the specified On Demand page. The authenticated user must be
        the owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background image was returned.

        Raises:
            ApiError: The authenticated user can't get this background image. No such On Demand page or background image
                exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_vod_background(background_id, ondemand_id, request_options=request_options)
        )

    def get_vod_backgrounds(
        self,
        ondemand_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every background image on the specified On Demand page. The authenticated user must be
        the owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background images were returned.

        Raises:
            ApiError: No such On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_vod_backgrounds(
                ondemand_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> OnDemandBackgroundsWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandBackgrounds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandBackgroundsWithRawResponse(client, server, auth)

    async def create_vod_background(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds a background image to the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background image was added.

        Raises:
            ApiError: The authenticated user can't add a background image to this On Demand page. No such On Demand page
                exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.create_vod_background(ondemand_id, request_options=request_options))

    async def delete_vod_background(
        self, background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified background image on an On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background image was deleted.

        Raises:
            ApiError: The authenticated user can't delete this background image. No such On Demand page or background
                image exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_vod_background(
                background_id, ondemand_id, request_options=request_options
            ),
        )

    async def edit_vod_background(
        self,
        background_id: float,
        ondemand_id: float,
        *,
        body: OndemandPagesBackgroundsRequest | OndemandPagesBackgroundsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits the specified background image on an On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background image was edited.

        Raises:
            ApiError: The authenticated user can't edit this background image. No such On Demand page or background
                image exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.edit_vod_background(
                background_id, ondemand_id, body=body, request_options=request_options
            ),
        )

    async def get_vod_background(
        self, background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single background image on the specified On Demand page. The authenticated user must be
        the owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background image was returned.

        Raises:
            ApiError: The authenticated user can't get this background image. No such On Demand page or background image
                exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_vod_background(
                background_id, ondemand_id, request_options=request_options
            ),
        )

    async def get_vod_backgrounds(
        self,
        ondemand_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every background image on the specified On Demand page. The authenticated user must be
        the owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The background images were returned.

        Raises:
            ApiError: No such On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_vod_backgrounds(
                ondemand_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncOnDemandBackgroundsWithRawResponse:
        return self._with_raw_response


class OnDemandBackgroundsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_vod_background(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateVodBackgroundErrorBody]:
        """This method adds a background image to the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_vod_background_error_mapper,
            request_options=request_options,
        )

    def delete_vod_background(
        self, background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodBackgroundErrorBody]:
        """This method deletes the specified background image on an On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"),
            path_params=[param[float]("background_id", background_id), param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_vod_background_error_mapper,
            request_options=request_options,
        )

    def edit_vod_background(
        self,
        background_id: float,
        ondemand_id: float,
        *,
        body: OndemandPagesBackgroundsRequest | OndemandPagesBackgroundsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, EditVodBackgroundErrorBody]:
        """This method edits the specified background image on an On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"),
            path_params=[param[float]("background_id", background_id), param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesBackgroundsRequest | OndemandPagesBackgroundsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=edit_vod_background_error_mapper,
            request_options=request_options,
        )

    def get_vod_background(
        self, background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetVodBackgroundErrorBody]:
        """This method returns a single background image on the specified On Demand page. The authenticated user must be
        the owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"),
            path_params=[param[float]("background_id", background_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_vod_background_error_mapper,
            request_options=request_options,
        )

    def get_vod_backgrounds(
        self,
        ondemand_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetVodBackgroundsErrorBody]:
        """This method returns every background image on the specified On Demand page. The authenticated user must be
        the owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_vod_backgrounds_error_mapper,
            request_options=request_options,
        )


class AsyncOnDemandBackgroundsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_vod_background(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateVodBackgroundErrorBody]:
        """This method adds a background image to the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=create_vod_background_error_mapper,
            request_options=request_options,
        )

    async def delete_vod_background(
        self, background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodBackgroundErrorBody]:
        """This method deletes the specified background image on an On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"),
            path_params=[param[float]("background_id", background_id), param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_vod_background_error_mapper,
            request_options=request_options,
        )

    async def edit_vod_background(
        self,
        background_id: float,
        ondemand_id: float,
        *,
        body: OndemandPagesBackgroundsRequest | OndemandPagesBackgroundsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, EditVodBackgroundErrorBody]:
        """This method edits the specified background image on an On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"),
            path_params=[param[float]("background_id", background_id), param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesBackgroundsRequest | OndemandPagesBackgroundsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=edit_vod_background_error_mapper,
            request_options=request_options,
        )

    async def get_vod_background(
        self, background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetVodBackgroundErrorBody]:
        """This method returns a single background image on the specified On Demand page. The authenticated user must be
        the owner of the page.

        Args:
            background_id: The ID of the background image.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds/{background_id}"),
            path_params=[param[float]("background_id", background_id), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=get_vod_background_error_mapper,
            request_options=request_options,
        )

    async def get_vod_backgrounds(
        self,
        ondemand_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetVodBackgroundsErrorBody]:
        """This method returns every background image on the specified On Demand page. The authenticated user must be
        the owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/backgrounds"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PictureConnection],
            error_mapper=get_vod_backgrounds_error_mapper,
            request_options=request_options,
        )
