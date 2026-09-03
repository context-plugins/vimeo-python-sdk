from __future__ import annotations

from uuid import UUID, uuid4

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
from ..errors.add_video_credit_alt1_error import AddVideoCreditAlt1ErrorBody, add_video_credit_alt1_error_mapper
from ..errors.add_video_credit_error import AddVideoCreditErrorBody, add_video_credit_error_mapper
from ..errors.delete_video_credit_error import DeleteVideoCreditErrorBody, delete_video_credit_error_mapper
from ..errors.edit_video_credit_error import EditVideoCreditErrorBody, edit_video_credit_error_mapper
from ..errors.get_video_credit_error import GetVideoCreditErrorBody, get_video_credit_error_mapper
from ..models.channels_videos_credits_request import ChannelsVideosCreditsRequest, ChannelsVideosCreditsRequestDict
from ..models.credit import Credit
from ..models.credit_connection import CreditConnection
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort8 import Sort8OrStr
from ..models.user_connection import UserConnection
from ..models.videos_credits_request import VideosCreditsRequest, VideosCreditsRequestDict
from ..models.videos_credits_request1 import VideosCreditsRequest1, VideosCreditsRequest1Dict
from ..server.server import Server


class VideosCredits:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosCreditsWithRawResponse(client, server, auth)

    def add_video_credit(
        self,
        video_id: float,
        body: VideosCreditsRequest | VideosCreditsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Credit:
        """This method adds a user credit to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was added.

        Raises:
            ApiError: * A parameter is invalid. * The authenticated user has an unverified email address. * There is a
                user block between the video owner and the person receiving credit. The authenticated user doesn't own
                the video. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_credit(video_id, body, request_options=request_options).unwrap()

    def add_video_credit_alt1(
        self,
        channel_id: float,
        video_id: float,
        body: ChannelsVideosCreditsRequest | ChannelsVideosCreditsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Credit:
        """This method adds a user credit to the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was added.

        Raises:
            ApiError: * A parameter is invalid. * The authenticated user has an unverified email address. * There is a
                user block between the video owner and the person receiving credit. The authenticated user doesn't own
                the video. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_credit_alt1(
            channel_id, video_id, body, request_options=request_options
        ).unwrap()

    def available_users(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns the users who can be credited on the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users who can be credited were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.available_users(
            video_id,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def delete_video_credit(
        self, credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified user credit from a video. The authenticated user must be the creator of the
        credit or the credited user.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was deleted.

        Raises:
            ApiError: The authenticated user isn't the creator of the credit or the credited user. ``error`` is
                ``LegacyError | RawError``."""
        return self._with_raw_response.delete_video_credit(
            credit_id, video_id, request_options=request_options
        ).unwrap()

    def edit_video_credit(
        self,
        credit_id: float,
        video_id: float,
        *,
        body: VideosCreditsRequest1 | VideosCreditsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Credit:
        """This method edits the specified user credit in a video.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was edited.

        Raises:
            ApiError: A parameter is invalid. No such video or credit exists. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.edit_video_credit(
            credit_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def get_video_credit(
        self, credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Credit:
        """This method returns a single credited user in a video.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was returned.

        Raises:
            ApiError: No such video or credit exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.get_video_credit(credit_id, video_id, request_options=request_options).unwrap()

    def get_video_credits(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreditConnection:
        """This method returns every credited user in a video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credited users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_credits(
            video_id,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_video_credits_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreditConnection:
        """This method returns every credited user in a video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credited users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_video_credits_alt1(
            channel_id,
            video_id,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosCreditsWithRawResponse:
        return self._with_raw_response


class AsyncVideosCredits:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosCreditsWithRawResponse(client, server, auth)

    async def add_video_credit(
        self,
        video_id: float,
        body: VideosCreditsRequest | VideosCreditsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Credit:
        """This method adds a user credit to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was added.

        Raises:
            ApiError: * A parameter is invalid. * The authenticated user has an unverified email address. * There is a
                user block between the video owner and the person receiving credit. The authenticated user doesn't own
                the video. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_credit(video_id, body, request_options=request_options)
        ).unwrap()

    async def add_video_credit_alt1(
        self,
        channel_id: float,
        video_id: float,
        body: ChannelsVideosCreditsRequest | ChannelsVideosCreditsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Credit:
        """This method adds a user credit to the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was added.

        Raises:
            ApiError: * A parameter is invalid. * The authenticated user has an unverified email address. * There is a
                user block between the video owner and the person receiving credit. The authenticated user doesn't own
                the video. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_credit_alt1(
                channel_id, video_id, body, request_options=request_options
            )
        ).unwrap()

    async def available_users(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns the users who can be credited on the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users who can be credited were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.available_users(
                video_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_video_credit(
        self, credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified user credit from a video. The authenticated user must be the creator of the
        credit or the credited user.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was deleted.

        Raises:
            ApiError: The authenticated user isn't the creator of the credit or the credited user. ``error`` is
                ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_video_credit(credit_id, video_id, request_options=request_options)
        ).unwrap()

    async def edit_video_credit(
        self,
        credit_id: float,
        video_id: float,
        *,
        body: VideosCreditsRequest1 | VideosCreditsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Credit:
        """This method edits the specified user credit in a video.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was edited.

        Raises:
            ApiError: A parameter is invalid. No such video or credit exists. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.edit_video_credit(
                credit_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_video_credit(
        self, credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Credit:
        """This method returns a single credited user in a video.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credit was returned.

        Raises:
            ApiError: No such video or credit exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_video_credit(credit_id, video_id, request_options=request_options)
        ).unwrap()

    async def get_video_credits(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreditConnection:
        """This method returns every credited user in a video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credited users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_credits(
                video_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_video_credits_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreditConnection:
        """This method returns every credited user in a video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The credited users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_video_credits_alt1(
                channel_id,
                video_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosCreditsWithRawResponse:
        return self._with_raw_response


class VideosCreditsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_credit(
        self,
        video_id: float,
        body: VideosCreditsRequest | VideosCreditsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Credit, AddVideoCreditErrorBody]:
        """This method adds a user credit to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/credits"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCreditsRequest | VideosCreditsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Credit],
            error_mapper=add_video_credit_error_mapper,
            request_options=request_options,
        )

    def add_video_credit_alt1(
        self,
        channel_id: float,
        video_id: float,
        body: ChannelsVideosCreditsRequest | ChannelsVideosCreditsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Credit, AddVideoCreditAlt1ErrorBody]:
        """This method adds a user credit to the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/credits"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsVideosCreditsRequest | ChannelsVideosCreditsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Credit],
            error_mapper=add_video_credit_alt1_error_mapper,
            request_options=request_options,
        )

    def available_users(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns the users who can be credited on the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/credits/available_users"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_video_credit(
        self, credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoCreditErrorBody]:
        """This method deletes the specified user credit from a video. The authenticated user must be the creator of the
        credit or the credited user.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/credits/{credit_id}"),
            path_params=[param[float]("credit_id", credit_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_credit_error_mapper,
            request_options=request_options,
        )

    def edit_video_credit(
        self,
        credit_id: float,
        video_id: float,
        *,
        body: VideosCreditsRequest1 | VideosCreditsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Credit, EditVideoCreditErrorBody]:
        """This method edits the specified user credit in a video.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/credits/{credit_id}"),
            path_params=[param[float]("credit_id", credit_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCreditsRequest1 | VideosCreditsRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Credit],
            error_mapper=edit_video_credit_error_mapper,
            request_options=request_options,
        )

    def get_video_credit(
        self, credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Credit, GetVideoCreditErrorBody]:
        """This method returns a single credited user in a video.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/credits/{credit_id}"),
            path_params=[param[float]("credit_id", credit_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Credit],
            error_mapper=get_video_credit_error_mapper,
            request_options=request_options,
        )

    def get_video_credits(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreditConnection, RawError]:
        """This method returns every credited user in a video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/credits"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CreditConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_video_credits_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreditConnection, RawError]:
        """This method returns every credited user in a video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/credits"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CreditConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVideosCreditsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_credit(
        self,
        video_id: float,
        body: VideosCreditsRequest | VideosCreditsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Credit, AddVideoCreditErrorBody]:
        """This method adds a user credit to the specified video.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/credits"),
            path_params=[param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCreditsRequest | VideosCreditsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Credit],
            error_mapper=add_video_credit_error_mapper,
            request_options=request_options,
        )

    async def add_video_credit_alt1(
        self,
        channel_id: float,
        video_id: float,
        body: ChannelsVideosCreditsRequest | ChannelsVideosCreditsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Credit, AddVideoCreditAlt1ErrorBody]:
        """This method adds a user credit to the specified video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/credits"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChannelsVideosCreditsRequest | ChannelsVideosCreditsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Credit],
            error_mapper=add_video_credit_alt1_error_mapper,
            request_options=request_options,
        )

    async def available_users(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns the users who can be credited on the specified video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/credits/available_users"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[UserConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_video_credit(
        self, credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoCreditErrorBody]:
        """This method deletes the specified user credit from a video. The authenticated user must be the creator of the
        credit or the credited user.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/videos/{video_id}/credits/{credit_id}"),
            path_params=[param[float]("credit_id", credit_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_credit_error_mapper,
            request_options=request_options,
        )

    async def edit_video_credit(
        self,
        credit_id: float,
        video_id: float,
        *,
        body: VideosCreditsRequest1 | VideosCreditsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Credit, EditVideoCreditErrorBody]:
        """This method edits the specified user credit in a video.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/credits/{credit_id}"),
            path_params=[param[float]("credit_id", credit_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideosCreditsRequest1 | VideosCreditsRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Credit],
            error_mapper=edit_video_credit_error_mapper,
            request_options=request_options,
        )

    async def get_video_credit(
        self, credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Credit, GetVideoCreditErrorBody]:
        """This method returns a single credited user in a video.

        Args:
            credit_id: The ID of the credit.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/credits/{credit_id}"),
            path_params=[param[float]("credit_id", credit_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Credit],
            error_mapper=get_video_credit_error_mapper,
            request_options=request_options,
        )

    async def get_video_credits(
        self,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreditConnection, RawError]:
        """This method returns every credited user in a video.

        Args:
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/credits"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CreditConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_video_credits_alt1(
        self,
        channel_id: float,
        video_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreditConnection, RawError]:
        """This method returns every credited user in a video.

        Args:
            channel_id: The ID of the channel.
            video_id: The ID of the video.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/channels/{channel_id}/videos/{video_id}/credits"),
            path_params=[param[float]("channel_id", channel_id), param[float]("video_id", video_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CreditConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
