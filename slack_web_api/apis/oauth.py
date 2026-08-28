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


class Oauth:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OauthWithRawResponse(client, server, auth)

    def oauth_access(
        self,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        single_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Exchanges a temporary OAuth verifier code for an access token.

        Args:
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            code: The ``code`` param returned via the OAuth callback.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            single_channel: Request the user to add your app only to a single channel. Only valid with a `legacy
                workspace app <https://api.slack.com/legacy-workspace-apps>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful user token negotiation for a single scope

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.oauth_access(
            content_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
            single_channel=single_channel,
            request_options=request_options,
        ).unwrap()

    def oauth_token(
        self,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        single_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Exchanges a temporary OAuth verifier code for a workspace token.

        Args:
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            code: The ``code`` param returned via the OAuth callback.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            single_channel: Request the user to add your app only to a single channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success example using a workspace app produces a very different kind of response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.oauth_token(
            content_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
            single_channel=single_channel,
            request_options=request_options,
        ).unwrap()

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
    def with_raw_response(self) -> OauthWithRawResponse:
        return self._with_raw_response


class AsyncOauth:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOauthWithRawResponse(client, server, auth)

    async def oauth_access(
        self,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        single_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Exchanges a temporary OAuth verifier code for an access token.

        Args:
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            code: The ``code`` param returned via the OAuth callback.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            single_channel: Request the user to add your app only to a single channel. Only valid with a `legacy
                workspace app <https://api.slack.com/legacy-workspace-apps>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful user token negotiation for a single scope

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.oauth_access(
                content_type,
                client_id=client_id,
                client_secret=client_secret,
                code=code,
                redirect_uri=redirect_uri,
                single_channel=single_channel,
                request_options=request_options,
            )
        ).unwrap()

    async def oauth_token(
        self,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        single_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Exchanges a temporary OAuth verifier code for a workspace token.

        Args:
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            code: The ``code`` param returned via the OAuth callback.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            single_channel: Request the user to add your app only to a single channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success example using a workspace app produces a very different kind of response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.oauth_token(
                content_type,
                client_id=client_id,
                client_secret=client_secret,
                code=code,
                redirect_uri=redirect_uri,
                single_channel=single_channel,
                request_options=request_options,
            )
        ).unwrap()

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
    def with_raw_response(self) -> AsyncOauthWithRawResponse:
        return self._with_raw_response


class OauthWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def oauth_access(
        self,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        single_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Exchanges a temporary OAuth verifier code for an access token.

        Args:
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            code: The ``code`` param returned via the OAuth callback.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            single_channel: Request the user to add your app only to a single channel. Only valid with a `legacy
                workspace app <https://api.slack.com/legacy-workspace-apps>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/oauth.access"),
            query_params=[
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
                param[str | None]("code", code),
                param[str | None]("redirect_uri", redirect_uri),
                param[bool | None]("single_channel", single_channel),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def oauth_token(
        self,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        single_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Exchanges a temporary OAuth verifier code for a workspace token.

        Args:
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            code: The ``code`` param returned via the OAuth callback.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            single_channel: Request the user to add your app only to a single channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/oauth.token"),
            query_params=[
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
                param[str | None]("code", code),
                param[str | None]("redirect_uri", redirect_uri),
                param[bool | None]("single_channel", single_channel),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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


class AsyncOauthWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def oauth_access(
        self,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        single_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Exchanges a temporary OAuth verifier code for an access token.

        Args:
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            code: The ``code`` param returned via the OAuth callback.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            single_channel: Request the user to add your app only to a single channel. Only valid with a `legacy
                workspace app <https://api.slack.com/legacy-workspace-apps>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/oauth.access"),
            query_params=[
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
                param[str | None]("code", code),
                param[str | None]("redirect_uri", redirect_uri),
                param[bool | None]("single_channel", single_channel),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def oauth_token(
        self,
        content_type: ContentTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        single_channel: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Exchanges a temporary OAuth verifier code for a workspace token.

        Args:
            content_type: Value sent with the request.
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            code: The ``code`` param returned via the OAuth callback.
            redirect_uri: This must match the originally submitted URI (if one was sent).
            single_channel: Request the user to add your app only to a single channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/oauth.token"),
            query_params=[
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
                param[str | None]("code", code),
                param[str | None]("redirect_uri", redirect_uri),
                param[bool | None]("single_channel", single_channel),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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
