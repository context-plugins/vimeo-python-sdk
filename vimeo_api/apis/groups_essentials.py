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
from ..errors.create_group_error import CreateGroupErrorBody, create_group_error_mapper
from ..errors.delete_group_error import DeleteGroupErrorBody, delete_group_error_mapper
from ..errors.get_group_error import GetGroupErrorBody, get_group_error_mapper
from ..errors.get_groups_error import GetGroupsErrorBody, get_groups_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter1 import Filter1OrStr
from ..models.enums.sort13 import Sort13OrStr
from ..models.group import Group
from ..models.group_connection import GroupConnection
from ..models.groups_request import GroupsRequest, GroupsRequestDict
from ..server.server import Server


class GroupsEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GroupsEssentialsWithRawResponse(client, server, auth)

    def create_group(
        self, body: GroupsRequest | GroupsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Group:
        """This method creates a new group.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The group was created.

        Raises:
            ApiError: A parameter is invalid. The authenticated user can't create groups. Error code 5451: This resource
                is restricted in your region. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.create_group(body, request_options=request_options).unwrap()

    def delete_group(self, group_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The group was deleted.

        Raises:
            ApiError: The authenticated user can't delete the group. Error code 5451: This resource is restricted in
                your region. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.delete_group(group_id, request_options=request_options).unwrap()

    def get_group(self, group_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Group:
        """This method returns the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The group was returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_group(group_id, request_options=request_options).unwrap()

    def get_groups(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter1OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort13OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupConnection:
        """This method returns every available group.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``featured`` - Return featured
                groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``relevant`` - Sort the results by relevance. This option is available for search
                queries only. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The groups were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_groups(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> GroupsEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncGroupsEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGroupsEssentialsWithRawResponse(client, server, auth)

    async def create_group(
        self, body: GroupsRequest | GroupsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Group:
        """This method creates a new group.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The group was created.

        Raises:
            ApiError: A parameter is invalid. The authenticated user can't create groups. Error code 5451: This resource
                is restricted in your region. ``error`` is ``LegacyError | Error | RawError``."""
        return (await self._with_raw_response.create_group(body, request_options=request_options)).unwrap()

    async def delete_group(self, group_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The group was deleted.

        Raises:
            ApiError: The authenticated user can't delete the group. Error code 5451: This resource is restricted in
                your region. ``error`` is ``LegacyError | Error | RawError``."""
        return (await self._with_raw_response.delete_group(group_id, request_options=request_options)).unwrap()

    async def get_group(self, group_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Group:
        """This method returns the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The group was returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.get_group(group_id, request_options=request_options)).unwrap()

    async def get_groups(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter1OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort13OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupConnection:
        """This method returns every available group.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``featured`` - Return featured
                groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``relevant`` - Sort the results by relevance. This option is available for search
                queries only. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The groups were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_groups(
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
    def with_raw_response(self) -> AsyncGroupsEssentialsWithRawResponse:
        return self._with_raw_response


class GroupsEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_group(
        self, body: GroupsRequest | GroupsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Group, CreateGroupErrorBody]:
        """This method creates a new group.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/groups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GroupsRequest | GroupsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Group],
            error_mapper=create_group_error_mapper,
            request_options=request_options,
        )

    def delete_group(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteGroupErrorBody]:
        """This method deletes the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_group_error_mapper,
            request_options=request_options,
        )

    def get_group(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Group, GetGroupErrorBody]:
        """This method returns the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Group],
            error_mapper=get_group_error_mapper,
            request_options=request_options,
        )

    def get_groups(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter1OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort13OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupConnection, GetGroupsErrorBody]:
        """This method returns every available group.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``featured`` - Return featured
                groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``relevant`` - Sort the results by relevance. This option is available for search
                queries only. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter1OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort13OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[GroupConnection],
            error_mapper=get_groups_error_mapper,
            request_options=request_options,
        )


class AsyncGroupsEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_group(
        self, body: GroupsRequest | GroupsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Group, CreateGroupErrorBody]:
        """This method creates a new group.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/groups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GroupsRequest | GroupsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Group],
            error_mapper=create_group_error_mapper,
            request_options=request_options,
        )

    async def delete_group(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteGroupErrorBody]:
        """This method deletes the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_group_error_mapper,
            request_options=request_options,
        )

    async def get_group(
        self, group_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Group, GetGroupErrorBody]:
        """This method returns the specified group.

        Args:
            group_id: The ID of the group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{group_id}"),
            path_params=[param[float]("group_id", group_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Group],
            error_mapper=get_group_error_mapper,
            request_options=request_options,
        )

    async def get_groups(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter1OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort13OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupConnection, GetGroupsErrorBody]:
        """This method returns every available group.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``featured`` - Return featured
                groups.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``followers`` - Sort the results by
                number of followers. * ``relevant`` - Sort the results by relevance. This option is available for search
                queries only. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter1OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort13OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[GroupConnection],
            error_mapper=get_groups_error_mapper,
            request_options=request_options,
        )
