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
    json_decoder,
    param,
)
from ..errors.create_video_custom_logo_error import (
    CreateVideoCustomLogoErrorBody,
    create_video_custom_logo_error_mapper,
)
from ..errors.get_video_custom_logo_error import GetVideoCustomLogoErrorBody, get_video_custom_logo_error_mapper
from ..models.picture import Picture
from ..server.server import Server


class EmbedPresetsTimelineEvents:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmbedPresetsTimelineEventsWithRawResponse(client, server, auth)

    def create_video_custom_logo(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds a timeline event thumbnail to the specified video. The authenticated user must be the owner
        of the video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The timeline event thumbnail was added.

        Raises:
            ApiError: The authenticated user can't add a timeline event thumbnail to the video. No such video exists.
                ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.create_video_custom_logo(video_id, request_options=request_options).unwrap()

    def get_video_custom_logo(
        self, thumbnail_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single timeline event thumbnail that belongs to the specified video.

        Args:
            thumbnail_id: The ID of the timeline event thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The timeline event thumbnail was returned.

        Raises:
            ApiError: The authenticated user can't access the timeline event thumbnail. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.get_video_custom_logo(
            thumbnail_id, video_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EmbedPresetsTimelineEventsWithRawResponse:
        return self._with_raw_response


class AsyncEmbedPresetsTimelineEvents:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmbedPresetsTimelineEventsWithRawResponse(client, server, auth)

    async def create_video_custom_logo(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method adds a timeline event thumbnail to the specified video. The authenticated user must be the owner
        of the video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The timeline event thumbnail was added.

        Raises:
            ApiError: The authenticated user can't add a timeline event thumbnail to the video. No such video exists.
                ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.create_video_custom_logo(video_id, request_options=request_options)
        ).unwrap()

    async def get_video_custom_logo(
        self, thumbnail_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Picture:
        """This method returns a single timeline event thumbnail that belongs to the specified video.

        Args:
            thumbnail_id: The ID of the timeline event thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The timeline event thumbnail was returned.

        Raises:
            ApiError: The authenticated user can't access the timeline event thumbnail. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.get_video_custom_logo(thumbnail_id, video_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEmbedPresetsTimelineEventsWithRawResponse:
        return self._with_raw_response


class EmbedPresetsTimelineEventsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_video_custom_logo(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateVideoCustomLogoErrorBody]:
        """This method adds a timeline event thumbnail to the specified video. The authenticated user must be the owner
        of the video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/timelinethumbnails"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_video_custom_logo_error_mapper,
            request_options=request_options,
        )

    def get_video_custom_logo(
        self, thumbnail_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetVideoCustomLogoErrorBody]:
        """This method returns a single timeline event thumbnail that belongs to the specified video.

        Args:
            thumbnail_id: The ID of the timeline event thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/timelinethumbnails/{thumbnail_id}"),
            path_params=[param[float]("thumbnail_id", thumbnail_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_video_custom_logo_error_mapper,
            request_options=request_options,
        )


class AsyncEmbedPresetsTimelineEventsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_video_custom_logo(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, CreateVideoCustomLogoErrorBody]:
        """This method adds a timeline event thumbnail to the specified video. The authenticated user must be the owner
        of the video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/timelinethumbnails"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=create_video_custom_logo_error_mapper,
            request_options=request_options,
        )

    async def get_video_custom_logo(
        self, thumbnail_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Picture, GetVideoCustomLogoErrorBody]:
        """This method returns a single timeline event thumbnail that belongs to the specified video.

        Args:
            thumbnail_id: The ID of the timeline event thumbnail.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/timelinethumbnails/{thumbnail_id}"),
            path_params=[param[float]("thumbnail_id", thumbnail_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Picture],
            error_mapper=get_video_custom_logo_error_mapper,
            request_options=request_options,
        )
