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
from ..errors.add_composer_video_graphic_item_error import (
    AddComposerVideoGraphicItemErrorBody,
    add_composer_video_graphic_item_error_mapper,
)
from ..errors.delete_composer_video_graphic_item_error import (
    DeleteComposerVideoGraphicItemErrorBody,
    delete_composer_video_graphic_item_error_mapper,
)
from ..errors.get_composer_video_graphic_items_error import (
    GetComposerVideoGraphicItemsErrorBody,
    get_composer_video_graphic_items_error_mapper,
)
from ..models.composer_graphics import ComposerGraphics
from ..models.composer_graphics_connection import ComposerGraphicsConnection
from ..models.live_events_composer_graphics_videos_request import (
    LiveEventsComposerGraphicsVideosRequest,
    LiveEventsComposerGraphicsVideosRequestDict,
)
from ..server.server import Server


class LiveGraphics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveGraphicsWithRawResponse(client, server, auth)

    def add_composer_video_graphic_item(
        self,
        live_event_id: float,
        body: LiveEventsComposerGraphicsVideosRequest | LiveEventsComposerGraphicsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComposerGraphics:
        """This method add a new video graphics item to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video graphic item was added.

        Raises:
            ApiError: Error code 3978: The Composer graphics API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_composer_video_graphic_item(
            live_event_id, body, request_options=request_options
        ).unwrap()

    def delete_composer_video_graphic_item(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a video graphics item belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the associated video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video graphic item was deleted.

        Raises:
            ApiError: Error code 3978: The Composer graphics API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't delete the specified video graphic item. * Error code 8000: The user
                credentials are invalid. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.delete_composer_video_graphic_item(
            live_event_id, video_id, request_options=request_options
        ).unwrap()

    def get_composer_video_graphic_items(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComposerGraphicsConnection:
        """The method returns every video graphics item belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video graphic items were returned.

        Raises:
            ApiError: Error code 3978: The Composer graphics API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_composer_video_graphic_items(
            live_event_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveGraphicsWithRawResponse:
        return self._with_raw_response


class AsyncLiveGraphics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveGraphicsWithRawResponse(client, server, auth)

    async def add_composer_video_graphic_item(
        self,
        live_event_id: float,
        body: LiveEventsComposerGraphicsVideosRequest | LiveEventsComposerGraphicsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComposerGraphics:
        """This method add a new video graphics item to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video graphic item was added.

        Raises:
            ApiError: Error code 3978: The Composer graphics API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.add_composer_video_graphic_item(
                live_event_id, body, request_options=request_options
            )
        ).unwrap()

    async def delete_composer_video_graphic_item(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a video graphics item belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the associated video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video graphic item was deleted.

        Raises:
            ApiError: Error code 3978: The Composer graphics API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't delete the specified video graphic item. * Error code 8000: The user
                credentials are invalid. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.delete_composer_video_graphic_item(
                live_event_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_composer_video_graphic_items(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComposerGraphicsConnection:
        """The method returns every video graphics item belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video graphic items were returned.

        Raises:
            ApiError: Error code 3978: The Composer graphics API isn't supported in the context of venues. * Error code
                3200: The authenticated user can't access the event. * Error code 8000: The user credentials are
                invalid. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_composer_video_graphic_items(
                live_event_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveGraphicsWithRawResponse:
        return self._with_raw_response


class LiveGraphicsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_composer_video_graphic_item(
        self,
        live_event_id: float,
        body: LiveEventsComposerGraphicsVideosRequest | LiveEventsComposerGraphicsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComposerGraphics, AddComposerVideoGraphicItemErrorBody]:
        """This method add a new video graphics item to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/composer/graphics/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsComposerGraphicsVideosRequest | LiveEventsComposerGraphicsVideosRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ComposerGraphics],
            error_mapper=add_composer_video_graphic_item_error_mapper,
            request_options=request_options,
        )

    def delete_composer_video_graphic_item(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteComposerVideoGraphicItemErrorBody]:
        """This method deletes a video graphics item belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the associated video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}/composer/graphics/videos/{video_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_composer_video_graphic_item_error_mapper,
            request_options=request_options,
        )

    def get_composer_video_graphic_items(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComposerGraphicsConnection, GetComposerVideoGraphicItemsErrorBody]:
        """The method returns every video graphics item belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/composer/graphics/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ComposerGraphicsConnection],
            error_mapper=get_composer_video_graphic_items_error_mapper,
            request_options=request_options,
        )


class AsyncLiveGraphicsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_composer_video_graphic_item(
        self,
        live_event_id: float,
        body: LiveEventsComposerGraphicsVideosRequest | LiveEventsComposerGraphicsVideosRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComposerGraphics, AddComposerVideoGraphicItemErrorBody]:
        """This method add a new video graphics item to the specified event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/composer/graphics/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsComposerGraphicsVideosRequest | LiveEventsComposerGraphicsVideosRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ComposerGraphics],
            error_mapper=add_composer_video_graphic_item_error_mapper,
            request_options=request_options,
        )

    async def delete_composer_video_graphic_item(
        self, live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteComposerVideoGraphicItemErrorBody]:
        """This method deletes a video graphics item belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            video_id: The ID of the associated video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}/composer/graphics/videos/{video_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_composer_video_graphic_item_error_mapper,
            request_options=request_options,
        )

    async def get_composer_video_graphic_items(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComposerGraphicsConnection, GetComposerVideoGraphicItemsErrorBody]:
        """The method returns every video graphics item belonging to the specified event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/composer/graphics/videos"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ComposerGraphicsConnection],
            error_mapper=get_composer_video_graphic_items_error_mapper,
            request_options=request_options,
        )
