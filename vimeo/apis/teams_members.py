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
    param,
    raw_error_response,
)
from ..server.server import Server


class TeamsMembers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TeamsMembersWithRawResponse(client, server, auth)

    def get_team_information(self, code: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns information about the membership of the specified team. Usage is currently limited to the
        team join forms.

        Args:
            code: The code corresponding to the desired team. This value appears under ``TeamUser`` > ``code``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_team_information(code, request_options=request_options).unwrap()

    def get_team_information2(
        self, team_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns information about the membership of the specified team. Usage is currently limited to the
        team join forms.

        Args:
            team_user_id: The ID of the team user.
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_team_information2(
            team_user_id, user_id, request_options=request_options
        ).unwrap()

    def get_team_role_information(self, user_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns information about the authenticated user's role on the specified team owner's team.

        Args:
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_team_role_information(user_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TeamsMembersWithRawResponse:
        return self._with_raw_response


class AsyncTeamsMembers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTeamsMembersWithRawResponse(client, server, auth)

    async def get_team_information(self, code: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns information about the membership of the specified team. Usage is currently limited to the
        team join forms.

        Args:
            code: The code corresponding to the desired team. This value appears under ``TeamUser`` > ``code``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_team_information(code, request_options=request_options)).unwrap()

    async def get_team_information2(
        self, team_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns information about the membership of the specified team. Usage is currently limited to the
        team join forms.

        Args:
            team_user_id: The ID of the team user.
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_team_information2(team_user_id, user_id, request_options=request_options)
        ).unwrap()

    async def get_team_role_information(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns information about the authenticated user's role on the specified team owner's team.

        Args:
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_team_role_information(user_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTeamsMembersWithRawResponse:
        return self._with_raw_response


class TeamsMembersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_team_information(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns information about the membership of the specified team. Usage is currently limited to the
        team join forms.

        Args:
            code: The code corresponding to the desired team. This value appears under ``TeamUser`` > ``code``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/teammembers/{code}"),
            path_params=[param[str]("code", code)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_team_information2(
        self, team_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns information about the membership of the specified team. Usage is currently limited to the
        team join forms.

        Args:
            team_user_id: The ID of the team user.
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/team_users/{team_user_id}"),
            path_params=[param[float]("team_user_id", team_user_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_team_role_information(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns information about the authenticated user's role on the specified team owner's team.

        Args:
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/team/role"),
            path_params=[param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTeamsMembersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_team_information(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns information about the membership of the specified team. Usage is currently limited to the
        team join forms.

        Args:
            code: The code corresponding to the desired team. This value appears under ``TeamUser`` > ``code``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/teammembers/{code}"),
            path_params=[param[str]("code", code)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_team_information2(
        self, team_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns information about the membership of the specified team. Usage is currently limited to the
        team join forms.

        Args:
            team_user_id: The ID of the team user.
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/team_users/{team_user_id}"),
            path_params=[param[float]("team_user_id", team_user_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_team_role_information(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """This method returns information about the authenticated user's role on the specified team owner's team.

        Args:
            user_id: The ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/team/role"),
            path_params=[param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
