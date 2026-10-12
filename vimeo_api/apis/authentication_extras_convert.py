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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.convert_access_token_error import ConvertAccessTokenErrorBody, convert_access_token_error_mapper
from ..models.auth_model import AuthModel
from ..models.oauth_authorize_vimeo_oauth1_request import (
    OauthAuthorizeVimeoOauth1Request,
    OauthAuthorizeVimeoOauth1RequestDict,
)
from ..server.server import Server


class AuthenticationExtrasConvert:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthenticationExtrasConvertWithRawResponse(client, server, auth)

    def convert_access_token(
        self,
        body: OauthAuthorizeVimeoOauth1Request | OauthAuthorizeVimeoOauth1RequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthModel:
        """This method exchanges a legacy Advanced API OAuth 1 token for an API v3 OAuth 2 token.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The token was converted.

        Raises:
            ApiError: * The token is invalid. * The token has unauthorized scopes. ``error`` is ``AuthError |
                RawError``."""
        return unwrap(self._with_raw_response.convert_access_token(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AuthenticationExtrasConvertWithRawResponse:
        return self._with_raw_response


class AsyncAuthenticationExtrasConvert:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthenticationExtrasConvertWithRawResponse(client, server, auth)

    async def convert_access_token(
        self,
        body: OauthAuthorizeVimeoOauth1Request | OauthAuthorizeVimeoOauth1RequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthModel:
        """This method exchanges a legacy Advanced API OAuth 1 token for an API v3 OAuth 2 token.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The token was converted.

        Raises:
            ApiError: * The token is invalid. * The token has unauthorized scopes. ``error`` is ``AuthError |
                RawError``."""
        return unwrap(await self._with_raw_response.convert_access_token(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncAuthenticationExtrasConvertWithRawResponse:
        return self._with_raw_response


class AuthenticationExtrasConvertWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def convert_access_token(
        self,
        body: OauthAuthorizeVimeoOauth1Request | OauthAuthorizeVimeoOauth1RequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthModel, ConvertAccessTokenErrorBody]:
        """This method exchanges a legacy Advanced API OAuth 1 token for an API v3 OAuth 2 token.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/authorize/vimeo_oauth1"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OauthAuthorizeVimeoOauth1Request | OauthAuthorizeVimeoOauth1RequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AuthModel],
            error_mapper=convert_access_token_error_mapper,
            request_options=request_options,
        )


class AsyncAuthenticationExtrasConvertWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def convert_access_token(
        self,
        body: OauthAuthorizeVimeoOauth1Request | OauthAuthorizeVimeoOauth1RequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthModel, ConvertAccessTokenErrorBody]:
        """This method exchanges a legacy Advanced API OAuth 1 token for an API v3 OAuth 2 token.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/authorize/vimeo_oauth1"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OauthAuthorizeVimeoOauth1Request | OauthAuthorizeVimeoOauth1RequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[AuthModel],
            error_mapper=convert_access_token_error_mapper,
            request_options=request_options,
        )
