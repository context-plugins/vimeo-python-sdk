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
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.federated_search_user_items_alt1_error import (
    FederatedSearchUserItemsAlt1ErrorBody,
    federated_search_user_items_alt1_error_mapper,
)
from ..errors.federated_search_user_items_error import (
    FederatedSearchUserItemsErrorBody,
    federated_search_user_items_error_mapper,
)
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter30 import Filter30OrStr
from ..models.enums.sort46 import Sort46OrStr
from ..models.federated_search_items_connection import FederatedSearchItemsConnection
from ..server.server import Server


class SearchFederated:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SearchFederatedWithRawResponse(client, server, auth)

    def federated_search_user_items(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter30OrStr | None = None,
        filter_privacy: str | None = None,
        modified_end_date: str | None = None,
        modified_start_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort46OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FederatedSearchItemsConnection:
        """This method returns the federated search results of the authenticated user's videos and folders according to
        a search query.

        If no query is provided, the method returns items sorted by the most recent user action.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``video`` - Return videos.
            filter_privacy: A comma-separated list of privacy settings to filter the results by. Possible values include
                ``unlisted`` for videos that are accessible but not searchable from Vimeo, ``password`` for videos on
                Vimeo that anyone can access with the correct password, ``hide-from-vimeo`` for videos that don't appear
                on Vimeo, ``private`` for videos on Vimeo that only their owner can access, and ``public`` for videos on
                Vimeo that anyone can access. By default, all privacy settings are considered.
            modified_end_date: The inclusive end date of the range.
            modified_start_date: The inclusive start date of the range. This value must be earlier than the modified end
                date.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                order. * ``duration`` - Sort the results by duration, where available. * ``folder_path`` - Sort the
                results by the hierarchy of folders. * ``last_user_action_event_date`` - Sort the results by most recent
                user interaction.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The federated search results were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.federated_search_user_items(
                user_id,
                direction=direction,
                filter_=filter_,
                filter_privacy=filter_privacy,
                modified_end_date=modified_end_date,
                modified_start_date=modified_start_date,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            ),
        )

    def federated_search_user_items_alt1(
        self,
        workspace_uuid: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter30OrStr | None = None,
        filter_privacy: str | None = None,
        modified_end_date: str | None = None,
        modified_start_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort46OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FederatedSearchItemsConnection:
        """This method returns the federated search results of the authenticated user's videos and folders according to
        a search query.

        If no query is provided, the method returns items sorted by the most recent user action.

        Args:
            workspace_uuid: The UUID of the workspace.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``video`` - Return videos.
            filter_privacy: A comma-separated list of privacy settings to filter the results by. Possible values include
                ``unlisted`` for videos that are accessible but not searchable from Vimeo, ``password`` for videos on
                Vimeo that anyone can access with the correct password, ``hide-from-vimeo`` for videos that don't appear
                on Vimeo, ``private`` for videos on Vimeo that only their owner can access, and ``public`` for videos on
                Vimeo that anyone can access. By default, all privacy settings are considered.
            modified_end_date: The inclusive end date of the range.
            modified_start_date: The inclusive start date of the range. This value must be earlier than the modified end
                date.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                order. * ``duration`` - Sort the results by duration, where available. * ``folder_path`` - Sort the
                results by the hierarchy of folders. * ``last_user_action_event_date`` - Sort the results by most recent
                user interaction.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The federated search results were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.federated_search_user_items_alt1(
                workspace_uuid,
                direction=direction,
                filter_=filter_,
                filter_privacy=filter_privacy,
                modified_end_date=modified_end_date,
                modified_start_date=modified_start_date,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SearchFederatedWithRawResponse:
        return self._with_raw_response


class AsyncSearchFederated:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSearchFederatedWithRawResponse(client, server, auth)

    async def federated_search_user_items(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter30OrStr | None = None,
        filter_privacy: str | None = None,
        modified_end_date: str | None = None,
        modified_start_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort46OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FederatedSearchItemsConnection:
        """This method returns the federated search results of the authenticated user's videos and folders according to
        a search query.

        If no query is provided, the method returns items sorted by the most recent user action.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``video`` - Return videos.
            filter_privacy: A comma-separated list of privacy settings to filter the results by. Possible values include
                ``unlisted`` for videos that are accessible but not searchable from Vimeo, ``password`` for videos on
                Vimeo that anyone can access with the correct password, ``hide-from-vimeo`` for videos that don't appear
                on Vimeo, ``private`` for videos on Vimeo that only their owner can access, and ``public`` for videos on
                Vimeo that anyone can access. By default, all privacy settings are considered.
            modified_end_date: The inclusive end date of the range.
            modified_start_date: The inclusive start date of the range. This value must be earlier than the modified end
                date.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                order. * ``duration`` - Sort the results by duration, where available. * ``folder_path`` - Sort the
                results by the hierarchy of folders. * ``last_user_action_event_date`` - Sort the results by most recent
                user interaction.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The federated search results were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.federated_search_user_items(
                user_id,
                direction=direction,
                filter_=filter_,
                filter_privacy=filter_privacy,
                modified_end_date=modified_end_date,
                modified_start_date=modified_start_date,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def federated_search_user_items_alt1(
        self,
        workspace_uuid: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter30OrStr | None = None,
        filter_privacy: str | None = None,
        modified_end_date: str | None = None,
        modified_start_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort46OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FederatedSearchItemsConnection:
        """This method returns the federated search results of the authenticated user's videos and folders according to
        a search query.

        If no query is provided, the method returns items sorted by the most recent user action.

        Args:
            workspace_uuid: The UUID of the workspace.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``video`` - Return videos.
            filter_privacy: A comma-separated list of privacy settings to filter the results by. Possible values include
                ``unlisted`` for videos that are accessible but not searchable from Vimeo, ``password`` for videos on
                Vimeo that anyone can access with the correct password, ``hide-from-vimeo`` for videos that don't appear
                on Vimeo, ``private`` for videos on Vimeo that only their owner can access, and ``public`` for videos on
                Vimeo that anyone can access. By default, all privacy settings are considered.
            modified_end_date: The inclusive end date of the range.
            modified_start_date: The inclusive start date of the range. This value must be earlier than the modified end
                date.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                order. * ``duration`` - Sort the results by duration, where available. * ``folder_path`` - Sort the
                results by the hierarchy of folders. * ``last_user_action_event_date`` - Sort the results by most recent
                user interaction.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The federated search results were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.federated_search_user_items_alt1(
                workspace_uuid,
                direction=direction,
                filter_=filter_,
                filter_privacy=filter_privacy,
                modified_end_date=modified_end_date,
                modified_start_date=modified_start_date,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSearchFederatedWithRawResponse:
        return self._with_raw_response


class SearchFederatedWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def federated_search_user_items(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter30OrStr | None = None,
        filter_privacy: str | None = None,
        modified_end_date: str | None = None,
        modified_start_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort46OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FederatedSearchItemsConnection, FederatedSearchUserItemsErrorBody]:
        """This method returns the federated search results of the authenticated user's videos and folders according to
        a search query.

        If no query is provided, the method returns items sorted by the most recent user action.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``video`` - Return videos.
            filter_privacy: A comma-separated list of privacy settings to filter the results by. Possible values include
                ``unlisted`` for videos that are accessible but not searchable from Vimeo, ``password`` for videos on
                Vimeo that anyone can access with the correct password, ``hide-from-vimeo`` for videos that don't appear
                on Vimeo, ``private`` for videos on Vimeo that only their owner can access, and ``public`` for videos on
                Vimeo that anyone can access. By default, all privacy settings are considered.
            modified_end_date: The inclusive end date of the range.
            modified_start_date: The inclusive start date of the range. This value must be earlier than the modified end
                date.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                order. * ``duration`` - Sort the results by duration, where available. * ``folder_path`` - Sort the
                results by the hierarchy of folders. * ``last_user_action_event_date`` - Sort the results by most recent
                user interaction.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/{user_id}/items"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter30OrStr | None]("filter", filter_),
                param[str | None]("filter_privacy", filter_privacy),
                param[str | None]("modified_end_date", modified_end_date),
                param[str | None]("modified_start_date", modified_start_date),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("query_fields", query_fields),
                param[Sort46OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[FederatedSearchItemsConnection],
            error_mapper=federated_search_user_items_error_mapper,
            request_options=request_options,
        )

    def federated_search_user_items_alt1(
        self,
        workspace_uuid: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter30OrStr | None = None,
        filter_privacy: str | None = None,
        modified_end_date: str | None = None,
        modified_start_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort46OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FederatedSearchItemsConnection, FederatedSearchUserItemsAlt1ErrorBody]:
        """This method returns the federated search results of the authenticated user's videos and folders according to
        a search query.

        If no query is provided, the method returns items sorted by the most recent user action.

        Args:
            workspace_uuid: The UUID of the workspace.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``video`` - Return videos.
            filter_privacy: A comma-separated list of privacy settings to filter the results by. Possible values include
                ``unlisted`` for videos that are accessible but not searchable from Vimeo, ``password`` for videos on
                Vimeo that anyone can access with the correct password, ``hide-from-vimeo`` for videos that don't appear
                on Vimeo, ``private`` for videos on Vimeo that only their owner can access, and ``public`` for videos on
                Vimeo that anyone can access. By default, all privacy settings are considered.
            modified_end_date: The inclusive end date of the range.
            modified_start_date: The inclusive start date of the range. This value must be earlier than the modified end
                date.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                order. * ``duration`` - Sort the results by duration, where available. * ``folder_path`` - Sort the
                results by the hierarchy of folders. * ``last_user_action_event_date`` - Sort the results by most recent
                user interaction.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/workspaces/search/{workspace_uuid}/items"),
            path_params=[param[str]("workspace_uuid", workspace_uuid)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter30OrStr | None]("filter", filter_),
                param[str | None]("filter_privacy", filter_privacy),
                param[str | None]("modified_end_date", modified_end_date),
                param[str | None]("modified_start_date", modified_start_date),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("query_fields", query_fields),
                param[Sort46OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[FederatedSearchItemsConnection],
            error_mapper=federated_search_user_items_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncSearchFederatedWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def federated_search_user_items(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter30OrStr | None = None,
        filter_privacy: str | None = None,
        modified_end_date: str | None = None,
        modified_start_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort46OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FederatedSearchItemsConnection, FederatedSearchUserItemsErrorBody]:
        """This method returns the federated search results of the authenticated user's videos and folders according to
        a search query.

        If no query is provided, the method returns items sorted by the most recent user action.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``video`` - Return videos.
            filter_privacy: A comma-separated list of privacy settings to filter the results by. Possible values include
                ``unlisted`` for videos that are accessible but not searchable from Vimeo, ``password`` for videos on
                Vimeo that anyone can access with the correct password, ``hide-from-vimeo`` for videos that don't appear
                on Vimeo, ``private`` for videos on Vimeo that only their owner can access, and ``public`` for videos on
                Vimeo that anyone can access. By default, all privacy settings are considered.
            modified_end_date: The inclusive end date of the range.
            modified_start_date: The inclusive start date of the range. This value must be earlier than the modified end
                date.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                order. * ``duration`` - Sort the results by duration, where available. * ``folder_path`` - Sort the
                results by the hierarchy of folders. * ``last_user_action_event_date`` - Sort the results by most recent
                user interaction.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/{user_id}/items"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter30OrStr | None]("filter", filter_),
                param[str | None]("filter_privacy", filter_privacy),
                param[str | None]("modified_end_date", modified_end_date),
                param[str | None]("modified_start_date", modified_start_date),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("query_fields", query_fields),
                param[Sort46OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[FederatedSearchItemsConnection],
            error_mapper=federated_search_user_items_error_mapper,
            request_options=request_options,
        )

    async def federated_search_user_items_alt1(
        self,
        workspace_uuid: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter30OrStr | None = None,
        filter_privacy: str | None = None,
        modified_end_date: str | None = None,
        modified_start_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort46OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FederatedSearchItemsConnection, FederatedSearchUserItemsAlt1ErrorBody]:
        """This method returns the federated search results of the authenticated user's videos and folders according to
        a search query.

        If no query is provided, the method returns items sorted by the most recent user action.

        Args:
            workspace_uuid: The UUID of the workspace.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``video`` - Return videos.
            filter_privacy: A comma-separated list of privacy settings to filter the results by. Possible values include
                ``unlisted`` for videos that are accessible but not searchable from Vimeo, ``password`` for videos on
                Vimeo that anyone can access with the correct password, ``hide-from-vimeo`` for videos that don't appear
                on Vimeo, ``private`` for videos on Vimeo that only their owner can access, and ``public`` for videos on
                Vimeo that anyone can access. By default, all privacy settings are considered.
            modified_end_date: The inclusive end date of the range.
            modified_start_date: The inclusive start date of the range. This value must be earlier than the modified end
                date.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                order. * ``duration`` - Sort the results by duration, where available. * ``folder_path`` - Sort the
                results by the hierarchy of folders. * ``last_user_action_event_date`` - Sort the results by most recent
                user interaction.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/workspaces/search/{workspace_uuid}/items"),
            path_params=[param[str]("workspace_uuid", workspace_uuid)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter30OrStr | None]("filter", filter_),
                param[str | None]("filter_privacy", filter_privacy),
                param[str | None]("modified_end_date", modified_end_date),
                param[str | None]("modified_start_date", modified_start_date),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("query_fields", query_fields),
                param[Sort46OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[FederatedSearchItemsConnection],
            error_mapper=federated_search_user_items_alt1_error_mapper,
            request_options=request_options,
        )
