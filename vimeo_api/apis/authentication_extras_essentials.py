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
    json_decoder,
    param,
)
from ..errors.delete_token_error import DeleteTokenErrorBody, delete_token_error_mapper
from ..errors.verify_token_error import VerifyTokenErrorBody, verify_token_error_mapper
from ..models.auth_model import AuthModel
from ..server.server import Server


class AuthenticationExtrasEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthenticationExtrasEssentialsWithRawResponse(client, server, auth)

    def delete_token(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method revokes the access token that the requesting app is currently using. The token must be of the
        OAuth 2 type.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The token was revoked.

        Raises:
            ApiError: Access can't be revoked for an OAuth 1 token. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_token(request_options=request_options).unwrap()

    def verify_token(self, *, request_options: RequestOptionsOrDict | None = None) -> AuthModel:
        """This method verifies that an OAuth 2 access token exists.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The token was verified.

        Raises:
            ApiError: The token isn't a valid OAuth 2 token. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.verify_token(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AuthenticationExtrasEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncAuthenticationExtrasEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthenticationExtrasEssentialsWithRawResponse(client, server, auth)

    async def delete_token(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method revokes the access token that the requesting app is currently using. The token must be of the
        OAuth 2 type.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The token was revoked.

        Raises:
            ApiError: Access can't be revoked for an OAuth 1 token. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.delete_token(request_options=request_options)).unwrap()

    async def verify_token(self, *, request_options: RequestOptionsOrDict | None = None) -> AuthModel:
        """This method verifies that an OAuth 2 access token exists.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The token was verified.

        Raises:
            ApiError: The token isn't a valid OAuth 2 token. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.verify_token(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAuthenticationExtrasEssentialsWithRawResponse:
        return self._with_raw_response


class AuthenticationExtrasEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_token(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTokenErrorBody]:
        """This method revokes the access token that the requesting app is currently using. The token must be of the
        OAuth 2 type.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/tokens"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_token_error_mapper,
            request_options=request_options,
        )

    def verify_token(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AuthModel, VerifyTokenErrorBody]:
        """This method verifies that an OAuth 2 access token exists.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/oauth/verify"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AuthModel],
            error_mapper=verify_token_error_mapper,
            request_options=request_options,
        )


class AsyncAuthenticationExtrasEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_token(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTokenErrorBody]:
        """This method revokes the access token that the requesting app is currently using. The token must be of the
        OAuth 2 type.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/tokens"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_token_error_mapper,
            request_options=request_options,
        )

    async def verify_token(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AuthModel, VerifyTokenErrorBody]:
        """This method verifies that an OAuth 2 access token exists.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/oauth/verify"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AuthModel],
            error_mapper=verify_token_error_mapper,
            request_options=request_options,
        )
