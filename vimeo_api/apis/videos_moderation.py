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
    async_json_decoder,
    json_decoder,
    unwrap,
)
from ..errors.get_video_reporting_reasons_error import (
    GetVideoReportingReasonsErrorBody,
    get_video_reporting_reasons_error_mapper,
)
from ..models.video_report_reason import VideoReportReason
from ..server.server import Server


class VideosModeration:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosModerationWithRawResponse(client, server, auth)

    def get_video_reporting_reasons(self, *, request_options: RequestOptionsOrDict | None = None) -> VideoReportReason:
        """This method returns a list of valid reasons for reporting inappropriate videos on Vimeo.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The list of reasons was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.get_video_reporting_reasons(request_options=request_options))

    @property
    def with_raw_response(self) -> VideosModerationWithRawResponse:
        return self._with_raw_response


class AsyncVideosModeration:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosModerationWithRawResponse(client, server, auth)

    async def get_video_reporting_reasons(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> VideoReportReason:
        """This method returns a list of valid reasons for reporting inappropriate videos on Vimeo.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The list of reasons was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.get_video_reporting_reasons(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncVideosModerationWithRawResponse:
        return self._with_raw_response


class VideosModerationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_video_reporting_reasons(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoReportReason, GetVideoReportingReasonsErrorBody]:
        """This method returns a list of valid reasons for reporting inappropriate videos on Vimeo.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/report/video_report_reasons"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoReportReason],
            error_mapper=get_video_reporting_reasons_error_mapper,
            request_options=request_options,
        )


class AsyncVideosModerationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_video_reporting_reasons(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VideoReportReason, GetVideoReportingReasonsErrorBody]:
        """This method returns a list of valid reasons for reporting inappropriate videos on Vimeo.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/report/video_report_reasons"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[VideoReportReason],
            error_mapper=get_video_reporting_reasons_error_mapper,
            request_options=request_options,
        )
