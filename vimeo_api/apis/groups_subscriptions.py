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
    param,
)
from ..errors.join_group_alt1_error import JoinGroupAlt1ErrorBody, join_group_alt1_error_mapper
from ..errors.join_group_error import JoinGroupErrorBody, join_group_error_mapper
from ..errors.leave_group_alt1_error import LeaveGroupAlt1ErrorBody, leave_group_alt1_error_mapper
from ..errors.leave_group_error import LeaveGroupErrorBody, leave_group_error_mapper
from ..server.server import Server


class GroupsSubscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GroupsSubscriptionsWithRawResponse(client, server, auth)

    def join_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the authenticated user to the specified group.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user joined the group.

        Raises:
            ApiError: The authenticated user can't join the group. Possible reasons are that the group isn't public or
                that its privacy setting is ``members``. Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.join_group(group_id, user_id, request_options=request_options).unwrap()

    def join_group_alt1(self, group_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method adds the authenticated user to the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user joined the group.

        Raises:
            ApiError: The authenticated user can't join the group. Possible reasons are that the group isn't public or
                that its privacy setting is ``members``. Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.join_group_alt1(group_id, request_options=request_options).unwrap()

    def leave_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the authenticated user from the specified group. The authenticated user can't be the
        owner of the group; assign a new owner through a PATCH request first.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was removed from the group.

        Raises:
            ApiError: The authenticated user can't leave the group. Error code 5451: This resource is restricted in your
                region. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.leave_group(group_id, user_id, request_options=request_options).unwrap()

    def leave_group_alt1(self, group_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method removes the authenticated user from the specified group. The authenticated user can't be the
        owner of the group; assign a new owner through a PATCH request first.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was removed from the group.

        Raises:
            ApiError: The authenticated user can't leave the group. Error code 5451: This resource is restricted in your
                region. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.leave_group_alt1(group_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GroupsSubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncGroupsSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGroupsSubscriptionsWithRawResponse(client, server, auth)

    async def join_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the authenticated user to the specified group.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user joined the group.

        Raises:
            ApiError: The authenticated user can't join the group. Possible reasons are that the group isn't public or
                that its privacy setting is ``members``. Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | Error | RawError``."""
        return (await self._with_raw_response.join_group(group_id, user_id, request_options=request_options)).unwrap()

    async def join_group_alt1(self, group_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method adds the authenticated user to the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user joined the group.

        Raises:
            ApiError: The authenticated user can't join the group. Possible reasons are that the group isn't public or
                that its privacy setting is ``members``. Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | Error | RawError``."""
        return (await self._with_raw_response.join_group_alt1(group_id, request_options=request_options)).unwrap()

    async def leave_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the authenticated user from the specified group. The authenticated user can't be the
        owner of the group; assign a new owner through a PATCH request first.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was removed from the group.

        Raises:
            ApiError: The authenticated user can't leave the group. Error code 5451: This resource is restricted in your
                region. ``error`` is ``LegacyError | Error | RawError``."""
        return (await self._with_raw_response.leave_group(group_id, user_id, request_options=request_options)).unwrap()

    async def leave_group_alt1(self, group_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method removes the authenticated user from the specified group. The authenticated user can't be the
        owner of the group; assign a new owner through a PATCH request first.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was removed from the group.

        Raises:
            ApiError: The authenticated user can't leave the group. Error code 5451: This resource is restricted in your
                region. ``error`` is ``LegacyError | Error | RawError``."""
        return (await self._with_raw_response.leave_group_alt1(group_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncGroupsSubscriptionsWithRawResponse:
        return self._with_raw_response


class GroupsSubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def join_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, JoinGroupErrorBody]:
        """This method adds the authenticated user to the specified group.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=join_group_error_mapper,
            request_options=request_options,
        )

    def join_group_alt1(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, JoinGroupAlt1ErrorBody]:
        """This method adds the authenticated user to the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=join_group_alt1_error_mapper,
            request_options=request_options,
        )

    def leave_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, LeaveGroupErrorBody]:
        """This method removes the authenticated user from the specified group. The authenticated user can't be the
        owner of the group; assign a new owner through a PATCH request first.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=leave_group_error_mapper,
            request_options=request_options,
        )

    def leave_group_alt1(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, LeaveGroupAlt1ErrorBody]:
        """This method removes the authenticated user from the specified group. The authenticated user can't be the
        owner of the group; assign a new owner through a PATCH request first.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=leave_group_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncGroupsSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def join_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, JoinGroupErrorBody]:
        """This method adds the authenticated user to the specified group.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=join_group_error_mapper,
            request_options=request_options,
        )

    async def join_group_alt1(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, JoinGroupAlt1ErrorBody]:
        """This method adds the authenticated user to the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=join_group_alt1_error_mapper,
            request_options=request_options,
        )

    async def leave_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, LeaveGroupErrorBody]:
        """This method removes the authenticated user from the specified group. The authenticated user can't be the
        owner of the group; assign a new owner through a PATCH request first.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=leave_group_error_mapper,
            request_options=request_options,
        )

    async def leave_group_alt1(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, LeaveGroupAlt1ErrorBody]:
        """This method removes the authenticated user from the specified group. The authenticated user can't be the
        owner of the group; assign a new owner through a PATCH request first.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=leave_group_alt1_error_mapper,
            request_options=request_options,
        )
