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
from ..errors.delete_video_embed_preset_error import (
    DeleteVideoEmbedPresetErrorBody,
    delete_video_embed_preset_error_mapper,
)
from ..errors.get_video_embed_preset_error import GetVideoEmbedPresetErrorBody, get_video_embed_preset_error_mapper
from ..models.video_connection import VideoConnection
from ..server.server import Server


class EmbedPresetsVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmbedPresetsVideosWithRawResponse(client, server, auth)

    def add_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds an embed preset to the specified video. The authenticated user must either be the owner of
        the video or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was added to the video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.add_video_embed_preset(
            preset_id, video_id, request_options=request_options
        ).unwrap()

    def delete_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified embed preset from a video. The authenticated user must either be the owner
        of the video or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was removed.

        Raises:
            ApiError: No such video or embed preset exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_video_embed_preset(
            preset_id, video_id, request_options=request_options
        ).unwrap()

    def get_embed_preset_videos(
        self,
        preset_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video to which the specified embed preset has been added. The authenticated user
        must be the owner of the videos.

        Args:
            preset_id: The ID of the embed preset.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_embed_preset_videos(
            preset_id, user_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_embed_preset_videos_alt1(
        self,
        preset_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video to which the specified embed preset has been added. The authenticated user
        must be the owner of the videos.

        Args:
            preset_id: The ID of the embed preset.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_embed_preset_videos_alt1(
            preset_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether a video has the specified embed preset.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset has been added to the video.

        Raises:
            ApiError: No such video or embed preset exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_video_embed_preset(
            preset_id, video_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EmbedPresetsVideosWithRawResponse:
        return self._with_raw_response


class AsyncEmbedPresetsVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmbedPresetsVideosWithRawResponse(client, server, auth)

    async def add_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds an embed preset to the specified video. The authenticated user must either be the owner of
        the video or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was added to the video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_video_embed_preset(preset_id, video_id, request_options=request_options)
        ).unwrap()

    async def delete_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes the specified embed preset from a video. The authenticated user must either be the owner
        of the video or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset was removed.

        Raises:
            ApiError: No such video or embed preset exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_video_embed_preset(
                preset_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_embed_preset_videos(
        self,
        preset_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video to which the specified embed preset has been added. The authenticated user
        must be the owner of the videos.

        Args:
            preset_id: The ID of the embed preset.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_embed_preset_videos(
                preset_id, user_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_embed_preset_videos_alt1(
        self,
        preset_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video to which the specified embed preset has been added. The authenticated user
        must be the owner of the videos.

        Args:
            preset_id: The ID of the embed preset.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_embed_preset_videos_alt1(
                preset_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether a video has the specified embed preset.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The embed preset has been added to the video.

        Raises:
            ApiError: No such video or embed preset exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_video_embed_preset(preset_id, video_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEmbedPresetsVideosWithRawResponse:
        return self._with_raw_response


class EmbedPresetsVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method adds an embed preset to the specified video. The authenticated user must either be the owner of
        the video or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoEmbedPresetErrorBody]:
        """This method removes the specified embed preset from a video. The authenticated user must either be the owner
        of the video or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_embed_preset_error_mapper,
            request_options=request_options,
        )

    def get_embed_preset_videos(
        self,
        preset_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video to which the specified embed preset has been added. The authenticated user
        must be the owner of the videos.

        Args:
            preset_id: The ID of the embed preset.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/presets/{preset_id}/videos"),
            path_params=[param[float]("preset_id", preset_id), param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_embed_preset_videos_alt1(
        self,
        preset_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video to which the specified embed preset has been added. The authenticated user
        must be the owner of the videos.

        Args:
            preset_id: The ID of the embed preset.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/presets/{preset_id}/videos"),
            path_params=[param[float]("preset_id", preset_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetVideoEmbedPresetErrorBody]:
        """This method determines whether a video has the specified embed preset.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_video_embed_preset_error_mapper,
            request_options=request_options,
        )


class AsyncEmbedPresetsVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method adds an embed preset to the specified video. The authenticated user must either be the owner of
        the video or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoEmbedPresetErrorBody]:
        """This method removes the specified embed preset from a video. The authenticated user must either be the owner
        of the video or a team user with the contributor or admin role.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_embed_preset_error_mapper,
            request_options=request_options,
        )

    async def get_embed_preset_videos(
        self,
        preset_id: float,
        user_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video to which the specified embed preset has been added. The authenticated user
        must be the owner of the videos.

        Args:
            preset_id: The ID of the embed preset.
            user_id: The ID of the user.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/presets/{preset_id}/videos"),
            path_params=[param[float]("preset_id", preset_id), param[float]("user_id", user_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_embed_preset_videos_alt1(
        self,
        preset_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video to which the specified embed preset has been added. The authenticated user
        must be the owner of the videos.

        Args:
            preset_id: The ID of the embed preset.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/presets/{preset_id}/videos"),
            path_params=[param[float]("preset_id", preset_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_video_embed_preset(
        self, preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetVideoEmbedPresetErrorBody]:
        """This method determines whether a video has the specified embed preset.

        Args:
            preset_id: The ID of the embed preset.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/presets/{preset_id}"),
            path_params=[param[float]("preset_id", preset_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_video_embed_preset_error_mapper,
            request_options=request_options,
        )
