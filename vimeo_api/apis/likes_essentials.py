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
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.check_if_user_liked_video_alt1_error import (
    CheckIfUserLikedVideoAlt1ErrorBody,
    check_if_user_liked_video_alt1_error_mapper,
)
from ..errors.check_if_user_liked_video_error import (
    CheckIfUserLikedVideoErrorBody,
    check_if_user_liked_video_error_mapper,
)
from ..errors.get_likes_alt1_error import GetLikesAlt1ErrorBody, get_likes_alt1_error_mapper
from ..errors.get_likes_error import GetLikesErrorBody, get_likes_error_mapper
from ..errors.get_vod_likes_error import GetVodLikesErrorBody, get_vod_likes_error_mapper
from ..errors.like_video_alt1_error import LikeVideoAlt1ErrorBody, like_video_alt1_error_mapper
from ..errors.like_video_error import LikeVideoErrorBody, like_video_error_mapper
from ..errors.unlike_video_alt1_error import UnlikeVideoAlt1ErrorBody, unlike_video_alt1_error_mapper
from ..errors.unlike_video_error import UnlikeVideoErrorBody, unlike_video_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter3 import Filter3OrStr
from ..models.enums.filter25 import Filter25OrStr
from ..models.enums.sort8 import Sort8OrStr
from ..models.enums.sort15 import Sort15OrStr
from ..models.user_connection import UserConnection
from ..models.video_connection import VideoConnection
from ..server.server import Server


class LikesEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LikesEssentialsWithRawResponse(client, server, auth)

    def check_if_user_liked_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method checks if the authenticated user has liked the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user has liked the video.

        Raises:
            ApiError: The user hasn't liked the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.check_if_user_liked_video(user_id, video_id, request_options=request_options)
        )

    def check_if_user_liked_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method checks if the authenticated user has liked the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user has liked the video.

        Raises:
            ApiError: The user hasn't liked the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.check_if_user_liked_video_alt1(video_id, request_options=request_options))

    def get_likes(
        self,
        user_id: float,
        *,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video that the authenticated user has liked.

        Args:
            user_id: The ID of the user.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_likes(
                user_id,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_likes_alt1(
        self,
        *,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video that the authenticated user has liked.

        Args:
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_likes_alt1(
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_video_likes(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has liked the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_video_likes(
                video_id, direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
            ),
        )

    def get_video_likes_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has liked the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_video_likes_alt1(
                channel_id,
                video_id,
                direction=direction,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_vod_likes(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter25OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has liked the specified video on an On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``extra`` - Consider extra
                content only. * ``main`` - Consider main content only. * ``trailer`` - Consider trailer content only.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_vod_likes(
                ondemand_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    def like_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to like the specified video. The user can't like their own video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was liked.

        Raises:
            ApiError: The authenticated user owns the video and can't like it. The authenticated user can't like videos.
                ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.like_video(user_id, video_id, request_options=request_options))

    def like_video_alt1(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method causes the authenticated user to like the specified video. The user can't like their own video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was liked.

        Raises:
            ApiError: The authenticated user owns the video and can't like it. The authenticated user can't like videos.
                ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.like_video_alt1(video_id, request_options=request_options))

    def unlike_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to unlike the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was unliked.

        Raises:
            ApiError: The authenticated user can't like videos. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.unlike_video(user_id, video_id, request_options=request_options))

    def unlike_video_alt1(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method causes the authenticated user to unlike the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was unliked.

        Raises:
            ApiError: The authenticated user can't like videos. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.unlike_video_alt1(video_id, request_options=request_options))

    @property
    def with_raw_response(self) -> LikesEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncLikesEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLikesEssentialsWithRawResponse(client, server, auth)

    async def check_if_user_liked_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method checks if the authenticated user has liked the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user has liked the video.

        Raises:
            ApiError: The user hasn't liked the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_if_user_liked_video(user_id, video_id, request_options=request_options)
        )

    async def check_if_user_liked_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method checks if the authenticated user has liked the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The user has liked the video.

        Raises:
            ApiError: The user hasn't liked the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_if_user_liked_video_alt1(video_id, request_options=request_options)
        )

    async def get_likes(
        self,
        user_id: float,
        *,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video that the authenticated user has liked.

        Args:
            user_id: The ID of the user.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_likes(
                user_id,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_likes_alt1(
        self,
        *,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video that the authenticated user has liked.

        Args:
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_likes_alt1(
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_video_likes(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has liked the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_video_likes(
                video_id, direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
            ),
        )

    async def get_video_likes_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has liked the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_video_likes_alt1(
                channel_id,
                video_id,
                direction=direction,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_vod_likes(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter25OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has liked the specified video on an On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``extra`` - Consider extra
                content only. * ``main`` - Consider main content only. * ``trailer`` - Consider trailer content only.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The users were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_vod_likes(
                ondemand_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def like_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to like the specified video. The user can't like their own video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was liked.

        Raises:
            ApiError: The authenticated user owns the video and can't like it. The authenticated user can't like videos.
                ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.like_video(user_id, video_id, request_options=request_options))

    async def like_video_alt1(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method causes the authenticated user to like the specified video. The user can't like their own video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was liked.

        Raises:
            ApiError: The authenticated user owns the video and can't like it. The authenticated user can't like videos.
                ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.like_video_alt1(video_id, request_options=request_options))

    async def unlike_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to unlike the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was unliked.

        Raises:
            ApiError: The authenticated user can't like videos. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.unlike_video(user_id, video_id, request_options=request_options))

    async def unlike_video_alt1(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method causes the authenticated user to unlike the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was unliked.

        Raises:
            ApiError: The authenticated user can't like videos. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.unlike_video_alt1(video_id, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncLikesEssentialsWithRawResponse:
        return self._with_raw_response


class LikesEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_if_user_liked_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserLikedVideoErrorBody]:
        """This method checks if the authenticated user has liked the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/likes/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_liked_video_error_mapper,
            request_options=request_options,
        )

    def check_if_user_liked_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserLikedVideoAlt1ErrorBody]:
        """This method checks if the authenticated user has liked the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/likes/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_liked_video_alt1_error_mapper,
            request_options=request_options,
        )

    def get_likes(
        self,
        user_id: float,
        *,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLikesErrorBody]:
        """This method returns every video that the authenticated user has liked.

        Args:
            user_id: The ID of the user.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/likes"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[Filter3OrStr | None]("filter", filter_),
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
            error_mapper=get_likes_error_mapper,
            request_options=request_options,
        )

    def get_likes_alt1(
        self,
        *,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLikesAlt1ErrorBody]:
        """This method returns every video that the authenticated user has liked.

        Args:
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/likes"),
            query_params=[
                param[Filter3OrStr | None]("filter", filter_),
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
            error_mapper=get_likes_alt1_error_mapper,
            request_options=request_options,
        )

    def get_video_likes(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every user who has liked the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/likes"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_video_likes_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every user who has liked the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/likes"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_vod_likes(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter25OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetVodLikesErrorBody]:
        """This method returns every user who has liked the specified video on an On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``extra`` - Consider extra
                content only. * ``main`` - Consider main content only. * ``trailer`` - Consider trailer content only.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/likes"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter25OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_vod_likes_error_mapper,
            request_options=request_options,
        )

    def like_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, LikeVideoErrorBody]:
        """This method causes the authenticated user to like the specified video. The user can't like their own video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/likes/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=like_video_error_mapper,
            request_options=request_options,
        )

    def like_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, LikeVideoAlt1ErrorBody]:
        """This method causes the authenticated user to like the specified video. The user can't like their own video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/likes/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=like_video_alt1_error_mapper,
            request_options=request_options,
        )

    def unlike_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnlikeVideoErrorBody]:
        """This method causes the authenticated user to unlike the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/likes/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=unlike_video_error_mapper,
            request_options=request_options,
        )

    def unlike_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnlikeVideoAlt1ErrorBody]:
        """This method causes the authenticated user to unlike the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/likes/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=unlike_video_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncLikesEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_if_user_liked_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserLikedVideoErrorBody]:
        """This method checks if the authenticated user has liked the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/likes/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=check_if_user_liked_video_error_mapper,
            request_options=request_options,
        )

    async def check_if_user_liked_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserLikedVideoAlt1ErrorBody]:
        """This method checks if the authenticated user has liked the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/likes/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=check_if_user_liked_video_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_likes(
        self,
        user_id: float,
        *,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLikesErrorBody]:
        """This method returns every video that the authenticated user has liked.

        Args:
            user_id: The ID of the user.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/likes"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[Filter3OrStr | None]("filter", filter_),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort15OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[VideoConnection],
            error_mapper=get_likes_error_mapper,
            request_options=request_options,
        )

    async def get_likes_alt1(
        self,
        *,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLikesAlt1ErrorBody]:
        """This method returns every video that the authenticated user has liked.

        Args:
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/likes"),
            query_params=[
                param[Filter3OrStr | None]("filter", filter_),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort15OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[VideoConnection],
            error_mapper=get_likes_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_video_likes(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every user who has liked the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/likes"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[UserConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_video_likes_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every user who has liked the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/likes"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[UserConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_vod_likes(
        self,
        ondemand_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter25OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetVodLikesErrorBody]:
        """This method returns every user who has liked the specified video on an On Demand page.

        Args:
            ondemand_id: The ID of the On Demand page.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``extra`` - Consider extra
                content only. * ``main`` - Consider main content only. * ``trailer`` - Consider trailer content only.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by join date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ondemand/pages/{ondemand_id}/likes"),
            path_params=[param[float]("ondemand_id", ondemand_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter25OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[UserConnection],
            error_mapper=get_vod_likes_error_mapper,
            request_options=request_options,
        )

    async def like_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, LikeVideoErrorBody]:
        """This method causes the authenticated user to like the specified video. The user can't like their own video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/likes/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=like_video_error_mapper,
            request_options=request_options,
        )

    async def like_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, LikeVideoAlt1ErrorBody]:
        """This method causes the authenticated user to like the specified video. The user can't like their own video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/likes/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=like_video_alt1_error_mapper,
            request_options=request_options,
        )

    async def unlike_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnlikeVideoErrorBody]:
        """This method causes the authenticated user to unlike the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/likes/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=unlike_video_error_mapper,
            request_options=request_options,
        )

    async def unlike_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, UnlikeVideoAlt1ErrorBody]:
        """This method causes the authenticated user to unlike the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/likes/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=unlike_video_alt1_error_mapper,
            request_options=request_options,
        )
