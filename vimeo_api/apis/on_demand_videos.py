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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.add_video_to_vod_error import AddVideoToVodErrorBody, add_video_to_vod_error_mapper
from ..errors.delete_video_from_vod_error import DeleteVideoFromVodErrorBody, delete_video_from_vod_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter29 import Filter29OrStr
from ..models.enums.sort45 import Sort45OrStr
from ..models.on_demand_video import OnDemandVideo
from ..models.on_demand_video_connection import OnDemandVideoConnection
from ..models.ondemand_pages_videos_request import OndemandPagesVideosRequest, OndemandPagesVideosRequestDict
from ..models.video import Video
from ..server.server import Server


class OnDemandVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnDemandVideosWithRawResponse(client, server, auth)

    def add_video_to_vod(
        self,
        ondemand_id: float,
        video_id: float,
        body: OndemandPagesVideosRequest | OndemandPagesVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandVideo:
        """This method adds a video to the specified On Demand page. The authenticated user must be the owner of the
        page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was added.

        Raises:
            ApiError: The video can't be added to this On Demand page. The authenticated user can't add videos to this
                On Demand page. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.add_video_to_vod(ondemand_id, video_id, body, request_options=request_options)
        )

    def delete_video_from_vod(
        self, ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a video from the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was removed.

        Raises:
            ApiError: The authenticated user can't remove videos from this On Demand page. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            self._with_raw_response.delete_video_from_vod(ondemand_id, video_id, request_options=request_options)
        )

    def get_vod_video(
        self, ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video on the specified On Demand page. Use this method to determine whether the
        video is on the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_vod_video(ondemand_id, video_id, request_options=request_options))

    def get_vod_videos(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter29OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort45OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandVideoConnection:
        """This method returns every video on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``all`` - Filter for all
                videos. * ``buy`` - Filter for purchased videos. * ``expiring_soon`` - Filter for videos that expire
                soon. * ``extra`` - Filter for extra footage videos. * ``main`` - Filter for main videos. *
                ``main.viewable`` - Filter for videos that are both the main video and are viewable. * ``rent`` - Filter
                for rented videos. * ``trailer`` - Filter for trailer videos. * ``unwatched`` - Filter for unwatched
                videos. * ``viewable`` - Filter for videos that are viewable. * ``watched`` - Filter for watched videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sorting method. * ``episode`` - Sort the results by episode. * ``manual`` - Sort the
                results manually. * ``name`` - Sort the results by name. * ``purchase_time`` - Sort the results by time
                of purchase. * ``release_date`` - Sort the results by release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_vod_videos(
                ondemand_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> OnDemandVideosWithRawResponse:
        return self._with_raw_response


class AsyncOnDemandVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnDemandVideosWithRawResponse(client, server, auth)

    async def add_video_to_vod(
        self,
        ondemand_id: float,
        video_id: float,
        body: OndemandPagesVideosRequest | OndemandPagesVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandVideo:
        """This method adds a video to the specified On Demand page. The authenticated user must be the owner of the
        page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was added.

        Raises:
            ApiError: The video can't be added to this On Demand page. The authenticated user can't add videos to this
                On Demand page. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.add_video_to_vod(ondemand_id, video_id, body, request_options=request_options)
        )

    async def delete_video_from_vod(
        self, ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a video from the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was removed.

        Raises:
            ApiError: The authenticated user can't remove videos from this On Demand page. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            await self._with_raw_response.delete_video_from_vod(ondemand_id, video_id, request_options=request_options)
        )

    async def get_vod_video(
        self, ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video on the specified On Demand page. Use this method to determine whether the
        video is on the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_vod_video(ondemand_id, video_id, request_options=request_options)
        )

    async def get_vod_videos(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter29OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort45OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnDemandVideoConnection:
        """This method returns every video on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``all`` - Filter for all
                videos. * ``buy`` - Filter for purchased videos. * ``expiring_soon`` - Filter for videos that expire
                soon. * ``extra`` - Filter for extra footage videos. * ``main`` - Filter for main videos. *
                ``main.viewable`` - Filter for videos that are both the main video and are viewable. * ``rent`` - Filter
                for rented videos. * ``trailer`` - Filter for trailer videos. * ``unwatched`` - Filter for unwatched
                videos. * ``viewable`` - Filter for videos that are viewable. * ``watched`` - Filter for watched videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sorting method. * ``episode`` - Sort the results by episode. * ``manual`` - Sort the
                results manually. * ``name`` - Sort the results by name. * ``purchase_time`` - Sort the results by time
                of purchase. * ``release_date`` - Sort the results by release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_vod_videos(
                ondemand_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncOnDemandVideosWithRawResponse:
        return self._with_raw_response


class OnDemandVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_to_vod(
        self,
        ondemand_id: float,
        video_id: float,
        body: OndemandPagesVideosRequest | OndemandPagesVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandVideo, AddVideoToVodErrorBody]:
        """This method adds a video to the specified On Demand page. The authenticated user must be the owner of the
        page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/videos/{video_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesVideosRequest | OndemandPagesVideosRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandVideo],
            error_mapper=add_video_to_vod_error_mapper,
            request_options=request_options,
        )

    def delete_video_from_vod(
        self, ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoFromVodErrorBody]:
        """This method removes a video from the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/videos/{video_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_vod_error_mapper,
            request_options=request_options,
        )

    def get_vod_video(
        self, ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, RawError]:
        """This method returns a single video on the specified On Demand page. Use this method to determine whether the
        video is on the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/videos/{video_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_vod_videos(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter29OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort45OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandVideoConnection, RawError]:
        """This method returns every video on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``all`` - Filter for all
                videos. * ``buy`` - Filter for purchased videos. * ``expiring_soon`` - Filter for videos that expire
                soon. * ``extra`` - Filter for extra footage videos. * ``main`` - Filter for main videos. *
                ``main.viewable`` - Filter for videos that are both the main video and are viewable. * ``rent`` - Filter
                for rented videos. * ``trailer`` - Filter for trailer videos. * ``unwatched`` - Filter for unwatched
                videos. * ``viewable`` - Filter for videos that are viewable. * ``watched`` - Filter for watched videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sorting method. * ``episode`` - Sort the results by episode. * ``manual`` - Sort the
                results manually. * ``name`` - Sort the results by name. * ``purchase_time`` - Sort the results by time
                of purchase. * ``release_date`` - Sort the results by release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/videos"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter29OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort45OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OnDemandVideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncOnDemandVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_to_vod(
        self,
        ondemand_id: float,
        video_id: float,
        body: OndemandPagesVideosRequest | OndemandPagesVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandVideo, AddVideoToVodErrorBody]:
        """This method adds a video to the specified On Demand page. The authenticated user must be the owner of the
        page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/videos/{video_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OndemandPagesVideosRequest | OndemandPagesVideosRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandVideo],
            error_mapper=add_video_to_vod_error_mapper,
            request_options=request_options,
        )

    async def delete_video_from_vod(
        self, ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoFromVodErrorBody]:
        """This method removes a video from the specified On Demand page. The authenticated user must be the owner of
        the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/videos/{video_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_video_from_vod_error_mapper,
            request_options=request_options,
        )

    async def get_vod_video(
        self, ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, RawError]:
        """This method returns a single video on the specified On Demand page. Use this method to determine whether the
        video is on the page.

        Args:
            ondemand_id: The ID of the On Demand page.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/videos/{video_id}"),
            path_params=[param[float]("ondemand_id", ondemand_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_vod_videos(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter29OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort45OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnDemandVideoConnection, RawError]:
        """This method returns every video on the specified On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``all`` - Filter for all
                videos. * ``buy`` - Filter for purchased videos. * ``expiring_soon`` - Filter for videos that expire
                soon. * ``extra`` - Filter for extra footage videos. * ``main`` - Filter for main videos. *
                ``main.viewable`` - Filter for videos that are both the main video and are viewable. * ``rent`` - Filter
                for rented videos. * ``trailer`` - Filter for trailer videos. * ``unwatched`` - Filter for unwatched
                videos. * ``viewable`` - Filter for videos that are viewable. * ``watched`` - Filter for watched videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``date`` - Sort the results by date. * ``default``
                - Use the default sorting method. * ``episode`` - Sort the results by episode. * ``manual`` - Sort the
                results manually. * ``name`` - Sort the results by name. * ``purchase_time`` - Sort the results by time
                of purchase. * ``release_date`` - Sort the results by release date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/videos"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter29OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort45OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[OnDemandVideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
