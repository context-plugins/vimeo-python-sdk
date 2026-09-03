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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_vod_promotion_error import CreateVodPromotionErrorBody, create_vod_promotion_error_mapper
from ..errors.delete_vod_promotion_error import DeleteVodPromotionErrorBody, delete_vod_promotion_error_mapper
from ..errors.get_vod_promotion_codes_error import GetVodPromotionCodesErrorBody, get_vod_promotion_codes_error_mapper
from ..errors.get_vod_promotion_error import GetVodPromotionErrorBody, get_vod_promotion_error_mapper
from ..errors.get_vod_promotions_error import GetVodPromotionsErrorBody, get_vod_promotions_error_mapper
from ..models.enums.filter26 import Filter26OrStr
from ..models.on_demand_promotion import OnDemandPromotion
from ..models.on_demand_promotion_code import OnDemandPromotionCode
from ..models.ondemand_pages_promotions_request import (
    OndemandPagesPromotionsRequest,
    OndemandPagesPromotionsRequestDict,
)
from ..server.server import Server


class OnDemandPromotions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandPromotionsWithRawResponse(client, server, auth)

    def create_vod_promotion(
        self,
        ondemand_id: float,
        body: OndemandPagesPromotionsRequest | OndemandPagesPromotionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPromotion:
        """This method adds a promotion to the specified On Demand page. The authenticated user must be the owner of the
        page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The promotion was added.

        Raises:
            ApiError: There are errors in the request, or the promotion code already exists. The authenticated user
                can't add promotions to this On Demand page. No such On Demand page exists. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.create_vod_promotion(ondemand_id, body, request_options=request_options).unwrap()

    def delete_vod_promotion(
        self, ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a promotion on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The promotion was deleted.

        Raises:
            ApiError: The authenticated user can't delete promotions on this On Demand page. No such On Demand page or
                promotion exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_vod_promotion(
            ondemand_id, promotion_id, request_options=request_options
        ).unwrap()

    def get_vod_promotion(
        self, ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandPromotion:
        """This method returns a single promotion on the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The promotion was returned.

        Raises:
            ApiError: The authenticated user can't get promotions on this On Demand page. No such On Demand page or
                promotion exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_promotion(
            ondemand_id, promotion_id, request_options=request_options
        ).unwrap()

    def get_vod_promotion_codes(
        self,
        ondemand_id: float,
        promotion_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPromotionCode:
        """This method returns every code of the specified promotion on an On Demand page. The authenticated user must
        be the owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The codes were returned.

        Raises:
            ApiError: The authenticated user can't get promotions on this On Demand page. No such On Demand page or
                promotion exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_promotion_codes(
            ondemand_id, promotion_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_vod_promotions(
        self,
        ondemand_id: float,
        filter: Filter26OrStr,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPromotion:
        """This method returns every promotion on the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            filter: The type of filter to apply to the results. Option descriptions: * ``batch`` - Filter the results by
                the ``batch`` promotion. * ``default`` - Filter the results by the default promotion. * ``single`` -
                Filter the results by the ``single`` promotion. * ``vip`` - Filter the results by the ``vip`` promotion.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The promotions were returned.

        Raises:
            ApiError: The filter is invalid. The authenticated user can't get promotions on this On Demand page. No such
                On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_vod_promotions(
            ondemand_id, filter, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> OnDemandPromotionsWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandPromotions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandPromotionsWithRawResponse(client, server, auth)

    async def create_vod_promotion(
        self,
        ondemand_id: float,
        body: OndemandPagesPromotionsRequest | OndemandPagesPromotionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPromotion:
        """This method adds a promotion to the specified On Demand page. The authenticated user must be the owner of the
        page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The promotion was added.

        Raises:
            ApiError: There are errors in the request, or the promotion code already exists. The authenticated user
                can't add promotions to this On Demand page. No such On Demand page exists. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.create_vod_promotion(ondemand_id, body, request_options=request_options)
        ).unwrap()

    async def delete_vod_promotion(
        self, ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a promotion on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The promotion was deleted.

        Raises:
            ApiError: The authenticated user can't delete promotions on this On Demand page. No such On Demand page or
                promotion exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_vod_promotion(
                ondemand_id, promotion_id, request_options=request_options
            )
        ).unwrap()

    async def get_vod_promotion(
        self, ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OnDemandPromotion:
        """This method returns a single promotion on the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The promotion was returned.

        Raises:
            ApiError: The authenticated user can't get promotions on this On Demand page. No such On Demand page or
                promotion exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_vod_promotion(ondemand_id, promotion_id, request_options=request_options)
        ).unwrap()

    async def get_vod_promotion_codes(
        self,
        ondemand_id: float,
        promotion_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPromotionCode:
        """This method returns every code of the specified promotion on an On Demand page. The authenticated user must
        be the owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The codes were returned.

        Raises:
            ApiError: The authenticated user can't get promotions on this On Demand page. No such On Demand page or
                promotion exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_vod_promotion_codes(
                ondemand_id, promotion_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_vod_promotions(
        self,
        ondemand_id: float,
        filter: Filter26OrStr,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandPromotion:
        """This method returns every promotion on the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            filter: The type of filter to apply to the results. Option descriptions: * ``batch`` - Filter the results by
                the ``batch`` promotion. * ``default`` - Filter the results by the default promotion. * ``single`` -
                Filter the results by the ``single`` promotion. * ``vip`` - Filter the results by the ``vip`` promotion.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The promotions were returned.

        Raises:
            ApiError: The filter is invalid. The authenticated user can't get promotions on this On Demand page. No such
                On Demand page exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_vod_promotions(
                ondemand_id, filter, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOnDemandPromotionsWithRawResponse:
        return self._with_raw_response


class OnDemandPromotionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_vod_promotion(
        self,
        ondemand_id: float,
        body: OndemandPagesPromotionsRequest | OndemandPagesPromotionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPromotion, CreateVodPromotionErrorBody]:
        """This method adds a promotion to the specified On Demand page. The authenticated user must be the owner of the
        page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesPromotionsRequest | OndemandPagesPromotionsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPromotion],
            error_mapper=create_vod_promotion_error_mapper,
            request_options=request_options,
        )

    def delete_vod_promotion(
        self, ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodPromotionErrorBody]:
        """This method deletes a promotion on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions/{promotion_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("promotion_id", promotion_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_vod_promotion_error_mapper,
            request_options=request_options,
        )

    def get_vod_promotion(
        self, ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandPromotion, GetVodPromotionErrorBody]:
        """This method returns a single promotion on the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions/{promotion_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("promotion_id", promotion_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPromotion],
            error_mapper=get_vod_promotion_error_mapper,
            request_options=request_options,
        )

    def get_vod_promotion_codes(
        self,
        ondemand_id: float,
        promotion_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPromotionCode, GetVodPromotionCodesErrorBody]:
        """This method returns every code of the specified promotion on an On Demand page. The authenticated user must
        be the owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("promotion_id", promotion_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPromotionCode],
            error_mapper=get_vod_promotion_codes_error_mapper,
            request_options=request_options,
        )

    def get_vod_promotions(
        self,
        ondemand_id: float,
        filter: Filter26OrStr,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPromotion, GetVodPromotionsErrorBody]:
        """This method returns every promotion on the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            filter: The type of filter to apply to the results. Option descriptions: * ``batch`` - Filter the results by
                the ``batch`` promotion. * ``default`` - Filter the results by the default promotion. * ``single`` -
                Filter the results by the ``single`` promotion. * ``vip`` - Filter the results by the ``vip`` promotion.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[
                param[Filter26OrStr]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPromotion],
            error_mapper=get_vod_promotions_error_mapper,
            request_options=request_options,
        )


class AsyncOnDemandPromotionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_vod_promotion(
        self,
        ondemand_id: float,
        body: OndemandPagesPromotionsRequest | OndemandPagesPromotionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPromotion, CreateVodPromotionErrorBody]:
        """This method adds a promotion to the specified On Demand page. The authenticated user must be the owner of the
        page.

        Args:
            ondemand_id: The ID of the On Demand page.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesPromotionsRequest | OndemandPagesPromotionsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPromotion],
            error_mapper=create_vod_promotion_error_mapper,
            request_options=request_options,
        )

    async def delete_vod_promotion(
        self, ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVodPromotionErrorBody]:
        """This method deletes a promotion on the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions/{promotion_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("promotion_id", promotion_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_vod_promotion_error_mapper,
            request_options=request_options,
        )

    async def get_vod_promotion(
        self, ondemand_id: float, promotion_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnDemandPromotion, GetVodPromotionErrorBody]:
        """This method returns a single promotion on the specified On Demand page. The authenticated user must be the
        owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions/{promotion_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("promotion_id", promotion_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPromotion],
            error_mapper=get_vod_promotion_error_mapper,
            request_options=request_options,
        )

    async def get_vod_promotion_codes(
        self,
        ondemand_id: float,
        promotion_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPromotionCode, GetVodPromotionCodesErrorBody]:
        """This method returns every code of the specified promotion on an On Demand page. The authenticated user must
        be the owner of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            promotion_id: The ID of the promotion.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("promotion_id", promotion_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPromotionCode],
            error_mapper=get_vod_promotion_codes_error_mapper,
            request_options=request_options,
        )

    async def get_vod_promotions(
        self,
        ondemand_id: float,
        filter: Filter26OrStr,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandPromotion, GetVodPromotionsErrorBody]:
        """This method returns every promotion on the specified On Demand page. The authenticated user must be the owner
        of the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            filter: The type of filter to apply to the results. Option descriptions: * ``batch`` - Filter the results by
                the ``batch`` promotion. * ``default`` - Filter the results by the default promotion. * ``single`` -
                Filter the results by the ``single`` promotion. * ``vip`` - Filter the results by the ``vip`` promotion.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/promotions"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[
                param[Filter26OrStr]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandPromotion],
            error_mapper=get_vod_promotions_error_mapper,
            request_options=request_options,
        )
