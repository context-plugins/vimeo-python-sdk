from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.content_type import ContentTypeOrStr
from ..models.team_profile_getsuccessschema import TeamProfileGetsuccessschema
from ..server.server import Server


class TeamProfile:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TeamProfileWithRawResponse(client, server, auth)

    def team_profile_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        visibility: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamProfileGetsuccessschema:
        """Retrieve a team's profile.

        Args:
            token: Authentication token. Requires scope: ``users.profile:read``
            content_type: Value sent with the request.
            visibility: Filter by visibility.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.team_profile_get(
            token, content_type, visibility=visibility, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TeamProfileWithRawResponse:
        return self._with_raw_response


class AsyncTeamProfile:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTeamProfileWithRawResponse(client, server, auth)

    async def team_profile_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        visibility: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamProfileGetsuccessschema:
        """Retrieve a team's profile.

        Args:
            token: Authentication token. Requires scope: ``users.profile:read``
            content_type: Value sent with the request.
            visibility: Filter by visibility.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.team_profile_get(
                token, content_type, visibility=visibility, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTeamProfileWithRawResponse:
        return self._with_raw_response


class TeamProfileWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def team_profile_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        visibility: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamProfileGetsuccessschema, RawError]:
        """Retrieve a team's profile.

        Args:
            token: Authentication token. Requires scope: ``users.profile:read``
            content_type: Value sent with the request.
            visibility: Filter by visibility.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.profile.get"),
            query_params=[param[str]("token", token), param[str | None]("visibility", visibility)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[TeamProfileGetsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTeamProfileWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def team_profile_get(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        visibility: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamProfileGetsuccessschema, RawError]:
        """Retrieve a team's profile.

        Args:
            token: Authentication token. Requires scope: ``users.profile:read``
            content_type: Value sent with the request.
            visibility: Filter by visibility.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.profile.get"),
            query_params=[param[str]("token", token), param[str | None]("visibility", visibility)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[TeamProfileGetsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
