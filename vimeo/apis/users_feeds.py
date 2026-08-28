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
    json_decoder,
    param,
)
from ..errors.get_feed_alt1_error import GetFeedAlt1ErrorBody, get_feed_alt1_error_mapper
from ..errors.get_feed_error import GetFeedErrorBody, get_feed_error_mapper
from ..models.activity31_connection import Activity31Connection
from ..models.enums.type33 import Type33OrStr
from ..server.server import Server


class UsersFeeds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersFeedsWithRawResponse(client, server, auth)

    def get_feed(
        self,
        user_id: float,
        *,
        offset: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        type_: Type33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Activity31Connection:
        """This method returns every video in the authenticated user's feed.

        Args:
            user_id: The ID of the user.
            offset: The pagination offset. We recommend that you use the pagination links in the feed response instead
                of working with this value directly. For more details, see our `pagination documentation
                <https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter>`__.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            type_: The feed type. Option descriptions: * ``appears`` - Videos in which the user appears. *
                ``category_featured`` - Featured videos. * ``channel`` - Channel videos. * ``facebook_feed`` - Videos
                from the user's Facebook feed. * ``following`` - Videos from accounts that the user follows. * ``group``
                - Group videos. * ``likes`` - Liked videos. * ``ondemand_publish`` - On Demand videos. * ``share`` -
                Shared videos. * ``tagged_with`` - Tagged videos. * ``twitter_timeline`` - Videos from the user's
                Twitter timeline. * ``uploads`` - Uploaded videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_feed(
            user_id, offset=offset, page=page, per_page=per_page, type_=type_, request_options=request_options
        ).unwrap()

    def get_feed_alt1(
        self,
        *,
        offset: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        type_: Type33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Activity31Connection:
        """This method returns every video in the authenticated user's feed.

        Args:
            offset: The pagination offset. We recommend that you use the pagination links in the feed response instead
                of working with this value directly. For more details, see our `pagination documentation
                <https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter>`__.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            type_: The feed type. Option descriptions: * ``appears`` - Videos in which the user appears. *
                ``category_featured`` - Featured videos. * ``channel`` - Channel videos. * ``facebook_feed`` - Videos
                from the user's Facebook feed. * ``following`` - Videos from accounts that the user follows. * ``group``
                - Group videos. * ``likes`` - Liked videos. * ``ondemand_publish`` - On Demand videos. * ``share`` -
                Shared videos. * ``tagged_with`` - Tagged videos. * ``twitter_timeline`` - Videos from the user's
                Twitter timeline. * ``uploads`` - Uploaded videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_feed_alt1(
            offset=offset, page=page, per_page=per_page, type_=type_, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UsersFeedsWithRawResponse:
        return self._with_raw_response


class AsyncUsersFeeds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersFeedsWithRawResponse(client, server, auth)

    async def get_feed(
        self,
        user_id: float,
        *,
        offset: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        type_: Type33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Activity31Connection:
        """This method returns every video in the authenticated user's feed.

        Args:
            user_id: The ID of the user.
            offset: The pagination offset. We recommend that you use the pagination links in the feed response instead
                of working with this value directly. For more details, see our `pagination documentation
                <https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter>`__.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            type_: The feed type. Option descriptions: * ``appears`` - Videos in which the user appears. *
                ``category_featured`` - Featured videos. * ``channel`` - Channel videos. * ``facebook_feed`` - Videos
                from the user's Facebook feed. * ``following`` - Videos from accounts that the user follows. * ``group``
                - Group videos. * ``likes`` - Liked videos. * ``ondemand_publish`` - On Demand videos. * ``share`` -
                Shared videos. * ``tagged_with`` - Tagged videos. * ``twitter_timeline`` - Videos from the user's
                Twitter timeline. * ``uploads`` - Uploaded videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_feed(
                user_id, offset=offset, page=page, per_page=per_page, type_=type_, request_options=request_options
            )
        ).unwrap()

    async def get_feed_alt1(
        self,
        *,
        offset: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        type_: Type33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Activity31Connection:
        """This method returns every video in the authenticated user's feed.

        Args:
            offset: The pagination offset. We recommend that you use the pagination links in the feed response instead
                of working with this value directly. For more details, see our `pagination documentation
                <https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter>`__.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            type_: The feed type. Option descriptions: * ``appears`` - Videos in which the user appears. *
                ``category_featured`` - Featured videos. * ``channel`` - Channel videos. * ``facebook_feed`` - Videos
                from the user's Facebook feed. * ``following`` - Videos from accounts that the user follows. * ``group``
                - Group videos. * ``likes`` - Liked videos. * ``ondemand_publish`` - On Demand videos. * ``share`` -
                Shared videos. * ``tagged_with`` - Tagged videos. * ``twitter_timeline`` - Videos from the user's
                Twitter timeline. * ``uploads`` - Uploaded videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The videos were returned.

        Raises:
            ApiError: Error code 5451: This resource is restricted in your region. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_feed_alt1(
                offset=offset, page=page, per_page=per_page, type_=type_, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersFeedsWithRawResponse:
        return self._with_raw_response


class UsersFeedsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_feed(
        self,
        user_id: float,
        *,
        offset: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        type_: Type33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Activity31Connection, GetFeedErrorBody]:
        """This method returns every video in the authenticated user's feed.

        Args:
            user_id: The ID of the user.
            offset: The pagination offset. We recommend that you use the pagination links in the feed response instead
                of working with this value directly. For more details, see our `pagination documentation
                <https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter>`__.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            type_: The feed type. Option descriptions: * ``appears`` - Videos in which the user appears. *
                ``category_featured`` - Featured videos. * ``channel`` - Channel videos. * ``facebook_feed`` - Videos
                from the user's Facebook feed. * ``following`` - Videos from accounts that the user follows. * ``group``
                - Group videos. * ``likes`` - Liked videos. * ``ondemand_publish`` - On Demand videos. * ``share`` -
                Shared videos. * ``tagged_with`` - Tagged videos. * ``twitter_timeline`` - Videos from the user's
                Twitter timeline. * ``uploads`` - Uploaded videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/feed"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("offset", offset),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Type33OrStr | None]("type", type_),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Activity31Connection],
            error_mapper=get_feed_error_mapper,
            request_options=request_options,
        )

    def get_feed_alt1(
        self,
        *,
        offset: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        type_: Type33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Activity31Connection, GetFeedAlt1ErrorBody]:
        """This method returns every video in the authenticated user's feed.

        Args:
            offset: The pagination offset. We recommend that you use the pagination links in the feed response instead
                of working with this value directly. For more details, see our `pagination documentation
                <https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter>`__.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            type_: The feed type. Option descriptions: * ``appears`` - Videos in which the user appears. *
                ``category_featured`` - Featured videos. * ``channel`` - Channel videos. * ``facebook_feed`` - Videos
                from the user's Facebook feed. * ``following`` - Videos from accounts that the user follows. * ``group``
                - Group videos. * ``likes`` - Liked videos. * ``ondemand_publish`` - On Demand videos. * ``share`` -
                Shared videos. * ``tagged_with`` - Tagged videos. * ``twitter_timeline`` - Videos from the user's
                Twitter timeline. * ``uploads`` - Uploaded videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/feed"),
            query_params=[
                param[str | None]("offset", offset),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Type33OrStr | None]("type", type_),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Activity31Connection],
            error_mapper=get_feed_alt1_error_mapper,
            request_options=request_options,
        )


class AsyncUsersFeedsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_feed(
        self,
        user_id: float,
        *,
        offset: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        type_: Type33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Activity31Connection, GetFeedErrorBody]:
        """This method returns every video in the authenticated user's feed.

        Args:
            user_id: The ID of the user.
            offset: The pagination offset. We recommend that you use the pagination links in the feed response instead
                of working with this value directly. For more details, see our `pagination documentation
                <https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter>`__.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            type_: The feed type. Option descriptions: * ``appears`` - Videos in which the user appears. *
                ``category_featured`` - Featured videos. * ``channel`` - Channel videos. * ``facebook_feed`` - Videos
                from the user's Facebook feed. * ``following`` - Videos from accounts that the user follows. * ``group``
                - Group videos. * ``likes`` - Liked videos. * ``ondemand_publish`` - On Demand videos. * ``share`` -
                Shared videos. * ``tagged_with`` - Tagged videos. * ``twitter_timeline`` - Videos from the user's
                Twitter timeline. * ``uploads`` - Uploaded videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/feed"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[str | None]("offset", offset),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Type33OrStr | None]("type", type_),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Activity31Connection],
            error_mapper=get_feed_error_mapper,
            request_options=request_options,
        )

    async def get_feed_alt1(
        self,
        *,
        offset: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        type_: Type33OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Activity31Connection, GetFeedAlt1ErrorBody]:
        """This method returns every video in the authenticated user's feed.

        Args:
            offset: The pagination offset. We recommend that you use the pagination links in the feed response instead
                of working with this value directly. For more details, see our `pagination documentation
                <https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter>`__.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            type_: The feed type. Option descriptions: * ``appears`` - Videos in which the user appears. *
                ``category_featured`` - Featured videos. * ``channel`` - Channel videos. * ``facebook_feed`` - Videos
                from the user's Facebook feed. * ``following`` - Videos from accounts that the user follows. * ``group``
                - Group videos. * ``likes`` - Liked videos. * ``ondemand_publish`` - On Demand videos. * ``share`` -
                Shared videos. * ``tagged_with`` - Tagged videos. * ``twitter_timeline`` - Videos from the user's
                Twitter timeline. * ``uploads`` - Uploaded videos.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/feed"),
            query_params=[
                param[str | None]("offset", offset),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Type33OrStr | None]("type", type_),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[Activity31Connection],
            error_mapper=get_feed_alt1_error_mapper,
            request_options=request_options,
        )
