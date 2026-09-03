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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.edit_user_alt1_error import EditUserAlt1ErrorBody, edit_user_alt1_error_mapper
from ..errors.edit_user_error import EditUserErrorBody, edit_user_error_mapper
from ..models.me_request import MeRequest, MeRequestDict
from ..models.user import User
from ..models.users_request import UsersRequest, UsersRequestDict
from ..server.server import Server


class UsersEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersEssentialsWithRawResponse(client, server, auth)

    def edit_user(
        self,
        user_id: float,
        *,
        body: UsersRequest | UsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> User:
        """This method edits the Vimeo account of the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user's Vimeo account was edited.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.edit_user(user_id, body=body, request_options=request_options).unwrap()

    def edit_user_alt1(
        self, *, body: MeRequest | MeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """This method edits the Vimeo account of the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user's Vimeo account was edited.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.edit_user_alt1(body=body, request_options=request_options).unwrap()

    def get_user(self, user_id: float, *, request_options: RequestOptionsOrDict | None = None) -> User:
        """This method returns the authenticated user.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user(user_id, request_options=request_options).unwrap()

    def get_user_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> User:
        """This method returns the authenticated user.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_alt1(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> UsersEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncUsersEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersEssentialsWithRawResponse(client, server, auth)

    async def edit_user(
        self,
        user_id: float,
        *,
        body: UsersRequest | UsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> User:
        """This method edits the Vimeo account of the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user's Vimeo account was edited.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.edit_user(user_id, body=body, request_options=request_options)).unwrap()

    async def edit_user_alt1(
        self, *, body: MeRequest | MeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """This method edits the Vimeo account of the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user's Vimeo account was edited.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.edit_user_alt1(body=body, request_options=request_options)).unwrap()

    async def get_user(self, user_id: float, *, request_options: RequestOptionsOrDict | None = None) -> User:
        """This method returns the authenticated user.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_user(user_id, request_options=request_options)).unwrap()

    async def get_user_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> User:
        """This method returns the authenticated user.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The user was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_user_alt1(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersEssentialsWithRawResponse:
        return self._with_raw_response


class UsersEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def edit_user(
        self,
        user_id: float,
        *,
        body: UsersRequest | UsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[User, EditUserErrorBody]:
        """This method edits the Vimeo account of the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersRequest | UsersRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=edit_user_error_mapper,
            request_options=request_options,
        )

    def edit_user_alt1(
        self, *, body: MeRequest | MeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, EditUserAlt1ErrorBody]:
        """This method edits the Vimeo account of the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeRequest | MeRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=edit_user_alt1_error_mapper,
            request_options=request_options,
        )

    def get_user(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, RawError]:
        """This method returns the authenticated user.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}"),
            path_params=[param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_user_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[User, RawError]:
        """This method returns the authenticated user.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUsersEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def edit_user(
        self,
        user_id: float,
        *,
        body: UsersRequest | UsersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[User, EditUserErrorBody]:
        """This method edits the Vimeo account of the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersRequest | UsersRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=edit_user_error_mapper,
            request_options=request_options,
        )

    async def edit_user_alt1(
        self, *, body: MeRequest | MeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, EditUserAlt1ErrorBody]:
        """This method edits the Vimeo account of the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeRequest | MeRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=edit_user_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_user(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, RawError]:
        """This method returns the authenticated user.

        Args:
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}"),
            path_params=[param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_user_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[User, RawError]:
        """This method returns the authenticated user.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[User],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
