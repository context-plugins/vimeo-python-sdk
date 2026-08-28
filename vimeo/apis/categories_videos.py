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
    json_body,
    json_decoder,
    param,
)
from ..errors.check_category_for_video_error import (
    CheckCategoryForVideoErrorBody,
    check_category_for_video_error_mapper,
)
from ..errors.get_category_videos_error import GetCategoryVideosErrorBody, get_category_videos_error_mapper
from ..errors.get_video_categories_error import GetVideoCategoriesErrorBody, get_video_categories_error_mapper
from ..errors.suggest_video_category_error import SuggestVideoCategoryErrorBody, suggest_video_category_error_mapper
from ..models.category import Category
from ..models.category_connection import CategoryConnection
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter import FilterOrStr
from ..models.enums.sort6 import Sort6OrStr
from ..models.video import Video
from ..models.video_connection import VideoConnection
from ..models.videos_categories_request import VideosCategoriesRequest, VideosCategoriesRequestDict
from ..server.server import Server


class CategoriesVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CategoriesVideosWithRawResponse(client, server, auth)

    def check_category_for_video(
        self, category: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video in the specified category. You can use this method to determine whether
        the video belongs to the category.

        Args:
            category: The name of the category.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: * No such category exists, or the video doesn't belong to it. * Error code 5451: This resource is
                restricted in your region. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.check_category_for_video(
            category, video_id, request_options=request_options
        ).unwrap()

    def get_category_videos(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        filter: FilterOrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort6OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``conditional_featured`` -
                Return featured videos. * ``embeddable`` - Return embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``duration`` - Sort the results by duration. * ``featured`` - Sort the results by featured
                status. * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of
                plays. * ``relevant`` - Sort the results by relevance.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: * No such category exists. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_category_videos(
            category,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_video_categories(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoryConnection:
        """This method returns every category that contains the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_video_categories(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def suggest_video_category(
        self,
        video_id: float,
        body: VideosCategoriesRequest | VideosCategoriesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Category:
        """This method sets multiple categories and subcategories for the specified video. Include the categories as a
        JSON block in the body of the request using the **category** field, like this: ``[{ "category": "Tech" }, {
        "category": "Music" }]``. The authenticated user must have edit access to the video. For more information on
        batch requests like this one, see `Using Common Formats and Parameters
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were set.

        Raises:
            ApiError: The authenticated user doesn't own this video. No such video exists, or no such category exists.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.suggest_video_category(video_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CategoriesVideosWithRawResponse:
        return self._with_raw_response


class AsyncCategoriesVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCategoriesVideosWithRawResponse(client, server, auth)

    async def check_category_for_video(
        self, category: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video in the specified category. You can use this method to determine whether
        the video belongs to the category.

        Args:
            category: The name of the category.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: * No such category exists, or the video doesn't belong to it. * Error code 5451: This resource is
                restricted in your region. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.check_category_for_video(category, video_id, request_options=request_options)
        ).unwrap()

    async def get_category_videos(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        filter: FilterOrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort6OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``conditional_featured`` -
                Return featured videos. * ``embeddable`` - Return embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``duration`` - Sort the results by duration. * ``featured`` - Sort the results by featured
                status. * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of
                plays. * ``relevant`` - Sort the results by relevance.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: * No such category exists. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_category_videos(
                category,
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

    async def get_video_categories(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoryConnection:
        """This method returns every category that contains the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_video_categories(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def suggest_video_category(
        self,
        video_id: float,
        body: VideosCategoriesRequest | VideosCategoriesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Category:
        """This method sets multiple categories and subcategories for the specified video. Include the categories as a
        JSON block in the body of the request using the **category** field, like this: ``[{ "category": "Tech" }, {
        "category": "Music" }]``. The authenticated user must have edit access to the video. For more information on
        batch requests like this one, see `Using Common Formats and Parameters
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were set.

        Raises:
            ApiError: The authenticated user doesn't own this video. No such video exists, or no such category exists.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.suggest_video_category(video_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCategoriesVideosWithRawResponse:
        return self._with_raw_response


class CategoriesVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_category_for_video(
        self, category: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckCategoryForVideoErrorBody]:
        """This method returns a single video in the specified category. You can use this method to determine whether
        the video belongs to the category.

        Args:
            category: The name of the category.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}/videos/{video_id}"),
            path_params=[param[str]("category", category), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=check_category_for_video_error_mapper,
            request_options=request_options,
        )

    def get_category_videos(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        filter: FilterOrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort6OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetCategoryVideosErrorBody]:
        """This method returns every video that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``conditional_featured`` -
                Return featured videos. * ``embeddable`` - Return embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``duration`` - Sort the results by duration. * ``featured`` - Sort the results by featured
                status. * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of
                plays. * ``relevant`` - Sort the results by relevance.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}/videos"),
            path_params=[param[str]("category", category)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[FilterOrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort6OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_category_videos_error_mapper,
            request_options=request_options,
        )

    def get_video_categories(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoryConnection, GetVideoCategoriesErrorBody]:
        """This method returns every category that contains the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/categories"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=get_video_categories_error_mapper,
            request_options=request_options,
        )

    def suggest_video_category(
        self,
        video_id: float,
        body: VideosCategoriesRequest | VideosCategoriesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Category, SuggestVideoCategoryErrorBody]:
        """This method sets multiple categories and subcategories for the specified video. Include the categories as a
        JSON block in the body of the request using the **category** field, like this: ``[{ "category": "Tech" }, {
        "category": "Music" }]``. The authenticated user must have edit access to the video. For more information on
        batch requests like this one, see `Using Common Formats and Parameters
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/categories"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosCategoriesRequest | VideosCategoriesRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Category],
            error_mapper=suggest_video_category_error_mapper,
            request_options=request_options,
        )


class AsyncCategoriesVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_category_for_video(
        self, category: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckCategoryForVideoErrorBody]:
        """This method returns a single video in the specified category. You can use this method to determine whether
        the video belongs to the category.

        Args:
            category: The name of the category.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}/videos/{video_id}"),
            path_params=[param[str]("category", category), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=check_category_for_video_error_mapper,
            request_options=request_options,
        )

    async def get_category_videos(
        self,
        category: str,
        *,
        direction: DirectionOrStr | None = None,
        filter: FilterOrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort6OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetCategoryVideosErrorBody]:
        """This method returns every video that belongs to the specified category.

        Args:
            category: The name of the category.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``conditional_featured`` -
                Return featured videos. * ``embeddable`` - Return embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``duration`` - Sort the results by duration. * ``featured`` - Sort the results by featured
                status. * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of
                plays. * ``relevant`` - Sort the results by relevance.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories/{category}/videos"),
            path_params=[param[str]("category", category)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[FilterOrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort6OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_category_videos_error_mapper,
            request_options=request_options,
        )

    async def get_video_categories(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoryConnection, GetVideoCategoriesErrorBody]:
        """This method returns every category that contains the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/categories"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=get_video_categories_error_mapper,
            request_options=request_options,
        )

    async def suggest_video_category(
        self,
        video_id: float,
        body: VideosCategoriesRequest | VideosCategoriesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Category, SuggestVideoCategoryErrorBody]:
        """This method sets multiple categories and subcategories for the specified video. Include the categories as a
        JSON block in the body of the request using the **category** field, like this: ``[{ "category": "Tech" }, {
        "category": "Music" }]``. The authenticated user must have edit access to the video. For more information on
        batch requests like this one, see `Using Common Formats and Parameters
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/categories"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosCategoriesRequest | VideosCategoriesRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Category],
            error_mapper=suggest_video_category_error_mapper,
            request_options=request_options,
        )
