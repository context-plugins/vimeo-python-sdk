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
from ..errors.add_video_to_showcase_alt2_error import (
    AddVideoToShowcaseAlt2ErrorBody,
    add_video_to_showcase_alt2_error_mapper,
)
from ..errors.add_video_to_showcase_error import AddVideoToShowcaseErrorBody, add_video_to_showcase_error_mapper
from ..errors.get_available_showcase_videos_error import (
    GetAvailableShowcaseVideosErrorBody,
    get_available_showcase_videos_error_mapper,
)
from ..errors.get_available_video_showcases_error import (
    GetAvailableVideoShowcasesErrorBody,
    get_available_video_showcases_error_mapper,
)
from ..errors.get_showcase_video_alt2_error import GetShowcaseVideoAlt2ErrorBody, get_showcase_video_alt2_error_mapper
from ..errors.get_showcase_video_error import GetShowcaseVideoErrorBody, get_showcase_video_error_mapper
from ..errors.get_showcase_videos_alt2_error import (
    GetShowcaseVideosAlt2ErrorBody,
    get_showcase_videos_alt2_error_mapper,
)
from ..errors.get_showcase_videos_error import GetShowcaseVideosErrorBody, get_showcase_videos_error_mapper
from ..errors.remove_video_from_showcase_alt2_error import (
    RemoveVideoFromShowcaseAlt2ErrorBody,
    remove_video_from_showcase_alt2_error_mapper,
)
from ..errors.remove_video_from_showcase_error import (
    RemoveVideoFromShowcaseErrorBody,
    remove_video_from_showcase_error_mapper,
)
from ..errors.replace_videos_in_showcase_alt2_error import (
    ReplaceVideosInShowcaseAlt2ErrorBody,
    replace_videos_in_showcase_alt2_error_mapper,
)
from ..errors.replace_videos_in_showcase_error import (
    ReplaceVideosInShowcaseErrorBody,
    replace_videos_in_showcase_error_mapper,
)
from ..errors.set_video_as_showcase_featured_alt2_error import (
    SetVideoAsShowcaseFeaturedAlt2ErrorBody,
    set_video_as_showcase_featured_alt2_error_mapper,
)
from ..errors.set_video_as_showcase_featured_error import (
    SetVideoAsShowcaseFeaturedErrorBody,
    set_video_as_showcase_featured_error_mapper,
)
from ..errors.set_video_as_showcase_thumbnail_alt2_error import (
    SetVideoAsShowcaseThumbnailAlt2ErrorBody,
    set_video_as_showcase_thumbnail_alt2_error_mapper,
)
from ..errors.set_video_as_showcase_thumbnail_error import (
    SetVideoAsShowcaseThumbnailErrorBody,
    set_video_as_showcase_thumbnail_error_mapper,
)
from ..models.album import Album
from ..models.album_connection import AlbumConnection
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter10 import Filter10OrStr
from ..models.enums.sort2 import Sort2OrStr
from ..models.enums.sort21 import Sort21OrStr
from ..models.enums.sort74 import Sort74OrStr
from ..models.me_albums_videos_request import MeAlbumsVideosRequest, MeAlbumsVideosRequestDict
from ..models.me_albums_videos_set_album_thumbnail_request import (
    MeAlbumsVideosSetAlbumThumbnailRequest,
    MeAlbumsVideosSetAlbumThumbnailRequestDict,
)
from ..models.users_albums_videos_request import UsersAlbumsVideosRequest, UsersAlbumsVideosRequestDict
from ..models.users_albums_videos_video_id_set_album_thumbnail_request import (
    UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest,
    UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict,
)
from ..models.video import Video
from ..models.video_connection import VideoConnection
from ..server.server import Server


class ShowcasesShowcaseVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ShowcasesShowcaseVideosWithRawResponse(client, server, auth)

    def add_video_to_showcase(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't add videos to
                the showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_to_showcase(
            album_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def add_video_to_showcase_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't add videos to
                the showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_to_showcase_alt2(
            album_id, video_id, request_options=request_options
        ).unwrap()

    def get_available_showcase_videos(
        self,
        album_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video belonging to the authenticated user that can be added to or removed from the
        specified showcase.

        Args:
            album_id: The ID of the showcase.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``last_user_action_event_date`` - Sort the results by most recent user interaction. *
                ``likes`` - Sort the results by number of likes. * ``modified_time`` - Sort the results by last
                modification. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't add videos to this showcase. No such showcase
                exists. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.get_available_showcase_videos(
            album_id,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_available_video_showcases(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort74OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlbumConnection:
        """This method returns every showcase to which the authenticated user can add or remove the specified video. The
        user must be the owner of the showcase.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by
                duration. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcases were returned.

        Raises:
            ApiError: Error code 3433: The authenticated user can't add the video to or remove the video from any
                showcases. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_available_video_showcases(
            video_id,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_showcase_video(
        self,
        album_id: float,
        user_id: float,
        video_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method returns a single video belonging to the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            password: The password of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: No such showcase exists, or the video doesn't belong to it. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.get_showcase_video(
            album_id, user_id, video_id, password=password, request_options=request_options
        ).unwrap()

    def get_showcase_video_alt2(
        self,
        album_id: float,
        video_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method returns a single video belonging to the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            password: The password of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: No such showcase exists, or the video doesn't belong to it. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.get_showcase_video_alt2(
            album_id, video_id, password=password, request_options=request_options
        ).unwrap()

    def get_showcase_videos(
        self,
        album_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter10OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        password: str | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort21OrStr | None = None,
        weak_search: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            containing_uri: The page containing the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Filter the
                results by the **embeddable** attribute. * ``playable`` - Filter the results by the **playable**
                attribute.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            password: The password of the showcase.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``likes`` - Sort the results by number of likes. * ``manual`` - Sort the results by their
                manual order. * ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the
                results by number of plays.
            weak_search: Whether to include private videos in the search. Please note that a separate search service
                provides this functionality. The service performs a partial text search on the video's name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_showcase_videos(
            album_id,
            user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            password=password,
            per_page=per_page,
            query=query,
            sort=sort,
            weak_search=weak_search,
            request_options=request_options,
        ).unwrap()

    def get_showcase_videos_alt2(
        self,
        album_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter10OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        password: str | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort21OrStr | None = None,
        weak_search: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            containing_uri: The page containing the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Filter the
                results by the **embeddable** attribute. * ``playable`` - Filter the results by the **playable**
                attribute.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            password: The password of the showcase.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``likes`` - Sort the results by number of likes. * ``manual`` - Sort the results by their
                manual order. * ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the
                results by number of plays.
            weak_search: Whether to include private videos in the search. Please note that a separate search service
                provides this functionality. The service performs a partial text search on the video's name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_showcase_videos_alt2(
            album_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            password=password,
            per_page=per_page,
            query=query,
            sort=sort,
            weak_search=weak_search,
            request_options=request_options,
        ).unwrap()

    def remove_video_from_showcase(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified video from its showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't remove videos
                from the showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.remove_video_from_showcase(
            album_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def remove_video_from_showcase_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified video from its showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't remove videos
                from the showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.remove_video_from_showcase_alt2(
            album_id, video_id, request_options=request_options
        ).unwrap()

    def replace_videos_in_showcase(
        self,
        album_id: float,
        user_id: float,
        body: UsersAlbumsVideosRequest | UsersAlbumsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method replaces all the videos in the specified showcase with a new set of one or more videos. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were replaced.

        Raises:
            ApiError: The authenticated user can't add videos to the showcase. No such showcase exists. ``error`` is
                ``LegacyError | RawError``."""
        return self._with_raw_response.replace_videos_in_showcase(
            album_id, user_id, body, request_options=request_options
        ).unwrap()

    def replace_videos_in_showcase_alt2(
        self,
        album_id: float,
        body: MeAlbumsVideosRequest | MeAlbumsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method replaces all the videos in the specified showcase with a new set of one or more videos. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were replaced.

        Raises:
            ApiError: The authenticated user can't add videos to the showcase. No such showcase exists. ``error`` is
                ``LegacyError | RawError``."""
        return self._with_raw_response.replace_videos_in_showcase_alt2(
            album_id, body, request_options=request_options
        ).unwrap()

    def set_video_as_showcase_featured(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Album:
        """This method sets the featured video of the specified showcase. The authenticated user must be the owner of
        the showcase, and the featured video must belong to it.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video is now the featured video of the showcase.

        Raises:
            ApiError: Error code 3429: The authenticated user can't set the featured video of this showcase. Error code
                5000: No such showcase, user, or video exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.set_video_as_showcase_featured(
            album_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def set_video_as_showcase_featured_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Album:
        """This method sets the featured video of the specified showcase. The authenticated user must be the owner of
        the showcase, and the featured video must belong to it.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video is now the featured video of the showcase.

        Raises:
            ApiError: Error code 3429: The authenticated user can't set the featured video of this showcase. Error code
                5000: No such showcase, user, or video exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.set_video_as_showcase_featured_alt2(
            album_id, video_id, request_options=request_options
        ).unwrap()

    def set_video_as_showcase_thumbnail(
        self,
        album_id: float,
        user_id: float,
        video_id: float,
        *,
        body: (
            UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest
            | UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict
            | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a thumbnail image for a showcase from the specified frame of a showcase video. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase thumbnail was created.

        Raises:
            ApiError: Error code 3429: The authenticated user can't create a thumbnail for this showcase. Error code
                5000: No such showcase, user, or video exists. Error code 4016: An unexpected error occurred. ``error``
                is ``Error | RawError``."""
        return self._with_raw_response.set_video_as_showcase_thumbnail(
            album_id, user_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def set_video_as_showcase_thumbnail_alt2(
        self,
        album_id: float,
        video_id: float,
        *,
        body: MeAlbumsVideosSetAlbumThumbnailRequest | MeAlbumsVideosSetAlbumThumbnailRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a thumbnail image for a showcase from the specified frame of a showcase video. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase thumbnail was created.

        Raises:
            ApiError: Error code 3429: The authenticated user can't create a thumbnail for this showcase. Error code
                5000: No such showcase, user, or video exists. Error code 4016: An unexpected error occurred. ``error``
                is ``Error | RawError``."""
        return self._with_raw_response.set_video_as_showcase_thumbnail_alt2(
            album_id, video_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ShowcasesShowcaseVideosWithRawResponse:
        return self._with_raw_response


class AsyncShowcasesShowcaseVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncShowcasesShowcaseVideosWithRawResponse(client, server, auth)

    async def add_video_to_showcase(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't add videos to
                the showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_to_showcase(
                album_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def add_video_to_showcase_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a single video to the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't add videos to
                the showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_to_showcase_alt2(
                album_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_available_showcase_videos(
        self,
        album_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video belonging to the authenticated user that can be added to or removed from the
        specified showcase.

        Args:
            album_id: The ID of the showcase.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``last_user_action_event_date`` - Sort the results by most recent user interaction. *
                ``likes`` - Sort the results by number of likes. * ``modified_time`` - Sort the results by last
                modification. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't add videos to this showcase. No such showcase
                exists. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_available_showcase_videos(
                album_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_available_video_showcases(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort74OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AlbumConnection:
        """This method returns every showcase to which the authenticated user can add or remove the specified video. The
        user must be the owner of the showcase.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by
                duration. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcases were returned.

        Raises:
            ApiError: Error code 3433: The authenticated user can't add the video to or remove the video from any
                showcases. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_available_video_showcases(
                video_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_showcase_video(
        self,
        album_id: float,
        user_id: float,
        video_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method returns a single video belonging to the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            password: The password of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: No such showcase exists, or the video doesn't belong to it. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.get_showcase_video(
                album_id, user_id, video_id, password=password, request_options=request_options
            )
        ).unwrap()

    async def get_showcase_video_alt2(
        self,
        album_id: float,
        video_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method returns a single video belonging to the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            password: The password of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: No such showcase exists, or the video doesn't belong to it. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.get_showcase_video_alt2(
                album_id, video_id, password=password, request_options=request_options
            )
        ).unwrap()

    async def get_showcase_videos(
        self,
        album_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter10OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        password: str | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort21OrStr | None = None,
        weak_search: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            containing_uri: The page containing the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Filter the
                results by the **embeddable** attribute. * ``playable`` - Filter the results by the **playable**
                attribute.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            password: The password of the showcase.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``likes`` - Sort the results by number of likes. * ``manual`` - Sort the results by their
                manual order. * ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the
                results by number of plays.
            weak_search: Whether to include private videos in the search. Please note that a separate search service
                provides this functionality. The service performs a partial text search on the video's name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_showcase_videos(
                album_id,
                user_id,
                containing_uri=containing_uri,
                direction=direction,
                filter=filter,
                filter_embeddable=filter_embeddable,
                page=page,
                password=password,
                per_page=per_page,
                query=query,
                sort=sort,
                weak_search=weak_search,
                request_options=request_options,
            )
        ).unwrap()

    async def get_showcase_videos_alt2(
        self,
        album_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter10OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        password: str | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort21OrStr | None = None,
        weak_search: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video in the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            containing_uri: The page containing the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Filter the
                results by the **embeddable** attribute. * ``playable`` - Filter the results by the **playable**
                attribute.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            password: The password of the showcase.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``likes`` - Sort the results by number of likes. * ``manual`` - Sort the results by their
                manual order. * ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the
                results by number of plays.
            weak_search: Whether to include private videos in the search. Please note that a separate search service
                provides this functionality. The service performs a partial text search on the video's name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_showcase_videos_alt2(
                album_id,
                containing_uri=containing_uri,
                direction=direction,
                filter=filter,
                filter_embeddable=filter_embeddable,
                page=page,
                password=password,
                per_page=per_page,
                query=query,
                sort=sort,
                weak_search=weak_search,
                request_options=request_options,
            )
        ).unwrap()

    async def remove_video_from_showcase(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified video from its showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't remove videos
                from the showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.remove_video_from_showcase(
                album_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def remove_video_from_showcase_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified video from its showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't remove videos
                from the showcase. No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.remove_video_from_showcase_alt2(
                album_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def replace_videos_in_showcase(
        self,
        album_id: float,
        user_id: float,
        body: UsersAlbumsVideosRequest | UsersAlbumsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method replaces all the videos in the specified showcase with a new set of one or more videos. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were replaced.

        Raises:
            ApiError: The authenticated user can't add videos to the showcase. No such showcase exists. ``error`` is
                ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.replace_videos_in_showcase(
                album_id, user_id, body, request_options=request_options
            )
        ).unwrap()

    async def replace_videos_in_showcase_alt2(
        self,
        album_id: float,
        body: MeAlbumsVideosRequest | MeAlbumsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method replaces all the videos in the specified showcase with a new set of one or more videos. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were replaced.

        Raises:
            ApiError: The authenticated user can't add videos to the showcase. No such showcase exists. ``error`` is
                ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.replace_videos_in_showcase_alt2(
                album_id, body, request_options=request_options
            )
        ).unwrap()

    async def set_video_as_showcase_featured(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Album:
        """This method sets the featured video of the specified showcase. The authenticated user must be the owner of
        the showcase, and the featured video must belong to it.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video is now the featured video of the showcase.

        Raises:
            ApiError: Error code 3429: The authenticated user can't set the featured video of this showcase. Error code
                5000: No such showcase, user, or video exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_video_as_showcase_featured(
                album_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def set_video_as_showcase_featured_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Album:
        """This method sets the featured video of the specified showcase. The authenticated user must be the owner of
        the showcase, and the featured video must belong to it.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video is now the featured video of the showcase.

        Raises:
            ApiError: Error code 3429: The authenticated user can't set the featured video of this showcase. Error code
                5000: No such showcase, user, or video exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_video_as_showcase_featured_alt2(
                album_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def set_video_as_showcase_thumbnail(
        self,
        album_id: float,
        user_id: float,
        video_id: float,
        *,
        body: (
            UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest
            | UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict
            | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a thumbnail image for a showcase from the specified frame of a showcase video. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase thumbnail was created.

        Raises:
            ApiError: Error code 3429: The authenticated user can't create a thumbnail for this showcase. Error code
                5000: No such showcase, user, or video exists. Error code 4016: An unexpected error occurred. ``error``
                is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_video_as_showcase_thumbnail(
                album_id, user_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def set_video_as_showcase_thumbnail_alt2(
        self,
        album_id: float,
        video_id: float,
        *,
        body: MeAlbumsVideosSetAlbumThumbnailRequest | MeAlbumsVideosSetAlbumThumbnailRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Album:
        """This method creates a thumbnail image for a showcase from the specified frame of a showcase video. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The showcase thumbnail was created.

        Raises:
            ApiError: Error code 3429: The authenticated user can't create a thumbnail for this showcase. Error code
                5000: No such showcase, user, or video exists. Error code 4016: An unexpected error occurred. ``error``
                is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_video_as_showcase_thumbnail_alt2(
                album_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncShowcasesShowcaseVideosWithRawResponse:
        return self._with_raw_response


class ShowcasesShowcaseVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_to_showcase(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToShowcaseErrorBody]:
        """This method adds a single video to the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos/{video_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_showcase_error_mapper,
            request_options=request_options,
        )

    def add_video_to_showcase_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToShowcaseAlt2ErrorBody]:
        """This method adds a single video to the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    def get_available_showcase_videos(
        self,
        album_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetAvailableShowcaseVideosErrorBody]:
        """This method returns every video belonging to the authenticated user that can be added to or removed from the
        specified showcase.

        Args:
            album_id: The ID of the showcase.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``last_user_action_event_date`` - Sort the results by most recent user interaction. *
                ``likes`` - Sort the results by number of likes. * ``modified_time`` - Sort the results by last
                modification. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{album_id}/available_videos"),
            path_params=[param[float]("album_id", album_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort2OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_available_showcase_videos_error_mapper,
            request_options=request_options,
        )

    def get_available_video_showcases(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort74OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlbumConnection, GetAvailableVideoShowcasesErrorBody]:
        """This method returns every showcase to which the authenticated user can add or remove the specified video. The
        user must be the owner of the showcase.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by
                duration. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/available_albums"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort74OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlbumConnection],
            error_mapper=get_available_video_showcases_error_mapper,
            request_options=request_options,
        )

    def get_showcase_video(
        self,
        album_id: float,
        user_id: float,
        video_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, GetShowcaseVideoErrorBody]:
        """This method returns a single video belonging to the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            password: The password of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos/{video_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_showcase_video_error_mapper,
            request_options=request_options,
        )

    def get_showcase_video_alt2(
        self,
        album_id: float,
        video_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, GetShowcaseVideoAlt2ErrorBody]:
        """This method returns a single video belonging to the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            password: The password of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_showcase_video_alt2_error_mapper,
            request_options=request_options,
        )

    def get_showcase_videos(
        self,
        album_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter10OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        password: str | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort21OrStr | None = None,
        weak_search: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetShowcaseVideosErrorBody]:
        """This method returns every video in the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            containing_uri: The page containing the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Filter the
                results by the **embeddable** attribute. * ``playable`` - Filter the results by the **playable**
                attribute.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            password: The password of the showcase.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``likes`` - Sort the results by number of likes. * ``manual`` - Sort the results by their
                manual order. * ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the
                results by number of plays.
            weak_search: Whether to include private videos in the search. Please note that a separate search service
                provides this functionality. The service performs a partial text search on the video's name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter10OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[str | None]("password", password),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort21OrStr | None]("sort", sort),
                param[bool | None]("weak_search", weak_search),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_showcase_videos_error_mapper,
            request_options=request_options,
        )

    def get_showcase_videos_alt2(
        self,
        album_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter10OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        password: str | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort21OrStr | None = None,
        weak_search: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetShowcaseVideosAlt2ErrorBody]:
        """This method returns every video in the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            containing_uri: The page containing the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Filter the
                results by the **embeddable** attribute. * ``playable`` - Filter the results by the **playable**
                attribute.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            password: The password of the showcase.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``likes`` - Sort the results by number of likes. * ``manual`` - Sort the results by their
                manual order. * ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the
                results by number of plays.
            weak_search: Whether to include private videos in the search. Please note that a separate search service
                provides this functionality. The service performs a partial text search on the video's name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/{album_id}/videos"),
            path_params=[param[float]("album_id", album_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter10OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[str | None]("password", password),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort21OrStr | None]("sort", sort),
                param[bool | None]("weak_search", weak_search),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_showcase_videos_alt2_error_mapper,
            request_options=request_options,
        )

    def remove_video_from_showcase(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveVideoFromShowcaseErrorBody]:
        """This method removes the specified video from its showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos/{video_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_video_from_showcase_error_mapper,
            request_options=request_options,
        )

    def remove_video_from_showcase_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveVideoFromShowcaseAlt2ErrorBody]:
        """This method removes the specified video from its showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_video_from_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    def replace_videos_in_showcase(
        self,
        album_id: float,
        user_id: float,
        body: UsersAlbumsVideosRequest | UsersAlbumsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ReplaceVideosInShowcaseErrorBody]:
        """This method replaces all the videos in the specified showcase with a new set of one or more videos. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            body=json_body[UsersAlbumsVideosRequest | UsersAlbumsVideosRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=replace_videos_in_showcase_error_mapper,
            request_options=request_options,
        )

    def replace_videos_in_showcase_alt2(
        self,
        album_id: float,
        body: MeAlbumsVideosRequest | MeAlbumsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ReplaceVideosInShowcaseAlt2ErrorBody]:
        """This method replaces all the videos in the specified showcase with a new set of one or more videos. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/albums/{album_id}/videos"),
            path_params=[param[float]("album_id", album_id)],
            body=json_body[MeAlbumsVideosRequest | MeAlbumsVideosRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=replace_videos_in_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    def set_video_as_showcase_featured(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, SetVideoAsShowcaseFeaturedErrorBody]:
        """This method sets the featured video of the specified showcase. The authenticated user must be the owner of
        the showcase, and the featured video must belong to it.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/users/{user_id}/albums/{album_id}/videos/{video_id}/set_featured_video"
            ),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=set_video_as_showcase_featured_error_mapper,
            request_options=request_options,
        )

    def set_video_as_showcase_featured_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, SetVideoAsShowcaseFeaturedAlt2ErrorBody]:
        """This method sets the featured video of the specified showcase. The authenticated user must be the owner of
        the showcase, and the featured video must belong to it.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}/set_featured_video"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=set_video_as_showcase_featured_alt2_error_mapper,
            request_options=request_options,
        )

    def set_video_as_showcase_thumbnail(
        self,
        album_id: float,
        user_id: float,
        video_id: float,
        *,
        body: (
            UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest
            | UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict
            | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, SetVideoAsShowcaseThumbnailErrorBody]:
        """This method creates a thumbnail image for a showcase from the specified frame of a showcase video. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail"
            ),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            body=json_body[
                (
                    UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest
                    | UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict
                    | None
                )
            ](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=set_video_as_showcase_thumbnail_error_mapper,
            request_options=request_options,
        )

    def set_video_as_showcase_thumbnail_alt2(
        self,
        album_id: float,
        video_id: float,
        *,
        body: MeAlbumsVideosSetAlbumThumbnailRequest | MeAlbumsVideosSetAlbumThumbnailRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, SetVideoAsShowcaseThumbnailAlt2ErrorBody]:
        """This method creates a thumbnail image for a showcase from the specified frame of a showcase video. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}/set_album_thumbnail"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            body=json_body[MeAlbumsVideosSetAlbumThumbnailRequest | MeAlbumsVideosSetAlbumThumbnailRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=set_video_as_showcase_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncShowcasesShowcaseVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_to_showcase(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToShowcaseErrorBody]:
        """This method adds a single video to the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos/{video_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_showcase_error_mapper,
            request_options=request_options,
        )

    async def add_video_to_showcase_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToShowcaseAlt2ErrorBody]:
        """This method adds a single video to the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_available_showcase_videos(
        self,
        album_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetAvailableShowcaseVideosErrorBody]:
        """This method returns every video belonging to the authenticated user that can be added to or removed from the
        specified showcase.

        Args:
            album_id: The ID of the showcase.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``last_user_action_event_date`` - Sort the results by most recent user interaction. *
                ``likes`` - Sort the results by number of likes. * ``modified_time`` - Sort the results by last
                modification. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/albums/{album_id}/available_videos"),
            path_params=[param[float]("album_id", album_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort2OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_available_showcase_videos_error_mapper,
            request_options=request_options,
        )

    async def get_available_video_showcases(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort74OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AlbumConnection, GetAvailableVideoShowcasesErrorBody]:
        """This method returns every showcase to which the authenticated user can add or remove the specified video. The
        user must be the owner of the showcase.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date. * ``duration`` - Sort the results by
                duration. * ``videos`` - Sort the results by number of videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/available_albums"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort74OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AlbumConnection],
            error_mapper=get_available_video_showcases_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_video(
        self,
        album_id: float,
        user_id: float,
        video_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, GetShowcaseVideoErrorBody]:
        """This method returns a single video belonging to the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            password: The password of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos/{video_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_showcase_video_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_video_alt2(
        self,
        album_id: float,
        video_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, GetShowcaseVideoAlt2ErrorBody]:
        """This method returns a single video belonging to the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            password: The password of the showcase.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_showcase_video_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_videos(
        self,
        album_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter10OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        password: str | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort21OrStr | None = None,
        weak_search: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetShowcaseVideosErrorBody]:
        """This method returns every video in the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            containing_uri: The page containing the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Filter the
                results by the **embeddable** attribute. * ``playable`` - Filter the results by the **playable**
                attribute.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            password: The password of the showcase.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``likes`` - Sort the results by number of likes. * ``manual`` - Sort the results by their
                manual order. * ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the
                results by number of plays.
            weak_search: Whether to include private videos in the search. Please note that a separate search service
                provides this functionality. The service performs a partial text search on the video's name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter10OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[str | None]("password", password),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort21OrStr | None]("sort", sort),
                param[bool | None]("weak_search", weak_search),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_showcase_videos_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_videos_alt2(
        self,
        album_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter: Filter10OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        password: str | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort21OrStr | None = None,
        weak_search: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetShowcaseVideosAlt2ErrorBody]:
        """This method returns every video in the specified showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            containing_uri: The page containing the video URI.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Filter the
                results by the **embeddable** attribute. * ``playable`` - Filter the results by the **playable**
                attribute.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            password: The password of the showcase.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``default`` - Sort the results by the default method. * ``duration`` - Sort the results by
                duration. * ``likes`` - Sort the results by number of likes. * ``manual`` - Sort the results by their
                manual order. * ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the
                results by number of plays.
            weak_search: Whether to include private videos in the search. Please note that a separate search service
                provides this functionality. The service performs a partial text search on the video's name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/albums/{album_id}/videos"),
            path_params=[param[float]("album_id", album_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter10OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[str | None]("password", password),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort21OrStr | None]("sort", sort),
                param[bool | None]("weak_search", weak_search),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_showcase_videos_alt2_error_mapper,
            request_options=request_options,
        )

    async def remove_video_from_showcase(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveVideoFromShowcaseErrorBody]:
        """This method removes the specified video from its showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos/{video_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_video_from_showcase_error_mapper,
            request_options=request_options,
        )

    async def remove_video_from_showcase_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveVideoFromShowcaseAlt2ErrorBody]:
        """This method removes the specified video from its showcase. The authenticated user must be the owner of the
        showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=remove_video_from_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    async def replace_videos_in_showcase(
        self,
        album_id: float,
        user_id: float,
        body: UsersAlbumsVideosRequest | UsersAlbumsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ReplaceVideosInShowcaseErrorBody]:
        """This method replaces all the videos in the specified showcase with a new set of one or more videos. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/videos"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            body=json_body[UsersAlbumsVideosRequest | UsersAlbumsVideosRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=replace_videos_in_showcase_error_mapper,
            request_options=request_options,
        )

    async def replace_videos_in_showcase_alt2(
        self,
        album_id: float,
        body: MeAlbumsVideosRequest | MeAlbumsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ReplaceVideosInShowcaseAlt2ErrorBody]:
        """This method replaces all the videos in the specified showcase with a new set of one or more videos. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/albums/{album_id}/videos"),
            path_params=[param[float]("album_id", album_id)],
            body=json_body[MeAlbumsVideosRequest | MeAlbumsVideosRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=replace_videos_in_showcase_alt2_error_mapper,
            request_options=request_options,
        )

    async def set_video_as_showcase_featured(
        self, album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, SetVideoAsShowcaseFeaturedErrorBody]:
        """This method sets the featured video of the specified showcase. The authenticated user must be the owner of
        the showcase, and the featured video must belong to it.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/users/{user_id}/albums/{album_id}/videos/{video_id}/set_featured_video"
            ),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=set_video_as_showcase_featured_error_mapper,
            request_options=request_options,
        )

    async def set_video_as_showcase_featured_alt2(
        self, album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Album, SetVideoAsShowcaseFeaturedAlt2ErrorBody]:
        """This method sets the featured video of the specified showcase. The authenticated user must be the owner of
        the showcase, and the featured video must belong to it.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}/set_featured_video"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=set_video_as_showcase_featured_alt2_error_mapper,
            request_options=request_options,
        )

    async def set_video_as_showcase_thumbnail(
        self,
        album_id: float,
        user_id: float,
        video_id: float,
        *,
        body: (
            UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest
            | UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict
            | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, SetVideoAsShowcaseThumbnailErrorBody]:
        """This method creates a thumbnail image for a showcase from the specified frame of a showcase video. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail"
            ),
            path_params=[
                param[float]("album_id", album_id), param[float]("user_id", user_id), param[float]("video_id", video_id)
            ],
            body=json_body[
                (
                    UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest
                    | UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict
                    | None
                )
            ](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=set_video_as_showcase_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def set_video_as_showcase_thumbnail_alt2(
        self,
        album_id: float,
        video_id: float,
        *,
        body: MeAlbumsVideosSetAlbumThumbnailRequest | MeAlbumsVideosSetAlbumThumbnailRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Album, SetVideoAsShowcaseThumbnailAlt2ErrorBody]:
        """This method creates a thumbnail image for a showcase from the specified frame of a showcase video. The
        authenticated user must be the owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/albums/{album_id}/videos/{video_id}/set_album_thumbnail"),
            path_params=[param[float]("album_id", album_id), param[float]("video_id", video_id)],
            body=json_body[MeAlbumsVideosSetAlbumThumbnailRequest | MeAlbumsVideosSetAlbumThumbnailRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Album],
            error_mapper=set_video_as_showcase_thumbnail_alt2_error_mapper,
            request_options=request_options,
        )
