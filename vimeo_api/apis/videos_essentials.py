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
from ..errors.check_if_user_owns_video_alt1_error import (
    CheckIfUserOwnsVideoAlt1ErrorBody,
    check_if_user_owns_video_alt1_error_mapper,
)
from ..errors.check_if_user_owns_video_error import CheckIfUserOwnsVideoErrorBody, check_if_user_owns_video_error_mapper
from ..errors.copy_video_alt2_error import CopyVideoAlt2ErrorBody, copy_video_alt2_error_mapper
from ..errors.copy_video_error import CopyVideoErrorBody, copy_video_error_mapper
from ..errors.delete_video_error import DeleteVideoErrorBody, delete_video_error_mapper
from ..errors.delete_videos_alt1_error import DeleteVideosAlt1ErrorBody, delete_videos_alt1_error_mapper
from ..errors.delete_videos_error import DeleteVideosErrorBody, delete_videos_error_mapper
from ..errors.edit_video_error import EditVideoErrorBody, edit_video_error_mapper
from ..errors.get_appearances_alt1_error import GetAppearancesAlt1ErrorBody, get_appearances_alt1_error_mapper
from ..errors.get_appearances_error import GetAppearancesErrorBody, get_appearances_error_mapper
from ..errors.get_video_error import GetVideoErrorBody, get_video_error_mapper
from ..errors.search_videos_error import SearchVideosErrorBody, search_videos_error_mapper
from ..errors.update_video_custom_metadata_error import (
    UpdateVideoCustomMetadataErrorBody,
    update_video_custom_metadata_error_mapper,
)
from ..models.custom_metadata_values import CustomMetadataValues
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter3 import Filter3OrStr
from ..models.enums.filter22 import Filter22OrStr
from ..models.enums.filter45 import Filter45OrStr
from ..models.enums.query_fields import QueryFieldsOrStr
from ..models.enums.sort15 import Sort15OrStr
from ..models.enums.sort39 import Sort39OrStr
from ..models.enums.sort73 import Sort73OrStr
from ..models.me_videos_copy_request import MeVideosCopyRequest, MeVideosCopyRequestDict
from ..models.me_videos_request import MeVideosRequest, MeVideosRequestDict
from ..models.users_videos_copy_request import UsersVideosCopyRequest, UsersVideosCopyRequestDict
from ..models.users_videos_request import UsersVideosRequest, UsersVideosRequestDict
from ..models.video import Video
from ..models.video_connection import VideoConnection
from ..models.videos_custom_metadata_request import VideosCustomMetadataRequest, VideosCustomMetadataRequestDict
from ..models.videos_request import VideosRequest, VideosRequestDict
from ..models.videos_request1 import VideosRequest1, VideosRequest1Dict
from ..server.server import Server


class VideosEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosEssentialsWithRawResponse(client, server, auth)

    def check_if_user_owns_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method determines whether the authenticated user is the owner of the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The authenticated user owns the video.

        Raises:
            ApiError: The authenticated user doesn't own the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.check_if_user_owns_video(user_id, video_id, request_options=request_options)
        )

    def check_if_user_owns_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method determines whether the authenticated user is the owner of the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The authenticated user owns the video.

        Raises:
            ApiError: The authenticated user doesn't own the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.check_if_user_owns_video_alt1(video_id, request_options=request_options))

    def copy_video(
        self,
        user_id: float,
        video_id: float,
        *,
        body: UsersVideosCopyRequest | UsersVideosCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates a copy of the specified video. Only the source's current version is copied; prior version
        history is not carried over.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The copied video was created.

        Raises:
            ApiError: The authenticated user can't copy this video. No such video exists. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(self._with_raw_response.copy_video(user_id, video_id, body=body, request_options=request_options))

    def copy_video_alt2(
        self,
        video_id: float,
        *,
        body: MeVideosCopyRequest | MeVideosCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates a copy of the specified video. Only the source's current version is copied; prior version
        history is not carried over.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The copied video was created.

        Raises:
            ApiError: The authenticated user can't copy this video. No such video exists. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(self._with_raw_response.copy_video_alt2(video_id, body=body, request_options=request_options))

    def delete_video(
        self,
        video_id: float,
        *,
        body: VideosRequest | VideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes the specified video. The authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was deleted.

        Raises:
            ApiError: The authenticated user can't delete the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.delete_video(video_id, body=body, request_options=request_options))

    def delete_videos(
        self,
        user_id: float,
        uris: str,
        *,
        body: UsersVideosRequest | UsersVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes one or more videos belonging to the specified user. The authenticated user must have
        permission to delete the videos.

        Specify the videos to delete in a comma-separated list by URI using the **uris** query parameter.

        Args:
            user_id: The ID of the user.
            uris: A comma-separated list of the video URIs to delete.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were deleted.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 3200: The authenticated user can't delete
                one or more of the videos. Error code 8000: The user credentials are invalid. Error code 5000: No such
                video exists. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.delete_videos(user_id, uris, body=body, request_options=request_options))

    def delete_videos_alt1(
        self,
        uris: str,
        *,
        body: MeVideosRequest | MeVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes one or more videos belonging to the specified user. The authenticated user must have
        permission to delete the videos.

        Specify the videos to delete in a comma-separated list by URI using the **uris** query parameter.

        Args:
            uris: A comma-separated list of the video URIs to delete.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were deleted.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 3200: The authenticated user can't delete
                one or more of the videos. Error code 8000: The user credentials are invalid. Error code 5000: No such
                video exists. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.delete_videos_alt1(uris, body=body, request_options=request_options))

    def edit_video(
        self,
        video_id: float,
        body: VideosRequest1 | VideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method edits the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was edited.

        Raises:
            ApiError: A parameter is invalid. * The authenticated user doesn't own the video. * The **privacy** field is
                ``disable``, and the authenticated user can't set extra embed options. * The **privacy** field is
                ``contacts``, and the authenticated user can't follow creators. * The authenticated user has an
                opted-out Pro account, and **privacy.view** is ``users``, ``password``, ``nobody``, or ``public``.
                ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.edit_video(video_id, body, request_options=request_options))

    def get_appearances(
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
        """This method returns all the videos in which the authenticated user has a credited appearance.

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
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_appearances(
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

    def get_appearances_alt1(
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
        """This method returns all the videos in which the authenticated user has a credited appearance.

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
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.get_appearances_alt1(
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

    def get_video(
        self, video_id: float, *, time_links: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video.

        Args:
            video_id: The ID of the video.
            time_links: Whether to return timestamps in the description as links.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_video(video_id, time_links=time_links, request_options=request_options)
        )

    def get_videos(
        self,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter_: Filter22OrStr | None = None,
        filter_embeddable: bool | None = None,
        filter_playable: bool | None = None,
        filter_screen_recorded: bool | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        filter_uploader: float | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: QueryFieldsOrStr | None = None,
        sort: Sort39OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that the authenticated user has uploaded.

        Args:
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI. The field is available only when not paired with
                **query**.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``app_only`` - Return app-only
                videos. * ``cold_privacy`` - Return the owner's active videos whose privacy is suppressed because their
                plan no longer supports it (cold privacy). * ``cold_storage`` - Return cold storage videos. *
                ``embeddable`` - Return embeddable videos. * ``featured`` - Return featured videos. * ``live`` - Return
                only live videos. * ``no_placeholder`` - Return no placeholder videos. * ``nolive`` - Return no live
                videos. * ``playable`` - Return playable videos. * ``screen_recorded`` - Return screen-recorded videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            filter_playable: Whether to filter the results by playable videos (``true``) or non-playable videos
                (``false``).
            filter_screen_recorded: Whether to filter the results by screen-recorded videos (``true``) or
                non-screen-recorded videos (``false``).
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
            filter_tag_exclude: A comma-separated list of tags to exclude. All results must exclude all of these tags.
            filter_uploader: The ID of the team member or team owner uploader to filter for.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``. Option descriptions: * ``chapters`` - Query by chapter titles that
                have been added to the video. * ``description`` - Query by the description of the video. * ``tags`` -
                Query by tag names that have been added to the video. * ``title`` - Query by the title of the video.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results alphabetically
                by title. * ``date`` - Sort the results by date. * ``default`` - Use the default sorting method. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by
                last user interaction. If a result hasn't had an interaction, the upload date is used instead. *
                ``likes`` - Sort the results by number of likes. To use this option, **direction** must be ``desc``. *
                ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the results by number of
                plays. To use this option, **direction** must be ``desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_videos(
                user_id,
                containing_uri=containing_uri,
                direction=direction,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                filter_playable=filter_playable,
                filter_screen_recorded=filter_screen_recorded,
                filter_tag=filter_tag,
                filter_tag_all_of=filter_tag_all_of,
                filter_tag_exclude=filter_tag_exclude,
                filter_uploader=filter_uploader,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            ),
        )

    def get_videos_alt1(
        self,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter_: Filter22OrStr | None = None,
        filter_embeddable: bool | None = None,
        filter_playable: bool | None = None,
        filter_screen_recorded: bool | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        filter_uploader: float | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: QueryFieldsOrStr | None = None,
        sort: Sort39OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that the authenticated user has uploaded.

        Args:
            containing_uri: The page that contains the video URI. The field is available only when not paired with
                **query**.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``app_only`` - Return app-only
                videos. * ``cold_privacy`` - Return the owner's active videos whose privacy is suppressed because their
                plan no longer supports it (cold privacy). * ``cold_storage`` - Return cold storage videos. *
                ``embeddable`` - Return embeddable videos. * ``featured`` - Return featured videos. * ``live`` - Return
                only live videos. * ``no_placeholder`` - Return no placeholder videos. * ``nolive`` - Return no live
                videos. * ``playable`` - Return playable videos. * ``screen_recorded`` - Return screen-recorded videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            filter_playable: Whether to filter the results by playable videos (``true``) or non-playable videos
                (``false``).
            filter_screen_recorded: Whether to filter the results by screen-recorded videos (``true``) or
                non-screen-recorded videos (``false``).
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
            filter_tag_exclude: A comma-separated list of tags to exclude. All results must exclude all of these tags.
            filter_uploader: The ID of the team member or team owner uploader to filter for.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``. Option descriptions: * ``chapters`` - Query by chapter titles that
                have been added to the video. * ``description`` - Query by the description of the video. * ``tags`` -
                Query by tag names that have been added to the video. * ``title`` - Query by the title of the video.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results alphabetically
                by title. * ``date`` - Sort the results by date. * ``default`` - Use the default sorting method. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by
                last user interaction. If a result hasn't had an interaction, the upload date is used instead. *
                ``likes`` - Sort the results by number of likes. To use this option, **direction** must be ``desc``. *
                ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the results by number of
                plays. To use this option, **direction** must be ``desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_videos_alt1(
                containing_uri=containing_uri,
                direction=direction,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                filter_playable=filter_playable,
                filter_screen_recorded=filter_screen_recorded,
                filter_tag=filter_tag,
                filter_tag_all_of=filter_tag_all_of,
                filter_tag_exclude=filter_tag_exclude,
                filter_uploader=filter_uploader,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            ),
        )

    def search_videos(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter45OrStr | None = None,
        links: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort73OrStr | None = None,
        uris: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that match custom search criteria.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. ``CC`` and related filters target videos with the
                corresponding Creative Commons licenses. For more information, see our `Creative Commons
                <https://vimeo.com/creativecommons>`__ page. Option descriptions: * ``CC`` - Return videos under any
                Creative Commons license. * ``CC-BY`` - Return CC BY, or attribution-only, videos. * ``CC-BY-NC`` -
                Return CC BY-NC, or Attribution-NonCommercial, videos. * ``CC-BY-NC-ND`` - Return CC BY-NC-ND, or
                Attribution-NonCommercial-NoDerivs, videos. * ``CC-BY-NC-SA`` - Return CC BY-NC-SA, or
                Attribution-NonCommercial-ShareAlike, videos. * ``CC-BY-ND`` - Return CC BY-ND, or Attribution-NoDerivs,
                videos. * ``CC-BY-SA`` - Return CC BY-SA, or Attribution-ShareAlike, videos. * ``CC0`` - Return CC0, or
                public domain, videos. * ``categories`` - Filter by categories. * ``duration`` - Filter by duration. *
                ``in-progress`` - Return in-progress videos. * ``minimum_likes`` - Filter by minimum likes. *
                ``trending`` - Return trending videos. * ``upload_date`` - Filter by upload date.
            links: A comma-separated list of video URLs to find. Querying, filtering, and sorting aren't supported when
                using this field.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays. * ``relevant`` - Sort the results by
                relevance.
            uris: A comma-separated list of video URIs to find. Querying, filtering, and sorting aren't supported when
                using this field.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The search results were returned.

        Raises:
            ApiError: * Error code 2101: Either the **uris** or **links** parameter has filtering or sorting arguments.
                * Error code 2204: A problem occurred with the batch request. Error code 5451: This resource is
                restricted in your region. * Search is disabled. * Error code 7300: An internal search error occurred.
                ``error`` is ``Error | LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.search_videos(
                direction=direction,
                filter_=filter_,
                links=links,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                uris=uris,
                request_options=request_options,
            ),
        )

    def update_video_custom_metadata(
        self,
        video_id: float,
        *,
        body: VideosCustomMetadataRequest | VideosCustomMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CustomMetadataValues]:
        """This method sets, updates, or clears custom metadata values on a single video.

        The authenticated user must own the video or have team permission to edit it.

        Send each value as a ``{field_id, field_value}`` pair under the ``fields`` array. The value's data type is
        validated against the field's definition (set via ``POST /teams/{user_id}/custom_metadata``):

        | Type | Accepted format |
        | -------------- | ------------------------------------------------------- |
        | ``str`` | A non-empty string of up to 50 characters |
        | ``int`` | An integer, optionally negative (for example, ``42``) |
        | ``date`` | ``YYYY-MM-DD`` |
        | ``bool`` | ``"true"``, ``"false"``, ``"1"``, or ``"0"`` |
        | ``select`` | One of the values defined for the field |
        | ``multi-select`` | A JSON-encoded array of allowed values |

        To clear an existing value, send ``field_value: null``. The field will return to its default value (if one is
        defined) or become unset.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated custom metadata for the video.

        Raises:
            ApiError: Error code 2204: The request is malformed, references an unknown field, or contains a value that
                doesn't match the field's data type. The authentication credentials are missing or invalid. The
                authenticated user doesn't have permission to edit this video. No such video exists. ``error`` is
                ``Error | LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.update_video_custom_metadata(video_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> VideosEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncVideosEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosEssentialsWithRawResponse(client, server, auth)

    async def check_if_user_owns_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method determines whether the authenticated user is the owner of the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The authenticated user owns the video.

        Raises:
            ApiError: The authenticated user doesn't own the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_if_user_owns_video(user_id, video_id, request_options=request_options)
        )

    async def check_if_user_owns_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method determines whether the authenticated user is the owner of the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The authenticated user owns the video.

        Raises:
            ApiError: The authenticated user doesn't own the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.check_if_user_owns_video_alt1(video_id, request_options=request_options)
        )

    async def copy_video(
        self,
        user_id: float,
        video_id: float,
        *,
        body: UsersVideosCopyRequest | UsersVideosCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates a copy of the specified video. Only the source's current version is copied; prior version
        history is not carried over.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The copied video was created.

        Raises:
            ApiError: The authenticated user can't copy this video. No such video exists. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            await self._with_raw_response.copy_video(user_id, video_id, body=body, request_options=request_options)
        )

    async def copy_video_alt2(
        self,
        video_id: float,
        *,
        body: MeVideosCopyRequest | MeVideosCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method creates a copy of the specified video. Only the source's current version is copied; prior version
        history is not carried over.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The copied video was created.

        Raises:
            ApiError: The authenticated user can't copy this video. No such video exists. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            await self._with_raw_response.copy_video_alt2(video_id, body=body, request_options=request_options)
        )

    async def delete_video(
        self,
        video_id: float,
        *,
        body: VideosRequest | VideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes the specified video. The authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was deleted.

        Raises:
            ApiError: The authenticated user can't delete the video. ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.delete_video(video_id, body=body, request_options=request_options))

    async def delete_videos(
        self,
        user_id: float,
        uris: str,
        *,
        body: UsersVideosRequest | UsersVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes one or more videos belonging to the specified user. The authenticated user must have
        permission to delete the videos.

        Specify the videos to delete in a comma-separated list by URI using the **uris** query parameter.

        Args:
            user_id: The ID of the user.
            uris: A comma-separated list of the video URIs to delete.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were deleted.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 3200: The authenticated user can't delete
                one or more of the videos. Error code 8000: The user credentials are invalid. Error code 5000: No such
                video exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_videos(user_id, uris, body=body, request_options=request_options)
        )

    async def delete_videos_alt1(
        self,
        uris: str,
        *,
        body: MeVideosRequest | MeVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes one or more videos belonging to the specified user. The authenticated user must have
        permission to delete the videos.

        Specify the videos to delete in a comma-separated list by URI using the **uris** query parameter.

        Args:
            uris: A comma-separated list of the video URIs to delete.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were deleted.

        Raises:
            ApiError: * Error code 2204: The input is invalid. * Error code 3200: The authenticated user can't delete
                one or more of the videos. Error code 8000: The user credentials are invalid. Error code 5000: No such
                video exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_videos_alt1(uris, body=body, request_options=request_options)
        )

    async def edit_video(
        self,
        video_id: float,
        body: VideosRequest1 | VideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method edits the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was edited.

        Raises:
            ApiError: A parameter is invalid. * The authenticated user doesn't own the video. * The **privacy** field is
                ``disable``, and the authenticated user can't set extra embed options. * The **privacy** field is
                ``contacts``, and the authenticated user can't follow creators. * The authenticated user has an
                opted-out Pro account, and **privacy.view** is ``users``, ``password``, ``nobody``, or ``public``.
                ``error`` is ``LegacyError | RawError``."""
        return unwrap(await self._with_raw_response.edit_video(video_id, body, request_options=request_options))

    async def get_appearances(
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
        """This method returns all the videos in which the authenticated user has a credited appearance.

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
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_appearances(
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

    async def get_appearances_alt1(
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
        """This method returns all the videos in which the authenticated user has a credited appearance.

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
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.get_appearances_alt1(
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

    async def get_video(
        self, video_id: float, *, time_links: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video.

        Args:
            video_id: The ID of the video.
            time_links: Whether to return timestamps in the description as links.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The video was returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_video(video_id, time_links=time_links, request_options=request_options)
        )

    async def get_videos(
        self,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter_: Filter22OrStr | None = None,
        filter_embeddable: bool | None = None,
        filter_playable: bool | None = None,
        filter_screen_recorded: bool | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        filter_uploader: float | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: QueryFieldsOrStr | None = None,
        sort: Sort39OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that the authenticated user has uploaded.

        Args:
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI. The field is available only when not paired with
                **query**.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``app_only`` - Return app-only
                videos. * ``cold_privacy`` - Return the owner's active videos whose privacy is suppressed because their
                plan no longer supports it (cold privacy). * ``cold_storage`` - Return cold storage videos. *
                ``embeddable`` - Return embeddable videos. * ``featured`` - Return featured videos. * ``live`` - Return
                only live videos. * ``no_placeholder`` - Return no placeholder videos. * ``nolive`` - Return no live
                videos. * ``playable`` - Return playable videos. * ``screen_recorded`` - Return screen-recorded videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            filter_playable: Whether to filter the results by playable videos (``true``) or non-playable videos
                (``false``).
            filter_screen_recorded: Whether to filter the results by screen-recorded videos (``true``) or
                non-screen-recorded videos (``false``).
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
            filter_tag_exclude: A comma-separated list of tags to exclude. All results must exclude all of these tags.
            filter_uploader: The ID of the team member or team owner uploader to filter for.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``. Option descriptions: * ``chapters`` - Query by chapter titles that
                have been added to the video. * ``description`` - Query by the description of the video. * ``tags`` -
                Query by tag names that have been added to the video. * ``title`` - Query by the title of the video.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results alphabetically
                by title. * ``date`` - Sort the results by date. * ``default`` - Use the default sorting method. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by
                last user interaction. If a result hasn't had an interaction, the upload date is used instead. *
                ``likes`` - Sort the results by number of likes. To use this option, **direction** must be ``desc``. *
                ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the results by number of
                plays. To use this option, **direction** must be ``desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_videos(
                user_id,
                containing_uri=containing_uri,
                direction=direction,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                filter_playable=filter_playable,
                filter_screen_recorded=filter_screen_recorded,
                filter_tag=filter_tag,
                filter_tag_all_of=filter_tag_all_of,
                filter_tag_exclude=filter_tag_exclude,
                filter_uploader=filter_uploader,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def get_videos_alt1(
        self,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter_: Filter22OrStr | None = None,
        filter_embeddable: bool | None = None,
        filter_playable: bool | None = None,
        filter_screen_recorded: bool | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        filter_uploader: float | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: QueryFieldsOrStr | None = None,
        sort: Sort39OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that the authenticated user has uploaded.

        Args:
            containing_uri: The page that contains the video URI. The field is available only when not paired with
                **query**.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``app_only`` - Return app-only
                videos. * ``cold_privacy`` - Return the owner's active videos whose privacy is suppressed because their
                plan no longer supports it (cold privacy). * ``cold_storage`` - Return cold storage videos. *
                ``embeddable`` - Return embeddable videos. * ``featured`` - Return featured videos. * ``live`` - Return
                only live videos. * ``no_placeholder`` - Return no placeholder videos. * ``nolive`` - Return no live
                videos. * ``playable`` - Return playable videos. * ``screen_recorded`` - Return screen-recorded videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            filter_playable: Whether to filter the results by playable videos (``true``) or non-playable videos
                (``false``).
            filter_screen_recorded: Whether to filter the results by screen-recorded videos (``true``) or
                non-screen-recorded videos (``false``).
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
            filter_tag_exclude: A comma-separated list of tags to exclude. All results must exclude all of these tags.
            filter_uploader: The ID of the team member or team owner uploader to filter for.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``. Option descriptions: * ``chapters`` - Query by chapter titles that
                have been added to the video. * ``description`` - Query by the description of the video. * ``tags`` -
                Query by tag names that have been added to the video. * ``title`` - Query by the title of the video.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results alphabetically
                by title. * ``date`` - Sort the results by date. * ``default`` - Use the default sorting method. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by
                last user interaction. If a result hasn't had an interaction, the upload date is used instead. *
                ``likes`` - Sort the results by number of likes. To use this option, **direction** must be ``desc``. *
                ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the results by number of
                plays. To use this option, **direction** must be ``desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_videos_alt1(
                containing_uri=containing_uri,
                direction=direction,
                filter_=filter_,
                filter_embeddable=filter_embeddable,
                filter_playable=filter_playable,
                filter_screen_recorded=filter_screen_recorded,
                filter_tag=filter_tag,
                filter_tag_all_of=filter_tag_all_of,
                filter_tag_exclude=filter_tag_exclude,
                filter_uploader=filter_uploader,
                page=page,
                per_page=per_page,
                query=query,
                query_fields=query_fields,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def search_videos(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter45OrStr | None = None,
        links: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort73OrStr | None = None,
        uris: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the videos that match custom search criteria.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. ``CC`` and related filters target videos with the
                corresponding Creative Commons licenses. For more information, see our `Creative Commons
                <https://vimeo.com/creativecommons>`__ page. Option descriptions: * ``CC`` - Return videos under any
                Creative Commons license. * ``CC-BY`` - Return CC BY, or attribution-only, videos. * ``CC-BY-NC`` -
                Return CC BY-NC, or Attribution-NonCommercial, videos. * ``CC-BY-NC-ND`` - Return CC BY-NC-ND, or
                Attribution-NonCommercial-NoDerivs, videos. * ``CC-BY-NC-SA`` - Return CC BY-NC-SA, or
                Attribution-NonCommercial-ShareAlike, videos. * ``CC-BY-ND`` - Return CC BY-ND, or Attribution-NoDerivs,
                videos. * ``CC-BY-SA`` - Return CC BY-SA, or Attribution-ShareAlike, videos. * ``CC0`` - Return CC0, or
                public domain, videos. * ``categories`` - Filter by categories. * ``duration`` - Filter by duration. *
                ``in-progress`` - Return in-progress videos. * ``minimum_likes`` - Filter by minimum likes. *
                ``trending`` - Return trending videos. * ``upload_date`` - Filter by upload date.
            links: A comma-separated list of video URLs to find. Querying, filtering, and sorting aren't supported when
                using this field.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays. * ``relevant`` - Sort the results by
                relevance.
            uris: A comma-separated list of video URIs to find. Querying, filtering, and sorting aren't supported when
                using this field.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The search results were returned.

        Raises:
            ApiError: * Error code 2101: Either the **uris** or **links** parameter has filtering or sorting arguments.
                * Error code 2204: A problem occurred with the batch request. Error code 5451: This resource is
                restricted in your region. * Search is disabled. * Error code 7300: An internal search error occurred.
                ``error`` is ``Error | LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.search_videos(
                direction=direction,
                filter_=filter_,
                links=links,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                uris=uris,
                request_options=request_options,
            ),
        )

    async def update_video_custom_metadata(
        self,
        video_id: float,
        *,
        body: VideosCustomMetadataRequest | VideosCustomMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CustomMetadataValues]:
        """This method sets, updates, or clears custom metadata values on a single video.

        The authenticated user must own the video or have team permission to edit it.

        Send each value as a ``{field_id, field_value}`` pair under the ``fields`` array. The value's data type is
        validated against the field's definition (set via ``POST /teams/{user_id}/custom_metadata``):

        | Type | Accepted format |
        | -------------- | ------------------------------------------------------- |
        | ``str`` | A non-empty string of up to 50 characters |
        | ``int`` | An integer, optionally negative (for example, ``42``) |
        | ``date`` | ``YYYY-MM-DD`` |
        | ``bool`` | ``"true"``, ``"false"``, ``"1"``, or ``"0"`` |
        | ``select`` | One of the values defined for the field |
        | ``multi-select`` | A JSON-encoded array of allowed values |

        To clear an existing value, send ``field_value: null``. The field will return to its default value (if one is
        defined) or become unset.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated custom metadata for the video.

        Raises:
            ApiError: Error code 2204: The request is malformed, references an unknown field, or contains a value that
                doesn't match the field's data type. The authentication credentials are missing or invalid. The
                authenticated user doesn't have permission to edit this video. No such video exists. ``error`` is
                ``Error | LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.update_video_custom_metadata(
                video_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncVideosEssentialsWithRawResponse:
        return self._with_raw_response


class VideosEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_if_user_owns_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckIfUserOwnsVideoErrorBody]:
        """This method determines whether the authenticated user is the owner of the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/videos/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=check_if_user_owns_video_error_mapper,
            request_options=request_options,
        )

    def check_if_user_owns_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckIfUserOwnsVideoAlt1ErrorBody]:
        """This method determines whether the authenticated user is the owner of the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=check_if_user_owns_video_alt1_error_mapper,
            request_options=request_options,
        )

    def copy_video(
        self,
        user_id: float,
        video_id: float,
        *,
        body: UsersVideosCopyRequest | UsersVideosCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, CopyVideoErrorBody]:
        """This method creates a copy of the specified video. Only the source's current version is copied; prior version
        history is not carried over.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/videos/{video_id}/copy"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersVideosCopyRequest | UsersVideosCopyRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=copy_video_error_mapper,
            request_options=request_options,
        )

    def copy_video_alt2(
        self,
        video_id: float,
        *,
        body: MeVideosCopyRequest | MeVideosCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, CopyVideoAlt2ErrorBody]:
        """This method creates a copy of the specified video. Only the source's current version is copied; prior version
        history is not carried over.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/videos/{video_id}/copy"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeVideosCopyRequest | MeVideosCopyRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=copy_video_alt2_error_mapper,
            request_options=request_options,
        )

    def delete_video(
        self,
        video_id: float,
        *,
        body: VideosRequest | VideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteVideoErrorBody]:
        """This method deletes the specified video. The authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosRequest | VideosRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_error_mapper,
            request_options=request_options,
        )

    def delete_videos(
        self,
        user_id: float,
        uris: str,
        *,
        body: UsersVideosRequest | UsersVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteVideosErrorBody]:
        """This method deletes one or more videos belonging to the specified user. The authenticated user must have
        permission to delete the videos.

        Specify the videos to delete in a comma-separated list by URI using the **uris** query parameter.

        Args:
            user_id: The ID of the user.
            uris: A comma-separated list of the video URIs to delete.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/videos"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[str]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersVideosRequest | UsersVideosRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_videos_error_mapper,
            request_options=request_options,
        )

    def delete_videos_alt1(
        self,
        uris: str,
        *,
        body: MeVideosRequest | MeVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteVideosAlt1ErrorBody]:
        """This method deletes one or more videos belonging to the specified user. The authenticated user must have
        permission to delete the videos.

        Specify the videos to delete in a comma-separated list by URI using the **uris** query parameter.

        Args:
            uris: A comma-separated list of the video URIs to delete.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/videos"),
            query_params=[param[str]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeVideosRequest | MeVideosRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_videos_alt1_error_mapper,
            request_options=request_options,
        )

    def edit_video(
        self,
        video_id: float,
        body: VideosRequest1 | VideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, EditVideoErrorBody]:
        """This method edits the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosRequest1 | VideosRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=edit_video_error_mapper,
            request_options=request_options,
        )

    def get_appearances(
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
    ) -> ApiResult[VideoConnection, GetAppearancesErrorBody]:
        """This method returns all the videos in which the authenticated user has a credited appearance.

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
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/appearances"),
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
            error_mapper=get_appearances_error_mapper,
            request_options=request_options,
        )

    def get_appearances_alt1(
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
    ) -> ApiResult[VideoConnection, GetAppearancesAlt1ErrorBody]:
        """This method returns all the videos in which the authenticated user has a credited appearance.

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
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/appearances"),
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
            error_mapper=get_appearances_alt1_error_mapper,
            request_options=request_options,
        )

    def get_video(
        self, video_id: float, *, time_links: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetVideoErrorBody]:
        """This method returns a single video.

        Args:
            video_id: The ID of the video.
            time_links: Whether to return timestamps in the description as links.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[bool | None]("time_links", time_links)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=get_video_error_mapper,
            request_options=request_options,
        )

    def get_videos(
        self,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter_: Filter22OrStr | None = None,
        filter_embeddable: bool | None = None,
        filter_playable: bool | None = None,
        filter_screen_recorded: bool | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        filter_uploader: float | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: QueryFieldsOrStr | None = None,
        sort: Sort39OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns all the videos that the authenticated user has uploaded.

        Args:
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI. The field is available only when not paired with
                **query**.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``app_only`` - Return app-only
                videos. * ``cold_privacy`` - Return the owner's active videos whose privacy is suppressed because their
                plan no longer supports it (cold privacy). * ``cold_storage`` - Return cold storage videos. *
                ``embeddable`` - Return embeddable videos. * ``featured`` - Return featured videos. * ``live`` - Return
                only live videos. * ``no_placeholder`` - Return no placeholder videos. * ``nolive`` - Return no live
                videos. * ``playable`` - Return playable videos. * ``screen_recorded`` - Return screen-recorded videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            filter_playable: Whether to filter the results by playable videos (``true``) or non-playable videos
                (``false``).
            filter_screen_recorded: Whether to filter the results by screen-recorded videos (``true``) or
                non-screen-recorded videos (``false``).
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
            filter_tag_exclude: A comma-separated list of tags to exclude. All results must exclude all of these tags.
            filter_uploader: The ID of the team member or team owner uploader to filter for.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``. Option descriptions: * ``chapters`` - Query by chapter titles that
                have been added to the video. * ``description`` - Query by the description of the video. * ``tags`` -
                Query by tag names that have been added to the video. * ``title`` - Query by the title of the video.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results alphabetically
                by title. * ``date`` - Sort the results by date. * ``default`` - Use the default sorting method. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by
                last user interaction. If a result hasn't had an interaction, the upload date is used instead. *
                ``likes`` - Sort the results by number of likes. To use this option, **direction** must be ``desc``. *
                ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the results by number of
                plays. To use this option, **direction** must be ``desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/videos"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter22OrStr | None]("filter", filter_),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[bool | None]("filter_playable", filter_playable),
                param[bool | None]("filter_screen_recorded", filter_screen_recorded),
                param[str | None]("filter_tag", filter_tag),
                param[str | None]("filter_tag_all_of", filter_tag_all_of),
                param[str | None]("filter_tag_exclude", filter_tag_exclude),
                param[float | None]("filter_uploader", filter_uploader),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[QueryFieldsOrStr | None]("query_fields", query_fields),
                param[Sort39OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_videos_alt1(
        self,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter_: Filter22OrStr | None = None,
        filter_embeddable: bool | None = None,
        filter_playable: bool | None = None,
        filter_screen_recorded: bool | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        filter_uploader: float | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: QueryFieldsOrStr | None = None,
        sort: Sort39OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns all the videos that the authenticated user has uploaded.

        Args:
            containing_uri: The page that contains the video URI. The field is available only when not paired with
                **query**.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``app_only`` - Return app-only
                videos. * ``cold_privacy`` - Return the owner's active videos whose privacy is suppressed because their
                plan no longer supports it (cold privacy). * ``cold_storage`` - Return cold storage videos. *
                ``embeddable`` - Return embeddable videos. * ``featured`` - Return featured videos. * ``live`` - Return
                only live videos. * ``no_placeholder`` - Return no placeholder videos. * ``nolive`` - Return no live
                videos. * ``playable`` - Return playable videos. * ``screen_recorded`` - Return screen-recorded videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            filter_playable: Whether to filter the results by playable videos (``true``) or non-playable videos
                (``false``).
            filter_screen_recorded: Whether to filter the results by screen-recorded videos (``true``) or
                non-screen-recorded videos (``false``).
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
            filter_tag_exclude: A comma-separated list of tags to exclude. All results must exclude all of these tags.
            filter_uploader: The ID of the team member or team owner uploader to filter for.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``. Option descriptions: * ``chapters`` - Query by chapter titles that
                have been added to the video. * ``description`` - Query by the description of the video. * ``tags`` -
                Query by tag names that have been added to the video. * ``title`` - Query by the title of the video.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results alphabetically
                by title. * ``date`` - Sort the results by date. * ``default`` - Use the default sorting method. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by
                last user interaction. If a result hasn't had an interaction, the upload date is used instead. *
                ``likes`` - Sort the results by number of likes. To use this option, **direction** must be ``desc``. *
                ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the results by number of
                plays. To use this option, **direction** must be ``desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/videos"),
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter22OrStr | None]("filter", filter_),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[bool | None]("filter_playable", filter_playable),
                param[bool | None]("filter_screen_recorded", filter_screen_recorded),
                param[str | None]("filter_tag", filter_tag),
                param[str | None]("filter_tag_all_of", filter_tag_all_of),
                param[str | None]("filter_tag_exclude", filter_tag_exclude),
                param[float | None]("filter_uploader", filter_uploader),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[QueryFieldsOrStr | None]("query_fields", query_fields),
                param[Sort39OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_videos(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter45OrStr | None = None,
        links: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort73OrStr | None = None,
        uris: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, SearchVideosErrorBody]:
        """This method returns all the videos that match custom search criteria.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. ``CC`` and related filters target videos with the
                corresponding Creative Commons licenses. For more information, see our `Creative Commons
                <https://vimeo.com/creativecommons>`__ page. Option descriptions: * ``CC`` - Return videos under any
                Creative Commons license. * ``CC-BY`` - Return CC BY, or attribution-only, videos. * ``CC-BY-NC`` -
                Return CC BY-NC, or Attribution-NonCommercial, videos. * ``CC-BY-NC-ND`` - Return CC BY-NC-ND, or
                Attribution-NonCommercial-NoDerivs, videos. * ``CC-BY-NC-SA`` - Return CC BY-NC-SA, or
                Attribution-NonCommercial-ShareAlike, videos. * ``CC-BY-ND`` - Return CC BY-ND, or Attribution-NoDerivs,
                videos. * ``CC-BY-SA`` - Return CC BY-SA, or Attribution-ShareAlike, videos. * ``CC0`` - Return CC0, or
                public domain, videos. * ``categories`` - Filter by categories. * ``duration`` - Filter by duration. *
                ``in-progress`` - Return in-progress videos. * ``minimum_likes`` - Filter by minimum likes. *
                ``trending`` - Return trending videos. * ``upload_date`` - Filter by upload date.
            links: A comma-separated list of video URLs to find. Querying, filtering, and sorting aren't supported when
                using this field.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays. * ``relevant`` - Sort the results by
                relevance.
            uris: A comma-separated list of video URIs to find. Querying, filtering, and sorting aren't supported when
                using this field.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter45OrStr | None]("filter", filter_),
                param[str | None]("links", links),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort73OrStr | None]("sort", sort),
                param[str | None]("uris", uris),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=search_videos_error_mapper,
            request_options=request_options,
        )

    def update_video_custom_metadata(
        self,
        video_id: float,
        *,
        body: VideosCustomMetadataRequest | VideosCustomMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CustomMetadataValues], UpdateVideoCustomMetadataErrorBody]:
        """This method sets, updates, or clears custom metadata values on a single video.

        The authenticated user must own the video or have team permission to edit it.

        Send each value as a ``{field_id, field_value}`` pair under the ``fields`` array. The value's data type is
        validated against the field's definition (set via ``POST /teams/{user_id}/custom_metadata``):

        | Type | Accepted format |
        | -------------- | ------------------------------------------------------- |
        | ``str`` | A non-empty string of up to 50 characters |
        | ``int`` | An integer, optionally negative (for example, ``42``) |
        | ``date`` | ``YYYY-MM-DD`` |
        | ``bool`` | ``"true"``, ``"false"``, ``"1"``, or ``"0"`` |
        | ``select`` | One of the values defined for the field |
        | ``multi-select`` | A JSON-encoded array of allowed values |

        To clear an existing value, send ``field_value: null``. The field will return to its default value (if one is
        defined) or become unset.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/custom_metadata"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCustomMetadataRequest | VideosCustomMetadataRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[CustomMetadataValues]],
            error_mapper=update_video_custom_metadata_error_mapper,
            request_options=request_options,
        )


class AsyncVideosEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_if_user_owns_video(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckIfUserOwnsVideoErrorBody]:
        """This method determines whether the authenticated user is the owner of the specified video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/videos/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=check_if_user_owns_video_error_mapper,
            request_options=request_options,
        )

    async def check_if_user_owns_video_alt1(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, CheckIfUserOwnsVideoAlt1ErrorBody]:
        """This method determines whether the authenticated user is the owner of the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=check_if_user_owns_video_alt1_error_mapper,
            request_options=request_options,
        )

    async def copy_video(
        self,
        user_id: float,
        video_id: float,
        *,
        body: UsersVideosCopyRequest | UsersVideosCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, CopyVideoErrorBody]:
        """This method creates a copy of the specified video. Only the source's current version is copied; prior version
        history is not carried over.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/videos/{video_id}/copy"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersVideosCopyRequest | UsersVideosCopyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=copy_video_error_mapper,
            request_options=request_options,
        )

    async def copy_video_alt2(
        self,
        video_id: float,
        *,
        body: MeVideosCopyRequest | MeVideosCopyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, CopyVideoAlt2ErrorBody]:
        """This method creates a copy of the specified video. Only the source's current version is copied; prior version
        history is not carried over.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/videos/{video_id}/copy"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeVideosCopyRequest | MeVideosCopyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=copy_video_alt2_error_mapper,
            request_options=request_options,
        )

    async def delete_video(
        self,
        video_id: float,
        *,
        body: VideosRequest | VideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteVideoErrorBody]:
        """This method deletes the specified video. The authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosRequest | VideosRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_video_error_mapper,
            request_options=request_options,
        )

    async def delete_videos(
        self,
        user_id: float,
        uris: str,
        *,
        body: UsersVideosRequest | UsersVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteVideosErrorBody]:
        """This method deletes one or more videos belonging to the specified user. The authenticated user must have
        permission to delete the videos.

        Specify the videos to delete in a comma-separated list by URI using the **uris** query parameter.

        Args:
            user_id: The ID of the user.
            uris: A comma-separated list of the video URIs to delete.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/videos"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[str]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersVideosRequest | UsersVideosRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_videos_error_mapper,
            request_options=request_options,
        )

    async def delete_videos_alt1(
        self,
        uris: str,
        *,
        body: MeVideosRequest | MeVideosRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteVideosAlt1ErrorBody]:
        """This method deletes one or more videos belonging to the specified user. The authenticated user must have
        permission to delete the videos.

        Specify the videos to delete in a comma-separated list by URI using the **uris** query parameter.

        Args:
            uris: A comma-separated list of the video URIs to delete.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/videos"),
            query_params=[param[str]("uris", uris)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeVideosRequest | MeVideosRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_videos_alt1_error_mapper,
            request_options=request_options,
        )

    async def edit_video(
        self,
        video_id: float,
        body: VideosRequest1 | VideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, EditVideoErrorBody]:
        """This method edits the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosRequest1 | VideosRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=edit_video_error_mapper,
            request_options=request_options,
        )

    async def get_appearances(
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
    ) -> ApiResult[VideoConnection, GetAppearancesErrorBody]:
        """This method returns all the videos in which the authenticated user has a credited appearance.

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
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/appearances"),
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
            error_mapper=get_appearances_error_mapper,
            request_options=request_options,
        )

    async def get_appearances_alt1(
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
    ) -> ApiResult[VideoConnection, GetAppearancesAlt1ErrorBody]:
        """This method returns all the videos in which the authenticated user has a credited appearance.

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
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/appearances"),
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
            error_mapper=get_appearances_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_video(
        self, video_id: float, *, time_links: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, GetVideoErrorBody]:
        """This method returns a single video.

        Args:
            video_id: The ID of the video.
            time_links: Whether to return timestamps in the description as links.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[bool | None]("time_links", time_links)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Video],
            error_mapper=get_video_error_mapper,
            request_options=request_options,
        )

    async def get_videos(
        self,
        user_id: float,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter_: Filter22OrStr | None = None,
        filter_embeddable: bool | None = None,
        filter_playable: bool | None = None,
        filter_screen_recorded: bool | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        filter_uploader: float | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: QueryFieldsOrStr | None = None,
        sort: Sort39OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns all the videos that the authenticated user has uploaded.

        Args:
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI. The field is available only when not paired with
                **query**.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``app_only`` - Return app-only
                videos. * ``cold_privacy`` - Return the owner's active videos whose privacy is suppressed because their
                plan no longer supports it (cold privacy). * ``cold_storage`` - Return cold storage videos. *
                ``embeddable`` - Return embeddable videos. * ``featured`` - Return featured videos. * ``live`` - Return
                only live videos. * ``no_placeholder`` - Return no placeholder videos. * ``nolive`` - Return no live
                videos. * ``playable`` - Return playable videos. * ``screen_recorded`` - Return screen-recorded videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            filter_playable: Whether to filter the results by playable videos (``true``) or non-playable videos
                (``false``).
            filter_screen_recorded: Whether to filter the results by screen-recorded videos (``true``) or
                non-screen-recorded videos (``false``).
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
            filter_tag_exclude: A comma-separated list of tags to exclude. All results must exclude all of these tags.
            filter_uploader: The ID of the team member or team owner uploader to filter for.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``. Option descriptions: * ``chapters`` - Query by chapter titles that
                have been added to the video. * ``description`` - Query by the description of the video. * ``tags`` -
                Query by tag names that have been added to the video. * ``title`` - Query by the title of the video.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results alphabetically
                by title. * ``date`` - Sort the results by date. * ``default`` - Use the default sorting method. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by
                last user interaction. If a result hasn't had an interaction, the upload date is used instead. *
                ``likes`` - Sort the results by number of likes. To use this option, **direction** must be ``desc``. *
                ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the results by number of
                plays. To use this option, **direction** must be ``desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/videos"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter22OrStr | None]("filter", filter_),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[bool | None]("filter_playable", filter_playable),
                param[bool | None]("filter_screen_recorded", filter_screen_recorded),
                param[str | None]("filter_tag", filter_tag),
                param[str | None]("filter_tag_all_of", filter_tag_all_of),
                param[str | None]("filter_tag_exclude", filter_tag_exclude),
                param[float | None]("filter_uploader", filter_uploader),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[QueryFieldsOrStr | None]("query_fields", query_fields),
                param[Sort39OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_videos_alt1(
        self,
        *,
        containing_uri: str | None = None,
        direction: DirectionOrStr | None = None,
        filter_: Filter22OrStr | None = None,
        filter_embeddable: bool | None = None,
        filter_playable: bool | None = None,
        filter_screen_recorded: bool | None = None,
        filter_tag: str | None = None,
        filter_tag_all_of: str | None = None,
        filter_tag_exclude: str | None = None,
        filter_uploader: float | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        query_fields: QueryFieldsOrStr | None = None,
        sort: Sort39OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns all the videos that the authenticated user has uploaded.

        Args:
            containing_uri: The page that contains the video URI. The field is available only when not paired with
                **query**.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``app_only`` - Return app-only
                videos. * ``cold_privacy`` - Return the owner's active videos whose privacy is suppressed because their
                plan no longer supports it (cold privacy). * ``cold_storage`` - Return cold storage videos. *
                ``embeddable`` - Return embeddable videos. * ``featured`` - Return featured videos. * ``live`` - Return
                only live videos. * ``no_placeholder`` - Return no placeholder videos. * ``nolive`` - Return no live
                videos. * ``playable`` - Return playable videos. * ``screen_recorded`` - Return screen-recorded videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            filter_playable: Whether to filter the results by playable videos (``true``) or non-playable videos
                (``false``).
            filter_screen_recorded: Whether to filter the results by screen-recorded videos (``true``) or
                non-screen-recorded videos (``false``).
            filter_tag: A comma-separated list of tags to filter on. All results must include at least one of these
                tags.
            filter_tag_all_of: A comma-separated list of tags to filter on. All results must include all of these tags.
            filter_tag_exclude: A comma-separated list of tags to exclude. All results must exclude all of these tags.
            filter_uploader: The ID of the team member or team owner uploader to filter for.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            query_fields: A comma-separated list of fields to query over. The default value is
                ``title,description,chapters,tags``. Option descriptions: * ``chapters`` - Query by chapter titles that
                have been added to the video. * ``description`` - Query by the description of the video. * ``tags`` -
                Query by tag names that have been added to the video. * ``title`` - Query by the title of the video.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results alphabetically
                by title. * ``date`` - Sort the results by date. * ``default`` - Use the default sorting method. *
                ``duration`` - Sort the results by duration. * ``last_user_action_event_date`` - Sort the results by
                last user interaction. If a result hasn't had an interaction, the upload date is used instead. *
                ``likes`` - Sort the results by number of likes. To use this option, **direction** must be ``desc``. *
                ``modified_time`` - Sort the results by last modification. * ``plays`` - Sort the results by number of
                plays. To use this option, **direction** must be ``desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/videos"),
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[DirectionOrStr | None]("direction", direction),
                param[Filter22OrStr | None]("filter", filter_),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[bool | None]("filter_playable", filter_playable),
                param[bool | None]("filter_screen_recorded", filter_screen_recorded),
                param[str | None]("filter_tag", filter_tag),
                param[str | None]("filter_tag_all_of", filter_tag_all_of),
                param[str | None]("filter_tag_exclude", filter_tag_exclude),
                param[float | None]("filter_uploader", filter_uploader),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[QueryFieldsOrStr | None]("query_fields", query_fields),
                param[Sort39OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_videos(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter45OrStr | None = None,
        links: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort73OrStr | None = None,
        uris: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, SearchVideosErrorBody]:
        """This method returns all the videos that match custom search criteria.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. ``CC`` and related filters target videos with the
                corresponding Creative Commons licenses. For more information, see our `Creative Commons
                <https://vimeo.com/creativecommons>`__ page. Option descriptions: * ``CC`` - Return videos under any
                Creative Commons license. * ``CC-BY`` - Return CC BY, or attribution-only, videos. * ``CC-BY-NC`` -
                Return CC BY-NC, or Attribution-NonCommercial, videos. * ``CC-BY-NC-ND`` - Return CC BY-NC-ND, or
                Attribution-NonCommercial-NoDerivs, videos. * ``CC-BY-NC-SA`` - Return CC BY-NC-SA, or
                Attribution-NonCommercial-ShareAlike, videos. * ``CC-BY-ND`` - Return CC BY-ND, or Attribution-NoDerivs,
                videos. * ``CC-BY-SA`` - Return CC BY-SA, or Attribution-ShareAlike, videos. * ``CC0`` - Return CC0, or
                public domain, videos. * ``categories`` - Filter by categories. * ``duration`` - Filter by duration. *
                ``in-progress`` - Return in-progress videos. * ``minimum_likes`` - Filter by minimum likes. *
                ``trending`` - Return trending videos. * ``upload_date`` - Filter by upload date.
            links: A comma-separated list of video URLs to find. Querying, filtering, and sorting aren't supported when
                using this field.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by date. * ``duration`` - Sort the results by duration. * ``likes`` - Sort the results by number of
                likes. * ``plays`` - Sort the results by number of plays. * ``relevant`` - Sort the results by
                relevance.
            uris: A comma-separated list of video URIs to find. Querying, filtering, and sorting aren't supported when
                using this field.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter45OrStr | None]("filter", filter_),
                param[str | None]("links", links),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort73OrStr | None]("sort", sort),
                param[str | None]("uris", uris),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[VideoConnection],
            error_mapper=search_videos_error_mapper,
            request_options=request_options,
        )

    async def update_video_custom_metadata(
        self,
        video_id: float,
        *,
        body: VideosCustomMetadataRequest | VideosCustomMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CustomMetadataValues], UpdateVideoCustomMetadataErrorBody]:
        """This method sets, updates, or clears custom metadata values on a single video.

        The authenticated user must own the video or have team permission to edit it.

        Send each value as a ``{field_id, field_value}`` pair under the ``fields`` array. The value's data type is
        validated against the field's definition (set via ``POST /teams/{user_id}/custom_metadata``):

        | Type | Accepted format |
        | -------------- | ------------------------------------------------------- |
        | ``str`` | A non-empty string of up to 50 characters |
        | ``int`` | An integer, optionally negative (for example, ``42``) |
        | ``date`` | ``YYYY-MM-DD`` |
        | ``bool`` | ``"true"``, ``"false"``, ``"1"``, or ``"0"`` |
        | ``select`` | One of the values defined for the field |
        | ``multi-select`` | A JSON-encoded array of allowed values |

        To clear an existing value, send ``field_value: null``. The field will return to its default value (if one is
        defined) or become unset.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/custom_metadata"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCustomMetadataRequest | VideosCustomMetadataRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[list[CustomMetadataValues]],
            error_mapper=update_video_custom_metadata_error_mapper,
            request_options=request_options,
        )
