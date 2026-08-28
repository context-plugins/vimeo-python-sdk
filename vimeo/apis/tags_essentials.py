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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.tag import Tag
from ..server.server import Server


class TagsEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TagsEssentialsWithRawResponse(client, server, auth)

    def get_tag(self, word: str, *, request_options: RequestOptionsOrDict | None = None) -> Tag:
        """This method returns the specified tag.

        Args:
            word: The tag to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_tag(word, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TagsEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncTagsEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTagsEssentialsWithRawResponse(client, server, auth)

    async def get_tag(self, word: str, *, request_options: RequestOptionsOrDict | None = None) -> Tag:
        """This method returns the specified tag.

        Args:
            word: The tag to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_tag(word, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTagsEssentialsWithRawResponse:
        return self._with_raw_response


class TagsEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_tag(self, word: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Tag, RawError]:
        """This method returns the specified tag.

        Args:
            word: The tag to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tags/{word}"),
            path_params=[param[str]("word", word)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Tag],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTagsEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_tag(
        self, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Tag, RawError]:
        """This method returns the specified tag.

        Args:
            word: The tag to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tags/{word}"),
            path_params=[param[str]("word", word)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Tag],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
