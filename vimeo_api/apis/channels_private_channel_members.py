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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.delete_channel_privacy_user_error import (
    DeleteChannelPrivacyUserErrorBody,
    delete_channel_privacy_user_error_mapper,
)
from ..errors.get_channel_privacy_users_error import (
    GetChannelPrivacyUsersErrorBody,
    get_channel_privacy_users_error_mapper,
)
from ..errors.set_channel_privacy_user_error import (
    SetChannelPrivacyUserErrorBody,
    set_channel_privacy_user_error_mapper,
)
from ..errors.set_channel_privacy_users_error import (
    SetChannelPrivacyUsersErrorBody,
    set_channel_privacy_users_error_mapper,
)
from ..models.channels_privacy_users_request import ChannelsPrivacyUsersRequest, ChannelsPrivacyUsersRequestDict
from ..models.enums.direction import DirectionOrStr
from ..models.user import User
from ..models.user_connection import UserConnection
from ..server.server import Server


class ChannelsPrivateChannelMembers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChannelsPrivateChannelMembersWithRawResponse(client, server, auth)

    def delete_channel_privacy_user(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method prevents a single user from being able to access the specified private channel. The authenticated
        user must be the owner of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user can't acceess the private channel.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user doesn't
                own the channel. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.delete_channel_privacy_user(channel_id, user_id, request_options=request_options)
        )

    def get_channel_privacy_users(
        self,
        channel_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns all the users who have access to the specified private channel. The authenticated user
        must be the owner of the channel.

        Args:
            channel_id: The ID of the channel.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users were returned.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user doesn't
                own this channel. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_channel_privacy_users(
                channel_id, direction=direction, page=page, per_page=per_page, request_options=request_options
            ),
        )

    def set_channel_privacy_user(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method gives a single user access to the specified private channel. The authenticated user must be the
        owner of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user can now view the private channel.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user doesn't
                own the channel. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.set_channel_privacy_user(channel_id, user_id, request_options=request_options)
        )

    def set_channel_privacy_users(
        self,
        channel_id: float,
        body: ChannelsPrivacyUsersRequest | ChannelsPrivacyUsersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[User]:
        """This method gives multiple users access to the specified private channel. The authenticated user must be the
        owner of the channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users can access the private channel.

        Raises:
            ApiError: * Error code 2205: There was no request body, or the request body is malformed. * Error code 2900:
                No such user exists. Error code 8003: The user credentials are invalid. Error code 3200: The
                authenticated user doesn't own this channel. Error code 2204: A requested user can't have access to the
                channel. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.set_channel_privacy_users(channel_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> ChannelsPrivateChannelMembersWithRawResponse:
        return self._with_raw_response


class AsyncChannelsPrivateChannelMembers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChannelsPrivateChannelMembersWithRawResponse(client, server, auth)

    async def delete_channel_privacy_user(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method prevents a single user from being able to access the specified private channel. The authenticated
        user must be the owner of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user can't acceess the private channel.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user doesn't
                own the channel. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_channel_privacy_user(
                channel_id, user_id, request_options=request_options
            ),
        )

    async def get_channel_privacy_users(
        self,
        channel_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns all the users who have access to the specified private channel. The authenticated user
        must be the owner of the channel.

        Args:
            channel_id: The ID of the channel.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users were returned.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user doesn't
                own this channel. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_channel_privacy_users(
                channel_id, direction=direction, page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def set_channel_privacy_user(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method gives a single user access to the specified private channel. The authenticated user must be the
        owner of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user can now view the private channel.

        Raises:
            ApiError: Error code 8003: The user credentials are invalid. Error code 3200: The authenticated user doesn't
                own the channel. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.set_channel_privacy_user(channel_id, user_id, request_options=request_options)
        )

    async def set_channel_privacy_users(
        self,
        channel_id: float,
        body: ChannelsPrivacyUsersRequest | ChannelsPrivacyUsersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[User]:
        """This method gives multiple users access to the specified private channel. The authenticated user must be the
        owner of the channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users can access the private channel.

        Raises:
            ApiError: * Error code 2205: There was no request body, or the request body is malformed. * Error code 2900:
                No such user exists. Error code 8003: The user credentials are invalid. Error code 3200: The
                authenticated user doesn't own this channel. Error code 2204: A requested user can't have access to the
                channel. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.set_channel_privacy_users(channel_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncChannelsPrivateChannelMembersWithRawResponse:
        return self._with_raw_response


class ChannelsPrivateChannelMembersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_channel_privacy_user(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChannelPrivacyUserErrorBody]:
        """This method prevents a single user from being able to access the specified private channel. The authenticated
        user must be the owner of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/privacy/users/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_channel_privacy_user_error_mapper,
            request_options=request_options,
        )

    def get_channel_privacy_users(
        self,
        channel_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetChannelPrivacyUsersErrorBody]:
        """This method returns all the users who have access to the specified private channel. The authenticated user
        must be the owner of the channel.

        Args:
            channel_id: The ID of the channel.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/privacy/users"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_channel_privacy_users_error_mapper,
            request_options=request_options,
        )

    def set_channel_privacy_user(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SetChannelPrivacyUserErrorBody]:
        """This method gives a single user access to the specified private channel. The authenticated user must be the
        owner of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/privacy/users/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=set_channel_privacy_user_error_mapper,
            request_options=request_options,
        )

    def set_channel_privacy_users(
        self,
        channel_id: float,
        body: ChannelsPrivacyUsersRequest | ChannelsPrivacyUsersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[User], SetChannelPrivacyUsersErrorBody]:
        """This method gives multiple users access to the specified private channel. The authenticated user must be the
        owner of the channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/privacy/users"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsPrivacyUsersRequest | ChannelsPrivacyUsersRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[User]],
            error_mapper=set_channel_privacy_users_error_mapper,
            request_options=request_options,
        )


class AsyncChannelsPrivateChannelMembersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_channel_privacy_user(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChannelPrivacyUserErrorBody]:
        """This method prevents a single user from being able to access the specified private channel. The authenticated
        user must be the owner of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/privacy/users/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_channel_privacy_user_error_mapper,
            request_options=request_options,
        )

    async def get_channel_privacy_users(
        self,
        channel_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetChannelPrivacyUsersErrorBody]:
        """This method returns all the users who have access to the specified private channel. The authenticated user
        must be the owner of the channel.

        Args:
            channel_id: The ID of the channel.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/privacy/users"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[UserConnection],
            error_mapper=get_channel_privacy_users_error_mapper,
            request_options=request_options,
        )

    async def set_channel_privacy_user(
        self, channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SetChannelPrivacyUserErrorBody]:
        """This method gives a single user access to the specified private channel. The authenticated user must be the
        owner of the channel.

        Args:
            channel_id: The ID of the channel.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/privacy/users/{user_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=set_channel_privacy_user_error_mapper,
            request_options=request_options,
        )

    async def set_channel_privacy_users(
        self,
        channel_id: float,
        body: ChannelsPrivacyUsersRequest | ChannelsPrivacyUsersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[User], SetChannelPrivacyUsersErrorBody]:
        """This method gives multiple users access to the specified private channel. The authenticated user must be the
        owner of the channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/privacy/users"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsPrivacyUsersRequest | ChannelsPrivacyUsersRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[list[User]],
            error_mapper=set_channel_privacy_users_error_mapper,
            request_options=request_options,
        )
