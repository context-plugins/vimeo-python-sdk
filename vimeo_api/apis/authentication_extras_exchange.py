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
    json_body,
    json_decoder,
    param,
)
from ..errors.exchange_auth_code_error import ExchangeAuthCodeErrorBody, exchange_auth_code_error_mapper
from ..models.auth_model import AuthModel
from ..models.oauth_access_token_request import OauthAccessTokenRequest, OauthAccessTokenRequestDict
from ..server.server import Server


class AuthenticationExtrasExchange:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthenticationExtrasExchangeWithRawResponse(client, server, auth)

    def exchange_auth_code(
        self,
        body: OauthAccessTokenRequest | OauthAccessTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthModel:
        """This method exchanges an OAuth authorization code for an OAuth access token.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authorization code was exchanged.

        Raises:
            ApiError: * The grant type is invalid. * The authorization code is invalid. * The redirect URI doesn't match
                the URI to create the authorization code. ``error`` is ``AuthError | RawError``."""
        return self._with_raw_response.exchange_auth_code(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AuthenticationExtrasExchangeWithRawResponse:
        return self._with_raw_response


class AsyncAuthenticationExtrasExchange:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthenticationExtrasExchangeWithRawResponse(client, server, auth)

    async def exchange_auth_code(
        self,
        body: OauthAccessTokenRequest | OauthAccessTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthModel:
        """This method exchanges an OAuth authorization code for an OAuth access token.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authorization code was exchanged.

        Raises:
            ApiError: * The grant type is invalid. * The authorization code is invalid. * The redirect URI doesn't match
                the URI to create the authorization code. ``error`` is ``AuthError | RawError``."""
        return (await self._with_raw_response.exchange_auth_code(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAuthenticationExtrasExchangeWithRawResponse:
        return self._with_raw_response


class AuthenticationExtrasExchangeWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def exchange_auth_code(
        self,
        body: OauthAccessTokenRequest | OauthAccessTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthModel, ExchangeAuthCodeErrorBody]:
        """This method exchanges an OAuth authorization code for an OAuth access token.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/access_token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OauthAccessTokenRequest | OauthAccessTokenRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AuthModel],
            error_mapper=exchange_auth_code_error_mapper,
            request_options=request_options,
        )


class AsyncAuthenticationExtrasExchangeWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def exchange_auth_code(
        self,
        body: OauthAccessTokenRequest | OauthAccessTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthModel, ExchangeAuthCodeErrorBody]:
        """This method exchanges an OAuth authorization code for an OAuth access token.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/access_token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OauthAccessTokenRequest | OauthAccessTokenRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AuthModel],
            error_mapper=exchange_auth_code_error_mapper,
            request_options=request_options,
        )
