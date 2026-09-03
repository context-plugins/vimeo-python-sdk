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
from ..errors.check_if_user_is_following_alt1_error import (
    CheckIfUserIsFollowingAlt1ErrorBody,
    check_if_user_is_following_alt1_error_mapper,
)
from ..errors.check_if_user_is_following_error import (
    CheckIfUserIsFollowingErrorBody,
    check_if_user_is_following_error_mapper,
)
from ..errors.follow_user_alt1_error import FollowUserAlt1ErrorBody, follow_user_alt1_error_mapper
from ..errors.follow_user_error import FollowUserErrorBody, follow_user_error_mapper
from ..errors.follow_users_alt1_error import FollowUsersAlt1ErrorBody, follow_users_alt1_error_mapper
from ..errors.follow_users_error import FollowUsersErrorBody, follow_users_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter13 import Filter13OrStr
from ..models.enums.sort8 import Sort8OrStr
from ..models.me_following_request import MeFollowingRequest, MeFollowingRequestDict
from ..models.user_connection import UserConnection
from ..models.users_following_request import UsersFollowingRequest, UsersFollowingRequestDict
from ..server.server import Server


class UsersFollowers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersFollowersWithRawResponse(client, server, auth)

    def check_if_user_is_following(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user is a follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authenticated user follows the specified user.

        Raises:
            ApiError: The authenticated user doesn't follow the specified user. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.check_if_user_is_following(
            follow_user_id, user_id, request_options=request_options
        ).unwrap()

    def check_if_user_is_following_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user is a follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authenticated user follows the specified user.

        Raises:
            ApiError: The authenticated user doesn't follow the specified user. ``error`` is ``LegacyError |
                RawError``."""
        return self._with_raw_response.check_if_user_is_following_alt1(
            follow_user_id, request_options=request_options
        ).unwrap()

    def follow_user(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to become the follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was followed.

        Raises:
            ApiError: * The authenticated user can't follow other users. * Error code 3438: The authenticated user can't
                follow other users because an email verification check hasn't been completed. ``error`` is ``LegacyError
                | RawError``."""
        return self._with_raw_response.follow_user(follow_user_id, user_id, request_options=request_options).unwrap()

    def follow_user_alt1(self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method causes the authenticated user to become the follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was followed.

        Raises:
            ApiError: * The authenticated user can't follow other users. * Error code 3438: The authenticated user can't
                follow other users because an email verification check hasn't been completed. ``error`` is ``LegacyError
                | RawError``."""
        return self._with_raw_response.follow_user_alt1(follow_user_id, request_options=request_options).unwrap()

    def follow_users(
        self,
        user_id: float,
        body: UsersFollowingRequest | UsersFollowingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method causes the authenticated user to become a follower of multiple users. In the body of the request,
        specify the list of users to follow as an array of URIs, where ``user01_id``, ``user02_id``, ``user03_id``, and
        so on, are the user IDs of the users in question:

        ```
        {
         [
             {"uri" : "/users/{user01_id}"},
             {"uri" : "/users/{user02_id}"},
             {"uri" : "/users/{user03_id}"}
         ]
        }
        ```

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were followed.

        Raises:
            ApiError: * Error code 2205: The request body is empty, the users array is invalid, or the list of users
                doesn't contain URIs. * Error code 2900: A user in the list doesn't exist. * Error code 2901: The list
                contains more than 100 users. Error code 8000: The user access token is invalid. * Error code 3417: The
                authenticated user can't follow other users. * Error code 3438: The authenticated user can't follow
                other users because an email verification check hasn't been completed. Error code 9006: The
                authenticated user is rate-limited from following other users. Error code 4005: An unexpected error
                occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.follow_users(user_id, body, request_options=request_options).unwrap()

    def follow_users_alt1(
        self, body: MeFollowingRequest | MeFollowingRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to become a follower of multiple users. In the body of the request,
        specify the list of users to follow as an array of URIs, where ``user01_id``, ``user02_id``, ``user03_id``, and
        so on, are the user IDs of the users in question:

        ```
        {
         [
             {"uri" : "/users/{user01_id}"},
             {"uri" : "/users/{user02_id}"},
             {"uri" : "/users/{user03_id}"}
         ]
        }
        ```

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were followed.

        Raises:
            ApiError: * Error code 2205: The request body is empty, the users array is invalid, or the list of users
                doesn't contain URIs. * Error code 2900: A user in the list doesn't exist. * Error code 2901: The list
                contains more than 100 users. Error code 8000: The user access token is invalid. * Error code 3417: The
                authenticated user can't follow other users. * Error code 3438: The authenticated user can't follow
                other users because an email verification check hasn't been completed. Error code 9006: The
                authenticated user is rate-limited from following other users. Error code 4005: An unexpected error
                occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.follow_users_alt1(body, request_options=request_options).unwrap()

    def get_followers(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every follower of the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user's followers were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_followers(
            user_id,
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_followers_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every follower of the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user's followers were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_followers_alt1(
            direction=direction, page=page, per_page=per_page, query=query, sort=sort, request_options=request_options
        ).unwrap()

    def get_user_following(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter13OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who is followed by the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``online`` - Return users who
                are currently online.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The followed users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_following(
            user_id,
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def get_user_following_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter13OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who is followed by the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``online`` - Return users who
                are currently online.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The followed users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_following_alt1(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            request_options=request_options,
        ).unwrap()

    def unfollow_user(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to stop following another user.

        Args:
            follow_user_id: The ID of the user to unfollow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was unfollowed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.unfollow_user(follow_user_id, user_id, request_options=request_options).unwrap()

    def unfollow_user_alt1(self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method causes the authenticated user to stop following another user.

        Args:
            follow_user_id: The ID of the user to unfollow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was unfollowed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.unfollow_user_alt1(follow_user_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> UsersFollowersWithRawResponse:
        return self._with_raw_response


class AsyncUsersFollowers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersFollowersWithRawResponse(client, server, auth)

    async def check_if_user_is_following(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user is a follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authenticated user follows the specified user.

        Raises:
            ApiError: The authenticated user doesn't follow the specified user. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.check_if_user_is_following(
                follow_user_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def check_if_user_is_following_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method determines whether the authenticated user is a follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The authenticated user follows the specified user.

        Raises:
            ApiError: The authenticated user doesn't follow the specified user. ``error`` is ``LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.check_if_user_is_following_alt1(
                follow_user_id, request_options=request_options
            )
        ).unwrap()

    async def follow_user(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to become the follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was followed.

        Raises:
            ApiError: * The authenticated user can't follow other users. * Error code 3438: The authenticated user can't
                follow other users because an email verification check hasn't been completed. ``error`` is ``LegacyError
                | RawError``."""
        return (
            await self._with_raw_response.follow_user(follow_user_id, user_id, request_options=request_options)
        ).unwrap()

    async def follow_user_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to become the follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was followed.

        Raises:
            ApiError: * The authenticated user can't follow other users. * Error code 3438: The authenticated user can't
                follow other users because an email verification check hasn't been completed. ``error`` is ``LegacyError
                | RawError``."""
        return (
            await self._with_raw_response.follow_user_alt1(follow_user_id, request_options=request_options)
        ).unwrap()

    async def follow_users(
        self,
        user_id: float,
        body: UsersFollowingRequest | UsersFollowingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method causes the authenticated user to become a follower of multiple users. In the body of the request,
        specify the list of users to follow as an array of URIs, where ``user01_id``, ``user02_id``, ``user03_id``, and
        so on, are the user IDs of the users in question:

        ```
        {
         [
             {"uri" : "/users/{user01_id}"},
             {"uri" : "/users/{user02_id}"},
             {"uri" : "/users/{user03_id}"}
         ]
        }
        ```

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were followed.

        Raises:
            ApiError: * Error code 2205: The request body is empty, the users array is invalid, or the list of users
                doesn't contain URIs. * Error code 2900: A user in the list doesn't exist. * Error code 2901: The list
                contains more than 100 users. Error code 8000: The user access token is invalid. * Error code 3417: The
                authenticated user can't follow other users. * Error code 3438: The authenticated user can't follow
                other users because an email verification check hasn't been completed. Error code 9006: The
                authenticated user is rate-limited from following other users. Error code 4005: An unexpected error
                occurred. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.follow_users(user_id, body, request_options=request_options)).unwrap()

    async def follow_users_alt1(
        self, body: MeFollowingRequest | MeFollowingRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to become a follower of multiple users. In the body of the request,
        specify the list of users to follow as an array of URIs, where ``user01_id``, ``user02_id``, ``user03_id``, and
        so on, are the user IDs of the users in question:

        ```
        {
         [
             {"uri" : "/users/{user01_id}"},
             {"uri" : "/users/{user02_id}"},
             {"uri" : "/users/{user03_id}"}
         ]
        }
        ```

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The users were followed.

        Raises:
            ApiError: * Error code 2205: The request body is empty, the users array is invalid, or the list of users
                doesn't contain URIs. * Error code 2900: A user in the list doesn't exist. * Error code 2901: The list
                contains more than 100 users. Error code 8000: The user access token is invalid. * Error code 3417: The
                authenticated user can't follow other users. * Error code 3438: The authenticated user can't follow
                other users because an email verification check hasn't been completed. Error code 9006: The
                authenticated user is rate-limited from following other users. Error code 4005: An unexpected error
                occurred. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.follow_users_alt1(body, request_options=request_options)).unwrap()

    async def get_followers(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every follower of the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user's followers were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_followers(
                user_id,
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_followers_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every follower of the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user's followers were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_followers_alt1(
                direction=direction,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_user_following(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter13OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who is followed by the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``online`` - Return users who
                are currently online.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The followed users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_following(
                user_id,
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def get_user_following_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter13OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserConnection:
        """This method returns every user who is followed by the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``online`` - Return users who
                are currently online.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by date followed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The followed users were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_following_alt1(
                direction=direction,
                filter=filter,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    async def unfollow_user(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to stop following another user.

        Args:
            follow_user_id: The ID of the user to unfollow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was unfollowed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.unfollow_user(follow_user_id, user_id, request_options=request_options)
        ).unwrap()

    async def unfollow_user_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method causes the authenticated user to stop following another user.

        Args:
            follow_user_id: The ID of the user to unfollow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was unfollowed.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.unfollow_user_alt1(follow_user_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersFollowersWithRawResponse:
        return self._with_raw_response


class UsersFollowersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_if_user_is_following(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserIsFollowingErrorBody]:
        """This method determines whether the authenticated user is a follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_is_following_error_mapper,
            request_options=request_options,
        )

    def check_if_user_is_following_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserIsFollowingAlt1ErrorBody]:
        """This method determines whether the authenticated user is a follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_is_following_alt1_error_mapper,
            request_options=request_options,
        )

    def follow_user(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FollowUserErrorBody]:
        """This method causes the authenticated user to become the follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=follow_user_error_mapper,
            request_options=request_options,
        )

    def follow_user_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FollowUserAlt1ErrorBody]:
        """This method causes the authenticated user to become the follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=follow_user_alt1_error_mapper,
            request_options=request_options,
        )

    def follow_users(
        self,
        user_id: float,
        body: UsersFollowingRequest | UsersFollowingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, FollowUsersErrorBody]:
        """This method causes the authenticated user to become a follower of multiple users. In the body of the request,
        specify the list of users to follow as an array of URIs, where ``user01_id``, ``user02_id``, ``user03_id``, and
        so on, are the user IDs of the users in question:

        ```
        {
         [
             {"uri" : "/users/{user01_id}"},
             {"uri" : "/users/{user02_id}"},
             {"uri" : "/users/{user03_id}"}
         ]
        }
        ```

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/following"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersFollowingRequest | UsersFollowingRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=follow_users_error_mapper,
            request_options=request_options,
        )

    def follow_users_alt1(
        self, body: MeFollowingRequest | MeFollowingRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FollowUsersAlt1ErrorBody]:
        """This method causes the authenticated user to become a follower of multiple users. In the body of the request,
        specify the list of users to follow as an array of URIs, where ``user01_id``, ``user02_id``, ``user03_id``, and
        so on, are the user IDs of the users in question:

        ```
        {
         [
             {"uri" : "/users/{user01_id}"},
             {"uri" : "/users/{user02_id}"},
             {"uri" : "/users/{user03_id}"}
         ]
        }
        ```

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/following"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeFollowingRequest | MeFollowingRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=follow_users_alt1_error_mapper,
            request_options=request_options,
        )

    def get_followers(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every follower of the authenticated user.

        Args:
            user_id: The ID of the user.
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
            url_template=self._server.default("/users/{user_id}/followers"),
            path_params=[param[float]("user_id", user_id)],
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

    def get_followers_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every follower of the authenticated user.

        Args:
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
            url_template=self._server.default("/me/followers"),
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

    def get_user_following(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter13OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every user who is followed by the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``online`` - Return users who
                are currently online.
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
            url_template=self._server.default("/users/{user_id}/following"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter13OrStr | None]("filter", filter),
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

    def get_user_following_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter13OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every user who is followed by the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``online`` - Return users who
                are currently online.
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
            url_template=self._server.default("/me/following"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter13OrStr | None]("filter", filter),
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

    def unfollow_user(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to stop following another user.

        Args:
            follow_user_id: The ID of the user to unfollow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def unfollow_user_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to stop following another user.

        Args:
            follow_user_id: The ID of the user to unfollow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUsersFollowersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_if_user_is_following(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserIsFollowingErrorBody]:
        """This method determines whether the authenticated user is a follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_is_following_error_mapper,
            request_options=request_options,
        )

    async def check_if_user_is_following_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CheckIfUserIsFollowingAlt1ErrorBody]:
        """This method determines whether the authenticated user is a follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=check_if_user_is_following_alt1_error_mapper,
            request_options=request_options,
        )

    async def follow_user(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FollowUserErrorBody]:
        """This method causes the authenticated user to become the follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=follow_user_error_mapper,
            request_options=request_options,
        )

    async def follow_user_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FollowUserAlt1ErrorBody]:
        """This method causes the authenticated user to become the follower of the specified user.

        Args:
            follow_user_id: The ID of the user to follow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=follow_user_alt1_error_mapper,
            request_options=request_options,
        )

    async def follow_users(
        self,
        user_id: float,
        body: UsersFollowingRequest | UsersFollowingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, FollowUsersErrorBody]:
        """This method causes the authenticated user to become a follower of multiple users. In the body of the request,
        specify the list of users to follow as an array of URIs, where ``user01_id``, ``user02_id``, ``user03_id``, and
        so on, are the user IDs of the users in question:

        ```
        {
         [
             {"uri" : "/users/{user01_id}"},
             {"uri" : "/users/{user02_id}"},
             {"uri" : "/users/{user03_id}"}
         ]
        }
        ```

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/following"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersFollowingRequest | UsersFollowingRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=follow_users_error_mapper,
            request_options=request_options,
        )

    async def follow_users_alt1(
        self, body: MeFollowingRequest | MeFollowingRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FollowUsersAlt1ErrorBody]:
        """This method causes the authenticated user to become a follower of multiple users. In the body of the request,
        specify the list of users to follow as an array of URIs, where ``user01_id``, ``user02_id``, ``user03_id``, and
        so on, are the user IDs of the users in question:

        ```
        {
         [
             {"uri" : "/users/{user01_id}"},
             {"uri" : "/users/{user02_id}"},
             {"uri" : "/users/{user03_id}"}
         ]
        }
        ```

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/following"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeFollowingRequest | MeFollowingRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=follow_users_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_followers(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every follower of the authenticated user.

        Args:
            user_id: The ID of the user.
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
            url_template=self._server.default("/users/{user_id}/followers"),
            path_params=[param[float]("user_id", user_id)],
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

    async def get_followers_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every follower of the authenticated user.

        Args:
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
            url_template=self._server.default("/me/followers"),
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

    async def get_user_following(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter13OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every user who is followed by the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``online`` - Return users who
                are currently online.
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
            url_template=self._server.default("/users/{user_id}/following"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter13OrStr | None]("filter", filter),
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

    async def get_user_following_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter: Filter13OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserConnection, RawError]:
        """This method returns every user who is followed by the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter: The attribute by which to filter the results. Option descriptions: * ``online`` - Return users who
                are currently online.
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
            url_template=self._server.default("/me/following"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter13OrStr | None]("filter", filter),
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

    async def unfollow_user(
        self, follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to stop following another user.

        Args:
            follow_user_id: The ID of the user to unfollow.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def unfollow_user_alt1(
        self, follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method causes the authenticated user to stop following another user.

        Args:
            follow_user_id: The ID of the user to unfollow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/following/{follow_user_id}"),
            path_params=[param[float]("follow_user_id", follow_user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
