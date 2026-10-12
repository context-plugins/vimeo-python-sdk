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
from ..errors.check_watch_later_queue_alt1_error import (
    CheckWatchLaterQueueAlt1ErrorBody,
    check_watch_later_queue_alt1_error_mapper,
)
from ..errors.check_watch_later_queue_error import CheckWatchLaterQueueErrorBody, check_watch_later_queue_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter3 import Filter3OrStr
from ..models.enums.sort15 import Sort15OrStr
from ..models.video import Video
from ..models.video_connection import VideoConnection
from ..server.server import Server


class WatchLaterQueueEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WatchLaterQueueEssentialsWithRawResponse(client, server, auth)

    def add_video_to_watch_later(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the specified video to the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was added.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.add_video_to_watch_later(user_id, video_id, request_options=request_options)
        )

    def add_video_to_watch_later_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the specified video to the authenticated user's Watch Later queue.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was added.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.add_video_to_watch_later_alt1(video_id, request_options=request_options))

    def check_watch_later_queue(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method checks the authenticated user's Watch Later queue for the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video is in the user's Watch Later queue.

        Raises:
            ApiError: The video isn't in the user's Watch Later queue. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.check_watch_later_queue(user_id, video_id, request_options=request_options)
        )

    def check_watch_later_queue_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method checks the authenticated user's Watch Later queue for the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video is in the user's Watch Later queue.

        Raises:
            ApiError: The video isn't in the user's Watch Later queue. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.check_watch_later_queue_alt1(video_id, request_options=request_options))

    def delete_video_from_watch_later(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified video from the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was removed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_video_from_watch_later(user_id, video_id, request_options=request_options)
        )

    def delete_video_from_watch_later_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified video from the authenticated user's Watch Later queue.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was removed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_video_from_watch_later_alt1(video_id, request_options=request_options)
        )

    def get_watch_later_queue(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date added. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number
                of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_watch_later_queue(
                user_id,
                direction=direction,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_watch_later_queue_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the authenticated user's Watch Later queue.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date added. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number
                of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_watch_later_queue_alt1(
                direction=direction,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> WatchLaterQueueEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncWatchLaterQueueEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWatchLaterQueueEssentialsWithRawResponse(client, server, auth)

    async def add_video_to_watch_later(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the specified video to the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was added.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.add_video_to_watch_later(user_id, video_id, request_options=request_options)
        )

    async def add_video_to_watch_later_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds the specified video to the authenticated user's Watch Later queue.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was added.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.add_video_to_watch_later_alt1(video_id, request_options=request_options)
        )

    async def check_watch_later_queue(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method checks the authenticated user's Watch Later queue for the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video is in the user's Watch Later queue.

        Raises:
            ApiError: The video isn't in the user's Watch Later queue. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_watch_later_queue(user_id, video_id, request_options=request_options)
        )

    async def check_watch_later_queue_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method checks the authenticated user's Watch Later queue for the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video is in the user's Watch Later queue.

        Raises:
            ApiError: The video isn't in the user's Watch Later queue. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_watch_later_queue_alt1(video_id, request_options=request_options)
        )

    async def delete_video_from_watch_later(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified video from the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was removed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_video_from_watch_later(
                user_id, video_id, request_options=request_options
            ),
        )

    async def delete_video_from_watch_later_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified video from the authenticated user's Watch Later queue.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was removed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_video_from_watch_later_alt1(video_id, request_options=request_options)
        )

    async def get_watch_later_queue(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date added. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number
                of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_watch_later_queue(
                user_id,
                direction=direction,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_watch_later_queue_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the authenticated user's Watch Later queue.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date added. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number
                of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_watch_later_queue_alt1(
                direction=direction,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWatchLaterQueueEssentialsWithRawResponse:
        return self._with_raw_response


class WatchLaterQueueEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_to_watch_later(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method adds the specified video to the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/watchlater/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def add_video_to_watch_later_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method adds the specified video to the authenticated user's Watch Later queue.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/watchlater/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def check_watch_later_queue(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckWatchLaterQueueErrorBody]:
        """This method checks the authenticated user's Watch Later queue for the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/watchlater/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=check_watch_later_queue_error_mapper,
            request_options=request_options,
        )

    def check_watch_later_queue_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckWatchLaterQueueAlt1ErrorBody]:
        """This method checks the authenticated user's Watch Later queue for the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/watchlater/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=check_watch_later_queue_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_video_from_watch_later(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method removes the specified video from the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/watchlater/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_video_from_watch_later_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method removes the specified video from the authenticated user's Watch Later queue.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/watchlater/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_watch_later_queue(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video from the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date added. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number
                of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/watchlater"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
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
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_watch_later_queue_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video from the authenticated user's Watch Later queue.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date added. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number
                of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/watchlater"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
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
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncWatchLaterQueueEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_to_watch_later(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method adds the specified video to the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/watchlater/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def add_video_to_watch_later_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method adds the specified video to the authenticated user's Watch Later queue.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/watchlater/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def check_watch_later_queue(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckWatchLaterQueueErrorBody]:
        """This method checks the authenticated user's Watch Later queue for the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/watchlater/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=check_watch_later_queue_error_mapper,
            request_options=request_options,
        )

    async def check_watch_later_queue_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckWatchLaterQueueAlt1ErrorBody]:
        """This method checks the authenticated user's Watch Later queue for the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/watchlater/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=check_watch_later_queue_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_video_from_watch_later(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method removes the specified video from the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/watchlater/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_video_from_watch_later_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method removes the specified video from the authenticated user's Watch Later queue.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/watchlater/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_watch_later_queue(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video from the authenticated user's Watch Later queue.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date added. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number
                of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/watchlater"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
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
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_watch_later_queue_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video from the authenticated user's Watch Later queue.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date added. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number
                of likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/watchlater"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
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
            error_mapper=raw_error_response,
            request_options=request_options,
        )
