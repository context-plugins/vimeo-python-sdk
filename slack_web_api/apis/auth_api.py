from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.auth_revokeschema import AuthRevokeschema
from ..models.auth_testsuccessschema import AuthTestsuccessschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class AuthApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthApiWithRawResponse(client, server, auth)

    def auth_revoke(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        test: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthRevokeschema:
        """Revokes a token.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            test: Setting this parameter to ``1`` triggers a _testing mode_ where the specified token will not actually
                be revoked.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.auth_revoke(
            token, content_type, test=test, request_options=request_options
        ).unwrap()

    def auth_test(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> AuthTestsuccessschema:
        """Checks authentication & identity.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.auth_test(token, content_type, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AuthApiWithRawResponse:
        return self._with_raw_response


class AsyncAuthApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthApiWithRawResponse(client, server, auth)

    async def auth_revoke(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        test: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthRevokeschema:
        """Revokes a token.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            test: Setting this parameter to ``1`` triggers a _testing mode_ where the specified token will not actually
                be revoked.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.auth_revoke(token, content_type, test=test, request_options=request_options)
        ).unwrap()

    async def auth_test(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> AuthTestsuccessschema:
        """Checks authentication & identity.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.auth_test(token, content_type, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAuthApiWithRawResponse:
        return self._with_raw_response


class AuthApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def auth_revoke(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        test: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthRevokeschema, RawError]:
        """Revokes a token.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            test: Setting this parameter to ``1`` triggers a _testing mode_ where the specified token will not actually
                be revoked.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/auth.revoke"),
            query_params=[param[str]("token", token), param[bool | None]("test", test)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AuthRevokeschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def auth_test(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AuthTestsuccessschema, RawError]:
        """Checks authentication & identity.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/auth.test"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AuthTestsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAuthApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def auth_revoke(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        test: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthRevokeschema, RawError]:
        """Revokes a token.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            test: Setting this parameter to ``1`` triggers a _testing mode_ where the specified token will not actually
                be revoked.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/auth.revoke"),
            query_params=[param[str]("token", token), param[bool | None]("test", test)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AuthRevokeschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def auth_test(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AuthTestsuccessschema, RawError]:
        """Checks authentication & identity.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/auth.test"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AuthTestsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
