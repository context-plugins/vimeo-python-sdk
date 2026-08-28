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
    json_body,
    json_decoder,
)
from ..errors.client_auth_error import ClientAuthErrorBody, client_auth_error_mapper
from ..models.auth_model import AuthModel
from ..models.oauth_authorize_client_request import OauthAuthorizeClientRequest, OauthAuthorizeClientRequestDict
from ..server.server import Server


class AuthenticationExtrasAuthenticate:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthenticationExtrasAuthenticateWithRawResponse(client, server, auth)

    def client_auth(
        self,
        body: OauthAuthorizeClientRequest | OauthAuthorizeClientRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthModel:
        """This method uses the OAuth protocol to authorize a client. For details on OAuth client authorization, see our
        `Working with Authentication </api/authentication>`__ guide or the `OAuth spec
        <https://tools.ietf.org/html/draft-ietf-oauth-v2-31#section-4.4>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authorization was successful.

        Raises:
            ApiError: Error code 8001: No such client secret exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.client_auth(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AuthenticationExtrasAuthenticateWithRawResponse:
        return self._with_raw_response


class AsyncAuthenticationExtrasAuthenticate:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthenticationExtrasAuthenticateWithRawResponse(client, server, auth)

    async def client_auth(
        self,
        body: OauthAuthorizeClientRequest | OauthAuthorizeClientRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthModel:
        """This method uses the OAuth protocol to authorize a client. For details on OAuth client authorization, see our
        `Working with Authentication </api/authentication>`__ guide or the `OAuth spec
        <https://tools.ietf.org/html/draft-ietf-oauth-v2-31#section-4.4>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authorization was successful.

        Raises:
            ApiError: Error code 8001: No such client secret exists. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.client_auth(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAuthenticationExtrasAuthenticateWithRawResponse:
        return self._with_raw_response


class AuthenticationExtrasAuthenticateWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def client_auth(
        self,
        body: OauthAuthorizeClientRequest | OauthAuthorizeClientRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthModel, ClientAuthErrorBody]:
        """This method uses the OAuth protocol to authorize a client. For details on OAuth client authorization, see our
        `Working with Authentication </api/authentication>`__ guide or the `OAuth spec
        <https://tools.ietf.org/html/draft-ietf-oauth-v2-31#section-4.4>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/authorize/client"),
            body=json_body[OauthAuthorizeClientRequest | OauthAuthorizeClientRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AuthModel],
            error_mapper=client_auth_error_mapper,
            request_options=request_options,
        )


class AsyncAuthenticationExtrasAuthenticateWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def client_auth(
        self,
        body: OauthAuthorizeClientRequest | OauthAuthorizeClientRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthModel, ClientAuthErrorBody]:
        """This method uses the OAuth protocol to authorize a client. For details on OAuth client authorization, see our
        `Working with Authentication </api/authentication>`__ guide or the `OAuth spec
        <https://tools.ietf.org/html/draft-ietf-oauth-v2-31#section-4.4>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/authorize/client"),
            body=json_body[OauthAuthorizeClientRequest | OauthAuthorizeClientRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AuthModel],
            error_mapper=client_auth_error_mapper,
            request_options=request_options,
        )
