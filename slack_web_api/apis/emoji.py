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


class Emoji:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmojiWithRawResponse(client, server, auth)

    def emoji_list(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Defaultsuccesstemplate:
        """Lists custom emoji for a team.

        Args:
            token: Authentication token. Requires scope: ``emoji:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.emoji_list(token, content_type, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> EmojiWithRawResponse:
        return self._with_raw_response


class AsyncEmoji:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmojiWithRawResponse(client, server, auth)

    async def emoji_list(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Defaultsuccesstemplate:
        """Lists custom emoji for a team.

        Args:
            token: Authentication token. Requires scope: ``emoji:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.emoji_list(token, content_type, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncEmojiWithRawResponse:
        return self._with_raw_response


class EmojiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def emoji_list(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Lists custom emoji for a team.

        Args:
            token: Authentication token. Requires scope: ``emoji:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/emoji.list"),
            query_params=[param[str]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEmojiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def emoji_list(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Lists custom emoji for a team.

        Args:
            token: Authentication token. Requires scope: ``emoji:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/emoji.list"),
            query_params=[param[str]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
