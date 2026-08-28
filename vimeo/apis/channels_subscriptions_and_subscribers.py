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
    json_decoder,
    param,
)
from ..errors.check_if_user_subscribed_to_channel_alt1_error import (
    CheckIfUserSubscribedToChannelAlt1ErrorBody,
    check_if_user_subscribed_to_channel_alt1_error_mapper,
)
from ..errors.check_if_user_subscribed_to_channel_error import (
    CheckIfUserSubscribedToChannelErrorBody,
    check_if_user_subscribed_to_channel_error_mapper,
)
from ..errors.get_channel_subscribers_error import GetChannelSubscribersErrorBody, get_channel_subscribers_error_mapper
from ..errors.subscribe_to_channel_alt1_error import (
    SubscribeToChannelAlt1ErrorBody,
    subscribe_to_channel_alt1_error_mapper,
)
from ..errors.subscribe_to_channel_error import SubscribeToChannelErrorBody, subscribe_to_channel_error_mapper
from ..errors.unsubscribe_from_channel_alt1_error import (
    UnsubscribeFromChannelAlt1ErrorBody,
    unsubscribe_from_channel_alt1_error_mapper,
)
from ..errors.unsubscribe_from_channel_error import (
    UnsubscribeFromChannelErrorBody,
    unsubscribe_from_channel_error_mapper,
)
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter2 import Filter2OrStr
from ..models.enums.sort8 import Sort8OrStr
from ..models.user_connection import UserConnection
from ..server.server import Server


class ChannelsSubscriptionsAndSubscribers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChannelsSubscriptionsAndSubscribersWithRawResponse(client, server, auth)

    def check_if_user_subscribed_to_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the specified user is a follower of a particular channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user follows the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.check_if_user_subscribed_to_channel(
            channel_id, user_id, request_options=request_options
        ).unwrap()

    def check_if_user_subscribed_to_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the specified user is a follower of a particular channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user follows the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.check_if_user_subscribed_to_channel_alt1(
            channel_id, request_options=request_options
        ).unwrap()

    def get_channel_subscribers(
        self,
        channel_id: float,
        filter: Filter2OrStr,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every follower of the specified channel.

        Args:
            channel_id: The ID of the channel.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderators`` - Return
                moderators.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by follow date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The followers were returned.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_channel_subscribers(
            channel_id,
            filter,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def subscribe_to_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method subscribes the authenticated user to the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is subscribed to the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.subscribe_to_channel(
            channel_id, user_id, request_options=request_options
        ).unwrap()

    def subscribe_to_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method subscribes the authenticated user to the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is subscribed to the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.subscribe_to_channel_alt1(channel_id, request_options=request_options).unwrap()

    def unsubscribe_from_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method unsubscribes the authenticated user from the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is unsubscribed from the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.unsubscribe_from_channel(
            channel_id, user_id, request_options=request_options
        ).unwrap()

    def unsubscribe_from_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method unsubscribes the authenticated user from the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is unsubscribed from the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.unsubscribe_from_channel_alt1(
            channel_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ChannelsSubscriptionsAndSubscribersWithRawResponse:
        return self._with_raw_response


class AsyncChannelsSubscriptionsAndSubscribers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChannelsSubscriptionsAndSubscribersWithRawResponse(client, server, auth)

    async def check_if_user_subscribed_to_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the specified user is a follower of a particular channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user follows the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.check_if_user_subscribed_to_channel(
                channel_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def check_if_user_subscribed_to_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the specified user is a follower of a particular channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user follows the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.check_if_user_subscribed_to_channel_alt1(
                channel_id, request_options=request_options
            )
        ).unwrap()

    async def get_channel_subscribers(
        self,
        channel_id: float,
        filter: Filter2OrStr,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every follower of the specified channel.

        Args:
            channel_id: The ID of the channel.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderators`` - Return
                moderators.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by follow date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The followers were returned.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_channel_subscribers(
                channel_id,
                filter,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def subscribe_to_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method subscribes the authenticated user to the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is subscribed to the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.subscribe_to_channel(channel_id, user_id, request_options=request_options)
        ).unwrap()

    async def subscribe_to_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method subscribes the authenticated user to the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is subscribed to the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.subscribe_to_channel_alt1(channel_id, request_options=request_options)
        ).unwrap()

    async def unsubscribe_from_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method unsubscribes the authenticated user from the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is unsubscribed from the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.unsubscribe_from_channel(channel_id, user_id, request_options=request_options)
        ).unwrap()

    async def unsubscribe_from_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method unsubscribes the authenticated user from the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is unsubscribed from the channel.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.unsubscribe_from_channel_alt1(channel_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncChannelsSubscriptionsAndSubscribersWithRawResponse:
        return self._with_raw_response


class ChannelsSubscriptionsAndSubscribersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_if_user_subscribed_to_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserSubscribedToChannelErrorBody]:
        """This method determines whether the specified user is a follower of a particular channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_subscribed_to_channel_error_mapper,
            request_options=request_options,
        )

    def check_if_user_subscribed_to_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserSubscribedToChannelAlt1ErrorBody]:
        """This method determines whether the specified user is a follower of a particular channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_subscribed_to_channel_alt1_error_mapper,
            request_options=request_options,
        )

    def get_channel_subscribers(
        self,
        channel_id: float,
        filter: Filter2OrStr,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetChannelSubscribersErrorBody]:
        """This method returns every follower of the specified channel.

        Args:
            channel_id: The ID of the channel.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderators`` - Return
                moderators.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by follow date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/users"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[
                param[Filter2OrStr]("filter", filter),
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_channel_subscribers_error_mapper,
            request_options=request_options,
        )

    def subscribe_to_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SubscribeToChannelErrorBody]:
        """This method subscribes the authenticated user to the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=subscribe_to_channel_error_mapper,
            request_options=request_options,
        )

    def subscribe_to_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SubscribeToChannelAlt1ErrorBody]:
        """This method subscribes the authenticated user to the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=subscribe_to_channel_alt1_error_mapper,
            request_options=request_options,
        )

    def unsubscribe_from_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnsubscribeFromChannelErrorBody]:
        """This method unsubscribes the authenticated user from the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=unsubscribe_from_channel_error_mapper,
            request_options=request_options,
        )

    def unsubscribe_from_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnsubscribeFromChannelAlt1ErrorBody]:
        """This method unsubscribes the authenticated user from the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=unsubscribe_from_channel_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncChannelsSubscriptionsAndSubscribersWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def check_if_user_subscribed_to_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserSubscribedToChannelErrorBody]:
        """This method determines whether the specified user is a follower of a particular channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_subscribed_to_channel_error_mapper,
            request_options=request_options,
        )

    async def check_if_user_subscribed_to_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserSubscribedToChannelAlt1ErrorBody]:
        """This method determines whether the specified user is a follower of a particular channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_subscribed_to_channel_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_channel_subscribers(
        self,
        channel_id: float,
        filter: Filter2OrStr,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetChannelSubscribersErrorBody]:
        """This method returns every follower of the specified channel.

        Args:
            channel_id: The ID of the channel.
            filter: The attribute by which to filter the results. Option descriptions: * ``moderators`` - Return
                moderators.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by follow date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/users"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[
                param[Filter2OrStr]("filter", filter),
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_channel_subscribers_error_mapper,
            request_options=request_options,
        )

    async def subscribe_to_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SubscribeToChannelErrorBody]:
        """This method subscribes the authenticated user to the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=subscribe_to_channel_error_mapper,
            request_options=request_options,
        )

    async def subscribe_to_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SubscribeToChannelAlt1ErrorBody]:
        """This method subscribes the authenticated user to the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=subscribe_to_channel_alt1_error_mapper,
            request_options=request_options,
        )

    async def unsubscribe_from_channel(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnsubscribeFromChannelErrorBody]:
        """This method unsubscribes the authenticated user from the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=unsubscribe_from_channel_error_mapper,
            request_options=request_options,
        )

    async def unsubscribe_from_channel_alt1(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnsubscribeFromChannelAlt1ErrorBody]:
        """This method unsubscribes the authenticated user from the specified channel.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/channels/{channel_id}"),
            path_params=[param[float]("channel_id", channel_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=unsubscribe_from_channel_alt1_error_mapper,
            request_options=request_options,
        )
