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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.add_channel_categories_error import AddChannelCategoriesErrorBody, add_channel_categories_error_mapper
from ..errors.categorize_channel_error import CategorizeChannelErrorBody, categorize_channel_error_mapper
from ..errors.delete_channel_category_error import DeleteChannelCategoryErrorBody, delete_channel_category_error_mapper
from ..errors.get_channel_categories_error import GetChannelCategoriesErrorBody, get_channel_categories_error_mapper
from ..models.category_connection import CategoryConnection
from ..models.channels_categories_request import ChannelsCategoriesRequest, ChannelsCategoriesRequestDict
from ..server.server import Server


class ChannelsCategories:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChannelsCategoriesWithRawResponse(client, server, auth)

    def add_channel_categories(
        self,
        channel_id: float,
        body: ChannelsCategoriesRequest | ChannelsCategoriesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds the specified channel to multiple categories.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was added to the categories.

        Raises:
            ApiError: * Error code 2204: You exceeded the maximum number of channel categories. * Error code 2205: There
                was no request body, or the request body is malformed. Error code 8003: The user credentials are
                invalid. Error code 3200: The authenticated user can't add categories to the channel. No such channel
                exists. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.add_channel_categories(
            channel_id, body, request_options=request_options
        ).unwrap()

    def categorize_channel(
        self, category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the specified channel to a single category. The authenticated user must be the owner of the
        channel.

        Args:
            category: The name of the category.
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was added to the category.

        Raises:
            ApiError: Error code 2204: You exceeded the maximum number of channel categories. Error code 8003: The user
                credentials are invalid. Error code 3200: The authenticated user doesn't own the channel or isn't a
                channel moderator. No such channel or category exists. ``error`` is ``Error | LegacyError |
                RawError``."""
        return self._with_raw_response.categorize_channel(
            category, channel_id, request_options=request_options
        ).unwrap()

    def delete_channel_category(
        self, category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a channel from the specified category. The authenticated user must be the owner of the
        channel.

        Args:
            category: The name of the category.
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was removed.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user doesn't
                own the channel or isn't a channel moderator. No such channel or category exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.delete_channel_category(
            category, channel_id, request_options=request_options
        ).unwrap()

    def get_channel_categories(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> CategoryConnection:
        """This method returns every category to which the specified channel belongs.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were returned.

        Raises:
            ApiError: * No such channel exists. * Error code 5451: This resource is restricted in your region. ``error``
                is ``LegacyError | RawError``."""
        return self._with_raw_response.get_channel_categories(channel_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ChannelsCategoriesWithRawResponse:
        return self._with_raw_response


class AsyncChannelsCategories:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChannelsCategoriesWithRawResponse(client, server, auth)

    async def add_channel_categories(
        self,
        channel_id: float,
        body: ChannelsCategoriesRequest | ChannelsCategoriesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds the specified channel to multiple categories.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was added to the categories.

        Raises:
            ApiError: * Error code 2204: You exceeded the maximum number of channel categories. * Error code 2205: There
                was no request body, or the request body is malformed. Error code 8003: The user credentials are
                invalid. Error code 3200: The authenticated user can't add categories to the channel. No such channel
                exists. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_channel_categories(channel_id, body, request_options=request_options)
        ).unwrap()

    async def categorize_channel(
        self, category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the specified channel to a single category. The authenticated user must be the owner of the
        channel.

        Args:
            category: The name of the category.
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was added to the category.

        Raises:
            ApiError: Error code 2204: You exceeded the maximum number of channel categories. Error code 8003: The user
                credentials are invalid. Error code 3200: The authenticated user doesn't own the channel or isn't a
                channel moderator. No such channel or category exists. ``error`` is ``Error | LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.categorize_channel(category, channel_id, request_options=request_options)
        ).unwrap()

    async def delete_channel_category(
        self, category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a channel from the specified category. The authenticated user must be the owner of the
        channel.

        Args:
            category: The name of the category.
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was removed.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user doesn't
                own the channel or isn't a channel moderator. No such channel or category exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_channel_category(category, channel_id, request_options=request_options)
        ).unwrap()

    async def get_channel_categories(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> CategoryConnection:
        """This method returns every category to which the specified channel belongs.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were returned.

        Raises:
            ApiError: * No such channel exists. * Error code 5451: This resource is restricted in your region. ``error``
                is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_channel_categories(channel_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncChannelsCategoriesWithRawResponse:
        return self._with_raw_response


class ChannelsCategoriesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_channel_categories(
        self,
        channel_id: float,
        body: ChannelsCategoriesRequest | ChannelsCategoriesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddChannelCategoriesErrorBody]:
        """This method adds the specified channel to multiple categories.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/categories"),
            path_params=[param[float]("channel_id", channel_id)],
            body=json_body[ChannelsCategoriesRequest | ChannelsCategoriesRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_channel_categories_error_mapper,
            request_options=request_options,
        )

    def categorize_channel(
        self, category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CategorizeChannelErrorBody]:
        """This method adds the specified channel to a single category. The authenticated user must be the owner of the
        channel.

        Args:
            category: The name of the category.
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("channel_id", channel_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=categorize_channel_error_mapper,
            request_options=request_options,
        )

    def delete_channel_category(
        self, category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChannelCategoryErrorBody]:
        """This method removes a channel from the specified category. The authenticated user must be the owner of the
        channel.

        Args:
            category: The name of the category.
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("channel_id", channel_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_channel_category_error_mapper,
            request_options=request_options,
        )

    def get_channel_categories(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoryConnection, GetChannelCategoriesErrorBody]:
        """This method returns every category to which the specified channel belongs.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/categories"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=get_channel_categories_error_mapper,
            request_options=request_options,
        )


class AsyncChannelsCategoriesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_channel_categories(
        self,
        channel_id: float,
        body: ChannelsCategoriesRequest | ChannelsCategoriesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddChannelCategoriesErrorBody]:
        """This method adds the specified channel to multiple categories.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/categories"),
            path_params=[param[float]("channel_id", channel_id)],
            body=json_body[ChannelsCategoriesRequest | ChannelsCategoriesRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_channel_categories_error_mapper,
            request_options=request_options,
        )

    async def categorize_channel(
        self, category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CategorizeChannelErrorBody]:
        """This method adds the specified channel to a single category. The authenticated user must be the owner of the
        channel.

        Args:
            category: The name of the category.
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("channel_id", channel_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=categorize_channel_error_mapper,
            request_options=request_options,
        )

    async def delete_channel_category(
        self, category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChannelCategoryErrorBody]:
        """This method removes a channel from the specified category. The authenticated user must be the owner of the
        channel.

        Args:
            category: The name of the category.
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("channel_id", channel_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_channel_category_error_mapper,
            request_options=request_options,
        )

    async def get_channel_categories(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoryConnection, GetChannelCategoriesErrorBody]:
        """This method returns every category to which the specified channel belongs.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/categories"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=get_channel_categories_error_mapper,
            request_options=request_options,
        )
