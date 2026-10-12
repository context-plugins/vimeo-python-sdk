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
from ..errors.create_showcase_logo_error import CreateShowcaseLogoErrorBody, create_showcase_logo_error_mapper
from ..errors.delete_showcase_logo_error import DeleteShowcaseLogoErrorBody, delete_showcase_logo_error_mapper
from ..errors.get_showcase_logo_error import GetShowcaseLogoErrorBody, get_showcase_logo_error_mapper
from ..errors.get_showcase_logos_error import GetShowcaseLogosErrorBody, get_showcase_logos_error_mapper
from ..errors.replace_showcase_logo_error import ReplaceShowcaseLogoErrorBody, replace_showcase_logo_error_mapper
from ..models.picture import Picture
from ..models.picture_connection import PictureConnection
from ..models.users_albums_logos_logo_id_request import UsersAlbumsLogosLogoIdRequest, UsersAlbumsLogosLogoIdRequestDict
from ..server.server import Server


class ShowcasesCustomShowcaseLogos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ShowcasesCustomShowcaseLogosWithRawResponse(client, server, auth)

    def create_showcase_logo(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds an image file as a custom logo to the specified showcase. The authenticated user must be the
        owner of the showcase.

        For information on how to upload the logo, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The logo was added to the showcase.

        Raises:
            ApiError: The authenticated user can't add custom logos to this showcase. No such showcase exists. ``error``
                is ``LegacyError | RawError``."""
        return unwrap(self._with_raw_response.create_showcase_logo(album_id, user_id, request_options=request_options))

    def delete_showcase_logo(
        self, album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified custom logo from its showcase. The authenticated user must be the owner of
        the showcase.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The custom logo was deleted.

        Raises:
            ApiError: The authenticated user can't delete this custom logo. No such showcase exists, or it doesn't
                contain the specified custom logo. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.delete_showcase_logo(album_id, logo_id, user_id, request_options=request_options)
        )

    def get_showcase_logo(
        self, album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single custom logo of the specified showcase. The authenticated user must be the owner
        of the showcase.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The custom logo was returned.

        Raises:
            ApiError: The authenticated user can't access this custom logo. No such showcase exists, or it doesn't
                contain the specified custom logo. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_showcase_logo(album_id, logo_id, user_id, request_options=request_options)
        )

    def get_showcase_logos(
        self,
        album_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every custom logo of the specified showcase. The authenticated user must be the owner of
        the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The custom logos were returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.get_showcase_logos(
                album_id, user_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    def replace_showcase_logo(
        self,
        album_id: float,
        logo_id: float,
        user_id: float,
        *,
        body: UsersAlbumsLogosLogoIdRequest | UsersAlbumsLogosLogoIdRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method replaces the specified custom showcase logo with a new image file. The authenticated user must be
        the owner of the showcase.

        For information on how to upload the logo, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The custom logo was replaced.

        Raises:
            ApiError: The authenticated user can't replace this custom logo. No such showcase exists, or it doesn't
                contain the specified custom logo. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            self._with_raw_response.replace_showcase_logo(
                album_id, logo_id, user_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ShowcasesCustomShowcaseLogosWithRawResponse:
        return self._with_raw_response


class AsyncShowcasesCustomShowcaseLogos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncShowcasesCustomShowcaseLogosWithRawResponse(client, server, auth)

    async def create_showcase_logo(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds an image file as a custom logo to the specified showcase. The authenticated user must be the
        owner of the showcase.

        For information on how to upload the logo, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The logo was added to the showcase.

        Raises:
            ApiError: The authenticated user can't add custom logos to this showcase. No such showcase exists. ``error``
                is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.create_showcase_logo(album_id, user_id, request_options=request_options)
        )

    async def delete_showcase_logo(
        self, album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified custom logo from its showcase. The authenticated user must be the owner of
        the showcase.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The custom logo was deleted.

        Raises:
            ApiError: The authenticated user can't delete this custom logo. No such showcase exists, or it doesn't
                contain the specified custom logo. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_showcase_logo(
                album_id, logo_id, user_id, request_options=request_options
            ),
        )

    async def get_showcase_logo(
        self, album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single custom logo of the specified showcase. The authenticated user must be the owner
        of the showcase.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The custom logo was returned.

        Raises:
            ApiError: The authenticated user can't access this custom logo. No such showcase exists, or it doesn't
                contain the specified custom logo. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_showcase_logo(album_id, logo_id, user_id, request_options=request_options)
        )

    async def get_showcase_logos(
        self,
        album_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every custom logo of the specified showcase. The authenticated user must be the owner of
        the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The custom logos were returned.

        Raises:
            ApiError: No such showcase exists. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_showcase_logos(
                album_id, user_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def replace_showcase_logo(
        self,
        album_id: float,
        logo_id: float,
        user_id: float,
        *,
        body: UsersAlbumsLogosLogoIdRequest | UsersAlbumsLogosLogoIdRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method replaces the specified custom showcase logo with a new image file. The authenticated user must be
        the owner of the showcase.

        For information on how to upload the logo, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The custom logo was replaced.

        Raises:
            ApiError: The authenticated user can't replace this custom logo. No such showcase exists, or it doesn't
                contain the specified custom logo. ``error`` is ``LegacyError | RawError``."""
        return unwrap(
            await self._with_raw_response.replace_showcase_logo(
                album_id, logo_id, user_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncShowcasesCustomShowcaseLogosWithRawResponse:
        return self._with_raw_response


class ShowcasesCustomShowcaseLogosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_showcase_logo(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateShowcaseLogoErrorBody]:
        """This method adds an image file as a custom logo to the specified showcase. The authenticated user must be the
        owner of the showcase.

        For information on how to upload the logo, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_showcase_logo_error_mapper,
            request_options=request_options,
        )

    def delete_showcase_logo(
        self, album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteShowcaseLogoErrorBody]:
        """This method deletes the specified custom logo from its showcase. The authenticated user must be the owner of
        the showcase.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos/{logo_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("logo_id", logo_id), param[float]("user_id", user_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_showcase_logo_error_mapper,
            request_options=request_options,
        )

    def get_showcase_logo(
        self, album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetShowcaseLogoErrorBody]:
        """This method returns a single custom logo of the specified showcase. The authenticated user must be the owner
        of the showcase.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos/{logo_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("logo_id", logo_id), param[float]("user_id", user_id)
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_showcase_logo_error_mapper,
            request_options=request_options,
        )

    def get_showcase_logos(
        self,
        album_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetShowcaseLogosErrorBody]:
        """This method returns every custom logo of the specified showcase. The authenticated user must be the owner of
        the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_showcase_logos_error_mapper,
            request_options=request_options,
        )

    def replace_showcase_logo(
        self,
        album_id: float,
        logo_id: float,
        user_id: float,
        *,
        body: UsersAlbumsLogosLogoIdRequest | UsersAlbumsLogosLogoIdRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, ReplaceShowcaseLogoErrorBody]:
        """This method replaces the specified custom showcase logo with a new image file. The authenticated user must be
        the owner of the showcase.

        For information on how to upload the logo, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos/{logo_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("logo_id", logo_id), param[float]("user_id", user_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersAlbumsLogosLogoIdRequest | UsersAlbumsLogosLogoIdRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=replace_showcase_logo_error_mapper,
            request_options=request_options,
        )


class AsyncShowcasesCustomShowcaseLogosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_showcase_logo(
        self, album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateShowcaseLogoErrorBody]:
        """This method adds an image file as a custom logo to the specified showcase. The authenticated user must be the
        owner of the showcase.

        For information on how to upload the logo, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=create_showcase_logo_error_mapper,
            request_options=request_options,
        )

    async def delete_showcase_logo(
        self, album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteShowcaseLogoErrorBody]:
        """This method deletes the specified custom logo from its showcase. The authenticated user must be the owner of
        the showcase.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos/{logo_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("logo_id", logo_id), param[float]("user_id", user_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_showcase_logo_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_logo(
        self, album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetShowcaseLogoErrorBody]:
        """This method returns a single custom logo of the specified showcase. The authenticated user must be the owner
        of the showcase.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos/{logo_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("logo_id", logo_id), param[float]("user_id", user_id)
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=get_showcase_logo_error_mapper,
            request_options=request_options,
        )

    async def get_showcase_logos(
        self,
        album_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetShowcaseLogosErrorBody]:
        """This method returns every custom logo of the specified showcase. The authenticated user must be the owner of
        the showcase.

        Args:
            album_id: The ID of the showcase.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos"),
            path_params=[param[float]("album_id", album_id), param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PictureConnection],
            error_mapper=get_showcase_logos_error_mapper,
            request_options=request_options,
        )

    async def replace_showcase_logo(
        self,
        album_id: float,
        logo_id: float,
        user_id: float,
        *,
        body: UsersAlbumsLogosLogoIdRequest | UsersAlbumsLogosLogoIdRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, ReplaceShowcaseLogoErrorBody]:
        """This method replaces the specified custom showcase logo with a new image file. The authenticated user must be
        the owner of the showcase.

        For information on how to upload the logo, see our `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails>`__ guide.

        Args:
            album_id: The ID of the showcase.
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/albums/{album_id}/logos/{logo_id}"),
            path_params=[
                param[float]("album_id", album_id), param[float]("logo_id", logo_id), param[float]("user_id", user_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersAlbumsLogosLogoIdRequest | UsersAlbumsLogosLogoIdRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=replace_showcase_logo_error_mapper,
            request_options=request_options,
        )
