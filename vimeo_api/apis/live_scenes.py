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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.attach_graphic_item_to_scene_error import (
    AttachGraphicItemToSceneErrorBody,
    attach_graphic_item_to_scene_error_mapper,
)
from ..errors.create_composer_scene_error import CreateComposerSceneErrorBody, create_composer_scene_error_mapper
from ..errors.get_composer_scenes_error import GetComposerScenesErrorBody, get_composer_scenes_error_mapper
from ..errors.reset_composer_scenes_error import ResetComposerScenesErrorBody, reset_composer_scenes_error_mapper
from ..errors.update_composer_scene_error import UpdateComposerSceneErrorBody, update_composer_scene_error_mapper
from ..models.composer_scenes import ComposerScenes
from ..models.composer_scenes_connection import ComposerScenesConnection
from ..models.live_events_composer_scenes_graphics_request import (
    LiveEventsComposerScenesGraphicsRequest,
    LiveEventsComposerScenesGraphicsRequestDict,
)
from ..models.live_events_composer_scenes_request import (
    LiveEventsComposerScenesRequest,
    LiveEventsComposerScenesRequestDict,
)
from ..server.server import Server


class LiveScenes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveScenesWithRawResponse(client, server, auth)

    def attach_graphic_item_to_scene(
        self,
        live_event_id: float,
        scene_id: str,
        body: LiveEventsComposerScenesGraphicsRequest | LiveEventsComposerScenesGraphicsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComposerScenes:
        """This method attaches a graphic item to the specified scene.

        Args:
            live_event_id: The ID of the event.
            scene_id: The ID of the scene.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scene was returned.

        Raises:
            ApiError: Error code 3981: The provided graphic item type isn't supported yet. * Error code 3200: The
                authenticated user can't access the event. * Error code 8000: The user credentials are invalid.
                ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.attach_graphic_item_to_scene(
                live_event_id, scene_id, body, request_options=request_options
            ),
        )

    def create_composer_scene(
        self,
        live_event_id: float,
        *,
        body: LiveEventsComposerScenesRequest | LiveEventsComposerScenesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComposerScenes:
        """The method creates a new scene for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scene was created.

        Raises:
            ApiError: * Error code 3980: The Composer Scenes API isn't supported in the context of venues. * Error code
                3989: Scenes already exist for this event. * Error code 3200: The authenticated user can't access the
                event. * Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.create_composer_scene(live_event_id, body=body, request_options=request_options)
        )

    def get_composer_scenes(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComposerScenesConnection:
        """The method returns every scene belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scenes were returned.

        Raises:
            ApiError: Error code 3980: The Composer Scenes API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.get_composer_scenes(live_event_id, request_options=request_options))

    def reset_composer_scenes(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ComposerScenes]:
        """The method resets the scenes that belong to the specified event by deleting every existing scene and then
        recreating the default scene.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scenes were reset.

        Raises:
            ApiError: Error code 3980: The Composer Scenes API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.reset_composer_scenes(live_event_id, request_options=request_options))

    def update_composer_scene(
        self, live_event_id: float, scene_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComposerScenes:
        """The method updates a scene belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            scene_id: The ID of the scene.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scene was returned.

        Raises:
            ApiError: Error code 3980: The Composer Scenes API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.update_composer_scene(live_event_id, scene_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> LiveScenesWithRawResponse:
        return self._with_raw_response


class AsyncLiveScenes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveScenesWithRawResponse(client, server, auth)

    async def attach_graphic_item_to_scene(
        self,
        live_event_id: float,
        scene_id: str,
        body: LiveEventsComposerScenesGraphicsRequest | LiveEventsComposerScenesGraphicsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComposerScenes:
        """This method attaches a graphic item to the specified scene.

        Args:
            live_event_id: The ID of the event.
            scene_id: The ID of the scene.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scene was returned.

        Raises:
            ApiError: Error code 3981: The provided graphic item type isn't supported yet. * Error code 3200: The
                authenticated user can't access the event. * Error code 8000: The user credentials are invalid.
                ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.attach_graphic_item_to_scene(
                live_event_id, scene_id, body, request_options=request_options
            ),
        )

    async def create_composer_scene(
        self,
        live_event_id: float,
        *,
        body: LiveEventsComposerScenesRequest | LiveEventsComposerScenesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComposerScenes:
        """The method creates a new scene for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scene was created.

        Raises:
            ApiError: * Error code 3980: The Composer Scenes API isn't supported in the context of venues. * Error code
                3989: Scenes already exist for this event. * Error code 3200: The authenticated user can't access the
                event. * Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.create_composer_scene(
                live_event_id, body=body, request_options=request_options
            ),
        )

    async def get_composer_scenes(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComposerScenesConnection:
        """The method returns every scene belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scenes were returned.

        Raises:
            ApiError: Error code 3980: The Composer Scenes API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.get_composer_scenes(live_event_id, request_options=request_options))

    async def reset_composer_scenes(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ComposerScenes]:
        """The method resets the scenes that belong to the specified event by deleting every existing scene and then
        recreating the default scene.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scenes were reset.

        Raises:
            ApiError: Error code 3980: The Composer Scenes API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.reset_composer_scenes(live_event_id, request_options=request_options)
        )

    async def update_composer_scene(
        self, live_event_id: float, scene_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComposerScenes:
        """The method updates a scene belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            scene_id: The ID of the scene.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The scene was returned.

        Raises:
            ApiError: Error code 3980: The Composer Scenes API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.update_composer_scene(
                live_event_id, scene_id, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncLiveScenesWithRawResponse:
        return self._with_raw_response


class LiveScenesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def attach_graphic_item_to_scene(
        self,
        live_event_id: float,
        scene_id: str,
        body: LiveEventsComposerScenesGraphicsRequest | LiveEventsComposerScenesGraphicsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComposerScenes, AttachGraphicItemToSceneErrorBody]:
        """This method attaches a graphic item to the specified scene.

        Args:
            live_event_id: The ID of the event.
            scene_id: The ID of the scene.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes/{scene_id}/graphics"),
            path_params=[param[float]("live_event_id", live_event_id), param[str]("scene_id", scene_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsComposerScenesGraphicsRequest | LiveEventsComposerScenesGraphicsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ComposerScenes],
            error_mapper=attach_graphic_item_to_scene_error_mapper,
            request_options=request_options,
        )

    def create_composer_scene(
        self,
        live_event_id: float,
        *,
        body: LiveEventsComposerScenesRequest | LiveEventsComposerScenesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComposerScenes, CreateComposerSceneErrorBody]:
        """The method creates a new scene for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsComposerScenesRequest | LiveEventsComposerScenesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ComposerScenes],
            error_mapper=create_composer_scene_error_mapper,
            request_options=request_options,
        )

    def get_composer_scenes(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComposerScenesConnection, GetComposerScenesErrorBody]:
        """The method returns every scene belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ComposerScenesConnection],
            error_mapper=get_composer_scenes_error_mapper,
            request_options=request_options,
        )

    def reset_composer_scenes(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ComposerScenes], ResetComposerScenesErrorBody]:
        """The method resets the scenes that belong to the specified event by deleting every existing scene and then
        recreating the default scene.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[ComposerScenes]],
            error_mapper=reset_composer_scenes_error_mapper,
            request_options=request_options,
        )

    def update_composer_scene(
        self, live_event_id: float, scene_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComposerScenes, UpdateComposerSceneErrorBody]:
        """The method updates a scene belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            scene_id: The ID of the scene.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes/{scene_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[str]("scene_id", scene_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ComposerScenes],
            error_mapper=update_composer_scene_error_mapper,
            request_options=request_options,
        )


class AsyncLiveScenesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def attach_graphic_item_to_scene(
        self,
        live_event_id: float,
        scene_id: str,
        body: LiveEventsComposerScenesGraphicsRequest | LiveEventsComposerScenesGraphicsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComposerScenes, AttachGraphicItemToSceneErrorBody]:
        """This method attaches a graphic item to the specified scene.

        Args:
            live_event_id: The ID of the event.
            scene_id: The ID of the scene.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes/{scene_id}/graphics"),
            path_params=[param[float]("live_event_id", live_event_id), param[str]("scene_id", scene_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsComposerScenesGraphicsRequest | LiveEventsComposerScenesGraphicsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[ComposerScenes],
            error_mapper=attach_graphic_item_to_scene_error_mapper,
            request_options=request_options,
        )

    async def create_composer_scene(
        self,
        live_event_id: float,
        *,
        body: LiveEventsComposerScenesRequest | LiveEventsComposerScenesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComposerScenes, CreateComposerSceneErrorBody]:
        """The method creates a new scene for the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsComposerScenesRequest | LiveEventsComposerScenesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[ComposerScenes],
            error_mapper=create_composer_scene_error_mapper,
            request_options=request_options,
        )

    async def get_composer_scenes(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComposerScenesConnection, GetComposerScenesErrorBody]:
        """The method returns every scene belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[ComposerScenesConnection],
            error_mapper=get_composer_scenes_error_mapper,
            request_options=request_options,
        )

    async def reset_composer_scenes(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ComposerScenes], ResetComposerScenesErrorBody]:
        """The method resets the scenes that belong to the specified event by deleting every existing scene and then
        recreating the default scene.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[list[ComposerScenes]],
            error_mapper=reset_composer_scenes_error_mapper,
            request_options=request_options,
        )

    async def update_composer_scene(
        self, live_event_id: float, scene_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComposerScenes, UpdateComposerSceneErrorBody]:
        """The method updates a scene belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            scene_id: The ID of the scene.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}/composer/scenes/{scene_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[str]("scene_id", scene_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[ComposerScenes],
            error_mapper=update_composer_scene_error_mapper,
            request_options=request_options,
        )
