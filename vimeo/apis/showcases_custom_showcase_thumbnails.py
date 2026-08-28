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
from ..errors.create_showcase_custom_thumb_error import (
    CreateShowcaseCustomThumbErrorBody,
    create_showcase_custom_thumb_error_mapper,
)
from ..errors.delete_showcase_custom_thumbnail_error import (
    DeleteShowcaseCustomThumbnailErrorBody,
    delete_showcase_custom_thumbnail_error_mapper,
)
from ..errors.get_showcase_custom_thumbnail_error import (
    GetShowcaseCustomThumbnailErrorBody,
    get_showcase_custom_thumbnail_error_mapper,
)
from ..errors.get_showcase_custom_thumbs_error import (
    GetShowcaseCustomThumbsErrorBody,
    get_showcase_custom_thumbs_error_mapper,
)
from ..errors.replace_showcase_custom_thumb_error import (
    ReplaceShowcaseCustomThumbErrorBody,
    replace_showcase_custom_thumb_error_mapper,
)
from ..models.picture import Picture
from ..models.picture_connection import PictureConnection
from ..models.users_albums_custom_thumbnails_thumbnail_id_request import (
    UsersAlbumsCustomThumbnailsThumbnailIdRequest,
    UsersAlbumsCustomThumbnailsThumbnailIdRequestDict,
)
from ..server.server import Server


class ShowcasesCustomShowcaseThumbnails:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ShowcasesCustomShowcaseThumbnailsWithRawResponse(client, server, auth)

    def create_showcase_custom_thumb(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds an uploaded image file as a custom thumbnail for the specified showcase. The image doesn't
        need to be a still from a showcase video, unlike with the `standard thumbnail method
        <https://developer.vimeo.com/api/reference/showcases#set_video_as_showcase_thumbnail>`__. The authenticated user
        must be the owner of the showcase.

        For information on how to upload the thumbnail, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide, and follow the same steps.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnail was added to the showcase.

        Raises:
            ApiError: The authenticated user can't add custom thumbnails to this showcase. No such showcase exists.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_showcase_custom_thumb(
            album_id, user_id, request_options=request_options
        ).unwrap()

    def delete_showcase_custom_thumbnail(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes the specified custom thumbnail from its showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnail was deleted.

        Raises:
            ApiError: The authenticated user can't delete this custom thumbnail. No such showcase exists, or it doesn't
                contain the specified custom thumbnail. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_showcase_custom_thumbnail(
            album_id, thumbnail_id, user_id, request_options=request_options
        ).unwrap()

    def get_showcase_custom_thumbnail(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method returns a single custom thumbnail of the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnail was returned.

        Raises:
            ApiError: The authenticated user can't view this custom thumbnail. No such showcase exists, or it doesn't
                contain the specified custom thumbnail. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_showcase_custom_thumbnail(
            album_id, thumbnail_id, user_id, request_options=request_options
        ).unwrap()

    def get_showcase_custom_thumbs(
        self,
        album_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every custom thumbnail of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnails were returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't view the custon thumbnails from this showcase. No
                such showcase exists. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.get_showcase_custom_thumbs(
            album_id, user_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def replace_showcase_custom_thumb(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        body: (
            UsersAlbumsCustomThumbnailsThumbnailIdRequest | UsersAlbumsCustomThumbnailsThumbnailIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method replaces the specified custom showcase thumbnail with a new image file. The authenticated user
        must be the owner of the showcase.

        For information on how to upload the thumbnail, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnail was replaced.

        Raises:
            ApiError: The authenticated user can't replace this custom thumbnail. No such showcase exists, or it doesn't
                contain the specified custom thumbnail. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.replace_showcase_custom_thumb(
            album_id, thumbnail_id, user_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ShowcasesCustomShowcaseThumbnailsWithRawResponse:
        return self._with_raw_response


class AsyncShowcasesCustomShowcaseThumbnails:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncShowcasesCustomShowcaseThumbnailsWithRawResponse(client, server, auth)

    async def create_showcase_custom_thumb(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds an uploaded image file as a custom thumbnail for the specified showcase. The image doesn't
        need to be a still from a showcase video, unlike with the `standard thumbnail method
        <https://developer.vimeo.com/api/reference/showcases#set_video_as_showcase_thumbnail>`__. The authenticated user
        must be the owner of the showcase.

        For information on how to upload the thumbnail, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide, and follow the same steps.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnail was added to the showcase.

        Raises:
            ApiError: The authenticated user can't add custom thumbnails to this showcase. No such showcase exists.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.create_showcase_custom_thumb(
                album_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def delete_showcase_custom_thumbnail(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes the specified custom thumbnail from its showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnail was deleted.

        Raises:
            ApiError: The authenticated user can't delete this custom thumbnail. No such showcase exists, or it doesn't
                contain the specified custom thumbnail. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_showcase_custom_thumbnail(
                album_id, thumbnail_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def get_showcase_custom_thumbnail(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method returns a single custom thumbnail of the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnail was returned.

        Raises:
            ApiError: The authenticated user can't view this custom thumbnail. No such showcase exists, or it doesn't
                contain the specified custom thumbnail. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_showcase_custom_thumbnail(
                album_id, thumbnail_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def get_showcase_custom_thumbs(
        self,
        album_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every custom thumbnail of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnails were returned.

        Raises:
            ApiError: Error code 3200: The authenticated user can't view the custon thumbnails from this showcase. No
                such showcase exists. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_showcase_custom_thumbs(
                album_id, user_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def replace_showcase_custom_thumb(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        body: (
            UsersAlbumsCustomThumbnailsThumbnailIdRequest | UsersAlbumsCustomThumbnailsThumbnailIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method replaces the specified custom showcase thumbnail with a new image file. The authenticated user
        must be the owner of the showcase.

        For information on how to upload the thumbnail, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom thumbnail was replaced.

        Raises:
            ApiError: The authenticated user can't replace this custom thumbnail. No such showcase exists, or it doesn't
                contain the specified custom thumbnail. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.replace_showcase_custom_thumb(
                album_id, thumbnail_id, user_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncShowcasesCustomShowcaseThumbnailsWithRawResponse:
        return self._with_raw_response


class ShowcasesCustomShowcaseThumbnailsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_showcase_custom_thumb(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateShowcaseCustomThumbErrorBody]:
        """This method adds an uploaded image file as a custom thumbnail for the specified showcase. The image doesn't
        need to be a still from a showcase video, unlike with the `standard thumbnail method
        <https://developer.vimeo.com/api/reference/showcases#set_video_as_showcase_thumbnail>`__. The authenticated user
        must be the owner of the showcase.

        For information on how to upload the thumbnail, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide, and follow the same steps.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_showcase_custom_thumb_error_mapper,
            request_options=request_options,
        )

    def delete_showcase_custom_thumbnail(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteShowcaseCustomThumbnailErrorBody]:
        """This method deletes the specified custom thumbnail from its showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"),
            path_params=[
                param[float]("album_id", album_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_showcase_custom_thumbnail_error_mapper,
            request_options=request_options,
        )

    def get_showcase_custom_thumbnail(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, GetShowcaseCustomThumbnailErrorBody]:
        """This method returns a single custom thumbnail of the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"),
            path_params=[
                param[float]("album_id", album_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_showcase_custom_thumbnail_error_mapper,
            request_options=request_options,
        )

    def get_showcase_custom_thumbs(
        self,
        album_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetShowcaseCustomThumbsErrorBody]:
        """This method returns every custom thumbnail of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_showcase_custom_thumbs_error_mapper,
            request_options=request_options,
        )

    def replace_showcase_custom_thumb(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        body: (
            UsersAlbumsCustomThumbnailsThumbnailIdRequest | UsersAlbumsCustomThumbnailsThumbnailIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, ReplaceShowcaseCustomThumbErrorBody]:
        """This method replaces the specified custom showcase thumbnail with a new image file. The authenticated user
        must be the owner of the showcase.

        For information on how to upload the thumbnail, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"),
            path_params=[
                param[float]("album_id", album_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            body=json_body[
                UsersAlbumsCustomThumbnailsThumbnailIdRequest | UsersAlbumsCustomThumbnailsThumbnailIdRequestDict | None
            ](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=replace_showcase_custom_thumb_error_mapper,
            request_options=request_options,
        )


class AsyncShowcasesCustomShowcaseThumbnailsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_showcase_custom_thumb(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateShowcaseCustomThumbErrorBody]:
        """This method adds an uploaded image file as a custom thumbnail for the specified showcase. The image doesn't
        need to be a still from a showcase video, unlike with the `standard thumbnail method
        <https://developer.vimeo.com/api/reference/showcases#set_video_as_showcase_thumbnail>`__. The authenticated user
        must be the owner of the showcase.

        For information on how to upload the thumbnail, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide, and follow the same steps.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_showcase_custom_thumb_error_mapper,
            request_options=request_options,
        )

    async def delete_showcase_custom_thumbnail(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteShowcaseCustomThumbnailErrorBody]:
        """This method deletes the specified custom thumbnail from its showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"),
            path_params=[
                param[float]("album_id", album_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_showcase_custom_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_custom_thumbnail(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, GetShowcaseCustomThumbnailErrorBody]:
        """This method returns a single custom thumbnail of the specified showcase. The authenticated user must be the
        owner of the showcase.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"),
            path_params=[
                param[float]("album_id", album_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_showcase_custom_thumbnail_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_custom_thumbs(
        self,
        album_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetShowcaseCustomThumbsErrorBody]:
        """This method returns every custom thumbnail of the specified showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_showcase_custom_thumbs_error_mapper,
            request_options=request_options,
        )

    async def replace_showcase_custom_thumb(
        self,
        album_id: float,
        thumbnail_id: float,
        user_id: float,
        *,
        body: (
            UsersAlbumsCustomThumbnailsThumbnailIdRequest | UsersAlbumsCustomThumbnailsThumbnailIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, ReplaceShowcaseCustomThumbErrorBody]:
        """This method replaces the specified custom showcase thumbnail with a new image file. The authenticated user
        must be the owner of the showcase.

        For information on how to upload the thumbnail, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            thumbnail_id: The ID of the custom thumbnail.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}"),
            path_params=[
                param[float]("album_id", album_id),
                param[float]("thumbnail_id", thumbnail_id),
                param[float]("user_id", user_id),
            ],
            body=json_body[
                UsersAlbumsCustomThumbnailsThumbnailIdRequest | UsersAlbumsCustomThumbnailsThumbnailIdRequestDict | None
            ](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=replace_showcase_custom_thumb_error_mapper,
            request_options=request_options,
        )
