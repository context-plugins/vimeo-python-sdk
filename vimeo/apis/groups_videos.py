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
from ..errors.add_video_to_group_error import AddVideoToGroupErrorBody, add_video_to_group_error_mapper
from ..errors.delete_video_from_group_error import DeleteVideoFromGroupErrorBody, delete_video_from_group_error_mapper
from ..errors.get_available_video_groups_error import (
    GetAvailableVideoGroupsErrorBody,
    get_available_video_groups_error_mapper,
)
from ..errors.get_group_video_error import GetGroupVideoErrorBody, get_group_video_error_mapper
from ..errors.get_group_videos_error import GetGroupVideosErrorBody, get_group_videos_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter3 import Filter3OrStr
from ..models.enums.sort15 import Sort15OrStr
from ..models.group_connection import GroupConnection
from ..models.video import Video
from ..models.video_connection import VideoConnection
from ..server.server import Server


class GroupsVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GroupsVideosWithRawResponse(client, server, auth)

    def add_video_to_group(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method adds a video to the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: * The video is already in the group. * The authenticated user can't add videos to the group. Error
                code 5451: This resource is restricted in your region. ``error`` is ``LegacyError | Error |
                RawError``."""
        return self._with_raw_response.add_video_to_group(group_id, video_id, request_options=request_options).unwrap()

    def delete_video_from_group(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a video from the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: The authenticated user can't remove the video from the group. Error code 5451: This resource is
                restricted in your region. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.delete_video_from_group(
            group_id, video_id, request_options=request_options
        ).unwrap()

    def get_available_video_groups(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> GroupConnection:
        """This method returns every group to which the authenticated user can add or remove the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The groups were returned.

        Raises:
            ApiError: Error code 3433: The authenticated user can't add the video to or remove the video from any
                groups. Error code 5451: This resource is restricted in your region. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_available_video_groups(video_id, request_options=request_options).unwrap()

    def get_group_video(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video from the specified group. You can use this method to determine whether the
        video belongs to the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: * No such video or group exists. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_group_video(group_id, video_id, request_options=request_options).unwrap()

    def get_group_videos(
        self,
        group_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the specified group.

        Args:
            group_id: The ID of the group.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by
                number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: * No such group exists. * Error code 5451: This resource is restricted in your region. ``error``
                is ``LegacyError | RawError``."""
        return self._with_raw_response.get_group_videos(
            group_id,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> GroupsVideosWithRawResponse:
        return self._with_raw_response


class AsyncGroupsVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGroupsVideosWithRawResponse(client, server, auth)

    async def add_video_to_group(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method adds a video to the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: * The video is already in the group. * The authenticated user can't add videos to the group. Error
                code 5451: This resource is restricted in your region. ``error`` is ``LegacyError | Error |
                RawError``."""
        return (
            await self._with_raw_response.add_video_to_group(group_id, video_id, request_options=request_options)
        ).unwrap()

    async def delete_video_from_group(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a video from the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: The authenticated user can't remove the video from the group. Error code 5451: This resource is
                restricted in your region. ``error`` is ``LegacyError | Error | RawError``."""
        return (
            await self._with_raw_response.delete_video_from_group(group_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_available_video_groups(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> GroupConnection:
        """This method returns every group to which the authenticated user can add or remove the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The groups were returned.

        Raises:
            ApiError: Error code 3433: The authenticated user can't add the video to or remove the video from any
                groups. Error code 5451: This resource is restricted in your region. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_available_video_groups(video_id, request_options=request_options)
        ).unwrap()

    async def get_group_video(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video from the specified group. You can use this method to determine whether the
        video belongs to the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: * No such video or group exists. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_group_video(group_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_group_videos(
        self,
        group_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the specified group.

        Args:
            group_id: The ID of the group.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by
                number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: * No such group exists. * Error code 5451: This resource is restricted in your region. ``error``
                is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_group_videos(
                group_id,
                direction=direction,
                filter=filter,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncGroupsVideosWithRawResponse:
        return self._with_raw_response


class GroupsVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_to_group(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, AddVideoToGroupErrorBody]:
        """This method adds a video to the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/groups/{group_id}/videos/{video_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=add_video_to_group_error_mapper,
            request_options=request_options,
        )

    def delete_video_from_group(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoFromGroupErrorBody]:
        """This method removes a video from the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/groups/{group_id}/videos/{video_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_group_error_mapper,
            request_options=request_options,
        )

    def get_available_video_groups(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupConnection, GetAvailableVideoGroupsErrorBody]:
        """This method returns every group to which the authenticated user can add or remove the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/available_groups"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[GroupConnection],
            error_mapper=get_available_video_groups_error_mapper,
            request_options=request_options,
        )

    def get_group_video(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetGroupVideoErrorBody]:
        """This method returns a single video from the specified group. You can use this method to determine whether the
        video belongs to the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{group_id}/videos/{video_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_group_video_error_mapper,
            request_options=request_options,
        )

    def get_group_videos(
        self,
        group_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetGroupVideosErrorBody]:
        """This method returns every video from the specified group.

        Args:
            group_id: The ID of the group.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by
                number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{group_id}/videos"),
            path_params=[param[float]("group_id", group_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort15OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_group_videos_error_mapper,
            request_options=request_options,
        )


class AsyncGroupsVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_to_group(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, AddVideoToGroupErrorBody]:
        """This method adds a video to the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/groups/{group_id}/videos/{video_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=add_video_to_group_error_mapper,
            request_options=request_options,
        )

    async def delete_video_from_group(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoFromGroupErrorBody]:
        """This method removes a video from the specified group. The authenticated user must be the owner of the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/groups/{group_id}/videos/{video_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_group_error_mapper,
            request_options=request_options,
        )

    async def get_available_video_groups(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupConnection, GetAvailableVideoGroupsErrorBody]:
        """This method returns every group to which the authenticated user can add or remove the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/available_groups"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[GroupConnection],
            error_mapper=get_available_video_groups_error_mapper,
            request_options=request_options,
        )

    async def get_group_video(
        self, group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetGroupVideoErrorBody]:
        """This method returns a single video from the specified group. You can use this method to determine whether the
        video belongs to the group.

        Args:
            group_id: The ID of the group.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{group_id}/videos/{video_id}"),
            path_params=[param[float]("group_id", group_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_group_video_error_mapper,
            request_options=request_options,
        )

    async def get_group_videos(
        self,
        group_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetGroupVideosErrorBody]:
        """This method returns every video from the specified group.

        Args:
            group_id: The ID of the group.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by
                number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{group_id}/videos"),
            path_params=[param[float]("group_id", group_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort15OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_group_videos_error_mapper,
            request_options=request_options,
        )
