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
    param,
)
from ..errors.delete_folder_embed_preset_error import (
    DeleteFolderEmbedPresetErrorBody,
    delete_folder_embed_preset_error_mapper,
)
from ..server.server import Server


class EmbedPresetsFolders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmbedPresetsFoldersWithRawResponse(client, server, auth)

    def delete_folder_embed_preset(
        self,
        preset_id: float,
        project_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes the specified embed preset from a folder. The authenticated user must be either the owner
        of the folder or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            project_id: The ID of the folder.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was removed.

        Raises:
            ApiError: No such folder or embed preset exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_folder_embed_preset(
            preset_id, project_id, user_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EmbedPresetsFoldersWithRawResponse:
        return self._with_raw_response


class AsyncEmbedPresetsFolders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmbedPresetsFoldersWithRawResponse(client, server, auth)

    async def delete_folder_embed_preset(
        self,
        preset_id: float,
        project_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes the specified embed preset from a folder. The authenticated user must be either the owner
        of the folder or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            project_id: The ID of the folder.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was removed.

        Raises:
            ApiError: No such folder or embed preset exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_folder_embed_preset(
                preset_id, project_id, user_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEmbedPresetsFoldersWithRawResponse:
        return self._with_raw_response


class EmbedPresetsFoldersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_folder_embed_preset(
        self,
        preset_id: float,
        project_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteFolderEmbedPresetErrorBody]:
        """This method removes the specified embed preset from a folder. The authenticated user must be either the owner
        of the folder or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            project_id: The ID of the folder.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/presets/{preset_id}"),
            path_params=[
                param[float]("preset_id", preset_id),
                param[float]("project_id", project_id),
                param[float]("user_id", user_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_folder_embed_preset_error_mapper,
            request_options=request_options,
        )


class AsyncEmbedPresetsFoldersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_folder_embed_preset(
        self,
        preset_id: float,
        project_id: float,
        user_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteFolderEmbedPresetErrorBody]:
        """This method removes the specified embed preset from a folder. The authenticated user must be either the owner
        of the folder or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            project_id: The ID of the folder.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/projects/{project_id}/presets/{preset_id}"),
            path_params=[
                param[float]("preset_id", preset_id),
                param[float]("project_id", project_id),
                param[float]("user_id", user_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_folder_embed_preset_error_mapper,
            request_options=request_options,
        )
