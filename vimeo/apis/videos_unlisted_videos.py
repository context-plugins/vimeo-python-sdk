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
from ..errors.add_video_privacy_user_error import AddVideoPrivacyUserErrorBody, add_video_privacy_user_error_mapper
from ..errors.delete_video_privacy_user_error import (
    DeleteVideoPrivacyUserErrorBody,
    delete_video_privacy_user_error_mapper,
)
from ..errors.get_video_privacy_users_alt1_error import (
    GetVideoPrivacyUsersAlt1ErrorBody,
    get_video_privacy_users_alt1_error_mapper,
)
from ..errors.get_video_privacy_users_error import GetVideoPrivacyUsersErrorBody, get_video_privacy_users_error_mapper
from ..models.user import User
from ..models.user_connection import UserConnection
from ..server.server import Server


class VideosUnlistedVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosUnlistedVideosWithRawResponse(client, server, auth)

    def add_video_privacy_user(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """This method gives a single user permission to access the specified unlisted video. The authenticated user
        must be the owner of the video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was granted access to the unlisted video.

        Raises:
            ApiError: The video doesn't have a user-defined access list. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_privacy_user(
            user_id, video_id, request_options=request_options
        ).unwrap()

    def add_video_privacy_users(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[User]:
        """This method gives multiple users permission to access the specified unlisted video. The authenticated user
        must be the owner of the video. The body of the request should follow our `batch request format
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__: each object must contain a
        single **uri** field whose value is the URI of the user who can access the video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were granted access to the unlisted video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.add_video_privacy_users(video_id, request_options=request_options).unwrap()

    def add_video_privacy_users_alt1(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[User]:
        """This method gives multiple users permission to access the specified unlisted video. The authenticated user
        must be the owner of the video. The body of the request should follow our `batch request format
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__: each object must contain a
        single **uri** field whose value is the URI of the user who can access the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were granted access to the unlisted video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.add_video_privacy_users_alt1(
            channel_id, video_id, request_options=request_options
        ).unwrap()

    def delete_video_privacy_user(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method prevents a user from being able to view the specified unlisted video. The authenticated user must
        be the owner of the video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was restricted from accessing the unlisted video.

        Raises:
            ApiError: The video isn't set to a user-defined access list. No such user exists. ``error`` is ``LegacyError
                | RawError``."""
        return self._with_raw_response.delete_video_privacy_user(
            user_id, video_id, request_options=request_options
        ).unwrap()

    def get_video_privacy_users(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has access to the specified unlisted video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were returned.

        Raises:
            ApiError: No users can access this unlisted video. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_video_privacy_users(
            video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def get_video_privacy_users_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has access to the specified unlisted video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were returned.

        Raises:
            ApiError: No users can access this unlisted video. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_video_privacy_users_alt1(
            channel_id, video_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosUnlistedVideosWithRawResponse:
        return self._with_raw_response


class AsyncVideosUnlistedVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosUnlistedVideosWithRawResponse(client, server, auth)

    async def add_video_privacy_user(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """This method gives a single user permission to access the specified unlisted video. The authenticated user
        must be the owner of the video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was granted access to the unlisted video.

        Raises:
            ApiError: The video doesn't have a user-defined access list. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_privacy_user(user_id, video_id, request_options=request_options)
        ).unwrap()

    async def add_video_privacy_users(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[User]:
        """This method gives multiple users permission to access the specified unlisted video. The authenticated user
        must be the owner of the video. The body of the request should follow our `batch request format
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__: each object must contain a
        single **uri** field whose value is the URI of the user who can access the video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were granted access to the unlisted video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_video_privacy_users(video_id, request_options=request_options)
        ).unwrap()

    async def add_video_privacy_users_alt1(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[User]:
        """This method gives multiple users permission to access the specified unlisted video. The authenticated user
        must be the owner of the video. The body of the request should follow our `batch request format
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__: each object must contain a
        single **uri** field whose value is the URI of the user who can access the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were granted access to the unlisted video.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_video_privacy_users_alt1(
                channel_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def delete_video_privacy_user(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method prevents a user from being able to view the specified unlisted video. The authenticated user must
        be the owner of the video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was restricted from accessing the unlisted video.

        Raises:
            ApiError: The video isn't set to a user-defined access list. No such user exists. ``error`` is ``LegacyError
                | RawError``."""
        return (
            await self._with_raw_response.delete_video_privacy_user(user_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_video_privacy_users(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has access to the specified unlisted video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were returned.

        Raises:
            ApiError: No users can access this unlisted video. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_video_privacy_users(
                video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def get_video_privacy_users_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who has access to the specified unlisted video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were returned.

        Raises:
            ApiError: No users can access this unlisted video. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_video_privacy_users_alt1(
                channel_id, video_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosUnlistedVideosWithRawResponse:
        return self._with_raw_response


class VideosUnlistedVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_privacy_user(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, AddVideoPrivacyUserErrorBody]:
        """This method gives a single user permission to access the specified unlisted video. The authenticated user
        must be the owner of the video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/privacy/users/{user_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=add_video_privacy_user_error_mapper,
            request_options=request_options,
        )

    def add_video_privacy_users(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[User], RawError]:
        """This method gives multiple users permission to access the specified unlisted video. The authenticated user
        must be the owner of the video. The body of the request should follow our `batch request format
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__: each object must contain a
        single **uri** field whose value is the URI of the user who can access the video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/privacy/users"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[User]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def add_video_privacy_users_alt1(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[User], RawError]:
        """This method gives multiple users permission to access the specified unlisted video. The authenticated user
        must be the owner of the video. The body of the request should follow our `batch request format
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__: each object must contain a
        single **uri** field whose value is the URI of the user who can access the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/privacy/users"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[User]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_video_privacy_user(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoPrivacyUserErrorBody]:
        """This method prevents a user from being able to view the specified unlisted video. The authenticated user must
        be the owner of the video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/privacy/users/{user_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_privacy_user_error_mapper,
            request_options=request_options,
        )

    def get_video_privacy_users(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetVideoPrivacyUsersErrorBody]:
        """This method returns every user who has access to the specified unlisted video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/privacy/users"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_video_privacy_users_error_mapper,
            request_options=request_options,
        )

    def get_video_privacy_users_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetVideoPrivacyUsersAlt1ErrorBody]:
        """This method returns every user who has access to the specified unlisted video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/privacy/users"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_video_privacy_users_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncVideosUnlistedVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_privacy_user(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, AddVideoPrivacyUserErrorBody]:
        """This method gives a single user permission to access the specified unlisted video. The authenticated user
        must be the owner of the video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/privacy/users/{user_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=add_video_privacy_user_error_mapper,
            request_options=request_options,
        )

    async def add_video_privacy_users(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[User], RawError]:
        """This method gives multiple users permission to access the specified unlisted video. The authenticated user
        must be the owner of the video. The body of the request should follow our `batch request format
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__: each object must contain a
        single **uri** field whose value is the URI of the user who can access the video.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/videos/{video_id}/privacy/users"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[User]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def add_video_privacy_users_alt1(
        self, channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[User], RawError]:
        """This method gives multiple users permission to access the specified unlisted video. The authenticated user
        must be the owner of the video. The body of the request should follow our `batch request format
        <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__: each object must contain a
        single **uri** field whose value is the URI of the user who can access the video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/privacy/users"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[list[User]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_video_privacy_user(
        self, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoPrivacyUserErrorBody]:
        """This method prevents a user from being able to view the specified unlisted video. The authenticated user must
        be the owner of the video.

        Args:
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/privacy/users/{user_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_privacy_user_error_mapper,
            request_options=request_options,
        )

    async def get_video_privacy_users(
        self,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetVideoPrivacyUsersErrorBody]:
        """This method returns every user who has access to the specified unlisted video.

        Args:
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/privacy/users"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_video_privacy_users_error_mapper,
            request_options=request_options,
        )

    async def get_video_privacy_users_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, GetVideoPrivacyUsersAlt1ErrorBody]:
        """This method returns every user who has access to the specified unlisted video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/privacy/users"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=get_video_privacy_users_alt1_error_mapper,
            request_options=request_options,
        )
