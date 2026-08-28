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
from ..models.fragments import Fragments
from ..server.server import Server


class VideosFragments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosFragmentsWithRawResponse(client, server, auth)

    def delete_fragments(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes all fragments for the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The fragments were deleted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_fragments(video_id, request_options=request_options).unwrap()

    def get_fragments(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Fragments:
        """This method returns all of the fragments associated with the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The fragments were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_fragments(video_id, request_options=request_options).unwrap()

    def put_fragments(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method updates the specified video with new fragments.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The fragments were updated.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.put_fragments(video_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VideosFragmentsWithRawResponse:
        return self._with_raw_response


class AsyncVideosFragments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosFragmentsWithRawResponse(client, server, auth)

    async def delete_fragments(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method deletes all fragments for the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The fragments were deleted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_fragments(video_id, request_options=request_options)).unwrap()

    async def get_fragments(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> Fragments:
        """This method returns all of the fragments associated with the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The fragments were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_fragments(video_id, request_options=request_options)).unwrap()

    async def put_fragments(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method updates the specified video with new fragments.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The fragments were updated.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.put_fragments(video_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosFragmentsWithRawResponse:
        return self._with_raw_response


class VideosFragmentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_fragments(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method deletes all fragments for the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/fragments"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_fragments(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Fragments, RawError]:
        """This method returns all of the fragments associated with the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/fragments"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Fragments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def put_fragments(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method updates the specified video with new fragments.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/fragments"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideosFragmentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_fragments(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method deletes all fragments for the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/fragments"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_fragments(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Fragments, RawError]:
        """This method returns all of the fragments associated with the specified video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/fragments"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Fragments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def put_fragments(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method updates the specified video with new fragments.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/fragments"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
