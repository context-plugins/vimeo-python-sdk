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
    param,
)
from ..errors.export_vpaas_viewer_analytics_error import (
    ExportVpaasViewerAnalyticsErrorBody,
    export_vpaas_viewer_analytics_error_mapper,
)
from ..server.server import Server


class LiveAnalytics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveAnalyticsWithRawResponse(client, server, auth)

    def export_vpaas_viewer_analytics(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method queues an export of VPaaS viewer analytics for the specified live event.

        The authenticated user must be the owner of the event or have edit permissions. The webhook is delivered to the
        managing vendor app's registered webhook URL.

        Args:
            live_event_id: The ID of the live event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The analytics export has been queued for processing.

        Raises:
            ApiError: Error code 9101: The user isn't authorized. Error code 3422: The authenticated user can't export
                analytics for this event, or the event is not owned by a VPaaS managed user. Error code 5000: No such
                event exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.export_vpaas_viewer_analytics(
            live_event_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveAnalyticsWithRawResponse:
        return self._with_raw_response


class AsyncLiveAnalytics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveAnalyticsWithRawResponse(client, server, auth)

    async def export_vpaas_viewer_analytics(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method queues an export of VPaaS viewer analytics for the specified live event.

        The authenticated user must be the owner of the event or have edit permissions. The webhook is delivered to the
        managing vendor app's registered webhook URL.

        Args:
            live_event_id: The ID of the live event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The analytics export has been queued for processing.

        Raises:
            ApiError: Error code 9101: The user isn't authorized. Error code 3422: The authenticated user can't export
                analytics for this event, or the event is not owned by a VPaaS managed user. Error code 5000: No such
                event exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.export_vpaas_viewer_analytics(live_event_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveAnalyticsWithRawResponse:
        return self._with_raw_response


class LiveAnalyticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def export_vpaas_viewer_analytics(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ExportVpaasViewerAnalyticsErrorBody]:
        """This method queues an export of VPaaS viewer analytics for the specified live event.

        The authenticated user must be the owner of the event or have edit permissions. The webhook is delivered to the
        managing vendor app's registered webhook URL.

        Args:
            live_event_id: The ID of the live event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/export_vpaas_analytics"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=export_vpaas_viewer_analytics_error_mapper,
            request_options=request_options,
        )


class AsyncLiveAnalyticsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def export_vpaas_viewer_analytics(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ExportVpaasViewerAnalyticsErrorBody]:
        """This method queues an export of VPaaS viewer analytics for the specified live event.

        The authenticated user must be the owner of the event or have edit permissions. The webhook is delivered to the
        managing vendor app's registered webhook URL.

        Args:
            live_event_id: The ID of the live event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events/{live_event_id}/export_vpaas_analytics"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=export_vpaas_viewer_analytics_error_mapper,
            request_options=request_options,
        )
