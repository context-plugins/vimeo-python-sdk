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
    json_body,
    json_decoder,
    param,
)
from ..errors.add_channel_tag_error import AddChannelTagErrorBody, add_channel_tag_error_mapper
from ..errors.add_tags_to_channel_error import AddTagsToChannelErrorBody, add_tags_to_channel_error_mapper
from ..errors.check_if_channel_has_tag_error import CheckIfChannelHasTagErrorBody, check_if_channel_has_tag_error_mapper
from ..errors.delete_tag_from_channel_error import DeleteTagFromChannelErrorBody, delete_tag_from_channel_error_mapper
from ..errors.get_channel_tags_error import GetChannelTagsErrorBody, get_channel_tags_error_mapper
from ..models.channels_tags_request import ChannelsTagsRequest, ChannelsTagsRequestDict
from ..models.tag import Tag
from ..models.tag_connection import TagConnection
from ..server.server import Server


class ChannelsTags:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChannelsTagsWithRawResponse(client, server, auth)

    def add_channel_tag(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single tag to the specified channel. The authenticated user must be the owner of the
        channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was added.

        Raises:
            ApiError: * The tag is invalid, or a parameter is invalid. * Error code 2501: The channel can't have more
                than 20 tags. Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user
                can't add tags to this channel. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.add_channel_tag(channel_id, word, request_options=request_options).unwrap()

    def add_tags_to_channel(
        self,
        channel_id: float,
        body: list[ChannelsTagsRequest | ChannelsTagsRequestDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Tag]:
        """This method adds multiple tags to the specified channel. Include the tags as a JSON array in the body of the
        request using the **tag** field, like this: ``[{ "tag": "funny" }, { "tag": "concert" }]``. The authenticated
        user must be the owner of the channel. For more information on batch requests like this one, see `Using Common
        Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tags were added.

        Raises:
            ApiError: * No such channel exists, or a parameter is invalid. * Error code 2205: There was no request body,
                or the request body is malformed. * Error code 2501: The channel can't have more than 20 tags. Error
                code 8003: The user credentials are invalid. Error code 3200: The authenticated user can't add tags to
                this channel. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.add_tags_to_channel(channel_id, body, request_options=request_options).unwrap()

    def check_if_channel_has_tag(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether a tag has been added to the specified channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag has been added to the channel.

        Raises:
            ApiError: No such tag exists. Error code 5000: The tag exists, but the channel isn't tagged by it. ``error``
                is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.check_if_channel_has_tag(
            channel_id, word, request_options=request_options
        ).unwrap()

    def delete_tag_from_channel(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single tag from the specified channel. The authenticated user must be the owner of the
        channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was removed.

        Raises:
            ApiError: The tag is invalid, or a parameter is invalid. Error code 8003: The user credentials are invalid.
                Error code 3200: The authenticated user can't remove tags from this channel. ``error`` is ``LegacyError
                | Error | RawError``."""
        return self._with_raw_response.delete_tag_from_channel(
            channel_id, word, request_options=request_options
        ).unwrap()

    def get_channel_tags(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> TagConnection:
        """This method returns every tag that has been added to the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tags were returned.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_channel_tags(channel_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ChannelsTagsWithRawResponse:
        return self._with_raw_response


class AsyncChannelsTags:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChannelsTagsWithRawResponse(client, server, auth)

    async def add_channel_tag(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single tag to the specified channel. The authenticated user must be the owner of the
        channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was added.

        Raises:
            ApiError: * The tag is invalid, or a parameter is invalid. * Error code 2501: The channel can't have more
                than 20 tags. Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user
                can't add tags to this channel. ``error`` is ``LegacyError | Error | RawError``."""
        return (
            await self._with_raw_response.add_channel_tag(channel_id, word, request_options=request_options)
        ).unwrap()

    async def add_tags_to_channel(
        self,
        channel_id: float,
        body: list[ChannelsTagsRequest | ChannelsTagsRequestDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Tag]:
        """This method adds multiple tags to the specified channel. Include the tags as a JSON array in the body of the
        request using the **tag** field, like this: ``[{ "tag": "funny" }, { "tag": "concert" }]``. The authenticated
        user must be the owner of the channel. For more information on batch requests like this one, see `Using Common
        Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tags were added.

        Raises:
            ApiError: * No such channel exists, or a parameter is invalid. * Error code 2205: There was no request body,
                or the request body is malformed. * Error code 2501: The channel can't have more than 20 tags. Error
                code 8003: The user credentials are invalid. Error code 3200: The authenticated user can't add tags to
                this channel. ``error`` is ``LegacyError | Error | RawError``."""
        return (
            await self._with_raw_response.add_tags_to_channel(channel_id, body, request_options=request_options)
        ).unwrap()

    async def check_if_channel_has_tag(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether a tag has been added to the specified channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag has been added to the channel.

        Raises:
            ApiError: No such tag exists. Error code 5000: The tag exists, but the channel isn't tagged by it. ``error``
                is ``LegacyError | Error | RawError``."""
        return (
            await self._with_raw_response.check_if_channel_has_tag(channel_id, word, request_options=request_options)
        ).unwrap()

    async def delete_tag_from_channel(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single tag from the specified channel. The authenticated user must be the owner of the
        channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was removed.

        Raises:
            ApiError: The tag is invalid, or a parameter is invalid. Error code 8003: The user credentials are invalid.
                Error code 3200: The authenticated user can't remove tags from this channel. ``error`` is ``LegacyError
                | Error | RawError``."""
        return (
            await self._with_raw_response.delete_tag_from_channel(channel_id, word, request_options=request_options)
        ).unwrap()

    async def get_channel_tags(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> TagConnection:
        """This method returns every tag that has been added to the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tags were returned.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.get_channel_tags(channel_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncChannelsTagsWithRawResponse:
        return self._with_raw_response


class ChannelsTagsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_channel_tag(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddChannelTagErrorBody]:
        """This method adds a single tag to the specified channel. The authenticated user must be the owner of the
        channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/tags/{word}"),
            path_params=[param[float]("channel_id", channel_id), param[str]("word", word)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_channel_tag_error_mapper,
            request_options=request_options,
        )

    def add_tags_to_channel(
        self,
        channel_id: float,
        body: list[ChannelsTagsRequest | ChannelsTagsRequestDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Tag], AddTagsToChannelErrorBody]:
        """This method adds multiple tags to the specified channel. Include the tags as a JSON array in the body of the
        request using the **tag** field, like this: ``[{ "tag": "funny" }, { "tag": "concert" }]``. The authenticated
        user must be the owner of the channel. For more information on batch requests like this one, see `Using Common
        Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/tags"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[ChannelsTagsRequest | ChannelsTagsRequestDict]](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[Tag]],
            error_mapper=add_tags_to_channel_error_mapper,
            request_options=request_options,
        )

    def check_if_channel_has_tag(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfChannelHasTagErrorBody]:
        """This method determines whether a tag has been added to the specified channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/tags/{word}"),
            path_params=[param[float]("channel_id", channel_id), param[str]("word", word)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_channel_has_tag_error_mapper,
            request_options=request_options,
        )

    def delete_tag_from_channel(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTagFromChannelErrorBody]:
        """This method removes a single tag from the specified channel. The authenticated user must be the owner of the
        channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/tags/{word}"),
            path_params=[param[float]("channel_id", channel_id), param[str]("word", word)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_tag_from_channel_error_mapper,
            request_options=request_options,
        )

    def get_channel_tags(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagConnection, GetChannelTagsErrorBody]:
        """This method returns every tag that has been added to the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/tags"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TagConnection],
            error_mapper=get_channel_tags_error_mapper,
            request_options=request_options,
        )


class AsyncChannelsTagsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_channel_tag(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddChannelTagErrorBody]:
        """This method adds a single tag to the specified channel. The authenticated user must be the owner of the
        channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/tags/{word}"),
            path_params=[param[float]("channel_id", channel_id), param[str]("word", word)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_channel_tag_error_mapper,
            request_options=request_options,
        )

    async def add_tags_to_channel(
        self,
        channel_id: float,
        body: list[ChannelsTagsRequest | ChannelsTagsRequestDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Tag], AddTagsToChannelErrorBody]:
        """This method adds multiple tags to the specified channel. Include the tags as a JSON array in the body of the
        request using the **tag** field, like this: ``[{ "tag": "funny" }, { "tag": "concert" }]``. The authenticated
        user must be the owner of the channel. For more information on batch requests like this one, see `Using Common
        Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/tags"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[ChannelsTagsRequest | ChannelsTagsRequestDict]](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[Tag]],
            error_mapper=add_tags_to_channel_error_mapper,
            request_options=request_options,
        )

    async def check_if_channel_has_tag(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfChannelHasTagErrorBody]:
        """This method determines whether a tag has been added to the specified channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/tags/{word}"),
            path_params=[param[float]("channel_id", channel_id), param[str]("word", word)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_channel_has_tag_error_mapper,
            request_options=request_options,
        )

    async def delete_tag_from_channel(
        self, channel_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTagFromChannelErrorBody]:
        """This method removes a single tag from the specified channel. The authenticated user must be the owner of the
        channel.

        Args:
            channel_id: The ID of the channel.
            word: The word to use as the tag.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/tags/{word}"),
            path_params=[param[float]("channel_id", channel_id), param[str]("word", word)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_tag_from_channel_error_mapper,
            request_options=request_options,
        )

    async def get_channel_tags(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagConnection, GetChannelTagsErrorBody]:
        """This method returns every tag that has been added to the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/tags"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TagConnection],
            error_mapper=get_channel_tags_error_mapper,
            request_options=request_options,
        )
