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
from ..errors.add_video_to_channel_error import AddVideoToChannelErrorBody, add_video_to_channel_error_mapper
from ..errors.add_videos_to_channel_error import AddVideosToChannelErrorBody, add_videos_to_channel_error_mapper
from ..errors.delete_video_from_channel_error import (
    DeleteVideoFromChannelErrorBody,
    delete_video_from_channel_error_mapper,
)
from ..errors.get_available_video_channels_error import (
    GetAvailableVideoChannelsErrorBody,
    get_available_video_channels_error_mapper,
)
from ..errors.get_channel_video_error import GetChannelVideoErrorBody, get_channel_video_error_mapper
from ..errors.get_channel_videos_error import GetChannelVideosErrorBody, get_channel_videos_error_mapper
from ..errors.remove_videos_from_channel_error import (
    RemoveVideosFromChannelErrorBody,
    remove_videos_from_channel_error_mapper,
)
from ..models.channel_connection import ChannelConnection
from ..models.channels_videos_request import ChannelsVideosRequest, ChannelsVideosRequestDict
from ..models.channels_videos_request1 import ChannelsVideosRequest1, ChannelsVideosRequest1Dict
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter3 import Filter3OrStr
from ..models.enums.sort10 import Sort10OrStr
from ..models.video import Video
from ..models.video_connection import VideoConnection
from ..server.server import Server


class ChannelsVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChannelsVideosWithRawResponse(client, server, auth)

    def add_video_to_channel(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified channel. The authenticated user must be a moderator of the
        channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: The video can't be added to a channel, or the authenticated user can't add videos to this channel.
                No such channel or video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_to_channel(
            channel_id, video_id, request_options=request_options
        ).unwrap()

    def add_videos_to_channel(
        self,
        channel_id: float,
        body: ChannelsVideosRequest1 | ChannelsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified channel. The authenticated user must be a moderator of the
        channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: The authenticated user can't add videos to the channel, or a video can't be added to the channel.
                No such channel or user exist. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_videos_to_channel(channel_id, body, request_options=request_options).unwrap()

    def delete_video_from_channel(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single video from the specified channel. The authenticated user must be a moderator of
        the channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: The authenticated user can't remove videos from this channel, or the video can't be removed from
                the channel. No such channel or video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_video_from_channel(
            channel_id, video_id, request_options=request_options
        ).unwrap()

    def get_available_video_channels(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ChannelConnection:
        """This method returns every channel to which the authenticated user can add or remove the specified video. The
        authenticated user must be a moderator of the channel.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: The authenticated user can't add or remove this video from a channel. * The authenticated user
                isn't a moderator of the channel. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_available_video_channels(video_id, request_options=request_options).unwrap()

    def get_channel_video(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video in the specified channel. You can use it to determine whether the video is
        in the channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_channel_video(channel_id, video_id, request_options=request_options).unwrap()

    def get_channel_videos(
        self,
        channel_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sizes: str | None = None,
        sort: Sort10OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified channel.

        Args:
            channel_id: The ID of the channel.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by date added. *
                ``alphabetical`` - Sort the results alphabetically. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                method. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``manual`` - Sort the results as the user has arranged them. * ``modified_time`` - Sort the
                results by last modification. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: The **sort** field is ``default``, but the **direction** field has a value. * No such channel
                exists. * Error code 5451: This resource is restricted in your region. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.get_channel_videos(
            channel_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sizes=sizes,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def remove_videos_from_channel(
        self,
        channel_id: float,
        body: ChannelsVideosRequest | ChannelsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified channel. Include the videos by their URI as a JSON
        block in the body of the request using the **video_uri** field, like this: ``[{ "video_uri": "/videos/1234" }, {
        "video_uri": "/videos/1235" }]``. The authenticated user must be a moderator of the channel. For more
        information on batch requests like this one, see `Using Common Formats and Parameters
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: The authenticated user can't remove videos from this channel, or a video can't be removed from the
                channel. No such channel or user exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.remove_videos_from_channel(
            channel_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ChannelsVideosWithRawResponse:
        return self._with_raw_response


class AsyncChannelsVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChannelsVideosWithRawResponse(client, server, auth)

    async def add_video_to_channel(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified channel. The authenticated user must be a moderator of the
        channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: The video can't be added to a channel, or the authenticated user can't add videos to this channel.
                No such channel or video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_to_channel(channel_id, video_id, request_options=request_options)
        ).unwrap()

    async def add_videos_to_channel(
        self,
        channel_id: float,
        body: ChannelsVideosRequest1 | ChannelsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified channel. The authenticated user must be a moderator of the
        channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: The authenticated user can't add videos to the channel, or a video can't be added to the channel.
                No such channel or user exist. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_videos_to_channel(channel_id, body, request_options=request_options)
        ).unwrap()

    async def delete_video_from_channel(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a single video from the specified channel. The authenticated user must be a moderator of
        the channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: The authenticated user can't remove videos from this channel, or the video can't be removed from
                the channel. No such channel or video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_video_from_channel(
                channel_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_available_video_channels(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ChannelConnection:
        """This method returns every channel to which the authenticated user can add or remove the specified video. The
        authenticated user must be a moderator of the channel.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The channels were returned.

        Raises:
            ApiError: The authenticated user can't add or remove this video from a channel. * The authenticated user
                isn't a moderator of the channel. * Error code 5451: This resource is restricted in your region.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_available_video_channels(video_id, request_options=request_options)
        ).unwrap()

    async def get_channel_video(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video in the specified channel. You can use it to determine whether the video is
        in the channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: No such channel exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_channel_video(channel_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_channel_videos(
        self,
        channel_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sizes: str | None = None,
        sort: Sort10OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified channel.

        Args:
            channel_id: The ID of the channel.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by date added. *
                ``alphabetical`` - Sort the results alphabetically. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                method. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``manual`` - Sort the results as the user has arranged them. * ``modified_time`` - Sort the
                results by last modification. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: The **sort** field is ``default``, but the **direction** field has a value. * No such channel
                exists. * Error code 5451: This resource is restricted in your region. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.get_channel_videos(
                channel_id,
                containing_uri=containing_uri,
                direction=direction,
                filter=filter,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sizes=sizes,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def remove_videos_from_channel(
        self,
        channel_id: float,
        body: ChannelsVideosRequest | ChannelsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified channel. Include the videos by their URI as a JSON
        block in the body of the request using the **video_uri** field, like this: ``[{ "video_uri": "/videos/1234" }, {
        "video_uri": "/videos/1235" }]``. The authenticated user must be a moderator of the channel. For more
        information on batch requests like this one, see `Using Common Formats and Parameters
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: The authenticated user can't remove videos from this channel, or a video can't be removed from the
                channel. No such channel or user exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.remove_videos_from_channel(channel_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncChannelsVideosWithRawResponse:
        return self._with_raw_response


class ChannelsVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_to_channel(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToChannelErrorBody]:
        """This method adds a single video to the specified channel. The authenticated user must be a moderator of the
        channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_channel_error_mapper,
            request_options=request_options,
        )

    def add_videos_to_channel(
        self,
        channel_id: float,
        body: ChannelsVideosRequest1 | ChannelsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToChannelErrorBody]:
        """This method adds multiple videos to the specified channel. The authenticated user must be a moderator of the
        channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/videos"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsVideosRequest1 | ChannelsVideosRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_channel_error_mapper,
            request_options=request_options,
        )

    def delete_video_from_channel(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoFromChannelErrorBody]:
        """This method removes a single video from the specified channel. The authenticated user must be a moderator of
        the channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_channel_error_mapper,
            request_options=request_options,
        )

    def get_available_video_channels(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChannelConnection, GetAvailableVideoChannelsErrorBody]:
        """This method returns every channel to which the authenticated user can add or remove the specified video. The
        authenticated user must be a moderator of the channel.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/available_channels"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_available_video_channels_error_mapper,
            request_options=request_options,
        )

    def get_channel_video(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetChannelVideoErrorBody]:
        """This method returns a single video in the specified channel. You can use it to determine whether the video is
        in the channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_channel_video_error_mapper,
            request_options=request_options,
        )

    def get_channel_videos(
        self,
        channel_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sizes: str | None = None,
        sort: Sort10OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetChannelVideosErrorBody]:
        """This method returns every video in the specified channel.

        Args:
            channel_id: The ID of the channel.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by date added. *
                ``alphabetical`` - Sort the results alphabetically. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                method. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``manual`` - Sort the results as the user has arranged them. * ``modified_time`` - Sort the
                results by last modification. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("sizes", sizes),
                param[Sort10OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_channel_videos_error_mapper,
            request_options=request_options,
        )

    def remove_videos_from_channel(
        self,
        channel_id: float,
        body: ChannelsVideosRequest | ChannelsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromChannelErrorBody]:
        """This method removes multiple videos from the specified channel. Include the videos by their URI as a JSON
        block in the body of the request using the **video_uri** field, like this: ``[{ "video_uri": "/videos/1234" }, {
        "video_uri": "/videos/1235" }]``. The authenticated user must be a moderator of the channel. For more
        information on batch requests like this one, see `Using Common Formats and Parameters
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/videos"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsVideosRequest | ChannelsVideosRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_channel_error_mapper,
            request_options=request_options,
        )


class AsyncChannelsVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_to_channel(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToChannelErrorBody]:
        """This method adds a single video to the specified channel. The authenticated user must be a moderator of the
        channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_channel_error_mapper,
            request_options=request_options,
        )

    async def add_videos_to_channel(
        self,
        channel_id: float,
        body: ChannelsVideosRequest1 | ChannelsVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToChannelErrorBody]:
        """This method adds multiple videos to the specified channel. The authenticated user must be a moderator of the
        channel.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/videos"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsVideosRequest1 | ChannelsVideosRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_channel_error_mapper,
            request_options=request_options,
        )

    async def delete_video_from_channel(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoFromChannelErrorBody]:
        """This method removes a single video from the specified channel. The authenticated user must be a moderator of
        the channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_channel_error_mapper,
            request_options=request_options,
        )

    async def get_available_video_channels(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChannelConnection, GetAvailableVideoChannelsErrorBody]:
        """This method returns every channel to which the authenticated user can add or remove the specified video. The
        authenticated user must be a moderator of the channel.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/available_channels"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChannelConnection],
            error_mapper=get_available_video_channels_error_mapper,
            request_options=request_options,
        )

    async def get_channel_video(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetChannelVideoErrorBody]:
        """This method returns a single video in the specified channel. You can use it to determine whether the video is
        in the channel.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_channel_video_error_mapper,
            request_options=request_options,
        )

    async def get_channel_videos(
        self,
        channel_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sizes: str | None = None,
        sort: Sort10OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetChannelVideosErrorBody]:
        """This method returns every video in the specified channel.

        Args:
            channel_id: The ID of the channel.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by date added. *
                ``alphabetical`` - Sort the results alphabetically. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``default`` - Use the default sorting
                method. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``manual`` - Sort the results as the user has arranged them. * ``modified_time`` - Sort the
                results by last modification. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos"),
            path_params=[param[float]("channel_id", channel_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[str | None]("sizes", sizes),
                param[Sort10OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_channel_videos_error_mapper,
            request_options=request_options,
        )

    async def remove_videos_from_channel(
        self,
        channel_id: float,
        body: ChannelsVideosRequest | ChannelsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromChannelErrorBody]:
        """This method removes multiple videos from the specified channel. Include the videos by their URI as a JSON
        block in the body of the request using the **video_uri** field, like this: ``[{ "video_uri": "/videos/1234" }, {
        "video_uri": "/videos/1235" }]``. The authenticated user must be a moderator of the channel. For more
        information on batch requests like this one, see `Using Common Formats and Parameters
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            channel_id: The ID of the channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/channels/{channel_id}/videos"),
            path_params=[param[float]("channel_id", channel_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsVideosRequest | ChannelsVideosRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_channel_error_mapper,
            request_options=request_options,
        )
