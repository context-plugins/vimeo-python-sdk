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
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.tag_model import TagModel
from ..server.server import Server


class TagsEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TagsEssentialsWithRawResponse(client, server, auth)

    def get_tag(self, word: str, *, request_options: RequestOptionsOrDict | None = None) -> TagModel:
        """This method returns the specified tag.

        Args:
            word: The tag to return.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The tag was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_tag(word, request_options=request_options))

    @property
    def with_raw_response(self) -> TagsEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncTagsEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTagsEssentialsWithRawResponse(client, server, auth)

    async def get_tag(self, word: str, *, request_options: RequestOptionsOrDict | None = None) -> TagModel:
        """This method returns the specified tag.

        Args:
            word: The tag to return.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The tag was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_tag(word, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncTagsEssentialsWithRawResponse:
        return self._with_raw_response


class TagsEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_tag(
        self, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagModel, RawError]:
        """This method returns the specified tag.

        Args:
            word: The tag to return.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tags/{word}"),
            path_params=[param[str]("word", word)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TagModel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTagsEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_tag(
        self, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagModel, RawError]:
        """This method returns the specified tag.

        Args:
            word: The tag to return.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tags/{word}"),
            path_params=[param[str]("word", word)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[TagModel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
