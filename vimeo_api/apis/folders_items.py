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
    param,
    raw_error_response,
)
from ..errors.delete_folder_items_alt1_error import (
    DeleteFolderItemsAlt1ErrorBody,
    delete_folder_items_alt1_error_mapper,
)
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter21 import Filter21OrStr
from ..models.enums.sort37 import Sort37OrStr
from ..server.server import Server


class FoldersItems:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FoldersItemsWithRawResponse(client, server, auth)

    def delete_folder_items_alt1(
        self,
        project_id: float,
        uris: str,
        *,
        send_to_recently_deleted: bool | None = None,
        should_delete_items: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes all items from the specified folder.

        Args:
            project_id: The ID of the folder.
            uris: A comma-separated list of video, event, or folder URIs to remove. Folder URIs are moved to the library
                root (with their contents).
            send_to_recently_deleted: When ``should_delete_items`` is true, send deleted clips to Recently Deleted
                purgatory (``TYPE_RECENTLY_DELETED``) instead of legacy user delete purgatory.
            should_delete_items: Whether to delete the items when removing them from the folder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The items were removed.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 3200: The authenticated user can't remove
                items from the folder. Error code 8000: The user credentials are invalid. Error code 5000: No such
                folder or video exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.delete_folder_items_alt1(
            project_id,
            uris,
            send_to_recently_deleted=send_to_recently_deleted,
            should_delete_items=should_delete_items,
            request_options=request_options,
        ).unwrap()

    def get_folder_items(
        self,
        project_id: float,
        *,
        clip_privacy_filters: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter21OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns every item that belongs to the specified folder.

        Args:
            project_id: The ID of the folder.
            clip_privacy_filters: A comma-separated list of video privacy types to filter on. The accepted values are
                ``private`` for when only the creator and users with access grants can play the video; ``public`` for
                when anyone can play the video; ``password`` for when only users with the correct password can play the
                video; ``hide_from_vimeo`` for when the video is private but embeddable anywhere; and ``unlisted`` for
                when only users with the link can play the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``folder`` - Filter the results
                by folder. * ``live_event`` - Filter the results by event. * ``video`` - Filter the results by video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. Items without a duration, namely events and folders, are
                grouped by type in ascending alphabetical order, with events first. * ``last_user_action_event_date`` -
                Sort the results by the date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_folder_items(
            project_id,
            clip_privacy_filters=clip_privacy_filters,
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_folder_items2(
        self,
        project_id: float,
        user_id: float,
        *,
        clip_privacy_filters: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter21OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns every item that belongs to the specified folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            clip_privacy_filters: A comma-separated list of video privacy types to filter on. The accepted values are
                ``private`` for when only the creator and users with access grants can play the video; ``public`` for
                when anyone can play the video; ``password`` for when only users with the correct password can play the
                video; ``hide_from_vimeo`` for when the video is private but embeddable anywhere; and ``unlisted`` for
                when only users with the link can play the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``folder`` - Filter the results
                by folder. * ``live_event`` - Filter the results by event. * ``video`` - Filter the results by video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. Items without a duration, namely events and folders, are
                grouped by type in ascending alphabetical order, with events first. * ``last_user_action_event_date`` -
                Sort the results by the date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_folder_items2(
            project_id,
            user_id,
            clip_privacy_filters=clip_privacy_filters,
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FoldersItemsWithRawResponse:
        return self._with_raw_response


class AsyncFoldersItems:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFoldersItemsWithRawResponse(client, server, auth)

    async def delete_folder_items_alt1(
        self,
        project_id: float,
        uris: str,
        *,
        send_to_recently_deleted: bool | None = None,
        should_delete_items: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes all items from the specified folder.

        Args:
            project_id: The ID of the folder.
            uris: A comma-separated list of video, event, or folder URIs to remove. Folder URIs are moved to the library
                root (with their contents).
            send_to_recently_deleted: When ``should_delete_items`` is true, send deleted clips to Recently Deleted
                purgatory (``TYPE_RECENTLY_DELETED``) instead of legacy user delete purgatory.
            should_delete_items: Whether to delete the items when removing them from the folder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The items were removed.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 3200: The authenticated user can't remove
                items from the folder. Error code 8000: The user credentials are invalid. Error code 5000: No such
                folder or video exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.delete_folder_items_alt1(
                project_id,
                uris,
                send_to_recently_deleted=send_to_recently_deleted,
                should_delete_items=should_delete_items,
                request_options=request_options,
            )
        ).unwrap()

    async def get_folder_items(
        self,
        project_id: float,
        *,
        clip_privacy_filters: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter21OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns every item that belongs to the specified folder.

        Args:
            project_id: The ID of the folder.
            clip_privacy_filters: A comma-separated list of video privacy types to filter on. The accepted values are
                ``private`` for when only the creator and users with access grants can play the video; ``public`` for
                when anyone can play the video; ``password`` for when only users with the correct password can play the
                video; ``hide_from_vimeo`` for when the video is private but embeddable anywhere; and ``unlisted`` for
                when only users with the link can play the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``folder`` - Filter the results
                by folder. * ``live_event`` - Filter the results by event. * ``video`` - Filter the results by video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. Items without a duration, namely events and folders, are
                grouped by type in ascending alphabetical order, with events first. * ``last_user_action_event_date`` -
                Sort the results by the date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_folder_items(
                project_id,
                clip_privacy_filters=clip_privacy_filters,
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_folder_items2(
        self,
        project_id: float,
        user_id: float,
        *,
        clip_privacy_filters: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter21OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method returns every item that belongs to the specified folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            clip_privacy_filters: A comma-separated list of video privacy types to filter on. The accepted values are
                ``private`` for when only the creator and users with access grants can play the video; ``public`` for
                when anyone can play the video; ``password`` for when only users with the correct password can play the
                video; ``hide_from_vimeo`` for when the video is private but embeddable anywhere; and ``unlisted`` for
                when only users with the link can play the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``folder`` - Filter the results
                by folder. * ``live_event`` - Filter the results by event. * ``video`` - Filter the results by video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. Items without a duration, namely events and folders, are
                grouped by type in ascending alphabetical order, with events first. * ``last_user_action_event_date`` -
                Sort the results by the date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_folder_items2(
                project_id,
                user_id,
                clip_privacy_filters=clip_privacy_filters,
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFoldersItemsWithRawResponse:
        return self._with_raw_response


class FoldersItemsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_folder_items_alt1(
        self,
        project_id: float,
        uris: str,
        *,
        send_to_recently_deleted: bool | None = None,
        should_delete_items: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteFolderItemsAlt1ErrorBody]:
        """This method removes all items from the specified folder.

        Args:
            project_id: The ID of the folder.
            uris: A comma-separated list of video, event, or folder URIs to remove. Folder URIs are moved to the library
                root (with their contents).
            send_to_recently_deleted: When ``should_delete_items`` is true, send deleted clips to Recently Deleted
                purgatory (``TYPE_RECENTLY_DELETED``) instead of legacy user delete purgatory.
            should_delete_items: Whether to delete the items when removing them from the folder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/projects/{project_id}/items"),
            path_params=[param[float]("project_id", project_id)],
            query_params=[
                param[str]("uris", uris),
                param[bool | None]("send_to_recently_deleted", send_to_recently_deleted),
                param[bool | None]("should_delete_items", should_delete_items),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_folder_items_alt1_error_mapper,
            request_options=request_options,
        )

    def get_folder_items(
        self,
        project_id: float,
        *,
        clip_privacy_filters: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter21OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """This method returns every item that belongs to the specified folder.

        Args:
            project_id: The ID of the folder.
            clip_privacy_filters: A comma-separated list of video privacy types to filter on. The accepted values are
                ``private`` for when only the creator and users with access grants can play the video; ``public`` for
                when anyone can play the video; ``password`` for when only users with the correct password can play the
                video; ``hide_from_vimeo`` for when the video is private but embeddable anywhere; and ``unlisted`` for
                when only users with the link can play the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``folder`` - Filter the results
                by folder. * ``live_event`` - Filter the results by event. * ``video`` - Filter the results by video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. Items without a duration, namely events and folders, are
                grouped by type in ascending alphabetical order, with events first. * ``last_user_action_event_date`` -
                Sort the results by the date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/projects/{project_id}/items"),
            path_params=[param[float]("project_id", project_id)],
            query_params=[
                param[str | None]("clip_privacy_filters", clip_privacy_filters),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter21OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort37OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_folder_items2(
        self,
        project_id: float,
        user_id: float,
        *,
        clip_privacy_filters: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter21OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """This method returns every item that belongs to the specified folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            clip_privacy_filters: A comma-separated list of video privacy types to filter on. The accepted values are
                ``private`` for when only the creator and users with access grants can play the video; ``public`` for
                when anyone can play the video; ``password`` for when only users with the correct password can play the
                video; ``hide_from_vimeo`` for when the video is private but embeddable anywhere; and ``unlisted`` for
                when only users with the link can play the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``folder`` - Filter the results
                by folder. * ``live_event`` - Filter the results by event. * ``video`` - Filter the results by video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. Items without a duration, namely events and folders, are
                grouped by type in ascending alphabetical order, with events first. * ``last_user_action_event_date`` -
                Sort the results by the date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/items"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("clip_privacy_filters", clip_privacy_filters),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter21OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort37OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFoldersItemsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_folder_items_alt1(
        self,
        project_id: float,
        uris: str,
        *,
        send_to_recently_deleted: bool | None = None,
        should_delete_items: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteFolderItemsAlt1ErrorBody]:
        """This method removes all items from the specified folder.

        Args:
            project_id: The ID of the folder.
            uris: A comma-separated list of video, event, or folder URIs to remove. Folder URIs are moved to the library
                root (with their contents).
            send_to_recently_deleted: When ``should_delete_items`` is true, send deleted clips to Recently Deleted
                purgatory (``TYPE_RECENTLY_DELETED``) instead of legacy user delete purgatory.
            should_delete_items: Whether to delete the items when removing them from the folder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/projects/{project_id}/items"),
            path_params=[param[float]("project_id", project_id)],
            query_params=[
                param[str]("uris", uris),
                param[bool | None]("send_to_recently_deleted", send_to_recently_deleted),
                param[bool | None]("should_delete_items", should_delete_items),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_folder_items_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_folder_items(
        self,
        project_id: float,
        *,
        clip_privacy_filters: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter21OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """This method returns every item that belongs to the specified folder.

        Args:
            project_id: The ID of the folder.
            clip_privacy_filters: A comma-separated list of video privacy types to filter on. The accepted values are
                ``private`` for when only the creator and users with access grants can play the video; ``public`` for
                when anyone can play the video; ``password`` for when only users with the correct password can play the
                video; ``hide_from_vimeo`` for when the video is private but embeddable anywhere; and ``unlisted`` for
                when only users with the link can play the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``folder`` - Filter the results
                by folder. * ``live_event`` - Filter the results by event. * ``video`` - Filter the results by video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. Items without a duration, namely events and folders, are
                grouped by type in ascending alphabetical order, with events first. * ``last_user_action_event_date`` -
                Sort the results by the date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/projects/{project_id}/items"),
            path_params=[param[float]("project_id", project_id)],
            query_params=[
                param[str | None]("clip_privacy_filters", clip_privacy_filters),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter21OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort37OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_folder_items2(
        self,
        project_id: float,
        user_id: float,
        *,
        clip_privacy_filters: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter21OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """This method returns every item that belongs to the specified folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            clip_privacy_filters: A comma-separated list of video privacy types to filter on. The accepted values are
                ``private`` for when only the creator and users with access grants can play the video; ``public`` for
                when anyone can play the video; ``password`` for when only users with the correct password can play the
                video; ``hide_from_vimeo`` for when the video is private but embeddable anywhere; and ``unlisted`` for
                when only users with the link can play the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``folder`` - Filter the results
                by folder. * ``live_event`` - Filter the results by event. * ``video`` - Filter the results by video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. Items without a duration, namely events and folders, are
                grouped by type in ascending alphabetical order, with events first. * ``last_user_action_event_date`` -
                Sort the results by the date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/items"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("clip_privacy_filters", clip_privacy_filters),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter21OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort37OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
