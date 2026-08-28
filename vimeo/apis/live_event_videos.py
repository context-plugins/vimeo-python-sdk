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
    json_body,
    json_decoder,
    param,
)
from ..errors.add_videos_to_live_event_alt1_error import (
    AddVideosToLiveEventAlt1ErrorBody,
    add_videos_to_live_event_alt1_error_mapper,
)
from ..errors.add_videos_to_live_event_alt2_error import (
    AddVideosToLiveEventAlt2ErrorBody,
    add_videos_to_live_event_alt2_error_mapper,
)
from ..errors.add_videos_to_live_event_error import AddVideosToLiveEventErrorBody, add_videos_to_live_event_error_mapper
from ..errors.get_live_event_video_alt1_error import (
    GetLiveEventVideoAlt1ErrorBody,
    get_live_event_video_alt1_error_mapper,
)
from ..errors.get_live_event_video_alt2_error import (
    GetLiveEventVideoAlt2ErrorBody,
    get_live_event_video_alt2_error_mapper,
)
from ..errors.get_live_event_video_error import GetLiveEventVideoErrorBody, get_live_event_video_error_mapper
from ..errors.get_live_event_videos_alt1_error import (
    GetLiveEventVideosAlt1ErrorBody,
    get_live_event_videos_alt1_error_mapper,
)
from ..errors.get_live_event_videos_alt2_error import (
    GetLiveEventVideosAlt2ErrorBody,
    get_live_event_videos_alt2_error_mapper,
)
from ..errors.get_live_event_videos_error import GetLiveEventVideosErrorBody, get_live_event_videos_error_mapper
from ..errors.remove_videos_from_live_event_alt1_error import (
    RemoveVideosFromLiveEventAlt1ErrorBody,
    remove_videos_from_live_event_alt1_error_mapper,
)
from ..errors.remove_videos_from_live_event_alt2_error import (
    RemoveVideosFromLiveEventAlt2ErrorBody,
    remove_videos_from_live_event_alt2_error_mapper,
)
from ..errors.remove_videos_from_live_event_error import (
    RemoveVideosFromLiveEventErrorBody,
    remove_videos_from_live_event_error_mapper,
)
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter3 import Filter3OrStr
from ..models.enums.sort17 import Sort17OrStr
from ..models.live_events_videos_request import LiveEventsVideosRequest, LiveEventsVideosRequestDict
from ..models.live_events_videos_request1 import LiveEventsVideosRequest1, LiveEventsVideosRequest1Dict
from ..models.me_live_events_videos_request import MeLiveEventsVideosRequest, MeLiveEventsVideosRequestDict
from ..models.me_live_events_videos_request1 import MeLiveEventsVideosRequest1, MeLiveEventsVideosRequest1Dict
from ..models.users_live_events_videos_request import UsersLiveEventsVideosRequest, UsersLiveEventsVideosRequestDict
from ..models.users_live_events_videos_request1 import UsersLiveEventsVideosRequest1, UsersLiveEventsVideosRequest1Dict
from ..models.video import Video
from ..models.video_connection import VideoConnection
from ..server.server import Server


class LiveEventVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventVideosWithRawResponse(client, server, auth)

    def add_videos_to_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsVideosRequest1 | UsersLiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't add
                videos to the event. * Error code 3422: The authenticated user can't add one or more of the listed
                videos. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_videos_to_live_event(
            live_event_id, user_id, body=body, request_options=request_options
        ).unwrap()

    def add_videos_to_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsVideosRequest1 | LiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't add
                videos to the event. * Error code 3422: The authenticated user can't add one or more of the listed
                videos. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_videos_to_live_event_alt1(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    def add_videos_to_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsVideosRequest1 | MeLiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't add
                videos to the event. * Error code 3422: The authenticated user can't add one or more of the listed
                videos. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_videos_to_live_event_alt2(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    def get_live_event_video(
        self,
        live_event_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event, video, or user exists.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_live_event_video(
            live_event_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def get_live_event_video_alt1(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event, video, or user exists.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_live_event_video_alt1(
            live_event_id, video_id, request_options=request_options
        ).unwrap()

    def get_live_event_video_alt2(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event, video, or user exists.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_live_event_video_alt2(
            live_event_id, video_id, request_options=request_options
        ).unwrap()

    def get_live_event_videos(
        self,
        live_event_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_live_event_videos(
            live_event_id,
            user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_live_event_videos_alt1(
        self,
        live_event_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_live_event_videos_alt1(
            live_event_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_live_event_videos_alt2(
        self,
        live_event_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_live_event_videos_alt2(
            live_event_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def remove_videos_from_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsVideosRequest | UsersLiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't remove
                one or more of the listed videos. * Error code 3422: The authenticated user can't remove videos from the
                event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.remove_videos_from_live_event(
            live_event_id, user_id, body=body, request_options=request_options
        ).unwrap()

    def remove_videos_from_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsVideosRequest | LiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't remove
                one or more of the listed videos. * Error code 3422: The authenticated user can't remove videos from the
                event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.remove_videos_from_live_event_alt1(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    def remove_videos_from_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsVideosRequest | MeLiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't remove
                one or more of the listed videos. * Error code 3422: The authenticated user can't remove videos from the
                event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.remove_videos_from_live_event_alt2(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveEventVideosWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventVideosWithRawResponse(client, server, auth)

    async def add_videos_to_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsVideosRequest1 | UsersLiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't add
                videos to the event. * Error code 3422: The authenticated user can't add one or more of the listed
                videos. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_videos_to_live_event(
                live_event_id, user_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def add_videos_to_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsVideosRequest1 | LiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't add
                videos to the event. * Error code 3422: The authenticated user can't add one or more of the listed
                videos. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_videos_to_live_event_alt1(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def add_videos_to_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsVideosRequest1 | MeLiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were added.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't add
                videos to the event. * Error code 3422: The authenticated user can't add one or more of the listed
                videos. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_videos_to_live_event_alt2(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_live_event_video(
        self,
        live_event_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event, video, or user exists.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_live_event_video(
                live_event_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_live_event_video_alt1(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event, video, or user exists.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_live_event_video_alt1(
                live_event_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_live_event_video_alt2(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event, video, or user exists.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_live_event_video_alt2(
                live_event_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_live_event_videos(
        self,
        live_event_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_live_event_videos(
                live_event_id,
                user_id,
                containing_uri=containing_uri,
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

    async def get_live_event_videos_alt1(
        self,
        live_event_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_live_event_videos_alt1(
                live_event_id,
                containing_uri=containing_uri,
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

    async def get_live_event_videos_alt2(
        self,
        live_event_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_live_event_videos_alt2(
                live_event_id,
                containing_uri=containing_uri,
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

    async def remove_videos_from_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsVideosRequest | UsersLiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't remove
                one or more of the listed videos. * Error code 3422: The authenticated user can't remove videos from the
                event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.remove_videos_from_live_event(
                live_event_id, user_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def remove_videos_from_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsVideosRequest | LiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't remove
                one or more of the listed videos. * Error code 3422: The authenticated user can't remove videos from the
                event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.remove_videos_from_live_event_alt1(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def remove_videos_from_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsVideosRequest | MeLiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were removed.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't remove
                one or more of the listed videos. * Error code 3422: The authenticated user can't remove videos from the
                event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.remove_videos_from_live_event_alt2(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveEventVideosWithRawResponse:
        return self._with_raw_response


class LiveEventVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_videos_to_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsVideosRequest1 | UsersLiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToLiveEventErrorBody]:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            body=json_body[UsersLiveEventsVideosRequest1 | UsersLiveEventsVideosRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_live_event_error_mapper,
            request_options=request_options,
        )

    def add_videos_to_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsVideosRequest1 | LiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToLiveEventAlt1ErrorBody]:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[LiveEventsVideosRequest1 | LiveEventsVideosRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    def add_videos_to_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsVideosRequest1 | MeLiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToLiveEventAlt2ErrorBody]:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[MeLiveEventsVideosRequest1 | MeLiveEventsVideosRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_live_event_alt2_error_mapper,
            request_options=request_options,
        )

    def get_live_event_video(
        self,
        live_event_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, GetLiveEventVideoErrorBody]:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/videos/{video_id}"),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_live_event_video_error_mapper,
            request_options=request_options,
        )

    def get_live_event_video_alt1(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetLiveEventVideoAlt1ErrorBody]:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/videos/{video_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_live_event_video_alt1_error_mapper,
            request_options=request_options,
        )

    def get_live_event_video_alt2(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetLiveEventVideoAlt2ErrorBody]:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/videos/{video_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_live_event_video_alt2_error_mapper,
            request_options=request_options,
        )

    def get_live_event_videos(
        self,
        live_event_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLiveEventVideosErrorBody]:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_live_event_videos_error_mapper,
            request_options=request_options,
        )

    def get_live_event_videos_alt1(
        self,
        live_event_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLiveEventVideosAlt1ErrorBody]:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_live_event_videos_alt1_error_mapper,
            request_options=request_options,
        )

    def get_live_event_videos_alt2(
        self,
        live_event_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLiveEventVideosAlt2ErrorBody]:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_live_event_videos_alt2_error_mapper,
            request_options=request_options,
        )

    def remove_videos_from_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsVideosRequest | UsersLiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromLiveEventErrorBody]:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            body=json_body[UsersLiveEventsVideosRequest | UsersLiveEventsVideosRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_live_event_error_mapper,
            request_options=request_options,
        )

    def remove_videos_from_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsVideosRequest | LiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromLiveEventAlt1ErrorBody]:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[LiveEventsVideosRequest | LiveEventsVideosRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    def remove_videos_from_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsVideosRequest | MeLiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromLiveEventAlt2ErrorBody]:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[MeLiveEventsVideosRequest | MeLiveEventsVideosRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_live_event_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEventVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_videos_to_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsVideosRequest1 | UsersLiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToLiveEventErrorBody]:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            body=json_body[UsersLiveEventsVideosRequest1 | UsersLiveEventsVideosRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_live_event_error_mapper,
            request_options=request_options,
        )

    async def add_videos_to_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsVideosRequest1 | LiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToLiveEventAlt1ErrorBody]:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[LiveEventsVideosRequest1 | LiveEventsVideosRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    async def add_videos_to_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsVideosRequest1 | MeLiveEventsVideosRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideosToLiveEventAlt2ErrorBody]:
        """This method adds multiple videos to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[MeLiveEventsVideosRequest1 | MeLiveEventsVideosRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_videos_to_live_event_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_video(
        self,
        live_event_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, GetLiveEventVideoErrorBody]:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/videos/{video_id}"),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_live_event_video_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_video_alt1(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetLiveEventVideoAlt1ErrorBody]:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/videos/{video_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_live_event_video_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_video_alt2(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetLiveEventVideoAlt2ErrorBody]:
        """This method returns a single video in the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/videos/{video_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_live_event_video_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_videos(
        self,
        live_event_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLiveEventVideosErrorBody]:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_live_event_videos_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_videos_alt1(
        self,
        live_event_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLiveEventVideosAlt1ErrorBody]:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_live_event_videos_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_videos_alt2(
        self,
        live_event_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort17OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetLiveEventVideosAlt2ErrorBody]:
        """This method returns every video in the specified event.

        Args:
            live_event_id: The ID of the event.
            containing_uri: The page that contains the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable events.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``added`` - Sort the results by most recently
                added videos. * ``alphabetical`` - Sort the results alphabetically. * ``arranged`` - Sort the results in
                the order that the user has arranged the videos. * ``comments`` - Sort the results by number of
                comments. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by duration.
                * ``likes`` - Sort the results by number of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort17OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_live_event_videos_alt2_error_mapper,
            request_options=request_options,
        )

    async def remove_videos_from_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsVideosRequest | UsersLiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromLiveEventErrorBody]:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            body=json_body[UsersLiveEventsVideosRequest | UsersLiveEventsVideosRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_live_event_error_mapper,
            request_options=request_options,
        )

    async def remove_videos_from_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsVideosRequest | LiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromLiveEventAlt1ErrorBody]:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[LiveEventsVideosRequest | LiveEventsVideosRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    async def remove_videos_from_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsVideosRequest | MeLiveEventsVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveVideosFromLiveEventAlt2ErrorBody]:
        """This method removes multiple videos from the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/live_events/{live_event_id}/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            body=json_body[MeLiveEventsVideosRequest | MeLiveEventsVideosRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_videos_from_live_event_alt2_error_mapper,
            request_options=request_options,
        )
