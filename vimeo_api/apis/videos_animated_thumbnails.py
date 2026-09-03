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
from ..errors.create_animated_thumbset_error import (
    CreateAnimatedThumbsetErrorBody,
    create_animated_thumbset_error_mapper,
)
from ..errors.delete_animated_thumbset_error import (
    DeleteAnimatedThumbsetErrorBody,
    delete_animated_thumbset_error_mapper,
)
from ..errors.get_all_animated_thumbset_error import (
    GetAllAnimatedThumbsetErrorBody,
    get_all_animated_thumbset_error_mapper,
)
from ..errors.get_animated_thumbset_error import GetAnimatedThumbsetErrorBody, get_animated_thumbset_error_mapper
from ..errors.get_animated_thumbset_status_error import (
    GetAnimatedThumbsetStatusErrorBody,
    get_animated_thumbset_status_error_mapper,
)
from ..models.animated_thumbset import AnimatedThumbset
from ..models.animated_thumbset_connection import AnimatedThumbsetConnection
from ..models.videos_animated_thumbsets_request import (
    VideosAnimatedThumbsetsRequest,
    VideosAnimatedThumbsetsRequestDict,
)
from ..server.server import Server


class VideosAnimatedThumbnails:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosAnimatedThumbnailsWithRawResponse(client, server, auth)

    def create_animated_thumbset(
        self,
        video_id: float,
        body: VideosAnimatedThumbsetsRequest | VideosAnimatedThumbsetsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnimatedThumbset:
        """This method creates a set of animated thumbnails for the specified video. Please note that you can't create
        more than four sets of animated thumbnails for the same video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The set of animated thumbnails was created.

        Raises:
            ApiError: * Error code 2204: A parameter is invalid. * Error code 3130: The video can't have more than four
                sets of animated thumbnails. The user can't create a set of animated thumbnails from the specified
                section of the video. The authenticated user is rate-limited from creating new animated thumbnails.
                ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.create_animated_thumbset(
            video_id, body, request_options=request_options
        ).unwrap()

    def delete_animated_thumbset(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a set of animated thumbnails for the specified video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The set of animated thumbnails was deleted.

        Raises:
            ApiError: * Error code 5001: The authenticated user doesn't have permission to delete the animated thumbset.
                * Error code 5017: No such set of animated thumbnails exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.delete_animated_thumbset(
            picture_id, video_id, request_options=request_options
        ).unwrap()

    def get_all_animated_thumbset(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnimatedThumbsetConnection:
        """This method returns all the sets of animated thumbnails associated with the specified video. The
        authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The sets of animated thumbnails were returned.

        Raises:
            ApiError: * Error code 5001: The authenticated user doesn't own the video. * Error code 5017: No such set of
                animated thumbnails exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_all_animated_thumbset(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_animated_thumbset(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnimatedThumbset:
        """This method returns a particular set of animated thumbnails associated with the specified video. The
        authenticated user must be the owner of the video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The set of animated thumbnails was returned.

        Raises:
            ApiError: * Error code 5001: The authenticated user doesn't own the video. * Error code 5017: No such set of
                animated thumbnails exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_animated_thumbset(
            picture_id, video_id, request_options=request_options
        ).unwrap()

    def get_animated_thumbset_status(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnimatedThumbset:
        """This method returns the status of a particular set of animated thumbnails associated with the specified
        video. The status indicates whether the thumbnails are ready to use. The authenticated user must be the owner of
        the video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The status of the set of animated thumbnails was returned.

        Raises:
            ApiError: * Error code 5001: The authenticated user doesn't own the video. * Error code 5017: No such set of
                animated thumbnails exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_animated_thumbset_status(
            picture_id, video_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosAnimatedThumbnailsWithRawResponse:
        return self._with_raw_response


class AsyncVideosAnimatedThumbnails:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosAnimatedThumbnailsWithRawResponse(client, server, auth)

    async def create_animated_thumbset(
        self,
        video_id: float,
        body: VideosAnimatedThumbsetsRequest | VideosAnimatedThumbsetsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnimatedThumbset:
        """This method creates a set of animated thumbnails for the specified video. Please note that you can't create
        more than four sets of animated thumbnails for the same video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The set of animated thumbnails was created.

        Raises:
            ApiError: * Error code 2204: A parameter is invalid. * Error code 3130: The video can't have more than four
                sets of animated thumbnails. The user can't create a set of animated thumbnails from the specified
                section of the video. The authenticated user is rate-limited from creating new animated thumbnails.
                ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.create_animated_thumbset(video_id, body, request_options=request_options)
        ).unwrap()

    async def delete_animated_thumbset(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a set of animated thumbnails for the specified video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The set of animated thumbnails was deleted.

        Raises:
            ApiError: * Error code 5001: The authenticated user doesn't have permission to delete the animated thumbset.
                * Error code 5017: No such set of animated thumbnails exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.delete_animated_thumbset(
                picture_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_all_animated_thumbset(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnimatedThumbsetConnection:
        """This method returns all the sets of animated thumbnails associated with the specified video. The
        authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The sets of animated thumbnails were returned.

        Raises:
            ApiError: * Error code 5001: The authenticated user doesn't own the video. * Error code 5017: No such set of
                animated thumbnails exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_all_animated_thumbset(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_animated_thumbset(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnimatedThumbset:
        """This method returns a particular set of animated thumbnails associated with the specified video. The
        authenticated user must be the owner of the video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The set of animated thumbnails was returned.

        Raises:
            ApiError: * Error code 5001: The authenticated user doesn't own the video. * Error code 5017: No such set of
                animated thumbnails exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_animated_thumbset(picture_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_animated_thumbset_status(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnimatedThumbset:
        """This method returns the status of a particular set of animated thumbnails associated with the specified
        video. The status indicates whether the thumbnails are ready to use. The authenticated user must be the owner of
        the video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The status of the set of animated thumbnails was returned.

        Raises:
            ApiError: * Error code 5001: The authenticated user doesn't own the video. * Error code 5017: No such set of
                animated thumbnails exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_animated_thumbset_status(
                picture_id, video_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosAnimatedThumbnailsWithRawResponse:
        return self._with_raw_response


class VideosAnimatedThumbnailsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_animated_thumbset(
        self,
        video_id: float,
        body: VideosAnimatedThumbsetsRequest | VideosAnimatedThumbsetsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnimatedThumbset, CreateAnimatedThumbsetErrorBody]:
        """This method creates a set of animated thumbnails for the specified video. Please note that you can't create
        more than four sets of animated thumbnails for the same video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosAnimatedThumbsetsRequest | VideosAnimatedThumbsetsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnimatedThumbset],
            error_mapper=create_animated_thumbset_error_mapper,
            request_options=request_options,
        )

    def delete_animated_thumbset(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteAnimatedThumbsetErrorBody]:
        """This method deletes a set of animated thumbnails for the specified video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets/{picture_id}"),
            path_params=[param[str]("picture_id", picture_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_animated_thumbset_error_mapper,
            request_options=request_options,
        )

    def get_all_animated_thumbset(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnimatedThumbsetConnection, GetAllAnimatedThumbsetErrorBody]:
        """This method returns all the sets of animated thumbnails associated with the specified video. The
        authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnimatedThumbsetConnection],
            error_mapper=get_all_animated_thumbset_error_mapper,
            request_options=request_options,
        )

    def get_animated_thumbset(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnimatedThumbset, GetAnimatedThumbsetErrorBody]:
        """This method returns a particular set of animated thumbnails associated with the specified video. The
        authenticated user must be the owner of the video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets/{picture_id}"),
            path_params=[param[str]("picture_id", picture_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnimatedThumbset],
            error_mapper=get_animated_thumbset_error_mapper,
            request_options=request_options,
        )

    def get_animated_thumbset_status(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnimatedThumbset, GetAnimatedThumbsetStatusErrorBody]:
        """This method returns the status of a particular set of animated thumbnails associated with the specified
        video. The status indicates whether the thumbnails are ready to use. The authenticated user must be the owner of
        the video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets/{picture_id}/status"),
            path_params=[param[str]("picture_id", picture_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnimatedThumbset],
            error_mapper=get_animated_thumbset_status_error_mapper,
            request_options=request_options,
        )


class AsyncVideosAnimatedThumbnailsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_animated_thumbset(
        self,
        video_id: float,
        body: VideosAnimatedThumbsetsRequest | VideosAnimatedThumbsetsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnimatedThumbset, CreateAnimatedThumbsetErrorBody]:
        """This method creates a set of animated thumbnails for the specified video. Please note that you can't create
        more than four sets of animated thumbnails for the same video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosAnimatedThumbsetsRequest | VideosAnimatedThumbsetsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnimatedThumbset],
            error_mapper=create_animated_thumbset_error_mapper,
            request_options=request_options,
        )

    async def delete_animated_thumbset(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteAnimatedThumbsetErrorBody]:
        """This method deletes a set of animated thumbnails for the specified video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets/{picture_id}"),
            path_params=[param[str]("picture_id", picture_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_animated_thumbset_error_mapper,
            request_options=request_options,
        )

    async def get_all_animated_thumbset(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnimatedThumbsetConnection, GetAllAnimatedThumbsetErrorBody]:
        """This method returns all the sets of animated thumbnails associated with the specified video. The
        authenticated user must be the owner of the video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnimatedThumbsetConnection],
            error_mapper=get_all_animated_thumbset_error_mapper,
            request_options=request_options,
        )

    async def get_animated_thumbset(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnimatedThumbset, GetAnimatedThumbsetErrorBody]:
        """This method returns a particular set of animated thumbnails associated with the specified video. The
        authenticated user must be the owner of the video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets/{picture_id}"),
            path_params=[param[str]("picture_id", picture_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnimatedThumbset],
            error_mapper=get_animated_thumbset_error_mapper,
            request_options=request_options,
        )

    async def get_animated_thumbset_status(
        self, picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnimatedThumbset, GetAnimatedThumbsetStatusErrorBody]:
        """This method returns the status of a particular set of animated thumbnails associated with the specified
        video. The status indicates whether the thumbnails are ready to use. The authenticated user must be the owner of
        the video.

        Args:
            picture_id: The UUID of the set of animated thumbnails.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/animated_thumbsets/{picture_id}/status"),
            path_params=[param[str]("picture_id", picture_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnimatedThumbset],
            error_mapper=get_animated_thumbset_status_error_mapper,
            request_options=request_options,
        )
