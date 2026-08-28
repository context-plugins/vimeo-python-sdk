from __future__ import annotations

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
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.add_video_tag_error import AddVideoTagErrorBody, add_video_tag_error_mapper
from ..errors.add_video_tags_error import AddVideoTagsErrorBody, add_video_tags_error_mapper
from ..errors.check_video_for_tag_error import CheckVideoForTagErrorBody, check_video_for_tag_error_mapper
from ..errors.delete_video_tag_error import DeleteVideoTagErrorBody, delete_video_tag_error_mapper
from ..errors.get_videos_with_tag_error import GetVideosWithTagErrorBody, get_videos_with_tag_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort47 import Sort47OrStr
from ..models.tag import Tag
from ..models.tag_connection import TagConnection
from ..models.video_connection import VideoConnection
from ..server.server import Server


class VideosTags:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosTagsWithRawResponse(client, server, auth)

    def add_video_tag(self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None) -> Tag:
        """This method adds a single tag to the specified video. The authenticated user must have edit access to the
        video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was added.

        Raises:
            ApiError: * The tag is invalid. * An unsupported parameter was supplied. The total number of tags can't
                exceed 20. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_tag(video_id, word, request_options=request_options).unwrap()

    def add_video_tags(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Tag]:
        """This method adds multiple tags to the specified video. Include the tags as a JSON array as the body of the
        request with the **name** field, like this: ``[{ "name": "funny"}, {"name": "concert" }]``. The authenticated
        user must have edit access to the video. For more information on batch requests like this one, see `Using Common
        Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tags were added.

        Raises:
            ApiError: * The request body wasn't supplied. * A parameter is invalid. * The request body doesn't contain a
                JSON-encoded list of tags. * The authenticated user can't add tags to this video. * The total number of
                tags can't exceed 20. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_tags(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def check_video_for_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Tag:
        """This method determines whether the specified tag has been added to a video. The authenticated user must be
        the owner of the video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag has been added to the video.

        Raises:
            ApiError: * A parameter is invalid. * The tag is invalid. The video has no such tag. ``error`` is
                ``LegacyError | RawError``."""
        return self._with_raw_response.check_video_for_tag(video_id, word, request_options=request_options).unwrap()

    def delete_video_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified tag from a video. The authenticated user must have edit access to the
        video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was removed.

        Raises:
            ApiError: * A parameter is invalid. * The tag is invalid. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_video_tag(video_id, word, request_options=request_options).unwrap()

    def get_video_tags(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TagConnection:
        """This method returns all the tags associated with the specified video. The authenticated user must be the
        owner of the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tags were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_tags(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_videos_with_tag(
        self,
        word: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort47OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the public videos associated with the specified tag.

        Args:
            word: The tag word.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``created_time`` - Sort the results by creation
                time. * ``duration`` - Sort the results by duration. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: * No such tag exists. * Error code 5451: This resource is restricted in your region. ``error`` is
                ``LegacyError | RawError``."""
        return self._with_raw_response.get_videos_with_tag(
            word, direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosTagsWithRawResponse:
        return self._with_raw_response


class AsyncVideosTags:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosTagsWithRawResponse(client, server, auth)

    async def add_video_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Tag:
        """This method adds a single tag to the specified video. The authenticated user must have edit access to the
        video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was added.

        Raises:
            ApiError: * The tag is invalid. * An unsupported parameter was supplied. The total number of tags can't
                exceed 20. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.add_video_tag(video_id, word, request_options=request_options)).unwrap()

    async def add_video_tags(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Tag]:
        """This method adds multiple tags to the specified video. Include the tags as a JSON array as the body of the
        request with the **name** field, like this: ``[{ "name": "funny"}, {"name": "concert" }]``. The authenticated
        user must have edit access to the video. For more information on batch requests like this one, see `Using Common
        Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tags were added.

        Raises:
            ApiError: * The request body wasn't supplied. * A parameter is invalid. * The request body doesn't contain a
                JSON-encoded list of tags. * The authenticated user can't add tags to this video. * The total number of
                tags can't exceed 20. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_tags(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def check_video_for_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Tag:
        """This method determines whether the specified tag has been added to a video. The authenticated user must be
        the owner of the video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag has been added to the video.

        Raises:
            ApiError: * A parameter is invalid. * The tag is invalid. The video has no such tag. ``error`` is
                ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.check_video_for_tag(video_id, word, request_options=request_options)
        ).unwrap()

    async def delete_video_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified tag from a video. The authenticated user must have edit access to the
        video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tag was removed.

        Raises:
            ApiError: * A parameter is invalid. * The tag is invalid. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_video_tag(video_id, word, request_options=request_options)
        ).unwrap()

    async def get_video_tags(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TagConnection:
        """This method returns all the tags associated with the specified video. The authenticated user must be the
        owner of the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The tags were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_tags(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_videos_with_tag(
        self,
        word: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort47OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns all the public videos associated with the specified tag.

        Args:
            word: The tag word.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``created_time`` - Sort the results by creation
                time. * ``duration`` - Sort the results by duration. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: * No such tag exists. * Error code 5451: This resource is restricted in your region. ``error`` is
                ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_videos_with_tag(
                word, direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosTagsWithRawResponse:
        return self._with_raw_response


class VideosTagsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Tag, AddVideoTagErrorBody]:
        """This method adds a single tag to the specified video. The authenticated user must have edit access to the
        video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/tags/{word}"),
            path_params=[param[float]("video_id", video_id), param[str]("word", word)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Tag],
            error_mapper=add_video_tag_error_mapper,
            request_options=request_options,
        )

    def add_video_tags(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Tag], AddVideoTagsErrorBody]:
        """This method adds multiple tags to the specified video. Include the tags as a JSON array as the body of the
        request with the **name** field, like this: ``[{ "name": "funny"}, {"name": "concert" }]``. The authenticated
        user must have edit access to the video. For more information on batch requests like this one, see `Using Common
        Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/tags"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[Tag]],
            error_mapper=add_video_tags_error_mapper,
            request_options=request_options,
        )

    def check_video_for_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Tag, CheckVideoForTagErrorBody]:
        """This method determines whether the specified tag has been added to a video. The authenticated user must be
        the owner of the video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/tags/{word}"),
            path_params=[param[float]("video_id", video_id), param[str]("word", word)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Tag],
            error_mapper=check_video_for_tag_error_mapper,
            request_options=request_options,
        )

    def delete_video_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoTagErrorBody]:
        """This method removes the specified tag from a video. The authenticated user must have edit access to the
        video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/tags/{word}"),
            path_params=[param[float]("video_id", video_id), param[str]("word", word)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_tag_error_mapper,
            request_options=request_options,
        )

    def get_video_tags(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TagConnection, RawError]:
        """This method returns all the tags associated with the specified video. The authenticated user must be the
        owner of the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/tags"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TagConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_videos_with_tag(
        self,
        word: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort47OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetVideosWithTagErrorBody]:
        """This method returns all the public videos associated with the specified tag.

        Args:
            word: The tag word.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``created_time`` - Sort the results by creation
                time. * ``duration`` - Sort the results by duration. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tags/{word}/videos"),
            path_params=[param[str]("word", word)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort47OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_videos_with_tag_error_mapper,
            request_options=request_options,
        )


class AsyncVideosTagsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Tag, AddVideoTagErrorBody]:
        """This method adds a single tag to the specified video. The authenticated user must have edit access to the
        video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/tags/{word}"),
            path_params=[param[float]("video_id", video_id), param[str]("word", word)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Tag],
            error_mapper=add_video_tag_error_mapper,
            request_options=request_options,
        )

    async def add_video_tags(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Tag], AddVideoTagsErrorBody]:
        """This method adds multiple tags to the specified video. Include the tags as a JSON array as the body of the
        request with the **name** field, like this: ``[{ "name": "funny"}, {"name": "concert" }]``. The authenticated
        user must have edit access to the video. For more information on batch requests like this one, see `Using Common
        Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/tags"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[Tag]],
            error_mapper=add_video_tags_error_mapper,
            request_options=request_options,
        )

    async def check_video_for_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Tag, CheckVideoForTagErrorBody]:
        """This method determines whether the specified tag has been added to a video. The authenticated user must be
        the owner of the video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/tags/{word}"),
            path_params=[param[float]("video_id", video_id), param[str]("word", word)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Tag],
            error_mapper=check_video_for_tag_error_mapper,
            request_options=request_options,
        )

    async def delete_video_tag(
        self, video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoTagErrorBody]:
        """This method removes the specified tag from a video. The authenticated user must have edit access to the
        video.

        Args:
            video_id: The ID of the video.
            word: The tag word.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/tags/{word}"),
            path_params=[param[float]("video_id", video_id), param[str]("word", word)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_tag_error_mapper,
            request_options=request_options,
        )

    async def get_video_tags(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TagConnection, RawError]:
        """This method returns all the tags associated with the specified video. The authenticated user must be the
        owner of the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/tags"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[TagConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_videos_with_tag(
        self,
        word: str,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort47OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetVideosWithTagErrorBody]:
        """This method returns all the public videos associated with the specified tag.

        Args:
            word: The tag word.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``created_time`` - Sort the results by creation
                time. * ``duration`` - Sort the results by duration. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tags/{word}/videos"),
            path_params=[param[str]("word", word)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort47OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_videos_with_tag_error_mapper,
            request_options=request_options,
        )
