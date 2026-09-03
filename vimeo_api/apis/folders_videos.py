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
from ..errors.add_video_to_project_alt1_error import (
    AddVideoToProjectAlt1ErrorBody,
    add_video_to_project_alt1_error_mapper,
)
from ..errors.add_video_to_project_error import AddVideoToProjectErrorBody, add_video_to_project_error_mapper
from ..errors.add_videos_to_project_alt1_error import (
    AddVideosToProjectAlt1ErrorBody,
    add_videos_to_project_alt1_error_mapper,
)
from ..errors.add_videos_to_project_error import AddVideosToProjectErrorBody, add_videos_to_project_error_mapper
from ..errors.get_project_videos_alt1_error import GetProjectVideosAlt1ErrorBody, get_project_videos_alt1_error_mapper
from ..errors.get_project_videos_error import GetProjectVideosErrorBody, get_project_videos_error_mapper
from ..errors.remove_video_from_project_alt1_error import (
    RemoveVideoFromProjectAlt1ErrorBody,
    remove_video_from_project_alt1_error_mapper,
)
from ..errors.remove_video_from_project_error import (
    RemoveVideoFromProjectErrorBody,
    remove_video_from_project_error_mapper,
)
from ..errors.remove_videos_from_project_alt1_error import (
    RemoveVideosFromProjectAlt1ErrorBody,
    remove_videos_from_project_alt1_error_mapper,
)
from ..errors.remove_videos_from_project_error import (
    RemoveVideosFromProjectErrorBody,
    remove_videos_from_project_error_mapper,
)
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort37 import Sort37OrStr
from ..models.me_projects_videos_request import MeProjectsVideosRequest, MeProjectsVideosRequestDict
from ..models.me_projects_videos_request1 import MeProjectsVideosRequest1, MeProjectsVideosRequest1Dict
from ..models.users_projects_videos_request import UsersProjectsVideosRequest, UsersProjectsVideosRequestDict
from ..models.users_projects_videos_request1 import UsersProjectsVideosRequest1, UsersProjectsVideosRequest1Dict
from ..models.video_connection import VideoConnection
from ..server.server import Server


class FoldersVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FoldersVideosWithRawResponse(client, server, auth)

    def add_video_to_project(
        self, project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: Error code 5000: No such user, folder, or video exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_video_to_project(
            project_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def add_video_to_project_alt1(
        self, project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: Error code 5000: No such user, folder, or video exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_video_to_project_alt1(
            project_id, video_id, request_options=request_options
        ).unwrap()

    def add_videos_to_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsVideosRequest1 | UsersProjectsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such folder or video exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_videos_to_project(
            project_id, user_id, body, request_options=request_options
        ).unwrap()

    def add_videos_to_project_alt1(
        self,
        project_id: float,
        body: MeProjectsVideosRequest1 | MeProjectsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such folder or video exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_videos_to_project_alt1(
            project_id, body, request_options=request_options
        ).unwrap()

    def get_project_videos(
        self,
        project_id: float,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        include_subfolders: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that belong to the specified folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags. The use of this parameter triggers a search.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
                The use of this parameter triggers a search.
            filter_tag_exclude: A comma-separated list of tags to exclude. The use of this parameter triggers a search.
            include_subfolders: Whether to include subfolders.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by the
                date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_project_videos(
            project_id,
            user_id,
            direction=direction,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_project_videos_alt1(
        self,
        project_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        include_subfolders: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that belong to the specified folder.

        Args:
            project_id: The ID of the folder.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags. The use of this parameter triggers a search.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
                The use of this parameter triggers a search.
            filter_tag_exclude: A comma-separated list of tags to exclude. The use of this parameter triggers a search.
            include_subfolders: Whether to include subfolders.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by the
                date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_project_videos_alt1(
            project_id,
            direction=direction,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def remove_video_from_project(
        self, project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single video from the specified folder. Please note that this doesn't delete the video
        itself.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such video exists in the folder. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.remove_video_from_project(
            project_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def remove_video_from_project_alt1(
        self, project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single video from the specified folder. Please note that this doesn't delete the video
        itself.

        Args:
            project_id: The ID of the folder.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such video exists in the folder. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.remove_video_from_project_alt1(
            project_id, video_id, request_options=request_options
        ).unwrap()

    def remove_videos_from_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsVideosRequest | UsersProjectsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified folder. The authenticated user must be the owner of
        the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such folder exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.remove_videos_from_project(
            project_id, user_id, body, request_options=request_options
        ).unwrap()

    def remove_videos_from_project_alt1(
        self,
        project_id: float,
        body: MeProjectsVideosRequest | MeProjectsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified folder. The authenticated user must be the owner of
        the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such folder exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.remove_videos_from_project_alt1(
            project_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FoldersVideosWithRawResponse:
        return self._with_raw_response


class AsyncFoldersVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFoldersVideosWithRawResponse(client, server, auth)

    async def add_video_to_project(
        self, project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: Error code 5000: No such user, folder, or video exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_video_to_project(
                project_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def add_video_to_project_alt1(
        self, project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: Error code 5000: No such user, folder, or video exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_video_to_project_alt1(
                project_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def add_videos_to_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsVideosRequest1 | UsersProjectsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such folder or video exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_videos_to_project(
                project_id, user_id, body, request_options=request_options
            )
        ).unwrap()

    async def add_videos_to_project_alt1(
        self,
        project_id: float,
        body: MeProjectsVideosRequest1 | MeProjectsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such folder or video exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_videos_to_project_alt1(project_id, body, request_options=request_options)
        ).unwrap()

    async def get_project_videos(
        self,
        project_id: float,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        include_subfolders: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that belong to the specified folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags. The use of this parameter triggers a search.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
                The use of this parameter triggers a search.
            filter_tag_exclude: A comma-separated list of tags to exclude. The use of this parameter triggers a search.
            include_subfolders: Whether to include subfolders.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by the
                date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_project_videos(
                project_id,
                user_id,
                direction=direction,
                filter_tag=filter_tag,
                filter_tag_all_of=filter_tag_all_of,
                filter_tag_exclude=filter_tag_exclude,
                include_subfolders=include_subfolders,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_project_videos_alt1(
        self,
        project_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        include_subfolders: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that belong to the specified folder.

        Args:
            project_id: The ID of the folder.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags. The use of this parameter triggers a search.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
                The use of this parameter triggers a search.
            filter_tag_exclude: A comma-separated list of tags to exclude. The use of this parameter triggers a search.
            include_subfolders: Whether to include subfolders.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by the
                date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 5000: No such folder exists.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_project_videos_alt1(
                project_id,
                direction=direction,
                filter_tag=filter_tag,
                filter_tag_all_of=filter_tag_all_of,
                filter_tag_exclude=filter_tag_exclude,
                include_subfolders=include_subfolders,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def remove_video_from_project(
        self, project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single video from the specified folder. Please note that this doesn't delete the video
        itself.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such video exists in the folder. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.remove_video_from_project(
                project_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def remove_video_from_project_alt1(
        self, project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single video from the specified folder. Please note that this doesn't delete the video
        itself.

        Args:
            project_id: The ID of the folder.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such video exists in the folder. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.remove_video_from_project_alt1(
                project_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def remove_videos_from_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsVideosRequest | UsersProjectsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified folder. The authenticated user must be the owner of
        the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such folder exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.remove_videos_from_project(
                project_id, user_id, body, request_options=request_options
            )
        ).unwrap()

    async def remove_videos_from_project_alt1(
        self,
        project_id: float,
        body: MeProjectsVideosRequest | MeProjectsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified folder. The authenticated user must be the owner of
        the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 8000: The user credentials are invalid. Error
                code 5000: No such folder exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.remove_videos_from_project_alt1(
                project_id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFoldersVideosWithRawResponse:
        return self._with_raw_response


class FoldersVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_to_project(
        self, project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToProjectErrorBody]:
        """This method adds a single video to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos/{video_id}"),
            path_params=[
                param[float]("project_id", project_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_project_error_mapper,
            request_options=request_options,
        )

    def add_video_to_project_alt1(
        self, project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToProjectAlt1ErrorBody]:
        """This method adds a single video to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/projects/{project_id}/videos/{video_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_project_alt1_error_mapper,
            request_options=request_options,
        )

    def add_videos_to_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsVideosRequest1 | UsersProjectsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToProjectErrorBody]:
        """This method adds multiple videos to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsVideosRequest1 | UsersProjectsVideosRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_project_error_mapper,
            request_options=request_options,
        )

    def add_videos_to_project_alt1(
        self,
        project_id: float,
        body: MeProjectsVideosRequest1 | MeProjectsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToProjectAlt1ErrorBody]:
        """This method adds multiple videos to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsVideosRequest1 | MeProjectsVideosRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_project_alt1_error_mapper,
            request_options=request_options,
        )

    def get_project_videos(
        self,
        project_id: float,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        include_subfolders: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetProjectVideosErrorBody]:
        """This method returns all the videos that belong to the specified folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags. The use of this parameter triggers a search.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
                The use of this parameter triggers a search.
            filter_tag_exclude: A comma-separated list of tags to exclude. The use of this parameter triggers a search.
            include_subfolders: Whether to include subfolders.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by the
                date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_tag", filter_tag),
                param[str | None]("filter_tag_all_of", filter_tag_all_of),
                param[str | None]("filter_tag_exclude", filter_tag_exclude),
                param[bool | None]("include_subfolders", include_subfolders),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("query_fields", query_fields),
                param[Sort37OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_project_videos_error_mapper,
            request_options=request_options,
        )

    def get_project_videos_alt1(
        self,
        project_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        include_subfolders: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetProjectVideosAlt1ErrorBody]:
        """This method returns all the videos that belong to the specified folder.

        Args:
            project_id: The ID of the folder.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags. The use of this parameter triggers a search.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
                The use of this parameter triggers a search.
            filter_tag_exclude: A comma-separated list of tags to exclude. The use of this parameter triggers a search.
            include_subfolders: Whether to include subfolders.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by the
                date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_tag", filter_tag),
                param[str | None]("filter_tag_all_of", filter_tag_all_of),
                param[str | None]("filter_tag_exclude", filter_tag_exclude),
                param[bool | None]("include_subfolders", include_subfolders),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("query_fields", query_fields),
                param[Sort37OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_project_videos_alt1_error_mapper,
            request_options=request_options,
        )

    def remove_video_from_project(
        self, project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveVideoFromProjectErrorBody]:
        """This method removes a single video from the specified folder. Please note that this doesn't delete the video
        itself.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos/{video_id}"),
            path_params=[
                param[float]("project_id", project_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_video_from_project_error_mapper,
            request_options=request_options,
        )

    def remove_video_from_project_alt1(
        self, project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveVideoFromProjectAlt1ErrorBody]:
        """This method removes a single video from the specified folder. Please note that this doesn't delete the video
        itself.

        Args:
            project_id: The ID of the folder.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/projects/{project_id}/videos/{video_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_video_from_project_alt1_error_mapper,
            request_options=request_options,
        )

    def remove_videos_from_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsVideosRequest | UsersProjectsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromProjectErrorBody]:
        """This method removes multiple videos from the specified folder. The authenticated user must be the owner of
        the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsVideosRequest | UsersProjectsVideosRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_project_error_mapper,
            request_options=request_options,
        )

    def remove_videos_from_project_alt1(
        self,
        project_id: float,
        body: MeProjectsVideosRequest | MeProjectsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromProjectAlt1ErrorBody]:
        """This method removes multiple videos from the specified folder. The authenticated user must be the owner of
        the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsVideosRequest | MeProjectsVideosRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_project_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncFoldersVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_to_project(
        self, project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToProjectErrorBody]:
        """This method adds a single video to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos/{video_id}"),
            path_params=[
                param[float]("project_id", project_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_project_error_mapper,
            request_options=request_options,
        )

    async def add_video_to_project_alt1(
        self, project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToProjectAlt1ErrorBody]:
        """This method adds a single video to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/projects/{project_id}/videos/{video_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_project_alt1_error_mapper,
            request_options=request_options,
        )

    async def add_videos_to_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsVideosRequest1 | UsersProjectsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToProjectErrorBody]:
        """This method adds multiple videos to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsVideosRequest1 | UsersProjectsVideosRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_project_error_mapper,
            request_options=request_options,
        )

    async def add_videos_to_project_alt1(
        self,
        project_id: float,
        body: MeProjectsVideosRequest1 | MeProjectsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToProjectAlt1ErrorBody]:
        """This method adds multiple videos to the specified folder. The authenticated user must be the owner of the
        folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsVideosRequest1 | MeProjectsVideosRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_project_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_project_videos(
        self,
        project_id: float,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        include_subfolders: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetProjectVideosErrorBody]:
        """This method returns all the videos that belong to the specified folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags. The use of this parameter triggers a search.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
                The use of this parameter triggers a search.
            filter_tag_exclude: A comma-separated list of tags to exclude. The use of this parameter triggers a search.
            include_subfolders: Whether to include subfolders.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by the
                date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_tag", filter_tag),
                param[str | None]("filter_tag_all_of", filter_tag_all_of),
                param[str | None]("filter_tag_exclude", filter_tag_exclude),
                param[bool | None]("include_subfolders", include_subfolders),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("query_fields", query_fields),
                param[Sort37OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_project_videos_error_mapper,
            request_options=request_options,
        )

    async def get_project_videos_alt1(
        self,
        project_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        include_subfolders: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: str | None = None,
        sort: Sort37OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetProjectVideosAlt1ErrorBody]:
        """This method returns all the videos that belong to the specified folder.

        Args:
            project_id: The ID of the folder.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags. The use of this parameter triggers a search.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
                The use of this parameter triggers a search.
            filter_tag_exclude: A comma-separated list of tags to exclude. The use of this parameter triggers a search.
            include_subfolders: Whether to include subfolders.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``default`` - Use the default sort order. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by the
                date of the last user action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_tag", filter_tag),
                param[str | None]("filter_tag_all_of", filter_tag_all_of),
                param[str | None]("filter_tag_exclude", filter_tag_exclude),
                param[bool | None]("include_subfolders", include_subfolders),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("query_fields", query_fields),
                param[Sort37OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_project_videos_alt1_error_mapper,
            request_options=request_options,
        )

    async def remove_video_from_project(
        self, project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveVideoFromProjectErrorBody]:
        """This method removes a single video from the specified folder. Please note that this doesn't delete the video
        itself.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos/{video_id}"),
            path_params=[
                param[float]("project_id", project_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_video_from_project_error_mapper,
            request_options=request_options,
        )

    async def remove_video_from_project_alt1(
        self, project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveVideoFromProjectAlt1ErrorBody]:
        """This method removes a single video from the specified folder. Please note that this doesn't delete the video
        itself.

        Args:
            project_id: The ID of the folder.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/projects/{project_id}/videos/{video_id}"),
            path_params=[param[float]("project_id", project_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_video_from_project_alt1_error_mapper,
            request_options=request_options,
        )

    async def remove_videos_from_project(
        self,
        project_id: float,
        user_id: float,
        body: UsersProjectsVideosRequest | UsersProjectsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromProjectErrorBody]:
        """This method removes multiple videos from the specified folder. The authenticated user must be the owner of
        the folder.

        Args:
            project_id: The ID of the folder.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersProjectsVideosRequest | UsersProjectsVideosRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_project_error_mapper,
            request_options=request_options,
        )

    async def remove_videos_from_project_alt1(
        self,
        project_id: float,
        body: MeProjectsVideosRequest | MeProjectsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromProjectAlt1ErrorBody]:
        """This method removes multiple videos from the specified folder. The authenticated user must be the owner of
        the folder.

        Args:
            project_id: The ID of the folder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/projects/{project_id}/videos"),
            path_params=[param[float]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeProjectsVideosRequest | MeProjectsVideosRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_project_alt1_error_mapper,
            request_options=request_options,
        )
