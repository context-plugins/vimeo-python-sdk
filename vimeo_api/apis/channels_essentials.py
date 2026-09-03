from __future__ import annotations

from uuid import UUID, uuid4

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
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.create_channel_error import CreateChannelErrorBody, create_channel_error_mapper
from ..errors.delete_channel_error import DeleteChannelErrorBody, delete_channel_error_mapper
from ..errors.edit_channel_error import EditChannelErrorBody, edit_channel_error_mapper
from ..errors.get_channel_subscriptions_alt1_error import (
    GetChannelSubscriptionsAlt1ErrorBody,
    get_channel_subscriptions_alt1_error_mapper,
)
from ..errors.get_channel_subscriptions_error import (
    GetChannelSubscriptionsErrorBody,
    get_channel_subscriptions_error_mapper,
)
from ..errors.get_channels_error import GetChannelsErrorBody, get_channels_error_mapper
from ..models.channel import Channel
from ..models.channel_connection import ChannelConnection
from ..models.channels_request import ChannelsRequest, ChannelsRequestDict
from ..models.channels_request1 import ChannelsRequest1, ChannelsRequest1Dict
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter1 import Filter1OrStr
from ..models.enums.filter12 import Filter12OrStr
from ..models.enums.sort4 import Sort4OrStr
from ..models.enums.sort7 import Sort7OrStr
from ..server.server import Server


class ChannelsEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChannelsEssentialsWithRawResponse(client, server, auth)

    def create_channel(
        self, body: ChannelsRequest | ChannelsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Channel:
        """This method creates a new channel.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was created.

        Raises:
            ApiError: A parameter is invalid. The authenticated user can't create channels. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.create_channel(body, request_options=request_options).unwrap()

    def delete_channel(self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the specified channel. The authenticated user must own the channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was deleted.

        Raises:
            ApiError: The authenticated user doesn't own this channel. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_channel(channel_id, request_options=request_options).unwrap()

    def edit_channel(
        self,
        channel_id: float,
        *,
        body: ChannelsRequest1 | ChannelsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Channel:
        """This method edits the specified channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was edited.

        Raises:
            ApiError: A parameter is invalid. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.edit_channel(channel_id, body=body, request_options=request_options).unwrap()

    def get_channel(
        self, channel_id: float, *, sizes: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Channel:
        """This method returns a single channel.

        Args:
            channel_id: The ID of the channel.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_channel(channel_id, sizes=sizes, request_options=request_options).unwrap()

    def get_channel_subscriptions(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChannelConnection:
        """This method returns all the channels to which the specified user subscribes.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_channel_subscriptions(
            user_id,
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_channel_subscriptions_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChannelConnection:
        """This method returns all the channels to which the specified user subscribes.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_channel_subscriptions_alt1(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_channels(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter1OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort7OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChannelConnection:
        """This method returns all available channels.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``featured`` - Return featured
                channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Sort the results by
                creation date. * ``followers`` - Sort the results by number of followers. * ``relevant`` - Sort the
                results by relevance. This option is available for search queries only. * ``videos`` - Sort the results
                by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: The relevant sort has no search query. Error code 5451: This resource is restricted in your
                region. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.get_channels(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ChannelsEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncChannelsEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChannelsEssentialsWithRawResponse(client, server, auth)

    async def create_channel(
        self, body: ChannelsRequest | ChannelsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Channel:
        """This method creates a new channel.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was created.

        Raises:
            ApiError: A parameter is invalid. The authenticated user can't create channels. ``error`` is ``LegacyError |
                RawError``."""
        return (await self._with_raw_response.create_channel(body, request_options=request_options)).unwrap()

    async def delete_channel(self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the specified channel. The authenticated user must own the channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was deleted.

        Raises:
            ApiError: The authenticated user doesn't own this channel. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.delete_channel(channel_id, request_options=request_options)).unwrap()

    async def edit_channel(
        self,
        channel_id: float,
        *,
        body: ChannelsRequest1 | ChannelsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Channel:
        """This method edits the specified channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was edited.

        Raises:
            ApiError: A parameter is invalid. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_channel(channel_id, body=body, request_options=request_options)
        ).unwrap()

    async def get_channel(
        self, channel_id: float, *, sizes: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Channel:
        """This method returns a single channel.

        Args:
            channel_id: The ID of the channel.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channel was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_channel(channel_id, sizes=sizes, request_options=request_options)
        ).unwrap()

    async def get_channel_subscriptions(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChannelConnection:
        """This method returns all the channels to which the specified user subscribes.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_channel_subscriptions(
                user_id,
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_channel_subscriptions_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChannelConnection:
        """This method returns all the channels to which the specified user subscribes.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_channel_subscriptions_alt1(
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_channels(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter1OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort7OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChannelConnection:
        """This method returns all available channels.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``featured`` - Return featured
                channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Sort the results by
                creation date. * ``followers`` - Sort the results by number of followers. * ``relevant`` - Sort the
                results by relevance. This option is available for search queries only. * ``videos`` - Sort the results
                by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: The relevant sort has no search query. Error code 5451: This resource is restricted in your
                region. ``error`` is ``LegacyError | Error | RawError``."""
        return (
            await self._with_raw_response.get_channels(
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncChannelsEssentialsWithRawResponse:
        return self._with_raw_response


class ChannelsEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_channel(
        self, body: ChannelsRequest | ChannelsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, CreateChannelErrorBody]:
        """This method creates a new channel.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsRequest | ChannelsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Channel],
            error_mapper=create_channel_error_mapper,
            request_options=request_options,
        )

    def delete_channel(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChannelErrorBody]:
        """This method deletes the specified channel. The authenticated user must own the channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_channel_error_mapper,
            request_options=request_options,
        )

    def edit_channel(
        self,
        channel_id: float,
        *,
        body: ChannelsRequest1 | ChannelsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Channel, EditChannelErrorBody]:
        """This method edits the specified channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsRequest1 | ChannelsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Channel],
            error_mapper=edit_channel_error_mapper,
            request_options=request_options,
        )

    def get_channel(
        self, channel_id: float, *, sizes: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, RawError]:
        """This method returns a single channel.

        Args:
            channel_id: The ID of the channel.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[param[str | None]("sizes", sizes)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Channel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_channel_subscriptions(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChannelConnection, GetChannelSubscriptionsErrorBody]:
        """This method returns all the channels to which the specified user subscribes.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/channels"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter12OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort4OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_channel_subscriptions_error_mapper,
            request_options=request_options,
        )

    def get_channel_subscriptions_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChannelConnection, GetChannelSubscriptionsAlt1ErrorBody]:
        """This method returns all the channels to which the specified user subscribes.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/channels"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter12OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort4OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_channel_subscriptions_alt1_error_mapper,
            request_options=request_options,
        )

    def get_channels(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter1OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort7OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChannelConnection, GetChannelsErrorBody]:
        """This method returns all available channels.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``featured`` - Return featured
                channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Sort the results by
                creation date. * ``followers`` - Sort the results by number of followers. * ``relevant`` - Sort the
                results by relevance. This option is available for search queries only. * ``videos`` - Sort the results
                by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter1OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort7OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_channels_error_mapper,
            request_options=request_options,
        )


class AsyncChannelsEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_channel(
        self, body: ChannelsRequest | ChannelsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, CreateChannelErrorBody]:
        """This method creates a new channel.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsRequest | ChannelsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Channel],
            error_mapper=create_channel_error_mapper,
            request_options=request_options,
        )

    async def delete_channel(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChannelErrorBody]:
        """This method deletes the specified channel. The authenticated user must own the channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_channel_error_mapper,
            request_options=request_options,
        )

    async def edit_channel(
        self,
        channel_id: float,
        *,
        body: ChannelsRequest1 | ChannelsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Channel, EditChannelErrorBody]:
        """This method edits the specified channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsRequest1 | ChannelsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Channel],
            error_mapper=edit_channel_error_mapper,
            request_options=request_options,
        )

    async def get_channel(
        self, channel_id: float, *, sizes: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, RawError]:
        """This method returns a single channel.

        Args:
            channel_id: The ID of the channel.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[param[str | None]("sizes", sizes)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Channel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_channel_subscriptions(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChannelConnection, GetChannelSubscriptionsErrorBody]:
        """This method returns all the channels to which the specified user subscribes.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/channels"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter12OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort4OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_channel_subscriptions_error_mapper,
            request_options=request_options,
        )

    async def get_channel_subscriptions_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort4OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChannelConnection, GetChannelSubscriptionsAlt1ErrorBody]:
        """This method returns all the channels to which the specified user subscribes.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/channels"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter12OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort4OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_channel_subscriptions_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_channels(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter1OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort7OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChannelConnection, GetChannelsErrorBody]:
        """This method returns all available channels.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``featured`` - Return featured
                channels.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Sort the results by
                creation date. * ``followers`` - Sort the results by number of followers. * ``relevant`` - Sort the
                results by relevance. This option is available for search queries only. * ``videos`` - Sort the results
                by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter1OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort7OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_channels_error_mapper,
            request_options=request_options,
        )
