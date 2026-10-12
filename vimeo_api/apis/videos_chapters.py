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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_chapter_error import CreateChapterErrorBody, create_chapter_error_mapper
from ..errors.create_chapter_thumbnail_or_upload_link_error import (
    CreateChapterThumbnailOrUploadLinkErrorBody,
    create_chapter_thumbnail_or_upload_link_error_mapper,
)
from ..errors.create_unsaved_chapter_thumbnail_or_upload_link_error import (
    CreateUnsavedChapterThumbnailOrUploadLinkErrorBody,
    create_unsaved_chapter_thumbnail_or_upload_link_error_mapper,
)
from ..errors.delete_chapter_error import DeleteChapterErrorBody, delete_chapter_error_mapper
from ..errors.delete_chapter_thumbnail_error import (
    DeleteChapterThumbnailErrorBody,
    delete_chapter_thumbnail_error_mapper,
)
from ..errors.edit_chapter_error import EditChapterErrorBody, edit_chapter_error_mapper
from ..errors.get_chapter_error import GetChapterErrorBody, get_chapter_error_mapper
from ..errors.get_chapter_thumbnail_error import GetChapterThumbnailErrorBody, get_chapter_thumbnail_error_mapper
from ..errors.get_chapter_thumbnails_error import GetChapterThumbnailsErrorBody, get_chapter_thumbnails_error_mapper
from ..errors.get_chapters_error import GetChaptersErrorBody, get_chapters_error_mapper
from ..errors.get_unsaved_chapter_thumbnail_error import (
    GetUnsavedChapterThumbnailErrorBody,
    get_unsaved_chapter_thumbnail_error_mapper,
)
from ..errors.set_chapter_thumbnail_active_error import (
    SetChapterThumbnailActiveErrorBody,
    set_chapter_thumbnail_active_error_mapper,
)
from ..models.chapter import Chapter
from ..models.chapter_connection import ChapterConnection
from ..models.picture import Picture
from ..models.videos_chapters_pictures_request import VideosChaptersPicturesRequest, VideosChaptersPicturesRequestDict
from ..models.videos_chapters_pictures_uid_request import (
    VideosChaptersPicturesUidRequest,
    VideosChaptersPicturesUidRequestDict,
)
from ..models.videos_chapters_request import VideosChaptersRequest, VideosChaptersRequestDict
from ..models.videos_chapters_request1 import VideosChaptersRequest1, VideosChaptersRequest1Dict
from ..models.videos_chapters_temporary_pictures_request import (
    VideosChaptersTemporaryPicturesRequest,
    VideosChaptersTemporaryPicturesRequestDict,
)
from ..server.server import Server


class VideosChapters:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosChaptersWithRawResponse(client, server, auth)

    def create_chapter(
        self,
        video_id: float,
        *,
        body: VideosChaptersRequest | VideosChaptersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Chapter:
        """This method adds a chapter to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter was added.

        Raises:
            ApiError: * The authenticated user can't add the chapter. * Error code 2204: The request contains errors.
                ``error`` is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.create_chapter(video_id, body=body, request_options=request_options))

    def create_chapter_thumbnail_or_upload_link(
        self,
        chapter_id: float,
        video_id: float,
        *,
        body: VideosChaptersPicturesRequest | VideosChaptersPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method generates either an upload link or a timecode-based thumbnail for the specified saved video
        chapter. To generate the upload link, which enables the authenticated user to upload a chapter thumbnail image
        manually, leave the body of the request empty. To generate an automatic timecode-based thumbnail, include the
        **timecode** parameter in the body of the request.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail or upload link was generated.

        Raises:
            ApiError: * The authenticated user can't perform this action. * Error code 2204: The request contains
                errors. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.create_chapter_thumbnail_or_upload_link(
                chapter_id, video_id, body=body, request_options=request_options
            ),
        )

    def create_unsaved_chapter_thumbnail_or_upload_link(
        self,
        video_id: float,
        *,
        body: VideosChaptersTemporaryPicturesRequest | VideosChaptersTemporaryPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method generates either an upload link or a timecode-based thumbnail for an unsaved video chapter. To
        generate the upload link, which enables the authenticated user to upload a chapter thumbnail image manually,
        leave the body of the request empty. To generate an automatic timecode-based thumbnail, specify the **timecode**
        parameter in the body of the request.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The upload link or chapter thumbnail was generated.

        Raises:
            ApiError: * The authenticated user can't perform this action. * Error code 2204: The request contains
                errors. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.create_unsaved_chapter_thumbnail_or_upload_link(
                video_id, body=body, request_options=request_options
            ),
        )

    def delete_chapter(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified chapter from a video. The authenticated user must be the owner of the
        video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter was deleted.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(self._with_raw_response.delete_chapter(chapter_id, video_id, request_options=request_options))

    def delete_chapter_thumbnail(
        self, chapter_id: float, uid: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified chapter thumbnail from a video.

        The authenticated user must be the owner of the video that the chapter belongs to. This method deletes both
        timecode-generated and custom-uploaded thumbnails.

        Args:
            chapter_id: The ID of the chapter.
            uid: The unique ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail was deleted.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            self._with_raw_response.delete_chapter_thumbnail(chapter_id, uid, video_id, request_options=request_options)
        )

    def edit_chapter(
        self,
        chapter_id: float,
        video_id: float,
        *,
        body: VideosChaptersRequest1 | VideosChaptersRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Chapter:
        """This method edits the specified chapter of a video. The authenticated user must be the owner of the video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter was edited.

        Raises:
            ApiError: Error code 2204: There are errors in the request. * No such video or chapter exists. * Error code
                5020: The specified chapter doesn't exist. * Error code 5021: The specified chapter belongs to a
                different video. ``error`` is ``Error | LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.edit_chapter(chapter_id, video_id, body=body, request_options=request_options)
        )

    def get_chapter(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Chapter:
        """This method returns a single chapter of the specified video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter was returned.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(self._with_raw_response.get_chapter(chapter_id, video_id, request_options=request_options))

    def get_chapter_thumbnail(
        self, chapter_id: float, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns the specified thumbnail associated with a saved video chapter.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            uid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail was returned.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_chapter_thumbnail(chapter_id, video_id, uid, request_options=request_options)
        )

    def get_chapter_thumbnails(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns every thumbnail associated with the specified saved video chapter.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnails were returned.

        Raises:
            ApiError: * The authenticated user can't perform this action. * Error code 2204: The request contains
                errors. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_chapter_thumbnails(chapter_id, video_id, request_options=request_options)
        )

    def get_chapters(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChapterConnection:
        """This method returns every chapter of the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapters were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_chapters(
                video_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    def get_unsaved_chapter_thumbnail(
        self, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns the specified thumbnail associated with an unsaved video chapter.

        Args:
            video_id: The ID of the video.
            uid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail was returned.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_unsaved_chapter_thumbnail(video_id, uid, request_options=request_options)
        )

    def set_chapter_thumbnail_active(
        self,
        chapter_id: float,
        video_id: float,
        uid: str,
        *,
        body: VideosChaptersPicturesUidRequest | VideosChaptersPicturesUidRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method sets the specified chapter thumbnail for a video as active.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            uid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail was set as active.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            self._with_raw_response.set_chapter_thumbnail_active(
                chapter_id, video_id, uid, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> VideosChaptersWithRawResponse:
        return self._with_raw_response


class AsyncVideosChapters:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosChaptersWithRawResponse(client, server, auth)

    async def create_chapter(
        self,
        video_id: float,
        *,
        body: VideosChaptersRequest | VideosChaptersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Chapter:
        """This method adds a chapter to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter was added.

        Raises:
            ApiError: * The authenticated user can't add the chapter. * Error code 2204: The request contains errors.
                ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.create_chapter(video_id, body=body, request_options=request_options)
        )

    async def create_chapter_thumbnail_or_upload_link(
        self,
        chapter_id: float,
        video_id: float,
        *,
        body: VideosChaptersPicturesRequest | VideosChaptersPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method generates either an upload link or a timecode-based thumbnail for the specified saved video
        chapter. To generate the upload link, which enables the authenticated user to upload a chapter thumbnail image
        manually, leave the body of the request empty. To generate an automatic timecode-based thumbnail, include the
        **timecode** parameter in the body of the request.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail or upload link was generated.

        Raises:
            ApiError: * The authenticated user can't perform this action. * Error code 2204: The request contains
                errors. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.create_chapter_thumbnail_or_upload_link(
                chapter_id, video_id, body=body, request_options=request_options
            ),
        )

    async def create_unsaved_chapter_thumbnail_or_upload_link(
        self,
        video_id: float,
        *,
        body: VideosChaptersTemporaryPicturesRequest | VideosChaptersTemporaryPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method generates either an upload link or a timecode-based thumbnail for an unsaved video chapter. To
        generate the upload link, which enables the authenticated user to upload a chapter thumbnail image manually,
        leave the body of the request empty. To generate an automatic timecode-based thumbnail, specify the **timecode**
        parameter in the body of the request.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The upload link or chapter thumbnail was generated.

        Raises:
            ApiError: * The authenticated user can't perform this action. * Error code 2204: The request contains
                errors. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.create_unsaved_chapter_thumbnail_or_upload_link(
                video_id, body=body, request_options=request_options
            ),
        )

    async def delete_chapter(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified chapter from a video. The authenticated user must be the owner of the
        video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter was deleted.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            await self._with_raw_response.delete_chapter(chapter_id, video_id, request_options=request_options)
        )

    async def delete_chapter_thumbnail(
        self, chapter_id: float, uid: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified chapter thumbnail from a video.

        The authenticated user must be the owner of the video that the chapter belongs to. This method deletes both
        timecode-generated and custom-uploaded thumbnails.

        Args:
            chapter_id: The ID of the chapter.
            uid: The unique ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail was deleted.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            await self._with_raw_response.delete_chapter_thumbnail(
                chapter_id, uid, video_id, request_options=request_options
            ),
        )

    async def edit_chapter(
        self,
        chapter_id: float,
        video_id: float,
        *,
        body: VideosChaptersRequest1 | VideosChaptersRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Chapter:
        """This method edits the specified chapter of a video. The authenticated user must be the owner of the video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter was edited.

        Raises:
            ApiError: Error code 2204: There are errors in the request. * No such video or chapter exists. * Error code
                5020: The specified chapter doesn't exist. * Error code 5021: The specified chapter belongs to a
                different video. ``error`` is ``Error | LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.edit_chapter(chapter_id, video_id, body=body, request_options=request_options)
        )

    async def get_chapter(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Chapter:
        """This method returns a single chapter of the specified video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter was returned.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(await self._with_raw_response.get_chapter(chapter_id, video_id, request_options=request_options))

    async def get_chapter_thumbnail(
        self, chapter_id: float, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns the specified thumbnail associated with a saved video chapter.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            uid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail was returned.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_chapter_thumbnail(
                chapter_id, video_id, uid, request_options=request_options
            ),
        )

    async def get_chapter_thumbnails(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns every thumbnail associated with the specified saved video chapter.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnails were returned.

        Raises:
            ApiError: * The authenticated user can't perform this action. * Error code 2204: The request contains
                errors. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_chapter_thumbnails(chapter_id, video_id, request_options=request_options)
        )

    async def get_chapters(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChapterConnection:
        """This method returns every chapter of the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapters were returned.

        Raises:
            ApiError: No such video exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_chapters(
                video_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def get_unsaved_chapter_thumbnail(
        self, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns the specified thumbnail associated with an unsaved video chapter.

        Args:
            video_id: The ID of the video.
            uid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail was returned.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_unsaved_chapter_thumbnail(video_id, uid, request_options=request_options)
        )

    async def set_chapter_thumbnail_active(
        self,
        chapter_id: float,
        video_id: float,
        uid: str,
        *,
        body: VideosChaptersPicturesUidRequest | VideosChaptersPicturesUidRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method sets the specified chapter thumbnail for a video as active.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            uid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The chapter thumbnail was set as active.

        Raises:
            ApiError: * No such video or chapter exists. * Error code 5020: The specified chapter doesn't exist. * Error
                code 5021: The specified chapter belongs to a different video. ``error`` is ``LegacyError |
                RawError``."""
        return unwrap(
            await self._with_raw_response.set_chapter_thumbnail_active(
                chapter_id, video_id, uid, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncVideosChaptersWithRawResponse:
        return self._with_raw_response


class VideosChaptersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_chapter(
        self,
        video_id: float,
        *,
        body: VideosChaptersRequest | VideosChaptersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Chapter, CreateChapterErrorBody]:
        """This method adds a chapter to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/chapters"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersRequest | VideosChaptersRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Chapter],
            error_mapper=create_chapter_error_mapper,
            request_options=request_options,
        )

    def create_chapter_thumbnail_or_upload_link(
        self,
        chapter_id: float,
        video_id: float,
        *,
        body: VideosChaptersPicturesRequest | VideosChaptersPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateChapterThumbnailOrUploadLinkErrorBody]:
        """This method generates either an upload link or a timecode-based thumbnail for the specified saved video
        chapter. To generate the upload link, which enables the authenticated user to upload a chapter thumbnail image
        manually, leave the body of the request empty. To generate an automatic timecode-based thumbnail, include the
        **timecode** parameter in the body of the request.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersPicturesRequest | VideosChaptersPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_chapter_thumbnail_or_upload_link_error_mapper,
            request_options=request_options,
        )

    def create_unsaved_chapter_thumbnail_or_upload_link(
        self,
        video_id: float,
        *,
        body: VideosChaptersTemporaryPicturesRequest | VideosChaptersTemporaryPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateUnsavedChapterThumbnailOrUploadLinkErrorBody]:
        """This method generates either an upload link or a timecode-based thumbnail for an unsaved video chapter. To
        generate the upload link, which enables the authenticated user to upload a chapter thumbnail image manually,
        leave the body of the request empty. To generate an automatic timecode-based thumbnail, specify the **timecode**
        parameter in the body of the request.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/chapters/temporary/pictures"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersTemporaryPicturesRequest | VideosChaptersTemporaryPicturesRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_unsaved_chapter_thumbnail_or_upload_link_error_mapper,
            request_options=request_options,
        )

    def delete_chapter(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChapterErrorBody]:
        """This method deletes the specified chapter from a video. The authenticated user must be the owner of the
        video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_chapter_error_mapper,
            request_options=request_options,
        )

    def delete_chapter_thumbnail(
        self, chapter_id: float, uid: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChapterThumbnailErrorBody]:
        """This method deletes the specified chapter thumbnail from a video.

        The authenticated user must be the owner of the video that the chapter belongs to. This method deletes both
        timecode-generated and custom-uploaded thumbnails.

        Args:
            chapter_id: The ID of the chapter.
            uid: The unique ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}"),
            path_params=[
                param[float]("chapter_id", chapter_id), param[str]("uid", uid), param[float]("video_id", video_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_chapter_thumbnail_error_mapper,
            request_options=request_options,
        )

    def edit_chapter(
        self,
        chapter_id: float,
        video_id: float,
        *,
        body: VideosChaptersRequest1 | VideosChaptersRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Chapter, EditChapterErrorBody]:
        """This method edits the specified chapter of a video. The authenticated user must be the owner of the video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersRequest1 | VideosChaptersRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Chapter],
            error_mapper=edit_chapter_error_mapper,
            request_options=request_options,
        )

    def get_chapter(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Chapter, GetChapterErrorBody]:
        """This method returns a single chapter of the specified video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Chapter],
            error_mapper=get_chapter_error_mapper,
            request_options=request_options,
        )

    def get_chapter_thumbnail(
        self, chapter_id: float, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetChapterThumbnailErrorBody]:
        """This method returns the specified thumbnail associated with a saved video chapter.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            uid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}"),
            path_params=[
                param[float]("chapter_id", chapter_id), param[float]("video_id", video_id), param[str]("uid", uid)
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_chapter_thumbnail_error_mapper,
            request_options=request_options,
        )

    def get_chapter_thumbnails(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetChapterThumbnailsErrorBody]:
        """This method returns every thumbnail associated with the specified saved video chapter.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_chapter_thumbnails_error_mapper,
            request_options=request_options,
        )

    def get_chapters(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChapterConnection, GetChaptersErrorBody]:
        """This method returns every chapter of the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ChapterConnection],
            error_mapper=get_chapters_error_mapper,
            request_options=request_options,
        )

    def get_unsaved_chapter_thumbnail(
        self, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetUnsavedChapterThumbnailErrorBody]:
        """This method returns the specified thumbnail associated with an unsaved video chapter.

        Args:
            video_id: The ID of the video.
            uid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters/temporary/pictures/{uid}"),
            path_params=[param[float]("video_id", video_id), param[str]("uid", uid)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_unsaved_chapter_thumbnail_error_mapper,
            request_options=request_options,
        )

    def set_chapter_thumbnail_active(
        self,
        chapter_id: float,
        video_id: float,
        uid: str,
        *,
        body: VideosChaptersPicturesUidRequest | VideosChaptersPicturesUidRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, SetChapterThumbnailActiveErrorBody]:
        """This method sets the specified chapter thumbnail for a video as active.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            uid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}"),
            path_params=[
                param[float]("chapter_id", chapter_id), param[float]("video_id", video_id), param[str]("uid", uid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersPicturesUidRequest | VideosChaptersPicturesUidRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=set_chapter_thumbnail_active_error_mapper,
            request_options=request_options,
        )


class AsyncVideosChaptersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_chapter(
        self,
        video_id: float,
        *,
        body: VideosChaptersRequest | VideosChaptersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Chapter, CreateChapterErrorBody]:
        """This method adds a chapter to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/chapters"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersRequest | VideosChaptersRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Chapter],
            error_mapper=create_chapter_error_mapper,
            request_options=request_options,
        )

    async def create_chapter_thumbnail_or_upload_link(
        self,
        chapter_id: float,
        video_id: float,
        *,
        body: VideosChaptersPicturesRequest | VideosChaptersPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateChapterThumbnailOrUploadLinkErrorBody]:
        """This method generates either an upload link or a timecode-based thumbnail for the specified saved video
        chapter. To generate the upload link, which enables the authenticated user to upload a chapter thumbnail image
        manually, leave the body of the request empty. To generate an automatic timecode-based thumbnail, include the
        **timecode** parameter in the body of the request.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersPicturesRequest | VideosChaptersPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=create_chapter_thumbnail_or_upload_link_error_mapper,
            request_options=request_options,
        )

    async def create_unsaved_chapter_thumbnail_or_upload_link(
        self,
        video_id: float,
        *,
        body: VideosChaptersTemporaryPicturesRequest | VideosChaptersTemporaryPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, CreateUnsavedChapterThumbnailOrUploadLinkErrorBody]:
        """This method generates either an upload link or a timecode-based thumbnail for an unsaved video chapter. To
        generate the upload link, which enables the authenticated user to upload a chapter thumbnail image manually,
        leave the body of the request empty. To generate an automatic timecode-based thumbnail, specify the **timecode**
        parameter in the body of the request.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/chapters/temporary/pictures"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersTemporaryPicturesRequest | VideosChaptersTemporaryPicturesRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=create_unsaved_chapter_thumbnail_or_upload_link_error_mapper,
            request_options=request_options,
        )

    async def delete_chapter(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChapterErrorBody]:
        """This method deletes the specified chapter from a video. The authenticated user must be the owner of the
        video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_chapter_error_mapper,
            request_options=request_options,
        )

    async def delete_chapter_thumbnail(
        self, chapter_id: float, uid: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteChapterThumbnailErrorBody]:
        """This method deletes the specified chapter thumbnail from a video.

        The authenticated user must be the owner of the video that the chapter belongs to. This method deletes both
        timecode-generated and custom-uploaded thumbnails.

        Args:
            chapter_id: The ID of the chapter.
            uid: The unique ID of the thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}"),
            path_params=[
                param[float]("chapter_id", chapter_id), param[str]("uid", uid), param[float]("video_id", video_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_chapter_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def edit_chapter(
        self,
        chapter_id: float,
        video_id: float,
        *,
        body: VideosChaptersRequest1 | VideosChaptersRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Chapter, EditChapterErrorBody]:
        """This method edits the specified chapter of a video. The authenticated user must be the owner of the video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersRequest1 | VideosChaptersRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Chapter],
            error_mapper=edit_chapter_error_mapper,
            request_options=request_options,
        )

    async def get_chapter(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Chapter, GetChapterErrorBody]:
        """This method returns a single chapter of the specified video.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Chapter],
            error_mapper=get_chapter_error_mapper,
            request_options=request_options,
        )

    async def get_chapter_thumbnail(
        self, chapter_id: float, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetChapterThumbnailErrorBody]:
        """This method returns the specified thumbnail associated with a saved video chapter.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            uid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}"),
            path_params=[
                param[float]("chapter_id", chapter_id), param[float]("video_id", video_id), param[str]("uid", uid)
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=get_chapter_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def get_chapter_thumbnails(
        self, chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetChapterThumbnailsErrorBody]:
        """This method returns every thumbnail associated with the specified saved video chapter.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures"),
            path_params=[param[float]("chapter_id", chapter_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=get_chapter_thumbnails_error_mapper,
            request_options=request_options,
        )

    async def get_chapters(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChapterConnection, GetChaptersErrorBody]:
        """This method returns every chapter of the specified video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[ChapterConnection],
            error_mapper=get_chapters_error_mapper,
            request_options=request_options,
        )

    async def get_unsaved_chapter_thumbnail(
        self, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetUnsavedChapterThumbnailErrorBody]:
        """This method returns the specified thumbnail associated with an unsaved video chapter.

        Args:
            video_id: The ID of the video.
            uid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/chapters/temporary/pictures/{uid}"),
            path_params=[param[float]("video_id", video_id), param[str]("uid", uid)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=get_unsaved_chapter_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def set_chapter_thumbnail_active(
        self,
        chapter_id: float,
        video_id: float,
        uid: str,
        *,
        body: VideosChaptersPicturesUidRequest | VideosChaptersPicturesUidRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, SetChapterThumbnailActiveErrorBody]:
        """This method sets the specified chapter thumbnail for a video as active.

        Args:
            chapter_id: The ID of the chapter.
            video_id: The ID of the video.
            uid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}"),
            path_params=[
                param[float]("chapter_id", chapter_id), param[float]("video_id", video_id), param[str]("uid", uid)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosChaptersPicturesUidRequest | VideosChaptersPicturesUidRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=set_chapter_thumbnail_active_error_mapper,
            request_options=request_options,
        )
