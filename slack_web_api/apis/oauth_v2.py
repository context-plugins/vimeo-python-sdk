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
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class OauthV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OauthV2WithRawResponse(client, server, auth)

    def oauth_v2_access(
        self,
        code: str,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        redirect_uri: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Exchanges a temporary OAuth verifier code for an access token.

        Args:
            code: The ``code`` param returned via the OAuth callback.
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful token request with scopes for both a bot user and a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.oauth_v2_access(
            code,
            content_type,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> OauthV2WithRawResponse:
        return self._with_raw_response


class AsyncOauthV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOauthV2WithRawResponse(client, server, auth)

    async def oauth_v2_access(
        self,
        code: str,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        redirect_uri: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Exchanges a temporary OAuth verifier code for an access token.

        Args:
            code: The ``code`` param returned via the OAuth callback.
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful token request with scopes for both a bot user and a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.oauth_v2_access(
                code,
                content_type,
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOauthV2WithRawResponse:
        return self._with_raw_response


class OauthV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def oauth_v2_access(
        self,
        code: str,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        redirect_uri: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Exchanges a temporary OAuth verifier code for an access token.

        Args:
            code: The ``code`` param returned via the OAuth callback.
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/oauth.v2.access"),
            query_params=[
                param[str]("code", code),
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
                param[str | None]("redirect_uri", redirect_uri),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncOauthV2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def oauth_v2_access(
        self,
        code: str,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        redirect_uri: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Exchanges a temporary OAuth verifier code for an access token.

        Args:
            code: The ``code`` param returned via the OAuth callback.
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/oauth.v2.access"),
            query_params=[
                param[str]("code", code),
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
                param[str | None]("redirect_uri", redirect_uri),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
