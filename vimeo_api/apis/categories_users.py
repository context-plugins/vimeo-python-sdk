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
from ..errors.get_category_subscriptions_alt1_error import (
    GetCategorySubscriptionsAlt1ErrorBody,
    get_category_subscriptions_alt1_error_mapper,
)
from ..errors.get_category_subscriptions_error import (
    GetCategorySubscriptionsErrorBody,
    get_category_subscriptions_error_mapper,
)
from ..models.category_connection import CategoryConnection
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort24 import Sort24OrStr
from ..server.server import Server


class CategoriesUsers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CategoriesUsersWithRawResponse(client, server, auth)

    def check_if_user_subscribed_to_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user follows the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.check_if_user_subscribed_to_category(
            category, user_id, request_options=request_options
        ).unwrap()

    def check_if_user_subscribed_to_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user follows the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.check_if_user_subscribed_to_category_alt1(
            category, request_options=request_options
        ).unwrap()

    def get_category_subscriptions(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoryConnection:
        """This method returns every category that the authenticated user follows.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were returned.

        Raises:
            ApiError: Error code 3200: Only the authenticated user can access this information. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_category_subscriptions(
            user_id, direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
        ).unwrap()

    def get_category_subscriptions_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoryConnection:
        """This method returns every category that the authenticated user follows.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were returned.

        Raises:
            ApiError: Error code 3200: Only the authenticated user can access this information. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_category_subscriptions_alt1(
            direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
        ).unwrap()

    def subscribe_to_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to follow the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.subscribe_to_category(
            category, user_id, request_options=request_options
        ).unwrap()

    def subscribe_to_category_alt1(self, category: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method causes the authenticated user to follow the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.subscribe_to_category_alt1(category, request_options=request_options).unwrap()

    def unsubscribe_from_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to stop following the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user has stopped following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.unsubscribe_from_category(
            category, user_id, request_options=request_options
        ).unwrap()

    def unsubscribe_from_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to stop following the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user has stopped following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.unsubscribe_from_category_alt1(
            category, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CategoriesUsersWithRawResponse:
        return self._with_raw_response


class AsyncCategoriesUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCategoriesUsersWithRawResponse(client, server, auth)

    async def check_if_user_subscribed_to_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user follows the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.check_if_user_subscribed_to_category(
                category, user_id, request_options=request_options
            )
        ).unwrap()

    async def check_if_user_subscribed_to_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user follows the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.check_if_user_subscribed_to_category_alt1(
                category, request_options=request_options
            )
        ).unwrap()

    async def get_category_subscriptions(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoryConnection:
        """This method returns every category that the authenticated user follows.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were returned.

        Raises:
            ApiError: Error code 3200: Only the authenticated user can access this information. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_category_subscriptions(
                user_id, direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
            )
        ).unwrap()

    async def get_category_subscriptions_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoryConnection:
        """This method returns every category that the authenticated user follows.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The categories were returned.

        Raises:
            ApiError: Error code 3200: Only the authenticated user can access this information. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_category_subscriptions_alt1(
                direction=direction, page=page, per_page=per_page, sort=sort, request_options=request_options
            )
        ).unwrap()

    async def subscribe_to_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to follow the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.subscribe_to_category(category, user_id, request_options=request_options)
        ).unwrap()

    async def subscribe_to_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to follow the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user is following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.subscribe_to_category_alt1(category, request_options=request_options)
        ).unwrap()

    async def unsubscribe_from_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to stop following the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user has stopped following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.unsubscribe_from_category(category, user_id, request_options=request_options)
        ).unwrap()

    async def unsubscribe_from_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to stop following the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user has stopped following the category.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.unsubscribe_from_category_alt1(category, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCategoriesUsersWithRawResponse:
        return self._with_raw_response


class CategoriesUsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_if_user_subscribed_to_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method determines whether the authenticated user follows the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def check_if_user_subscribed_to_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method determines whether the authenticated user follows the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/categories/{category}"),
            path_params=[param[str]("category", category)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_category_subscriptions(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoryConnection, GetCategorySubscriptionsErrorBody]:
        """This method returns every category that the authenticated user follows.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/categories"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort24OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=get_category_subscriptions_error_mapper,
            request_options=request_options,
        )

    def get_category_subscriptions_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoryConnection, GetCategorySubscriptionsAlt1ErrorBody]:
        """This method returns every category that the authenticated user follows.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/categories"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort24OrStr | None]("sort", sort),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=get_category_subscriptions_alt1_error_mapper,
            request_options=request_options,
        )

    def subscribe_to_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to follow the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def subscribe_to_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to follow the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/categories/{category}"),
            path_params=[param[str]("category", category)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def unsubscribe_from_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to stop following the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def unsubscribe_from_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to stop following the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/categories/{category}"),
            path_params=[param[str]("category", category)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCategoriesUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_if_user_subscribed_to_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method determines whether the authenticated user follows the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def check_if_user_subscribed_to_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method determines whether the authenticated user follows the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/categories/{category}"),
            path_params=[param[str]("category", category)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_category_subscriptions(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoryConnection, GetCategorySubscriptionsErrorBody]:
        """This method returns every category that the authenticated user follows.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/categories"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort24OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=get_category_subscriptions_error_mapper,
            request_options=request_options,
        )

    async def get_category_subscriptions_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort24OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoryConnection, GetCategorySubscriptionsAlt1ErrorBody]:
        """This method returns every category that the authenticated user follows.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date. * ``name`` - Sort the results by name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/categories"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort24OrStr | None]("sort", sort),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[CategoryConnection],
            error_mapper=get_category_subscriptions_alt1_error_mapper,
            request_options=request_options,
        )

    async def subscribe_to_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to follow the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def subscribe_to_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to follow the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/categories/{category}"),
            path_params=[param[str]("category", category)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def unsubscribe_from_category(
        self, category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to stop following the specified category.

        Args:
            category: The name of the category.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/categories/{category}"),
            path_params=[param[str]("category", category), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def unsubscribe_from_category_alt1(
        self, category: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to stop following the specified category.

        Args:
            category: The name of the category.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/categories/{category}"),
            path_params=[param[str]("category", category)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
