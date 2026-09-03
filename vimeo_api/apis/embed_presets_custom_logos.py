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
    json_decoder,
    param,
)
from ..errors.create_custom_logo_alt1_error import CreateCustomLogoAlt1ErrorBody, create_custom_logo_alt1_error_mapper
from ..errors.create_custom_logo_error import CreateCustomLogoErrorBody, create_custom_logo_error_mapper
from ..errors.delete_custom_logo_alt1_error import DeleteCustomLogoAlt1ErrorBody, delete_custom_logo_alt1_error_mapper
from ..errors.delete_custom_logo_error import DeleteCustomLogoErrorBody, delete_custom_logo_error_mapper
from ..errors.get_custom_logo_alt1_error import GetCustomLogoAlt1ErrorBody, get_custom_logo_alt1_error_mapper
from ..errors.get_custom_logo_error import GetCustomLogoErrorBody, get_custom_logo_error_mapper
from ..errors.get_custom_logos_alt1_error import GetCustomLogosAlt1ErrorBody, get_custom_logos_alt1_error_mapper
from ..errors.get_custom_logos_error import GetCustomLogosErrorBody, get_custom_logos_error_mapper
from ..models.picture import Picture
from ..models.picture_connection import PictureConnection
from ..server.server import Server


class EmbedPresetsCustomLogos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmbedPresetsCustomLogosWithRawResponse(client, server, auth)

    def create_custom_logo(self, user_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method adds a custom logo representing the authenticated user for display in the embedded player. Be
        sure to use this method in the context of the multi-step upload procedure described in our `Working with
        Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail>`__ guide. This
        method represents Step 2 of the procedure.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was added.

        Raises:
            ApiError: The authenticated user can't add the custom logo. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_custom_logo(user_id, request_options=request_options).unwrap()

    def create_custom_logo_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method adds a custom logo representing the authenticated user for display in the embedded player. Be
        sure to use this method in the context of the multi-step upload procedure described in our `Working with
        Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail>`__ guide. This
        method represents Step 2 of the procedure.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was added.

        Raises:
            ApiError: The authenticated user can't add the custom logo. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_custom_logo_alt1(request_options=request_options).unwrap()

    def delete_custom_logo(
        self, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was deleted.

        Raises:
            ApiError: The authenticated user can't access the custom logo. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_custom_logo(logo_id, user_id, request_options=request_options).unwrap()

    def delete_custom_logo_alt1(self, logo_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the specified custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was deleted.

        Raises:
            ApiError: The authenticated user can't access the custom logo. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_custom_logo_alt1(logo_id, request_options=request_options).unwrap()

    def get_custom_logo(
        self, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was returned.

        Raises:
            ApiError: The authenticated user can't access the custom logo. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_custom_logo(logo_id, user_id, request_options=request_options).unwrap()

    def get_custom_logo_alt1(self, logo_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method returns a single custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was returned.

        Raises:
            ApiError: The authenticated user can't access the custom logo. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_custom_logo_alt1(logo_id, request_options=request_options).unwrap()

    def get_custom_logos(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sizes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every custom logo that belongs to the authenticated user or team owner.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logos were returned.

        Raises:
            ApiError: The authenticated user can't access the custom logos. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_custom_logos(
            user_id, page=page, per_page=per_page, sizes=sizes, request_options=request_options
        ).unwrap()

    def get_custom_logos_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sizes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every custom logo that belongs to the authenticated user or team owner.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logos were returned.

        Raises:
            ApiError: The authenticated user can't access the custom logos. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_custom_logos_alt1(
            page=page, per_page=per_page, sizes=sizes, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EmbedPresetsCustomLogosWithRawResponse:
        return self._with_raw_response


class AsyncEmbedPresetsCustomLogos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmbedPresetsCustomLogosWithRawResponse(client, server, auth)

    async def create_custom_logo(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds a custom logo representing the authenticated user for display in the embedded player. Be
        sure to use this method in the context of the multi-step upload procedure described in our `Working with
        Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail>`__ guide. This
        method represents Step 2 of the procedure.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was added.

        Raises:
            ApiError: The authenticated user can't add the custom logo. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.create_custom_logo(user_id, request_options=request_options)).unwrap()

    async def create_custom_logo_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method adds a custom logo representing the authenticated user for display in the embedded player. Be
        sure to use this method in the context of the multi-step upload procedure described in our `Working with
        Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail>`__ guide. This
        method represents Step 2 of the procedure.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was added.

        Raises:
            ApiError: The authenticated user can't add the custom logo. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.create_custom_logo_alt1(request_options=request_options)).unwrap()

    async def delete_custom_logo(
        self, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was deleted.

        Raises:
            ApiError: The authenticated user can't access the custom logo. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_custom_logo(logo_id, user_id, request_options=request_options)
        ).unwrap()

    async def delete_custom_logo_alt1(
        self, logo_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was deleted.

        Raises:
            ApiError: The authenticated user can't access the custom logo. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_custom_logo_alt1(logo_id, request_options=request_options)
        ).unwrap()

    async def get_custom_logo(
        self, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was returned.

        Raises:
            ApiError: The authenticated user can't access the custom logo. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_custom_logo(logo_id, user_id, request_options=request_options)
        ).unwrap()

    async def get_custom_logo_alt1(
        self, logo_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logo was returned.

        Raises:
            ApiError: The authenticated user can't access the custom logo. ``error`` is ``LegacyError | RawError``."""
        return (await self._with_raw_response.get_custom_logo_alt1(logo_id, request_options=request_options)).unwrap()

    async def get_custom_logos(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sizes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every custom logo that belongs to the authenticated user or team owner.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logos were returned.

        Raises:
            ApiError: The authenticated user can't access the custom logos. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_custom_logos(
                user_id, page=page, per_page=per_page, sizes=sizes, request_options=request_options
            )
        ).unwrap()

    async def get_custom_logos_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sizes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every custom logo that belongs to the authenticated user or team owner.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The custom logos were returned.

        Raises:
            ApiError: The authenticated user can't access the custom logos. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_custom_logos_alt1(
                page=page, per_page=per_page, sizes=sizes, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEmbedPresetsCustomLogosWithRawResponse:
        return self._with_raw_response


class EmbedPresetsCustomLogosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_custom_logo(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateCustomLogoErrorBody]:
        """This method adds a custom logo representing the authenticated user for display in the embedded player. Be
        sure to use this method in the context of the multi-step upload procedure described in our `Working with
        Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail>`__ guide. This
        method represents Step 2 of the procedure.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/customlogos"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_custom_logo_error_mapper,
            request_options=request_options,
        )

    def create_custom_logo_alt1(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateCustomLogoAlt1ErrorBody]:
        """This method adds a custom logo representing the authenticated user for display in the embedded player. Be
        sure to use this method in the context of the multi-step upload procedure described in our `Working with
        Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail>`__ guide. This
        method represents Step 2 of the procedure.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/customlogos"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_custom_logo_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_custom_logo(
        self, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCustomLogoErrorBody]:
        """This method deletes the specified custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/customlogos/{logo_id}"),
            path_params=[param[float]("logo_id", logo_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_custom_logo_error_mapper,
            request_options=request_options,
        )

    def delete_custom_logo_alt1(
        self, logo_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCustomLogoAlt1ErrorBody]:
        """This method deletes the specified custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/customlogos/{logo_id}"),
            path_params=[param[float]("logo_id", logo_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_custom_logo_alt1_error_mapper,
            request_options=request_options,
        )

    def get_custom_logo(
        self, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetCustomLogoErrorBody]:
        """This method returns a single custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/customlogos/{logo_id}"),
            path_params=[param[float]("logo_id", logo_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_custom_logo_error_mapper,
            request_options=request_options,
        )

    def get_custom_logo_alt1(
        self, logo_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetCustomLogoAlt1ErrorBody]:
        """This method returns a single custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/customlogos/{logo_id}"),
            path_params=[param[float]("logo_id", logo_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_custom_logo_alt1_error_mapper,
            request_options=request_options,
        )

    def get_custom_logos(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sizes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetCustomLogosErrorBody]:
        """This method returns every custom logo that belongs to the authenticated user or team owner.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/customlogos"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("sizes", sizes),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_custom_logos_error_mapper,
            request_options=request_options,
        )

    def get_custom_logos_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sizes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetCustomLogosAlt1ErrorBody]:
        """This method returns every custom logo that belongs to the authenticated user or team owner.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/customlogos"),
            query_params=[
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("sizes", sizes),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_custom_logos_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncEmbedPresetsCustomLogosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_custom_logo(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateCustomLogoErrorBody]:
        """This method adds a custom logo representing the authenticated user for display in the embedded player. Be
        sure to use this method in the context of the multi-step upload procedure described in our `Working with
        Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail>`__ guide. This
        method represents Step 2 of the procedure.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/customlogos"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_custom_logo_error_mapper,
            request_options=request_options,
        )

    async def create_custom_logo_alt1(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateCustomLogoAlt1ErrorBody]:
        """This method adds a custom logo representing the authenticated user for display in the embedded player. Be
        sure to use this method in the context of the multi-step upload procedure described in our `Working with
        Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail>`__ guide. This
        method represents Step 2 of the procedure.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/customlogos"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_custom_logo_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_custom_logo(
        self, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCustomLogoErrorBody]:
        """This method deletes the specified custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/customlogos/{logo_id}"),
            path_params=[param[float]("logo_id", logo_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_custom_logo_error_mapper,
            request_options=request_options,
        )

    async def delete_custom_logo_alt1(
        self, logo_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCustomLogoAlt1ErrorBody]:
        """This method deletes the specified custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/customlogos/{logo_id}"),
            path_params=[param[float]("logo_id", logo_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_custom_logo_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_custom_logo(
        self, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetCustomLogoErrorBody]:
        """This method returns a single custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/customlogos/{logo_id}"),
            path_params=[param[float]("logo_id", logo_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_custom_logo_error_mapper,
            request_options=request_options,
        )

    async def get_custom_logo_alt1(
        self, logo_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetCustomLogoAlt1ErrorBody]:
        """This method returns a single custom logo belonging to the authenticated user.

        Args:
            logo_id: The ID of the custom logo.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/customlogos/{logo_id}"),
            path_params=[param[float]("logo_id", logo_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_custom_logo_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_custom_logos(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sizes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetCustomLogosErrorBody]:
        """This method returns every custom logo that belongs to the authenticated user or team owner.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/customlogos"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("sizes", sizes),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_custom_logos_error_mapper,
            request_options=request_options,
        )

    async def get_custom_logos_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        sizes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, GetCustomLogosAlt1ErrorBody]:
        """This method returns every custom logo that belongs to the authenticated user or team owner.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sizes: The pixel dimensions of the image in ``{width}x{height}`` format. For more information, see our
                `Using Common Formats and Parameters
                <https://developer.vimeo.com/api/common-formats#using-the-sizes-parameter>`__ guide.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/customlogos"),
            query_params=[
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("sizes", sizes),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=get_custom_logos_alt1_error_mapper,
            request_options=request_options,
        )
