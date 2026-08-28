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
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.delete_payment_method_error import DeletePaymentMethodErrorBody, delete_payment_method_error_mapper
from ..errors.get_payment_method_info_error import GetPaymentMethodInfoErrorBody, get_payment_method_info_error_mapper
from ..errors.list_payment_methods_error import ListPaymentMethodsErrorBody, list_payment_methods_error_mapper
from ..models.payment_method import PaymentMethod
from ..models.payment_method_connection import PaymentMethodConnection
from ..server.server import Server


class PaymentsEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentsEssentialsWithRawResponse(client, server, auth)

    def delete_payment_method(
        self, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified Vimeo payments service payment method.

        Args:
            payment_method_id: The ID of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The payments service payment method was deleted.

        Raises:
            ApiError: Error code 2204: No such payment method exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.delete_payment_method(
            payment_method_id, request_options=request_options
        ).unwrap()

    def get_payment_method_info(
        self, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentMethod:
        """This method returns information about the specified Vimeo payments service payment method.

        Args:
            payment_method_id: The ID of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The payments service payment method information was returned.

        Raises:
            ApiError: Error code 5000: No such payment method exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_payment_method_info(
            payment_method_id, request_options=request_options
        ).unwrap()

    def get_subscription_info(
        self, subscription_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns information about the specified Vimeo payments service subscription.

        Args:
            subscription_id: The ID of the subscription.
            user_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_subscription_info(
            subscription_id, user_id, request_options=request_options
        ).unwrap()

    def list_payment_methods(
        self,
        *,
        cardmember_name: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        show_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentMethodConnection:
        """This method returns a list of all Vimeo payments service payment methods that are available to the
        authenticated user.

        Args:
            cardmember_name: The name of the card member.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            show_disabled: Whether to return disabled payment methods.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of payments service payment methods was returned.

        Raises:
            ApiError: Error code 5000: A parameter is invalid. Error code 8000: The authenticated user can't make this
                request. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.list_payment_methods(
            cardmember_name=cardmember_name,
            page=page,
            per_page=per_page,
            show_disabled=show_disabled,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> PaymentsEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncPaymentsEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentsEssentialsWithRawResponse(client, server, auth)

    async def delete_payment_method(
        self, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified Vimeo payments service payment method.

        Args:
            payment_method_id: The ID of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The payments service payment method was deleted.

        Raises:
            ApiError: Error code 2204: No such payment method exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.delete_payment_method(payment_method_id, request_options=request_options)
        ).unwrap()

    async def get_payment_method_info(
        self, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentMethod:
        """This method returns information about the specified Vimeo payments service payment method.

        Args:
            payment_method_id: The ID of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The payments service payment method information was returned.

        Raises:
            ApiError: Error code 5000: No such payment method exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_payment_method_info(payment_method_id, request_options=request_options)
        ).unwrap()

    async def get_subscription_info(
        self, subscription_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns information about the specified Vimeo payments service subscription.

        Args:
            subscription_id: The ID of the subscription.
            user_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_subscription_info(
                subscription_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def list_payment_methods(
        self,
        *,
        cardmember_name: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        show_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentMethodConnection:
        """This method returns a list of all Vimeo payments service payment methods that are available to the
        authenticated user.

        Args:
            cardmember_name: The name of the card member.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            show_disabled: Whether to return disabled payment methods.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of payments service payment methods was returned.

        Raises:
            ApiError: Error code 5000: A parameter is invalid. Error code 8000: The authenticated user can't make this
                request. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.list_payment_methods(
                cardmember_name=cardmember_name,
                page=page,
                per_page=per_page,
                show_disabled=show_disabled,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPaymentsEssentialsWithRawResponse:
        return self._with_raw_response


class PaymentsEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_payment_method(
        self, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeletePaymentMethodErrorBody]:
        """This method deletes the specified Vimeo payments service payment method.

        Args:
            payment_method_id: The ID of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/payment_methods/{payment_method_id}"),
            path_params=[param[str]("payment_method_id", payment_method_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_payment_method_error_mapper,
            request_options=request_options,
        )

    def get_payment_method_info(
        self, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentMethod, GetPaymentMethodInfoErrorBody]:
        """This method returns information about the specified Vimeo payments service payment method.

        Args:
            payment_method_id: The ID of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/payment_methods/{payment_method_id}"),
            path_params=[param[str]("payment_method_id", payment_method_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PaymentMethod],
            error_mapper=get_payment_method_info_error_mapper,
            request_options=request_options,
        )

    def get_subscription_info(
        self, subscription_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns information about the specified Vimeo payments service subscription.

        Args:
            subscription_id: The ID of the subscription.
            user_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id), param[str]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_payment_methods(
        self,
        *,
        cardmember_name: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        show_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentMethodConnection, ListPaymentMethodsErrorBody]:
        """This method returns a list of all Vimeo payments service payment methods that are available to the
        authenticated user.

        Args:
            cardmember_name: The name of the card member.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            show_disabled: Whether to return disabled payment methods.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/payment_methods"),
            query_params=[
                param[str | None]("cardmember_name", cardmember_name),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[bool | None]("show_disabled", show_disabled),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PaymentMethodConnection],
            error_mapper=list_payment_methods_error_mapper,
            request_options=request_options,
        )


class AsyncPaymentsEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_payment_method(
        self, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeletePaymentMethodErrorBody]:
        """This method deletes the specified Vimeo payments service payment method.

        Args:
            payment_method_id: The ID of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/payment_methods/{payment_method_id}"),
            path_params=[param[str]("payment_method_id", payment_method_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_payment_method_error_mapper,
            request_options=request_options,
        )

    async def get_payment_method_info(
        self, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentMethod, GetPaymentMethodInfoErrorBody]:
        """This method returns information about the specified Vimeo payments service payment method.

        Args:
            payment_method_id: The ID of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/payment_methods/{payment_method_id}"),
            path_params=[param[str]("payment_method_id", payment_method_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PaymentMethod],
            error_mapper=get_payment_method_info_error_mapper,
            request_options=request_options,
        )

    async def get_subscription_info(
        self, subscription_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns information about the specified Vimeo payments service subscription.

        Args:
            subscription_id: The ID of the subscription.
            user_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id), param[str]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_payment_methods(
        self,
        *,
        cardmember_name: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        show_disabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentMethodConnection, ListPaymentMethodsErrorBody]:
        """This method returns a list of all Vimeo payments service payment methods that are available to the
        authenticated user.

        Args:
            cardmember_name: The name of the card member.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            show_disabled: Whether to return disabled payment methods.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/payment_methods"),
            query_params=[
                param[str | None]("cardmember_name", cardmember_name),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[bool | None]("show_disabled", show_disabled),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PaymentMethodConnection],
            error_mapper=list_payment_methods_error_mapper,
            request_options=request_options,
        )
