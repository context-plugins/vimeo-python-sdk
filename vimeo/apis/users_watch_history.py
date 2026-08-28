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
from ..errors.get_watch_history_error import GetWatchHistoryErrorBody, get_watch_history_error_mapper
from ..models.video_connection import VideoConnection
from ..server.server import Server


class UsersWatchHistory:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersWatchHistoryWithRawResponse(client, server, auth)

    def delete_from_watch_history(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified video from the authenticated user's watch history.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was deleted from the authenticated user's watch history.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_from_watch_history(video_id, request_options=request_options).unwrap()

    def delete_watch_history(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the entire watch history of the authenticated user.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authenticated user's watch history was deleted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_watch_history(request_options=request_options).unwrap()

    def get_watch_history(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video on the authenticated user's watch history. _This endpoint is deprecated. Any
        request to it returns empty data with HTTP status code 200._

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: The authenticated user can't view another user's watch history. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.get_watch_history(
            page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UsersWatchHistoryWithRawResponse:
        return self._with_raw_response


class AsyncUsersWatchHistory:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersWatchHistoryWithRawResponse(client, server, auth)

    async def delete_from_watch_history(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified video from the authenticated user's watch history.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was deleted from the authenticated user's watch history.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_from_watch_history(video_id, request_options=request_options)
        ).unwrap()

    async def delete_watch_history(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes the entire watch history of the authenticated user.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authenticated user's watch history was deleted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_watch_history(request_options=request_options)).unwrap()

    async def get_watch_history(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video on the authenticated user's watch history. _This endpoint is deprecated. Any
        request to it returns empty data with HTTP status code 200._

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: The authenticated user can't view another user's watch history. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.get_watch_history(
                page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersWatchHistoryWithRawResponse:
        return self._with_raw_response


class UsersWatchHistoryWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_from_watch_history(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method deletes the specified video from the authenticated user's watch history.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/watched/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_watch_history(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]:
        """This method deletes the entire watch history of the authenticated user.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/watched/videos"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_watch_history(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetWatchHistoryErrorBody]:
        """This method returns every video on the authenticated user's watch history. _This endpoint is deprecated. Any
        request to it returns empty data with HTTP status code 200._

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/watched/videos"),
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_watch_history_error_mapper,
            request_options=request_options,
        )


class AsyncUsersWatchHistoryWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_from_watch_history(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method deletes the specified video from the authenticated user's watch history.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/watched/videos/{video_id}"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_watch_history(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method deletes the entire watch history of the authenticated user.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/watched/videos"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_watch_history(
        self,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, GetWatchHistoryErrorBody]:
        """This method returns every video on the authenticated user's watch history. _This endpoint is deprecated. Any
        request to it returns empty data with HTTP status code 200._

        Args:
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/watched/videos"),
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=get_watch_history_error_mapper,
            request_options=request_options,
        )
