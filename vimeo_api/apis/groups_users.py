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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_decoder,
    param,
    unwrap,
)
from ..errors.check_if_user_joined_group_alt1_error import (
    CheckIfUserJoinedGroupAlt1ErrorBody,
    check_if_user_joined_group_alt1_error_mapper,
)
from ..errors.check_if_user_joined_group_error import (
    CheckIfUserJoinedGroupErrorBody,
    check_if_user_joined_group_error_mapper,
)
from ..errors.get_group_members_error import GetGroupMembersErrorBody, get_group_members_error_mapper
from ..errors.get_user_groups_alt1_error import GetUserGroupsAlt1ErrorBody, get_user_groups_alt1_error_mapper
from ..errors.get_user_groups_error import GetUserGroupsErrorBody, get_user_groups_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter2 import Filter2OrStr
from ..models.enums.filter12 import Filter12OrStr
from ..models.enums.sort5 import Sort5OrStr
from ..models.enums.sort8 import Sort8OrStr
from ..models.group_connection import GroupConnection
from ..models.user_connection import UserConnection
from ..server.server import Server


class GroupsUsers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GroupsUsersWithRawResponse(client, server, auth)

    def check_if_user_joined_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user belongs to the specified group.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user belongs to the group.

        Raises:
            ApiError: * No such group exists. * The authenticated user isn't a member of the group. * Error code 5451:
                This resource is restricted in your region. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.check_if_user_joined_group(group_id, user_id, request_options=request_options)
        )

    def check_if_user_joined_group_alt1(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user belongs to the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user belongs to the group.

        Raises:
            ApiError: * No such group exists. * The authenticated user isn't a member of the group. * Error code 5451:
                This resource is restricted in your region. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.check_if_user_joined_group_alt1(group_id, request_options=request_options)
        )

    def get_group_members(
        self,
        group_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter2OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who belongs to the specified group.

        Args:
            group_id: The ID of the group.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderators`` - Return group
                moderators.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The members were returned.

        Raises:
            ApiError: * No such group exists. * Error code 5451: This resource is restricted in your region. ``error``
                is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_group_members(
                group_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_user_groups(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupConnection:
        """This method returns every group to which the authenticated user belongs.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``members`` - Sort the results by
                number of members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The groups were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_user_groups(
                user_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_user_groups_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupConnection:
        """This method returns every group to which the authenticated user belongs.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``members`` - Sort the results by
                number of members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The groups were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_user_groups_alt1(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> GroupsUsersWithRawResponse:
        return self._with_raw_response


class AsyncGroupsUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGroupsUsersWithRawResponse(client, server, auth)

    async def check_if_user_joined_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user belongs to the specified group.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user belongs to the group.

        Raises:
            ApiError: * No such group exists. * The authenticated user isn't a member of the group. * Error code 5451:
                This resource is restricted in your region. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_if_user_joined_group(group_id, user_id, request_options=request_options)
        )

    async def check_if_user_joined_group_alt1(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user belongs to the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user belongs to the group.

        Raises:
            ApiError: * No such group exists. * The authenticated user isn't a member of the group. * Error code 5451:
                This resource is restricted in your region. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_if_user_joined_group_alt1(group_id, request_options=request_options)
        )

    async def get_group_members(
        self,
        group_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter2OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who belongs to the specified group.

        Args:
            group_id: The ID of the group.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderators`` - Return group
                moderators.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The members were returned.

        Raises:
            ApiError: * No such group exists. * Error code 5451: This resource is restricted in your region. ``error``
                is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_group_members(
                group_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_user_groups(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupConnection:
        """This method returns every group to which the authenticated user belongs.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``members`` - Sort the results by
                number of members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The groups were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_user_groups(
                user_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_user_groups_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupConnection:
        """This method returns every group to which the authenticated user belongs.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``members`` - Sort the results by
                number of members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The groups were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_user_groups_alt1(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncGroupsUsersWithRawResponse:
        return self._with_raw_response


class GroupsUsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_if_user_joined_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserJoinedGroupErrorBody]:
        """This method determines whether the authenticated user belongs to the specified group.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_joined_group_error_mapper,
            request_options=request_options,
        )

    def check_if_user_joined_group_alt1(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserJoinedGroupAlt1ErrorBody]:
        """This method determines whether the authenticated user belongs to the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_joined_group_alt1_error_mapper,
            request_options=request_options,
        )

    def get_group_members(
        self,
        group_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter2OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetGroupMembersErrorBody]:
        """This method returns every user who belongs to the specified group.

        Args:
            group_id: The ID of the group.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderators`` - Return group
                moderators.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{group_id}/users"),
            path_params=[param[float]("group_id", group_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter2OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_group_members_error_mapper,
            request_options=request_options,
        )

    def get_user_groups(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupConnection, GetUserGroupsErrorBody]:
        """This method returns every group to which the authenticated user belongs.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``members`` - Sort the results by
                number of members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/groups"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter12OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[GroupConnection],
            error_mapper=get_user_groups_error_mapper,
            request_options=request_options,
        )

    def get_user_groups_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupConnection, GetUserGroupsAlt1ErrorBody]:
        """This method returns every group to which the authenticated user belongs.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``members`` - Sort the results by
                number of members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/groups"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter12OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[GroupConnection],
            error_mapper=get_user_groups_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncGroupsUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_if_user_joined_group(
        self, group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserJoinedGroupErrorBody]:
        """This method determines whether the authenticated user belongs to the specified group.

        Args:
            group_id: The ID of the group.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=check_if_user_joined_group_error_mapper,
            request_options=request_options,
        )

    async def check_if_user_joined_group_alt1(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserJoinedGroupAlt1ErrorBody]:
        """This method determines whether the authenticated user belongs to the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=check_if_user_joined_group_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_group_members(
        self,
        group_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter2OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetGroupMembersErrorBody]:
        """This method returns every user who belongs to the specified group.

        Args:
            group_id: The ID of the group.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderators`` - Return group
                moderators.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{group_id}/users"),
            path_params=[param[float]("group_id", group_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter2OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[UserConnection],
            error_mapper=get_group_members_error_mapper,
            request_options=request_options,
        )

    async def get_user_groups(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupConnection, GetUserGroupsErrorBody]:
        """This method returns every group to which the authenticated user belongs.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``members`` - Sort the results by
                number of members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/groups"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter12OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[GroupConnection],
            error_mapper=get_user_groups_error_mapper,
            request_options=request_options,
        )

    async def get_user_groups_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter12OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupConnection, GetUserGroupsAlt1ErrorBody]:
        """This method returns every group to which the authenticated user belongs.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``moderated`` - Return
                moderated groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``members`` - Sort the results by
                number of members. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/groups"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter12OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort5OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[GroupConnection],
            error_mapper=get_user_groups_alt1_error_mapper,
            request_options=request_options,
        )
