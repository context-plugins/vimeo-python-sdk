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
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.create_comment_alt1_error import CreateCommentAlt1ErrorBody, create_comment_alt1_error_mapper
from ..errors.create_comment_error import CreateCommentErrorBody, create_comment_error_mapper
from ..errors.create_comment_reply_error import CreateCommentReplyErrorBody, create_comment_reply_error_mapper
from ..errors.delete_comment_error import DeleteCommentErrorBody, delete_comment_error_mapper
from ..errors.edit_comment_error import EditCommentErrorBody, edit_comment_error_mapper
from ..errors.get_comment_error import GetCommentErrorBody, get_comment_error_mapper
from ..errors.get_comment_replies_error import GetCommentRepliesErrorBody, get_comment_replies_error_mapper
from ..models.channels_videos_comments_request import ChannelsVideosCommentsRequest, ChannelsVideosCommentsRequestDict
from ..models.comment import Comment
from ..models.comment_connection import CommentConnection
from ..models.enums.direction import DirectionOrStr
from ..models.videos_comments_replies_request import VideosCommentsRepliesRequest, VideosCommentsRepliesRequestDict
from ..models.videos_comments_request import VideosCommentsRequest, VideosCommentsRequestDict
from ..server.server import Server


class VideosVideoComments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosVideoCommentsWithRawResponse(client, server, auth)

    def create_comment(
        self,
        video_id: float,
        *,
        body: VideosCommentsRequest | VideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Comment:
        """This method adds a video comment to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was added.

        Raises:
            ApiError: * Error code 2207: The comment text is missing. * Error code 2204: The comment rich text is
                invalid. Error code 8003: The user credentials are invalid. * Error code 3301: The comment was flagged
                as spam. * Error code 3411: The authenticated user is unverified. * Error code 3412: The authenticated
                user can't comment. * Error code 3413: Comments are disabled for this video. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.create_comment(video_id, body=body, request_options=request_options).unwrap()

    def create_comment_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        body: ChannelsVideosCommentsRequest | ChannelsVideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Comment:
        """This method adds a video comment to the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was added.

        Raises:
            ApiError: * Error code 2207: The comment text is missing. * Error code 2204: The comment rich text is
                invalid. Error code 8003: The user credentials are invalid. * Error code 3301: The comment was flagged
                as spam. * Error code 3411: The authenticated user is unverified. * Error code 3412: The authenticated
                user can't comment. * Error code 3413: Comments are disabled for this video. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.create_comment_alt1(
            channel_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def create_comment_reply(
        self,
        comment_id: float,
        video_id: float,
        body: VideosCommentsRepliesRequest | VideosCommentsRepliesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Comment:
        """This method adds a reply to the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The reply was added.

        Raises:
            ApiError: * Error code 2207: The comment text is missing. * Error code 2204: The comment rich text is
                invalid. * Error code 3301: The comment was flagged as spam. * Error code 3411: The authenticated user
                is unverified. * Error code 3412: The authenticated user can't comment. * Error code 3413: Comments are
                disabled on this video. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.create_comment_reply(
            comment_id, video_id, body, request_options=request_options
        ).unwrap()

    def delete_comment(
        self, comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified video comment. The authenticated user must be the owner of the comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was deleted.

        Raises:
            ApiError: Error code 3415: The authenticated user can't delete this comment. * No such video or comment
                exists. * Error code 5000: The comment wasn't deleted and still exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.delete_comment(comment_id, video_id, request_options=request_options).unwrap()

    def edit_comment(
        self,
        comment_id: float,
        video_id: float,
        *,
        body: VideosCommentsRequest | VideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Comment:
        """This method edits the specified video comment. The authenticated user must be the owner of the comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was edited.

        Raises:
            ApiError: * Error code 2207: The comment text is missing. * Error code 2204: The comment rich text is
                invalid. * Error code 3301: The comment was flagged as spam. * Error code 3411: The authenticated user
                is unverified. * Error code 3412: The authenticated user can't post comments. * Error code 3414: The
                authenticated user can't edit this comment. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.edit_comment(
            comment_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def get_comment(
        self, comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Comment:
        """This method returns the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was returned.

        Raises:
            ApiError: No such video or comment exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_comment(comment_id, video_id, request_options=request_options).unwrap()

    def get_comment_replies(
        self,
        comment_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommentConnection:
        """This method returns every reply to the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The replies were returned.

        Raises:
            ApiError: No such video or comment exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_comment_replies(
            comment_id, video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_comments(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommentConnection:
        """This method returns every video comment on the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comments were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_comments(
            video_id, direction=direction, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_comments_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommentConnection:
        """This method returns every video comment on the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comments were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_comments_alt1(
            channel_id, video_id, direction=direction, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosVideoCommentsWithRawResponse:
        return self._with_raw_response


class AsyncVideosVideoComments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosVideoCommentsWithRawResponse(client, server, auth)

    async def create_comment(
        self,
        video_id: float,
        *,
        body: VideosCommentsRequest | VideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Comment:
        """This method adds a video comment to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was added.

        Raises:
            ApiError: * Error code 2207: The comment text is missing. * Error code 2204: The comment rich text is
                invalid. Error code 8003: The user credentials are invalid. * Error code 3301: The comment was flagged
                as spam. * Error code 3411: The authenticated user is unverified. * Error code 3412: The authenticated
                user can't comment. * Error code 3413: Comments are disabled for this video. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.create_comment(video_id, body=body, request_options=request_options)
        ).unwrap()

    async def create_comment_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        body: ChannelsVideosCommentsRequest | ChannelsVideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Comment:
        """This method adds a video comment to the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was added.

        Raises:
            ApiError: * Error code 2207: The comment text is missing. * Error code 2204: The comment rich text is
                invalid. Error code 8003: The user credentials are invalid. * Error code 3301: The comment was flagged
                as spam. * Error code 3411: The authenticated user is unverified. * Error code 3412: The authenticated
                user can't comment. * Error code 3413: Comments are disabled for this video. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.create_comment_alt1(
                channel_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def create_comment_reply(
        self,
        comment_id: float,
        video_id: float,
        body: VideosCommentsRepliesRequest | VideosCommentsRepliesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Comment:
        """This method adds a reply to the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The reply was added.

        Raises:
            ApiError: * Error code 2207: The comment text is missing. * Error code 2204: The comment rich text is
                invalid. * Error code 3301: The comment was flagged as spam. * Error code 3411: The authenticated user
                is unverified. * Error code 3412: The authenticated user can't comment. * Error code 3413: Comments are
                disabled on this video. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.create_comment_reply(
                comment_id, video_id, body, request_options=request_options
            )
        ).unwrap()

    async def delete_comment(
        self, comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified video comment. The authenticated user must be the owner of the comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was deleted.

        Raises:
            ApiError: Error code 3415: The authenticated user can't delete this comment. * No such video or comment
                exists. * Error code 5000: The comment wasn't deleted and still exists. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_comment(comment_id, video_id, request_options=request_options)
        ).unwrap()

    async def edit_comment(
        self,
        comment_id: float,
        video_id: float,
        *,
        body: VideosCommentsRequest | VideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Comment:
        """This method edits the specified video comment. The authenticated user must be the owner of the comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was edited.

        Raises:
            ApiError: * Error code 2207: The comment text is missing. * Error code 2204: The comment rich text is
                invalid. * Error code 3301: The comment was flagged as spam. * Error code 3411: The authenticated user
                is unverified. * Error code 3412: The authenticated user can't post comments. * Error code 3414: The
                authenticated user can't edit this comment. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.edit_comment(comment_id, video_id, body=body, request_options=request_options)
        ).unwrap()

    async def get_comment(
        self, comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Comment:
        """This method returns the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comment was returned.

        Raises:
            ApiError: No such video or comment exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_comment(comment_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_comment_replies(
        self,
        comment_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommentConnection:
        """This method returns every reply to the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The replies were returned.

        Raises:
            ApiError: No such video or comment exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_comment_replies(
                comment_id, video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_comments(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommentConnection:
        """This method returns every video comment on the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comments were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_comments(
                video_id, direction=direction, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_comments_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommentConnection:
        """This method returns every video comment on the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The comments were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_comments_alt1(
                channel_id, video_id, direction=direction, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosVideoCommentsWithRawResponse:
        return self._with_raw_response


class VideosVideoCommentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_comment(
        self,
        video_id: float,
        *,
        body: VideosCommentsRequest | VideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Comment, CreateCommentErrorBody]:
        """This method adds a video comment to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/comments"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCommentsRequest | VideosCommentsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=create_comment_error_mapper,
            request_options=request_options,
        )

    def create_comment_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        body: ChannelsVideosCommentsRequest | ChannelsVideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Comment, CreateCommentAlt1ErrorBody]:
        """This method adds a video comment to the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/comments"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsVideosCommentsRequest | ChannelsVideosCommentsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=create_comment_alt1_error_mapper,
            request_options=request_options,
        )

    def create_comment_reply(
        self,
        comment_id: float,
        video_id: float,
        body: VideosCommentsRepliesRequest | VideosCommentsRepliesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Comment, CreateCommentReplyErrorBody]:
        """This method adds a reply to the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}/replies"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCommentsRepliesRequest | VideosCommentsRepliesRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=create_comment_reply_error_mapper,
            request_options=request_options,
        )

    def delete_comment(
        self, comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCommentErrorBody]:
        """This method deletes the specified video comment. The authenticated user must be the owner of the comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_comment_error_mapper,
            request_options=request_options,
        )

    def edit_comment(
        self,
        comment_id: float,
        video_id: float,
        *,
        body: VideosCommentsRequest | VideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Comment, EditCommentErrorBody]:
        """This method edits the specified video comment. The authenticated user must be the owner of the comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCommentsRequest | VideosCommentsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=edit_comment_error_mapper,
            request_options=request_options,
        )

    def get_comment(
        self, comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Comment, GetCommentErrorBody]:
        """This method returns the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=get_comment_error_mapper,
            request_options=request_options,
        )

    def get_comment_replies(
        self,
        comment_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommentConnection, GetCommentRepliesErrorBody]:
        """This method returns every reply to the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}/replies"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CommentConnection],
            error_mapper=get_comment_replies_error_mapper,
            request_options=request_options,
        )

    def get_comments(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommentConnection, RawError]:
        """This method returns every video comment on the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/comments"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CommentConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_comments_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommentConnection, RawError]:
        """This method returns every video comment on the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/comments"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CommentConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideosVideoCommentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_comment(
        self,
        video_id: float,
        *,
        body: VideosCommentsRequest | VideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Comment, CreateCommentErrorBody]:
        """This method adds a video comment to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/comments"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCommentsRequest | VideosCommentsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=create_comment_error_mapper,
            request_options=request_options,
        )

    async def create_comment_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        body: ChannelsVideosCommentsRequest | ChannelsVideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Comment, CreateCommentAlt1ErrorBody]:
        """This method adds a video comment to the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/comments"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsVideosCommentsRequest | ChannelsVideosCommentsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=create_comment_alt1_error_mapper,
            request_options=request_options,
        )

    async def create_comment_reply(
        self,
        comment_id: float,
        video_id: float,
        body: VideosCommentsRepliesRequest | VideosCommentsRepliesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Comment, CreateCommentReplyErrorBody]:
        """This method adds a reply to the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}/replies"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCommentsRepliesRequest | VideosCommentsRepliesRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=create_comment_reply_error_mapper,
            request_options=request_options,
        )

    async def delete_comment(
        self, comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCommentErrorBody]:
        """This method deletes the specified video comment. The authenticated user must be the owner of the comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_comment_error_mapper,
            request_options=request_options,
        )

    async def edit_comment(
        self,
        comment_id: float,
        video_id: float,
        *,
        body: VideosCommentsRequest | VideosCommentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Comment, EditCommentErrorBody]:
        """This method edits the specified video comment. The authenticated user must be the owner of the comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCommentsRequest | VideosCommentsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=edit_comment_error_mapper,
            request_options=request_options,
        )

    async def get_comment(
        self, comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Comment, GetCommentErrorBody]:
        """This method returns the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Comment],
            error_mapper=get_comment_error_mapper,
            request_options=request_options,
        )

    async def get_comment_replies(
        self,
        comment_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommentConnection, GetCommentRepliesErrorBody]:
        """This method returns every reply to the specified video comment.

        Args:
            comment_id: The ID of the comment.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/comments/{comment_id}/replies"),
            path_params=[param[float]("comment_id", comment_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CommentConnection],
            error_mapper=get_comment_replies_error_mapper,
            request_options=request_options,
        )

    async def get_comments(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommentConnection, RawError]:
        """This method returns every video comment on the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/comments"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CommentConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_comments_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommentConnection, RawError]:
        """This method returns every video comment on the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/comments"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CommentConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
