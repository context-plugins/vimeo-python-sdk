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
from ..errors.add_channel_moderator_error import AddChannelModeratorErrorBody, add_channel_moderator_error_mapper
from ..errors.add_channel_moderators_error import AddChannelModeratorsErrorBody, add_channel_moderators_error_mapper
from ..errors.remove_channel_moderator_error import (
    RemoveChannelModeratorErrorBody,
    remove_channel_moderator_error_mapper,
)
from ..errors.remove_channel_moderators_error import (
    RemoveChannelModeratorsErrorBody,
    remove_channel_moderators_error_mapper,
)
from ..errors.replace_channel_moderators_error import (
    ReplaceChannelModeratorsErrorBody,
    replace_channel_moderators_error_mapper,
)
from ..models.channels_moderators_request import ChannelsModeratorsRequest, ChannelsModeratorsRequestDict
from ..models.channels_moderators_request1 import ChannelsModeratorsRequest1, ChannelsModeratorsRequest1Dict
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort8 import Sort8OrStr
from ..models.user import User
from ..models.user_connection import UserConnection
from ..server.server import Server


class ChannelsModerators:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChannelsModeratorsWithRawResponse(client, server, auth)

    def add_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single user as a moderator to the specified channel. The authenticated user must be a
        follower of the requested user to add them as a channel moderator.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: The authenticated user doesn't own the channel, the requested user is already a moderator of the
                channel, or the authenticated user doesn't follow the requested user. No such channel exists, or no such
                user exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_channel_moderator(
            channel_id, user_id, request_options=request_options
        ).unwrap()

    def add_channel_moderators(self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method adds multiple users as moderators to the specified channel. Include the users by their URI as a
        JSON array in the body of the request using the **user_uri** field, like this: ``[{ "user_uri": "/users/1234" },
        { "user_uri": "/users/1235" }]``. The authenticated user must be a follower of a requested user to add this
        person as a moderator. For more information on batch requests like this one, see `Using Common Formats and
        Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderators were added.

        Raises:
            ApiError: Error code 2908: The list contains more than 100 users. The authenticated user doesn't own the
                channel, a requested user is already a moderator of the channel, or the authenticated user doesn't
                follow a requested user. No such channel exists, or no such user exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.add_channel_moderators(channel_id, request_options=request_options).unwrap()

    def get_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """This method returns a single moderator of the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderator was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_channel_moderator(
            channel_id, user_id, request_options=request_options
        ).unwrap()

    def get_channel_moderators(
        self,
        channel_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every moderator of the specified channel.

        Args:
            channel_id: The ID of the channel.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date added.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderators were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_channel_moderators(
            channel_id,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def remove_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single moderator from the specified channel. The authenticated user must be the owner
        of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderator was removed.

        Raises:
            ApiError: The authenticated user doesn't own the channel, the requested user isn't a moderator of the
                channel, or the requested user is the owner of the channel. No such channel exists, or no such user
                exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.remove_channel_moderator(
            channel_id, user_id, request_options=request_options
        ).unwrap()

    def remove_channel_moderators(
        self,
        channel_id: float,
        body: ChannelsModeratorsRequest | ChannelsModeratorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple moderators from the specified channel. The authenticated user must be the owner
        of the channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderators were removed.

        Raises:
            ApiError: The authenticated user doesn't own the channel, a requested user isn't a moderator of the channel,
                or a requested user is the owner of the channel. No such channel exists, or no such user exists.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.remove_channel_moderators(
            channel_id, body, request_options=request_options
        ).unwrap()

    def replace_channel_moderators(
        self,
        channel_id: float,
        body: ChannelsModeratorsRequest1 | ChannelsModeratorsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[User]:
        """This method replaces the current list of channel moderators with a new list. The authenticated user must be
        the owner of the channel and a follower of each requested user to add them as a channel moderator.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderators were replaced.

        Raises:
            ApiError: Error code 2908: The list contains more than 100 users. The authenticated user doesn't own the
                channel. No such channel exists. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.replace_channel_moderators(
            channel_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ChannelsModeratorsWithRawResponse:
        return self._with_raw_response


class AsyncChannelsModerators:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChannelsModeratorsWithRawResponse(client, server, auth)

    async def add_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single user as a moderator to the specified channel. The authenticated user must be a
        follower of the requested user to add them as a channel moderator.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: The authenticated user doesn't own the channel, the requested user is already a moderator of the
                channel, or the authenticated user doesn't follow the requested user. No such channel exists, or no such
                user exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_channel_moderator(channel_id, user_id, request_options=request_options)
        ).unwrap()

    async def add_channel_moderators(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds multiple users as moderators to the specified channel. Include the users by their URI as a
        JSON array in the body of the request using the **user_uri** field, like this: ``[{ "user_uri": "/users/1234" },
        { "user_uri": "/users/1235" }]``. The authenticated user must be a follower of a requested user to add this
        person as a moderator. For more information on batch requests like this one, see `Using Common Formats and
        Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderators were added.

        Raises:
            ApiError: Error code 2908: The list contains more than 100 users. The authenticated user doesn't own the
                channel, a requested user is already a moderator of the channel, or the authenticated user doesn't
                follow a requested user. No such channel exists, or no such user exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_channel_moderators(channel_id, request_options=request_options)
        ).unwrap()

    async def get_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """This method returns a single moderator of the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderator was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_channel_moderator(channel_id, user_id, request_options=request_options)
        ).unwrap()

    async def get_channel_moderators(
        self,
        channel_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every moderator of the specified channel.

        Args:
            channel_id: The ID of the channel.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date added.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderators were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_channel_moderators(
                channel_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def remove_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single moderator from the specified channel. The authenticated user must be the owner
        of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderator was removed.

        Raises:
            ApiError: The authenticated user doesn't own the channel, the requested user isn't a moderator of the
                channel, or the requested user is the owner of the channel. No such channel exists, or no such user
                exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.remove_channel_moderator(channel_id, user_id, request_options=request_options)
        ).unwrap()

    async def remove_channel_moderators(
        self,
        channel_id: float,
        body: ChannelsModeratorsRequest | ChannelsModeratorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple moderators from the specified channel. The authenticated user must be the owner
        of the channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderators were removed.

        Raises:
            ApiError: The authenticated user doesn't own the channel, a requested user isn't a moderator of the channel,
                or a requested user is the owner of the channel. No such channel exists, or no such user exists.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.remove_channel_moderators(channel_id, body, request_options=request_options)
        ).unwrap()

    async def replace_channel_moderators(
        self,
        channel_id: float,
        body: ChannelsModeratorsRequest1 | ChannelsModeratorsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[User]:
        """This method replaces the current list of channel moderators with a new list. The authenticated user must be
        the owner of the channel and a follower of each requested user to add them as a channel moderator.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The moderators were replaced.

        Raises:
            ApiError: Error code 2908: The list contains more than 100 users. The authenticated user doesn't own the
                channel. No such channel exists. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.replace_channel_moderators(channel_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncChannelsModeratorsWithRawResponse:
        return self._with_raw_response


class ChannelsModeratorsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddChannelModeratorErrorBody]:
        """This method adds a single user as a moderator to the specified channel. The authenticated user must be a
        follower of the requested user to add them as a channel moderator.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/moderators/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_channel_moderator_error_mapper,
            request_options=request_options,
        )

    def add_channel_moderators(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddChannelModeratorsErrorBody]:
        """This method adds multiple users as moderators to the specified channel. Include the users by their URI as a
        JSON array in the body of the request using the **user_uri** field, like this: ``[{ "user_uri": "/users/1234" },
        { "user_uri": "/users/1235" }]``. The authenticated user must be a follower of a requested user to add this
        person as a moderator. For more information on batch requests like this one, see `Using Common Formats and
        Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/moderators"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_channel_moderators_error_mapper,
            request_options=request_options,
        )

    def get_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, RawError]:
        """This method returns a single moderator of the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/moderators/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_channel_moderators(
        self,
        channel_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every moderator of the specified channel.

        Args:
            channel_id: The ID of the channel.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date added.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/moderators"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[
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
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveChannelModeratorErrorBody]:
        """This method removes a single moderator from the specified channel. The authenticated user must be the owner
        of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/moderators/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_channel_moderator_error_mapper,
            request_options=request_options,
        )

    def remove_channel_moderators(
        self,
        channel_id: float,
        body: ChannelsModeratorsRequest | ChannelsModeratorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveChannelModeratorsErrorBody]:
        """This method removes multiple moderators from the specified channel. The authenticated user must be the owner
        of the channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/moderators"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsModeratorsRequest | ChannelsModeratorsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_channel_moderators_error_mapper,
            request_options=request_options,
        )

    def replace_channel_moderators(
        self,
        channel_id: float,
        body: ChannelsModeratorsRequest1 | ChannelsModeratorsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[User], ReplaceChannelModeratorsErrorBody]:
        """This method replaces the current list of channel moderators with a new list. The authenticated user must be
        the owner of the channel and a follower of each requested user to add them as a channel moderator.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/channels/{channel_id}/moderators"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsModeratorsRequest1 | ChannelsModeratorsRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[User]],
            error_mapper=replace_channel_moderators_error_mapper,
            request_options=request_options,
        )


class AsyncChannelsModeratorsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddChannelModeratorErrorBody]:
        """This method adds a single user as a moderator to the specified channel. The authenticated user must be a
        follower of the requested user to add them as a channel moderator.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/moderators/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_channel_moderator_error_mapper,
            request_options=request_options,
        )

    async def add_channel_moderators(
        self, channel_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddChannelModeratorsErrorBody]:
        """This method adds multiple users as moderators to the specified channel. Include the users by their URI as a
        JSON array in the body of the request using the **user_uri** field, like this: ``[{ "user_uri": "/users/1234" },
        { "user_uri": "/users/1235" }]``. The authenticated user must be a follower of a requested user to add this
        person as a moderator. For more information on batch requests like this one, see `Using Common Formats and
        Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/moderators"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_channel_moderators_error_mapper,
            request_options=request_options,
        )

    async def get_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, RawError]:
        """This method returns a single moderator of the specified channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/moderators/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_channel_moderators(
        self,
        channel_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every moderator of the specified channel.

        Args:
            channel_id: The ID of the channel.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date added.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/moderators"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[
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
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_channel_moderator(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveChannelModeratorErrorBody]:
        """This method removes a single moderator from the specified channel. The authenticated user must be the owner
        of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/moderators/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_channel_moderator_error_mapper,
            request_options=request_options,
        )

    async def remove_channel_moderators(
        self,
        channel_id: float,
        body: ChannelsModeratorsRequest | ChannelsModeratorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveChannelModeratorsErrorBody]:
        """This method removes multiple moderators from the specified channel. The authenticated user must be the owner
        of the channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/moderators"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsModeratorsRequest | ChannelsModeratorsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_channel_moderators_error_mapper,
            request_options=request_options,
        )

    async def replace_channel_moderators(
        self,
        channel_id: float,
        body: ChannelsModeratorsRequest1 | ChannelsModeratorsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[User], ReplaceChannelModeratorsErrorBody]:
        """This method replaces the current list of channel moderators with a new list. The authenticated user must be
        the owner of the channel and a follower of each requested user to add them as a channel moderator.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/channels/{channel_id}/moderators"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsModeratorsRequest1 | ChannelsModeratorsRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[User]],
            error_mapper=replace_channel_moderators_error_mapper,
            request_options=request_options,
        )
