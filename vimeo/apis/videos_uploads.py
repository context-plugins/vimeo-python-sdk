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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.complete_streaming_upload_error import (
    CompleteStreamingUploadErrorBody,
    complete_streaming_upload_error_mapper,
)
from ..errors.upload_video_alt1_error import UploadVideoAlt1ErrorBody, upload_video_alt1_error_mapper
from ..errors.upload_video_error import UploadVideoErrorBody, upload_video_error_mapper
from ..models.me_videos_request1 import MeVideosRequest1, MeVideosRequest1Dict
from ..models.upload_attempt import UploadAttempt
from ..models.users_videos_request1 import UsersVideosRequest1, UsersVideosRequest1Dict
from ..models.video import Video
from ..server.server import Server


class VideosUploads:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosUploadsWithRawResponse(client, server, auth)

    def complete_streaming_upload(
        self,
        upload_id: float,
        user_id: float,
        signature: str,
        video_file_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method completes the specified streaming upload of the authenticated user.

        Args:
            upload_id: The ID of the streaming upload.
            user_id: The ID of the user.
            signature: The crypto signature of the completed upload.
            video_file_id: The ID of the uploaded file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The streaming upload was completed.

        Raises:
            ApiError: Error code 2502: The format of the video file is invalid. * Error code 5006: No such video file
                exists. * Error code 5007: No such signature exists. * Error code 8400: The signature is invalid. Error
                code 4011: The upload server returned an HTTP status code other than 200. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.complete_streaming_upload(
            upload_id, user_id, signature, video_file_id, request_options=request_options
        ).unwrap()

    def get_upload_attempt(
        self, upload_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> UploadAttempt:
        """This method returns the specified upload attempt of the authenticated user. _This method has been deprecated.
        For information on our currently supported upload approaches, see our `Working with Video Uploads
        <https://developer.vimeo.com/api/upload/videos>`__ guide._

        Args:
            upload_id: The ID of the upload attempt.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The upload attempt was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_upload_attempt(upload_id, user_id, request_options=request_options).unwrap()

    def upload_video(
        self,
        user_id: float,
        body: UsersVideosRequest1 | UsersVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method begins the video upload process for the authenticated user. For more information, see our `upload
        documentation <https://developer.vimeo.com/api/upload/videos>`__.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The upload procedure has begun.

        Raises:
            ApiError: * Error code 2204: The request contains invalid body parameters. * Error code 2205: The body of
                the request isn't formatted properly. * Error code 2230: The upload type is invalid. * Error code 3116:
                The **type** payload parameter was supplied instead of **upload.approach**. Use **upload.approach**
                starting from API version 3.4. Error code 8002: No user is associated with the access token. * Error
                code 4101: The authenticated user's maximum disk space has been reached. * Error code 4102: The
                authenticated user's allotted weekly quota has been reached. * Error code 4104: The authenticated user's
                allotted daily quota has been reached. Error code 4003: There is a problem initiating the upload.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.upload_video(user_id, body, request_options=request_options).unwrap()

    def upload_video_alt1(
        self, body: MeVideosRequest1 | MeVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method begins the video upload process for the authenticated user. For more information, see our `upload
        documentation <https://developer.vimeo.com/api/upload/videos>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The upload procedure has begun.

        Raises:
            ApiError: * Error code 2204: The request contains invalid body parameters. * Error code 2205: The body of
                the request isn't formatted properly. * Error code 2230: The upload type is invalid. * Error code 3116:
                The **type** payload parameter was supplied instead of **upload.approach**. Use **upload.approach**
                starting from API version 3.4. Error code 8002: No user is associated with the access token. * Error
                code 4101: The authenticated user's maximum disk space has been reached. * Error code 4102: The
                authenticated user's allotted weekly quota has been reached. * Error code 4104: The authenticated user's
                allotted daily quota has been reached. Error code 4003: There is a problem initiating the upload.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.upload_video_alt1(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VideosUploadsWithRawResponse:
        return self._with_raw_response


class AsyncVideosUploads:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosUploadsWithRawResponse(client, server, auth)

    async def complete_streaming_upload(
        self,
        upload_id: float,
        user_id: float,
        signature: str,
        video_file_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method completes the specified streaming upload of the authenticated user.

        Args:
            upload_id: The ID of the streaming upload.
            user_id: The ID of the user.
            signature: The crypto signature of the completed upload.
            video_file_id: The ID of the uploaded file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The streaming upload was completed.

        Raises:
            ApiError: Error code 2502: The format of the video file is invalid. * Error code 5006: No such video file
                exists. * Error code 5007: No such signature exists. * Error code 8400: The signature is invalid. Error
                code 4011: The upload server returned an HTTP status code other than 200. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.complete_streaming_upload(
                upload_id, user_id, signature, video_file_id, request_options=request_options
            )
        ).unwrap()

    async def get_upload_attempt(
        self, upload_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> UploadAttempt:
        """This method returns the specified upload attempt of the authenticated user. _This method has been deprecated.
        For information on our currently supported upload approaches, see our `Working with Video Uploads
        <https://developer.vimeo.com/api/upload/videos>`__ guide._

        Args:
            upload_id: The ID of the upload attempt.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The upload attempt was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_upload_attempt(upload_id, user_id, request_options=request_options)
        ).unwrap()

    async def upload_video(
        self,
        user_id: float,
        body: UsersVideosRequest1 | UsersVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method begins the video upload process for the authenticated user. For more information, see our `upload
        documentation <https://developer.vimeo.com/api/upload/videos>`__.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The upload procedure has begun.

        Raises:
            ApiError: * Error code 2204: The request contains invalid body parameters. * Error code 2205: The body of
                the request isn't formatted properly. * Error code 2230: The upload type is invalid. * Error code 3116:
                The **type** payload parameter was supplied instead of **upload.approach**. Use **upload.approach**
                starting from API version 3.4. Error code 8002: No user is associated with the access token. * Error
                code 4101: The authenticated user's maximum disk space has been reached. * Error code 4102: The
                authenticated user's allotted weekly quota has been reached. * Error code 4104: The authenticated user's
                allotted daily quota has been reached. Error code 4003: There is a problem initiating the upload.
                ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.upload_video(user_id, body, request_options=request_options)).unwrap()

    async def upload_video_alt1(
        self, body: MeVideosRequest1 | MeVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method begins the video upload process for the authenticated user. For more information, see our `upload
        documentation <https://developer.vimeo.com/api/upload/videos>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The upload procedure has begun.

        Raises:
            ApiError: * Error code 2204: The request contains invalid body parameters. * Error code 2205: The body of
                the request isn't formatted properly. * Error code 2230: The upload type is invalid. * Error code 3116:
                The **type** payload parameter was supplied instead of **upload.approach**. Use **upload.approach**
                starting from API version 3.4. Error code 8002: No user is associated with the access token. * Error
                code 4101: The authenticated user's maximum disk space has been reached. * Error code 4102: The
                authenticated user's allotted weekly quota has been reached. * Error code 4104: The authenticated user's
                allotted daily quota has been reached. Error code 4003: There is a problem initiating the upload.
                ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.upload_video_alt1(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosUploadsWithRawResponse:
        return self._with_raw_response


class VideosUploadsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def complete_streaming_upload(
        self,
        upload_id: float,
        user_id: float,
        signature: str,
        video_file_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, CompleteStreamingUploadErrorBody]:
        """This method completes the specified streaming upload of the authenticated user.

        Args:
            upload_id: The ID of the streaming upload.
            user_id: The ID of the user.
            signature: The crypto signature of the completed upload.
            video_file_id: The ID of the uploaded file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/uploads/{upload_id}"),
            path_params=[param[float]("upload_id", upload_id), param[float]("user_id", user_id)],
            query_params=[param[str]("signature", signature), param[float]("video_file_id", video_file_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=complete_streaming_upload_error_mapper,
            request_options=request_options,
        )

    def get_upload_attempt(
        self, upload_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UploadAttempt, RawError]:
        """This method returns the specified upload attempt of the authenticated user. _This method has been deprecated.
        For information on our currently supported upload approaches, see our `Working with Video Uploads
        <https://developer.vimeo.com/api/upload/videos>`__ guide._

        Args:
            upload_id: The ID of the upload attempt.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/uploads/{upload_id}"),
            path_params=[param[float]("upload_id", upload_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UploadAttempt],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upload_video(
        self,
        user_id: float,
        body: UsersVideosRequest1 | UsersVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, UploadVideoErrorBody]:
        """This method begins the video upload process for the authenticated user. For more information, see our `upload
        documentation <https://developer.vimeo.com/api/upload/videos>`__.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/videos"),
            path_params=[param[float]("user_id", user_id)],
            body=json_body[UsersVideosRequest1 | UsersVideosRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=upload_video_error_mapper,
            request_options=request_options,
        )

    def upload_video_alt1(
        self, body: MeVideosRequest1 | MeVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, UploadVideoAlt1ErrorBody]:
        """This method begins the video upload process for the authenticated user. For more information, see our `upload
        documentation <https://developer.vimeo.com/api/upload/videos>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/videos"),
            body=json_body[MeVideosRequest1 | MeVideosRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=upload_video_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncVideosUploadsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def complete_streaming_upload(
        self,
        upload_id: float,
        user_id: float,
        signature: str,
        video_file_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, CompleteStreamingUploadErrorBody]:
        """This method completes the specified streaming upload of the authenticated user.

        Args:
            upload_id: The ID of the streaming upload.
            user_id: The ID of the user.
            signature: The crypto signature of the completed upload.
            video_file_id: The ID of the uploaded file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/uploads/{upload_id}"),
            path_params=[param[float]("upload_id", upload_id), param[float]("user_id", user_id)],
            query_params=[param[str]("signature", signature), param[float]("video_file_id", video_file_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=complete_streaming_upload_error_mapper,
            request_options=request_options,
        )

    async def get_upload_attempt(
        self, upload_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UploadAttempt, RawError]:
        """This method returns the specified upload attempt of the authenticated user. _This method has been deprecated.
        For information on our currently supported upload approaches, see our `Working with Video Uploads
        <https://developer.vimeo.com/api/upload/videos>`__ guide._

        Args:
            upload_id: The ID of the upload attempt.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/uploads/{upload_id}"),
            path_params=[param[float]("upload_id", upload_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UploadAttempt],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upload_video(
        self,
        user_id: float,
        body: UsersVideosRequest1 | UsersVideosRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, UploadVideoErrorBody]:
        """This method begins the video upload process for the authenticated user. For more information, see our `upload
        documentation <https://developer.vimeo.com/api/upload/videos>`__.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/videos"),
            path_params=[param[float]("user_id", user_id)],
            body=json_body[UsersVideosRequest1 | UsersVideosRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=upload_video_error_mapper,
            request_options=request_options,
        )

    async def upload_video_alt1(
        self, body: MeVideosRequest1 | MeVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, UploadVideoAlt1ErrorBody]:
        """This method begins the video upload process for the authenticated user. For more information, see our `upload
        documentation <https://developer.vimeo.com/api/upload/videos>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/videos"),
            body=json_body[MeVideosRequest1 | MeVideosRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=upload_video_alt1_error_mapper,
            request_options=request_options,
        )
