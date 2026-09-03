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
    json_decoder,
    param,
)
from ..errors.get_related_videos_error import GetRelatedVideosErrorBody, get_related_videos_error_mapper
from ..models.enums.filter46 import Filter46OrStr
from ..models.video_connection import VideoConnection
from ..server.server import Server


class VideosRecommendations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosRecommendationsWithRawResponse(client, server, auth)

    def get_related_videos(
        self,
        video_id: float,
        *,
        filter: Filter46OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every related video of the specified video.

        Args:
            video_id: The ID of the video.
            filter: The attribute by which to filter the results. Option descriptions: * ``related`` - Return related
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The related videos were returned.

        Raises:
            ApiError: The value of **filter** isn't ``related``. Error code 5451: This resource is restricted in your
                region. ``error`` is ``LegacyError | Error | RawError``."""
        return self._with_raw_response.get_related_videos(
            video_id, filter=filter, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosRecommendationsWithRawResponse:
        return self._with_raw_response


class AsyncVideosRecommendations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosRecommendationsWithRawResponse(client, server, auth)

    async def get_related_videos(
        self,
        video_id: float,
        *,
        filter: Filter46OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every related video of the specified video.

        Args:
            video_id: The ID of the video.
            filter: The attribute by which to filter the results. Option descriptions: * ``related`` - Return related
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The related videos were returned.

        Raises:
            ApiError: The value of **filter** isn't ``related``. Error code 5451: This resource is restricted in your
                region. ``error`` is ``LegacyError | Error | RawError``."""
        return (
            await self._with_raw_response.get_related_videos(
                video_id, filter=filter, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosRecommendationsWithRawResponse:
        return self._with_raw_response


class VideosRecommendationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_related_videos(
        self,
        video_id: float,
        *,
        filter: Filter46OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetRelatedVideosErrorBody]:
        """This method returns every related video of the specified video.

        Args:
            video_id: The ID of the video.
            filter: The attribute by which to filter the results. Option descriptions: * ``related`` - Return related
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/videos"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[Filter46OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_related_videos_error_mapper,
            request_options=request_options,
        )


class AsyncVideosRecommendationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_related_videos(
        self,
        video_id: float,
        *,
        filter: Filter46OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetRelatedVideosErrorBody]:
        """This method returns every related video of the specified video.

        Args:
            video_id: The ID of the video.
            filter: The attribute by which to filter the results. Option descriptions: * ``related`` - Return related
                videos.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/videos"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[Filter46OrStr | None]("filter", filter),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_related_videos_error_mapper,
            request_options=request_options,
        )
