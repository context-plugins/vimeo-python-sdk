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
from ..models.me_pictures_request import MePicturesRequest, MePicturesRequestDict
from ..models.picture import Picture
from ..models.picture_connection import PictureConnection
from ..models.users_pictures_request import UsersPicturesRequest, UsersPicturesRequestDict
from ..server.server import Server


class UsersPictures:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersPicturesWithRawResponse(client, server, auth)

    def create_picture(self, user_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method adds a portrait image to the authenticated user's Vimeo account. Send the binary data of the
        image file to the location that you receive from the **link** field in the response. For step-by-step
        instructions, see `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail-step-3>`__.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was added.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_picture(user_id, request_options=request_options))

    def create_picture_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method adds a portrait image to the authenticated user's Vimeo account. Send the binary data of the
        image file to the location that you receive from the **link** field in the response. For step-by-step
        instructions, see `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail-step-3>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was added.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_picture_alt1(request_options=request_options))

    def delete_picture(
        self, portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified portrait image from the authenticated user's Vimeo account.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was removed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.delete_picture(portraitset_id, user_id, request_options=request_options))

    def delete_picture_alt1(
        self, portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified portrait image from the authenticated user's Vimeo account.

        Args:
            portraitset_id: The ID of the picture.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was removed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.delete_picture_alt1(portraitset_id, request_options=request_options))

    def edit_picture(
        self,
        portraitset_id: float,
        user_id: float,
        *,
        body: UsersPicturesRequest | UsersPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits the specified portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was edited.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.edit_picture(portraitset_id, user_id, body=body, request_options=request_options)
        )

    def edit_picture_alt1(
        self,
        portraitset_id: float,
        *,
        body: MePicturesRequest | MePicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits the specified portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was edited.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.edit_picture_alt1(portraitset_id, body=body, request_options=request_options)
        )

    def get_picture(
        self, portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_picture(portraitset_id, user_id, request_options=request_options))

    def get_picture_alt1(
        self, portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_picture_alt1(portraitset_id, request_options=request_options))

    def get_pictures(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every portrait image belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait images were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_pictures(user_id, page=page, per_page=per_page, request_options=request_options)
        )

    def get_pictures_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every portrait image belonging to the authenticated user.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait images were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_pictures_alt1(page=page, per_page=per_page, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> UsersPicturesWithRawResponse:
        return self._with_raw_response


class AsyncUsersPictures:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersPicturesWithRawResponse(client, server, auth)

    async def create_picture(self, user_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method adds a portrait image to the authenticated user's Vimeo account. Send the binary data of the
        image file to the location that you receive from the **link** field in the response. For step-by-step
        instructions, see `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail-step-3>`__.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was added.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_picture(user_id, request_options=request_options))

    async def create_picture_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> Picture:
        """This method adds a portrait image to the authenticated user's Vimeo account. Send the binary data of the
        image file to the location that you receive from the **link** field in the response. For step-by-step
        instructions, see `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail-step-3>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was added.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_picture_alt1(request_options=request_options))

    async def delete_picture(
        self, portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified portrait image from the authenticated user's Vimeo account.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was removed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_picture(portraitset_id, user_id, request_options=request_options)
        )

    async def delete_picture_alt1(
        self, portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified portrait image from the authenticated user's Vimeo account.

        Args:
            portraitset_id: The ID of the picture.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was removed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_picture_alt1(portraitset_id, request_options=request_options)
        )

    async def edit_picture(
        self,
        portraitset_id: float,
        user_id: float,
        *,
        body: UsersPicturesRequest | UsersPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits the specified portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was edited.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.edit_picture(
                portraitset_id, user_id, body=body, request_options=request_options
            ),
        )

    async def edit_picture_alt1(
        self,
        portraitset_id: float,
        *,
        body: MePicturesRequest | MePicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Picture:
        """This method edits the specified portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was edited.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.edit_picture_alt1(portraitset_id, body=body, request_options=request_options)
        )

    async def get_picture(
        self, portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_picture(portraitset_id, user_id, request_options=request_options)
        )

    async def get_picture_alt1(
        self, portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait image was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_picture_alt1(portraitset_id, request_options=request_options))

    async def get_pictures(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every portrait image belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait images were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_pictures(
                user_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def get_pictures_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PictureConnection:
        """This method returns every portrait image belonging to the authenticated user.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The portrait images were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_pictures_alt1(
                page=page, per_page=per_page, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncUsersPicturesWithRawResponse:
        return self._with_raw_response


class UsersPicturesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_picture(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method adds a portrait image to the authenticated user's Vimeo account. Send the binary data of the
        image file to the location that you receive from the **link** field in the response. For step-by-step
        instructions, see `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail-step-3>`__.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/pictures"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_picture_alt1(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method adds a portrait image to the authenticated user's Vimeo account. Send the binary data of the
        image file to the location that you receive from the **link** field in the response. For step-by-step
        instructions, see `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail-step-3>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/pictures"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_picture(
        self, portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method removes the specified portrait image from the authenticated user's Vimeo account.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_picture_alt1(
        self, portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method removes the specified portrait image from the authenticated user's Vimeo account.

        Args:
            portraitset_id: The ID of the picture.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def edit_picture(
        self,
        portraitset_id: float,
        user_id: float,
        *,
        body: UsersPicturesRequest | UsersPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method edits the specified portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPicturesRequest | UsersPicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def edit_picture_alt1(
        self,
        portraitset_id: float,
        *,
        body: MePicturesRequest | MePicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method edits the specified portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MePicturesRequest | MePicturesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_picture(
        self, portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns a single portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_picture_alt1(
        self, portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns a single portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_pictures(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, RawError]:
        """This method returns every portrait image belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/pictures"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_pictures_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, RawError]:
        """This method returns every portrait image belonging to the authenticated user.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/pictures"),
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PictureConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUsersPicturesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_picture(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method adds a portrait image to the authenticated user's Vimeo account. Send the binary data of the
        image file to the location that you receive from the **link** field in the response. For step-by-step
        instructions, see `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail-step-3>`__.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/pictures"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_picture_alt1(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method adds a portrait image to the authenticated user's Vimeo account. Send the binary data of the
        image file to the location that you receive from the **link** field in the response. For step-by-step
        instructions, see `Working with Thumbnail Uploads
        <https://developer.vimeo.com/api/upload/thumbnails#uploading-a-thumbnail-step-3>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/pictures"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_picture(
        self, portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method removes the specified portrait image from the authenticated user's Vimeo account.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_picture_alt1(
        self, portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method removes the specified portrait image from the authenticated user's Vimeo account.

        Args:
            portraitset_id: The ID of the picture.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def edit_picture(
        self,
        portraitset_id: float,
        user_id: float,
        *,
        body: UsersPicturesRequest | UsersPicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method edits the specified portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPicturesRequest | UsersPicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def edit_picture_alt1(
        self,
        portraitset_id: float,
        *,
        body: MePicturesRequest | MePicturesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Picture, RawError]:
        """This method edits the specified portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MePicturesRequest | MePicturesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_picture(
        self, portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns a single portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_picture_alt1(
        self, portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, RawError]:
        """This method returns a single portrait image belonging to the authenticated user.

        Args:
            portraitset_id: The ID of the picture.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/pictures/{portraitset_id}"),
            path_params=[param[float]("portraitset_id", portraitset_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[Picture],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_pictures(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, RawError]:
        """This method returns every portrait image belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/pictures"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PictureConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_pictures_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PictureConnection, RawError]:
        """This method returns every portrait image belonging to the authenticated user.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/pictures"),
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[PictureConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
