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
from ..errors.delete_embed_preset_alt1_error import (
    DeleteEmbedPresetAlt1ErrorBody,
    delete_embed_preset_alt1_error_mapper,
)
from ..errors.delete_embed_preset_error import DeleteEmbedPresetErrorBody, delete_embed_preset_error_mapper
from ..errors.edit_embed_preset_alt1_error import EditEmbedPresetAlt1ErrorBody, edit_embed_preset_alt1_error_mapper
from ..errors.edit_embed_preset_error import EditEmbedPresetErrorBody, edit_embed_preset_error_mapper
from ..models.me_presets_request import MePresetsRequest, MePresetsRequestDict
from ..models.me_presets_request1 import MePresetsRequest1, MePresetsRequest1Dict
from ..models.preset import Preset
from ..models.preset_connection import PresetConnection
from ..models.users_presets_request import UsersPresetsRequest, UsersPresetsRequestDict
from ..models.users_presets_request1 import UsersPresetsRequest1, UsersPresetsRequest1Dict
from ..server.server import Server


class EmbedPresetsEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmbedPresetsEssentialsWithRawResponse(client, server, auth)

    def create_embed_presets(
        self,
        user_id: float,
        *,
        body: UsersPresetsRequest | UsersPresetsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Preset:
        """This method creates an embed preset.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_embed_presets(
            user_id, body=body, request_options=request_options
        ).unwrap()

    def create_embed_presets_alt1(
        self,
        *,
        body: MePresetsRequest | MePresetsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Preset:
        """This method creates an embed preset.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_embed_presets_alt1(body=body, request_options=request_options).unwrap()

    def delete_embed_preset(
        self, preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the embed preset.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was deleted.

        Raises:
            ApiError: The authenticated user can't delete the embed preset. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_embed_preset(preset_id, user_id, request_options=request_options).unwrap()

    def delete_embed_preset_alt1(
        self, preset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the embed preset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was deleted.

        Raises:
            ApiError: The authenticated user can't delete the embed preset. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_embed_preset_alt1(preset_id, request_options=request_options).unwrap()

    def edit_embed_preset(
        self,
        preset_id: float,
        user_id: float,
        *,
        body: UsersPresetsRequest1 | UsersPresetsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Preset:
        """This method edits the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was edited.

        Raises:
            ApiError: The outro type is invalid. * No such embed preset exists. * The authenticated user can't edit the
                embed preset. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.edit_embed_preset(
            preset_id, user_id, body=body, request_options=request_options
        ).unwrap()

    def edit_embed_preset_alt1(
        self,
        preset_id: float,
        *,
        body: MePresetsRequest1 | MePresetsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Preset:
        """This method edits the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was edited.

        Raises:
            ApiError: The outro type is invalid. * No such embed preset exists. * The authenticated user can't edit the
                embed preset. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.edit_embed_preset_alt1(
            preset_id, body=body, request_options=request_options
        ).unwrap()

    def get_embed_preset(
        self, preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Preset:
        """This method returns a single embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_embed_preset(preset_id, user_id, request_options=request_options).unwrap()

    def get_embed_preset_alt1(self, preset_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Preset:
        """This method returns a single embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_embed_preset_alt1(preset_id, request_options=request_options).unwrap()

    def get_embed_presets(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PresetConnection:
        """This method returns every embed preset that belongs to the authenticated user.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed presets were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_embed_presets(
            user_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_embed_presets_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PresetConnection:
        """This method returns every embed preset that belongs to the authenticated user.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed presets were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_embed_presets_alt1(
            page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EmbedPresetsEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncEmbedPresetsEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmbedPresetsEssentialsWithRawResponse(client, server, auth)

    async def create_embed_presets(
        self,
        user_id: float,
        *,
        body: UsersPresetsRequest | UsersPresetsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Preset:
        """This method creates an embed preset.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_embed_presets(user_id, body=body, request_options=request_options)
        ).unwrap()

    async def create_embed_presets_alt1(
        self,
        *,
        body: MePresetsRequest | MePresetsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Preset:
        """This method creates an embed preset.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_embed_presets_alt1(body=body, request_options=request_options)
        ).unwrap()

    async def delete_embed_preset(
        self, preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the embed preset.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was deleted.

        Raises:
            ApiError: The authenticated user can't delete the embed preset. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_embed_preset(preset_id, user_id, request_options=request_options)
        ).unwrap()

    async def delete_embed_preset_alt1(
        self, preset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the embed preset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was deleted.

        Raises:
            ApiError: The authenticated user can't delete the embed preset. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_embed_preset_alt1(preset_id, request_options=request_options)
        ).unwrap()

    async def edit_embed_preset(
        self,
        preset_id: float,
        user_id: float,
        *,
        body: UsersPresetsRequest1 | UsersPresetsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Preset:
        """This method edits the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was edited.

        Raises:
            ApiError: The outro type is invalid. * No such embed preset exists. * The authenticated user can't edit the
                embed preset. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_embed_preset(
                preset_id, user_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def edit_embed_preset_alt1(
        self,
        preset_id: float,
        *,
        body: MePresetsRequest1 | MePresetsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Preset:
        """This method edits the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was edited.

        Raises:
            ApiError: The outro type is invalid. * No such embed preset exists. * The authenticated user can't edit the
                embed preset. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_embed_preset_alt1(preset_id, body=body, request_options=request_options)
        ).unwrap()

    async def get_embed_preset(
        self, preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Preset:
        """This method returns a single embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_embed_preset(preset_id, user_id, request_options=request_options)
        ).unwrap()

    async def get_embed_preset_alt1(
        self, preset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Preset:
        """This method returns a single embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_embed_preset_alt1(preset_id, request_options=request_options)
        ).unwrap()

    async def get_embed_presets(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PresetConnection:
        """This method returns every embed preset that belongs to the authenticated user.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed presets were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_embed_presets(
                user_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_embed_presets_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PresetConnection:
        """This method returns every embed preset that belongs to the authenticated user.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed presets were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_embed_presets_alt1(
                page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEmbedPresetsEssentialsWithRawResponse:
        return self._with_raw_response


class EmbedPresetsEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_embed_presets(
        self,
        user_id: float,
        *,
        body: UsersPresetsRequest | UsersPresetsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Preset, RawError]:
        """This method creates an embed preset.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/presets"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPresetsRequest | UsersPresetsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_embed_presets_alt1(
        self,
        *,
        body: MePresetsRequest | MePresetsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Preset, RawError]:
        """This method creates an embed preset.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/presets"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MePresetsRequest | MePresetsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_embed_preset(
        self, preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteEmbedPresetErrorBody]:
        """This method deletes the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the embed preset.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_embed_preset_error_mapper,
            request_options=request_options,
        )

    def delete_embed_preset_alt1(
        self, preset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteEmbedPresetAlt1ErrorBody]:
        """This method deletes the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the embed preset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_embed_preset_alt1_error_mapper,
            request_options=request_options,
        )

    def edit_embed_preset(
        self,
        preset_id: float,
        user_id: float,
        *,
        body: UsersPresetsRequest1 | UsersPresetsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Preset, EditEmbedPresetErrorBody]:
        """This method edits the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPresetsRequest1 | UsersPresetsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=edit_embed_preset_error_mapper,
            request_options=request_options,
        )

    def edit_embed_preset_alt1(
        self,
        preset_id: float,
        *,
        body: MePresetsRequest1 | MePresetsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Preset, EditEmbedPresetAlt1ErrorBody]:
        """This method edits the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MePresetsRequest1 | MePresetsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=edit_embed_preset_alt1_error_mapper,
            request_options=request_options,
        )

    def get_embed_preset(
        self, preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Preset, RawError]:
        """This method returns a single embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_embed_preset_alt1(
        self, preset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Preset, RawError]:
        """This method returns a single embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_embed_presets(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PresetConnection, RawError]:
        """This method returns every embed preset that belongs to the authenticated user.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/presets"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PresetConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_embed_presets_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PresetConnection, RawError]:
        """This method returns every embed preset that belongs to the authenticated user.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/presets"),
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PresetConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEmbedPresetsEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_embed_presets(
        self,
        user_id: float,
        *,
        body: UsersPresetsRequest | UsersPresetsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Preset, RawError]:
        """This method creates an embed preset.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/presets"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPresetsRequest | UsersPresetsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_embed_presets_alt1(
        self,
        *,
        body: MePresetsRequest | MePresetsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Preset, RawError]:
        """This method creates an embed preset.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/presets"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MePresetsRequest | MePresetsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_embed_preset(
        self, preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteEmbedPresetErrorBody]:
        """This method deletes the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the embed preset.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_embed_preset_error_mapper,
            request_options=request_options,
        )

    async def delete_embed_preset_alt1(
        self, preset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteEmbedPresetAlt1ErrorBody]:
        """This method deletes the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the embed preset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_embed_preset_alt1_error_mapper,
            request_options=request_options,
        )

    async def edit_embed_preset(
        self,
        preset_id: float,
        user_id: float,
        *,
        body: UsersPresetsRequest1 | UsersPresetsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Preset, EditEmbedPresetErrorBody]:
        """This method edits the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPresetsRequest1 | UsersPresetsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=edit_embed_preset_error_mapper,
            request_options=request_options,
        )

    async def edit_embed_preset_alt1(
        self,
        preset_id: float,
        *,
        body: MePresetsRequest1 | MePresetsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Preset, EditEmbedPresetAlt1ErrorBody]:
        """This method edits the specified embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MePresetsRequest1 | MePresetsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=edit_embed_preset_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_embed_preset(
        self, preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Preset, RawError]:
        """This method returns a single embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_embed_preset_alt1(
        self, preset_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Preset, RawError]:
        """This method returns a single embed preset. The authenticated user must be the owner of the preset.

        Args:
            preset_id: The ID of the preset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Preset],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_embed_presets(
        self,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PresetConnection, RawError]:
        """This method returns every embed preset that belongs to the authenticated user.

        Args:
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/presets"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PresetConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_embed_presets_alt1(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PresetConnection, RawError]:
        """This method returns every embed preset that belongs to the authenticated user.

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/presets"),
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[PresetConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
