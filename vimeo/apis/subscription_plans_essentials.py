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
    empty_response,
    param,
    raw_error_response,
)
from ..models.enums.tier1 import Tier1OrStr
from ..server.server import Server


class SubscriptionPlansEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionPlansEssentialsWithRawResponse(client, server, auth)

    def get_plan(self, tier: Tier1OrStr, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns the specified subscription plan.

        Args:
            tier: The type of subscription plan. Option descriptions: * ``advanced`` - The plan type is Vimeo Advanced.
                * ``business`` - The plan type is Vimeo Business. * ``free`` - The plan type is Vimeo Free. *
                ``live_premium`` - The plan type is Vimeo Premium. * ``plus`` - The plan type is Vimeo Plus. * ``pro`` -
                The plan type is Vimeo Pro. * ``pro_unlimited`` - The plan type is Vimeo Pro Unlimited. * ``standard`` -
                The plan type is Vimeo Standard. * ``starter`` - The plan type is Vimeo Starter.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_plan(tier, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SubscriptionPlansEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionPlansEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionPlansEssentialsWithRawResponse(client, server, auth)

    async def get_plan(self, tier: Tier1OrStr, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns the specified subscription plan.

        Args:
            tier: The type of subscription plan. Option descriptions: * ``advanced`` - The plan type is Vimeo Advanced.
                * ``business`` - The plan type is Vimeo Business. * ``free`` - The plan type is Vimeo Free. *
                ``live_premium`` - The plan type is Vimeo Premium. * ``plus`` - The plan type is Vimeo Plus. * ``pro`` -
                The plan type is Vimeo Pro. * ``pro_unlimited`` - The plan type is Vimeo Pro Unlimited. * ``standard`` -
                The plan type is Vimeo Standard. * ``starter`` - The plan type is Vimeo Starter.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_plan(tier, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSubscriptionPlansEssentialsWithRawResponse:
        return self._with_raw_response


class SubscriptionPlansEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_plan(
        self, tier: Tier1OrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns the specified subscription plan.

        Args:
            tier: The type of subscription plan. Option descriptions: * ``advanced`` - The plan type is Vimeo Advanced.
                * ``business`` - The plan type is Vimeo Business. * ``free`` - The plan type is Vimeo Free. *
                ``live_premium`` - The plan type is Vimeo Premium. * ``plus`` - The plan type is Vimeo Plus. * ``pro`` -
                The plan type is Vimeo Pro. * ``pro_unlimited`` - The plan type is Vimeo Pro Unlimited. * ``standard`` -
                The plan type is Vimeo Standard. * ``starter`` - The plan type is Vimeo Starter.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/subscription_plans/{tier}"),
            path_params=[param[Tier1OrStr]("tier", tier)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSubscriptionPlansEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_plan(
        self, tier: Tier1OrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns the specified subscription plan.

        Args:
            tier: The type of subscription plan. Option descriptions: * ``advanced`` - The plan type is Vimeo Advanced.
                * ``business`` - The plan type is Vimeo Business. * ``free`` - The plan type is Vimeo Free. *
                ``live_premium`` - The plan type is Vimeo Premium. * ``plus`` - The plan type is Vimeo Plus. * ``pro`` -
                The plan type is Vimeo Pro. * ``pro_unlimited`` - The plan type is Vimeo Pro Unlimited. * ``standard`` -
                The plan type is Vimeo Standard. * ``starter`` - The plan type is Vimeo Starter.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/subscription_plans/{tier}"),
            path_params=[param[Tier1OrStr]("tier", tier)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
