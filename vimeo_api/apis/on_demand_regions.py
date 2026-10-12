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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.add_vod_region_error import AddVodRegionErrorBody, add_vod_region_error_mapper
from ..errors.delete_vod_region_error import DeleteVodRegionErrorBody, delete_vod_region_error_mapper
from ..errors.delete_vod_regions_error import DeleteVodRegionsErrorBody, delete_vod_regions_error_mapper
from ..errors.get_region_error import GetRegionErrorBody, get_region_error_mapper
from ..errors.get_vod_region_error import GetVodRegionErrorBody, get_vod_region_error_mapper
from ..errors.get_vod_regions_error import GetVodRegionsErrorBody, get_vod_regions_error_mapper
from ..errors.set_vod_regions_error import SetVodRegionsErrorBody, set_vod_regions_error_mapper
from ..models.on_demand_region import OnDemandRegion
from ..models.on_demand_region_connection import OnDemandRegionConnection
from ..models.ondemand_pages_regions_request import OndemandPagesRegionsRequest, OndemandPagesRegionsRequestDict
from ..models.ondemand_pages_regions_request1 import OndemandPagesRegionsRequest1, OndemandPagesRegionsRequest1Dict
from ..server.server import Server


class OnDemandRegions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandRegionsWithRawResponse(client, server, auth)

    def add_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandRegion:
        """This method adds a single region to the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            country: The country code of the region to add.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The region was added.

        Raises:
            ApiError: The authenticated user can't add regions to this On Demand page. No such On Demand page or region
                exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.add_vod_region(country, ondemand_id, request_options=request_options))

    def delete_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single region from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            country: The country code of the region to remove.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The region was removed.

        Raises:
            ApiError: The authenticated user can't remove regions from this On Demand page. No such On Demand page or
                region exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.delete_vod_region(country, ondemand_id, request_options=request_options))

    def delete_vod_regions(
        self,
        ondemand_id: float,
        *,
        body: OndemandPagesRegionsRequest | OndemandPagesRegionsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[OnDemandRegion]:
        """This method removes multiple regions from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The regions were removed.

        Raises:
            ApiError: The authenticated user can't remove regions from this On Demand page. No such On Demand page or
                region exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.delete_vod_regions(ondemand_id, body=body, request_options=request_options)
        )

    def get_region(self, country: str, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandRegion:
        """This method returns a single On Demand region.

        Args:
            country: The country code of the region to return.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The region was returned.

        Raises:
            ApiError: No such region exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.get_region(country, request_options=request_options))

    def get_regions(self, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandRegionConnection:
        """This method returns every existing On Demand region.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The regions were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_regions(request_options=request_options))

    def get_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandRegion:
        """This method returns a single region on the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            country: The country code of the region to return.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The region was returned.

        Raises:
            ApiError: No such On Demand page or region exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.get_vod_region(country, ondemand_id, request_options=request_options))

    def get_vod_regions(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandRegionConnection:
        """This method returns every region on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The regions were returned.

        Raises:
            ApiError: No such On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.get_vod_regions(ondemand_id, request_options=request_options))

    def set_vod_regions(
        self,
        ondemand_id: float,
        body: OndemandPagesRegionsRequest1 | OndemandPagesRegionsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandRegion:
        """This method adds multiple regions to the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The list of regions was added.

        Raises:
            ApiError: The authenticated user can't add regions to this On Demand page. No such On Demand page or region
                exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.set_vod_regions(ondemand_id, body, request_options=request_options))

    @property
    def with_raw_response(self) -> OnDemandRegionsWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandRegions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandRegionsWithRawResponse(client, server, auth)

    async def add_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandRegion:
        """This method adds a single region to the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            country: The country code of the region to add.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The region was added.

        Raises:
            ApiError: The authenticated user can't add regions to this On Demand page. No such On Demand page or region
                exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.add_vod_region(country, ondemand_id, request_options=request_options)
        )

    async def delete_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single region from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            country: The country code of the region to remove.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The region was removed.

        Raises:
            ApiError: The authenticated user can't remove regions from this On Demand page. No such On Demand page or
                region exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_vod_region(country, ondemand_id, request_options=request_options)
        )

    async def delete_vod_regions(
        self,
        ondemand_id: float,
        *,
        body: OndemandPagesRegionsRequest | OndemandPagesRegionsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[OnDemandRegion]:
        """This method removes multiple regions from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The regions were removed.

        Raises:
            ApiError: The authenticated user can't remove regions from this On Demand page. No such On Demand page or
                region exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_vod_regions(ondemand_id, body=body, request_options=request_options)
        )

    async def get_region(self, country: str, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandRegion:
        """This method returns a single On Demand region.

        Args:
            country: The country code of the region to return.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The region was returned.

        Raises:
            ApiError: No such region exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.get_region(country, request_options=request_options))

    async def get_regions(self, *, request_options: RequestOptionsOrDict | None = None) -> OnDemandRegionConnection:
        """This method returns every existing On Demand region.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The regions were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_regions(request_options=request_options))

    async def get_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandRegion:
        """This method returns a single region on the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            country: The country code of the region to return.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The region was returned.

        Raises:
            ApiError: No such On Demand page or region exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_vod_region(country, ondemand_id, request_options=request_options)
        )

    async def get_vod_regions(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandRegionConnection:
        """This method returns every region on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The regions were returned.

        Raises:
            ApiError: No such On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.get_vod_regions(ondemand_id, request_options=request_options))

    async def set_vod_regions(
        self,
        ondemand_id: float,
        body: OndemandPagesRegionsRequest1 | OndemandPagesRegionsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandRegion:
        """This method adds multiple regions to the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The list of regions was added.

        Raises:
            ApiError: The authenticated user can't add regions to this On Demand page. No such On Demand page or region
                exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.set_vod_regions(ondemand_id, body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncOnDemandRegionsWithRawResponse:
        return self._with_raw_response


class OnDemandRegionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegion, AddVodRegionErrorBody]:
        """This method adds a single region to the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            country: The country code of the region to add.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions/{country}"),
            path_params=[param[str]("country", country), param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandRegion],
            error_mapper=add_vod_region_error_mapper,
            request_options=request_options,
        )

    def delete_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodRegionErrorBody]:
        """This method removes a single region from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            country: The country code of the region to remove.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions/{country}"),
            path_params=[param[str]("country", country), param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_vod_region_error_mapper,
            request_options=request_options,
        )

    def delete_vod_regions(
        self,
        ondemand_id: float,
        *,
        body: OndemandPagesRegionsRequest | OndemandPagesRegionsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[OnDemandRegion], DeleteVodRegionsErrorBody]:
        """This method removes multiple regions from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesRegionsRequest | OndemandPagesRegionsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[OnDemandRegion]],
            error_mapper=delete_vod_regions_error_mapper,
            request_options=request_options,
        )

    def get_region(
        self, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegion, GetRegionErrorBody]:
        """This method returns a single On Demand region.

        Args:
            country: The country code of the region to return.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/regions/{country}"),
            path_params=[param[str]("country", country)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandRegion],
            error_mapper=get_region_error_mapper,
            request_options=request_options,
        )

    def get_regions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegionConnection, RawError]:
        """This method returns every existing On Demand region.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/regions"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandRegionConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegion, GetVodRegionErrorBody]:
        """This method returns a single region on the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            country: The country code of the region to return.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions/{country}"),
            path_params=[param[str]("country", country), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandRegion],
            error_mapper=get_vod_region_error_mapper,
            request_options=request_options,
        )

    def get_vod_regions(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegionConnection, GetVodRegionsErrorBody]:
        """This method returns every region on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandRegionConnection],
            error_mapper=get_vod_regions_error_mapper,
            request_options=request_options,
        )

    def set_vod_regions(
        self,
        ondemand_id: float,
        body: OndemandPagesRegionsRequest1 | OndemandPagesRegionsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandRegion, SetVodRegionsErrorBody]:
        """This method adds multiple regions to the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesRegionsRequest1 | OndemandPagesRegionsRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandRegion],
            error_mapper=set_vod_regions_error_mapper,
            request_options=request_options,
        )


class AsyncOnDemandRegionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegion, AddVodRegionErrorBody]:
        """This method adds a single region to the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            country: The country code of the region to add.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions/{country}"),
            path_params=[param[str]("country", country), param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandRegion],
            error_mapper=add_vod_region_error_mapper,
            request_options=request_options,
        )

    async def delete_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodRegionErrorBody]:
        """This method removes a single region from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            country: The country code of the region to remove.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions/{country}"),
            path_params=[param[str]("country", country), param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_vod_region_error_mapper,
            request_options=request_options,
        )

    async def delete_vod_regions(
        self,
        ondemand_id: float,
        *,
        body: OndemandPagesRegionsRequest | OndemandPagesRegionsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[OnDemandRegion], DeleteVodRegionsErrorBody]:
        """This method removes multiple regions from the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesRegionsRequest | OndemandPagesRegionsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[list[OnDemandRegion]],
            error_mapper=delete_vod_regions_error_mapper,
            request_options=request_options,
        )

    async def get_region(
        self, country: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegion, GetRegionErrorBody]:
        """This method returns a single On Demand region.

        Args:
            country: The country code of the region to return.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/regions/{country}"),
            path_params=[param[str]("country", country)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandRegion],
            error_mapper=get_region_error_mapper,
            request_options=request_options,
        )

    async def get_regions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegionConnection, RawError]:
        """This method returns every existing On Demand region.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/regions"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandRegionConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_vod_region(
        self, country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegion, GetVodRegionErrorBody]:
        """This method returns a single region on the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            country: The country code of the region to return.
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions/{country}"),
            path_params=[param[str]("country", country), param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandRegion],
            error_mapper=get_vod_region_error_mapper,
            request_options=request_options,
        )

    async def get_vod_regions(
        self, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandRegionConnection, GetVodRegionsErrorBody]:
        """This method returns every region on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandRegionConnection],
            error_mapper=get_vod_regions_error_mapper,
            request_options=request_options,
        )

    async def set_vod_regions(
        self,
        ondemand_id: float,
        body: OndemandPagesRegionsRequest1 | OndemandPagesRegionsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandRegion, SetVodRegionsErrorBody]:
        """This method adds multiple regions to the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/regions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesRegionsRequest1 | OndemandPagesRegionsRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandRegion],
            error_mapper=set_vod_regions_error_mapper,
            request_options=request_options,
        )
