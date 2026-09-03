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
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.add_video_to_portfolio_alt1_error import (
    AddVideoToPortfolioAlt1ErrorBody,
    add_video_to_portfolio_alt1_error_mapper,
)
from ..errors.add_video_to_portfolio_error import AddVideoToPortfolioErrorBody, add_video_to_portfolio_error_mapper
from ..errors.delete_video_from_portfolio_alt1_error import (
    DeleteVideoFromPortfolioAlt1ErrorBody,
    delete_video_from_portfolio_alt1_error_mapper,
)
from ..errors.delete_video_from_portfolio_error import (
    DeleteVideoFromPortfolioErrorBody,
    delete_video_from_portfolio_error_mapper,
)
from ..models.enums.filter3 import Filter3OrStr
from ..models.enums.sort35 import Sort35OrStr
from ..models.video import Video
from ..models.video_connection import VideoConnection
from ..server.server import Server


class PortfoliosVideos:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PortfoliosVideosWithRawResponse(client, server, auth)

    def add_video_to_portfolio(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds a video to the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: No such portfolio or video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_to_portfolio(
            portfolio_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def add_video_to_portfolio_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a video to the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: No such portfolio or video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.add_video_to_portfolio_alt1(
            portfolio_id, video_id, request_options=request_options
        ).unwrap()

    def delete_video_from_portfolio(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes a video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: No such portfolio or video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_video_from_portfolio(
            portfolio_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def delete_video_from_portfolio_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: No such portfolio or video exists. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_video_from_portfolio_alt1(
            portfolio_id, video_id, request_options=request_options
        ).unwrap()

    def get_portfolio_video(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method returns a single video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_portfolio_video(
            portfolio_id, user_id, video_id, request_options=request_options
        ).unwrap()

    def get_portfolio_video_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_portfolio_video_alt1(
            portfolio_id, video_id, request_options=request_options
        ).unwrap()

    def get_portfolio_videos(
        self,
        portfolio_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort35OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``default`` - Use the default sorting method. * ``likes`` - Sort the results by
                number of likes. * ``manual`` - Sort the results by their user-specified order. * ``plays`` - Sort the
                results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_portfolio_videos(
            portfolio_id,
            user_id,
            containing_uri=containing_uri,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_portfolio_videos_alt1(
        self,
        portfolio_id: float,
        *,
        containing_uri: str | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort35OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            containing_uri: The page that contains the video URI.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``default`` - Use the default sorting method. * ``likes`` - Sort the results by
                number of likes. * ``manual`` - Sort the results by their user-specified order. * ``plays`` - Sort the
                results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_portfolio_videos_alt1(
            portfolio_id,
            containing_uri=containing_uri,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> PortfoliosVideosWithRawResponse:
        return self._with_raw_response


class AsyncPortfoliosVideos:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPortfoliosVideosWithRawResponse(client, server, auth)

    async def add_video_to_portfolio(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method adds a video to the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: No such portfolio or video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_to_portfolio(
                portfolio_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def add_video_to_portfolio_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method adds a video to the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was added.

        Raises:
            ApiError: No such portfolio or video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.add_video_to_portfolio_alt1(
                portfolio_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def delete_video_from_portfolio(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method removes a video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: No such portfolio or video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_video_from_portfolio(
                portfolio_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def delete_video_from_portfolio_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method removes a video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was removed.

        Raises:
            ApiError: No such portfolio or video exists. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_video_from_portfolio_alt1(
                portfolio_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_portfolio_video(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Video:
        """This method returns a single video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_portfolio_video(
                portfolio_id, user_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_portfolio_video_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> Video:
        """This method returns a single video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The video was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_portfolio_video_alt1(
                portfolio_id, video_id, request_options=request_options
            )
        ).unwrap()

    async def get_portfolio_videos(
        self,
        portfolio_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort35OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``default`` - Use the default sorting method. * ``likes`` - Sort the results by
                number of likes. * ``manual`` - Sort the results by their user-specified order. * ``plays`` - Sort the
                results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_portfolio_videos(
                portfolio_id,
                user_id,
                containing_uri=containing_uri,
                filter=filter,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_portfolio_videos_alt1(
        self,
        portfolio_id: float,
        *,
        containing_uri: str | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort35OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> VideoConnection:
        """This method returns every video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            containing_uri: The page that contains the video URI.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``default`` - Use the default sorting method. * ``likes`` - Sort the results by
                number of likes. * ``manual`` - Sort the results by their user-specified order. * ``plays`` - Sort the
                results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_portfolio_videos_alt1(
                portfolio_id,
                containing_uri=containing_uri,
                filter=filter,
                filter_embeddable=filter_embeddable,
                page=page,
                per_page=per_page,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPortfoliosVideosWithRawResponse:
        return self._with_raw_response


class PortfoliosVideosWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_video_to_portfolio(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideoToPortfolioErrorBody]:
        """This method adds a video to the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[
                param[float]("portfolio_id", portfolio_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_portfolio_error_mapper,
            request_options=request_options,
        )

    def add_video_to_portfolio_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToPortfolioAlt1ErrorBody]:
        """This method adds a video to the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_portfolio_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_video_from_portfolio(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteVideoFromPortfolioErrorBody]:
        """This method removes a video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[
                param[float]("portfolio_id", portfolio_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_portfolio_error_mapper,
            request_options=request_options,
        )

    def delete_video_from_portfolio_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoFromPortfolioAlt1ErrorBody]:
        """This method removes a video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_portfolio_alt1_error_mapper,
            request_options=request_options,
        )

    def get_portfolio_video(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, RawError]:
        """This method returns a single video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[
                param[float]("portfolio_id", portfolio_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_portfolio_video_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, RawError]:
        """This method returns a single video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_portfolio_videos(
        self,
        portfolio_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort35OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``default`` - Use the default sorting method. * ``likes`` - Sort the results by
                number of likes. * ``manual`` - Sort the results by their user-specified order. * ``plays`` - Sort the
                results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}/videos"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort35OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_portfolio_videos_alt1(
        self,
        portfolio_id: float,
        *,
        containing_uri: str | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort35OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            containing_uri: The page that contains the video URI.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``default`` - Use the default sorting method. * ``likes`` - Sort the results by
                number of likes. * ``manual`` - Sort the results by their user-specified order. * ``plays`` - Sort the
                results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/portfolios/{portfolio_id}/videos"),
            path_params=[param[float]("portfolio_id", portfolio_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort35OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPortfoliosVideosWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_video_to_portfolio(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AddVideoToPortfolioErrorBody]:
        """This method adds a video to the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[
                param[float]("portfolio_id", portfolio_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_portfolio_error_mapper,
            request_options=request_options,
        )

    async def add_video_to_portfolio_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, AddVideoToPortfolioAlt1ErrorBody]:
        """This method adds a video to the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=add_video_to_portfolio_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_video_from_portfolio(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteVideoFromPortfolioErrorBody]:
        """This method removes a video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[
                param[float]("portfolio_id", portfolio_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_portfolio_error_mapper,
            request_options=request_options,
        )

    async def delete_video_from_portfolio_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteVideoFromPortfolioAlt1ErrorBody]:
        """This method removes a video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("video_id", video_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_video_from_portfolio_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_portfolio_video(
        self,
        portfolio_id: float,
        user_id: float,
        video_id: float,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Video, RawError]:
        """This method returns a single video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[
                param[float]("portfolio_id", portfolio_id),
                param[float]("user_id", user_id),
                param[float]("video_id", video_id),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_portfolio_video_alt1(
        self, portfolio_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Video, RawError]:
        """This method returns a single video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/portfolios/{portfolio_id}/videos/{video_id}"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Video],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_portfolio_videos(
        self,
        portfolio_id: float,
        user_id: float,
        *,
        containing_uri: str | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort35OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            user_id: The ID of the user.
            containing_uri: The page that contains the video URI.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``default`` - Use the default sorting method. * ``likes`` - Sort the results by
                number of likes. * ``manual`` - Sort the results by their user-specified order. * ``plays`` - Sort the
                results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/portfolios/{portfolio_id}/videos"),
            path_params=[param[float]("portfolio_id", portfolio_id), param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort35OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_portfolio_videos_alt1(
        self,
        portfolio_id: float,
        *,
        containing_uri: str | None = None,
        filter: Filter3OrStr | None = None,
        filter_embeddable: bool | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort35OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[VideoConnection, RawError]:
        """This method returns every video from the specified portfolio belonging to the authenticated user.

        Args:
            portfolio_id: The ID of the portfolio.
            containing_uri: The page that contains the video URI.
            filter: The attribute by which to filter the results. Option descriptions: * ``embeddable`` - Return
                embeddable videos.
            filter_embeddable: Whether to filter the results by embeddable videos (``true``) or non-embeddable videos
                (``false``). This parameter is required only when **filter** is ``embeddable``.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``comments`` - Sort the results by number of comments. * ``date`` - Sort the results
                by creation date. * ``default`` - Use the default sorting method. * ``likes`` - Sort the results by
                number of likes. * ``manual`` - Sort the results by their user-specified order. * ``plays`` - Sort the
                results by number of plays.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/portfolios/{portfolio_id}/videos"),
            path_params=[param[float]("portfolio_id", portfolio_id)],
            query_params=[
                param[str | None]("containing_uri", containing_uri),
                param[Filter3OrStr | None]("filter", filter),
                param[bool | None]("filter_embeddable", filter_embeddable),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort35OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[VideoConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
