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
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..models.team_access_logsschema import TeamAccessLogsschema
from ..models.team_infoschema import TeamInfoschema
from ..models.team_integration_logsschema import TeamIntegrationLogsschema
from ..models.team_profile_getsuccessschema import TeamProfileGetsuccessschema
from ..server.server import Server


class TeamApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TeamApiWithRawResponse(client, server, auth)

    def team_access_logs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        before: str | None = None,
        count: str | None = None,
        page: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamAccessLogsschema:
        """Gets the access logs for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            before: End of time range of logs to include in results (inclusive).
            count: Value sent with the request.
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            This response demonstrates pagination and two access log entries.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.team_access_logs(
            token, content_type, before=before, count=count, page=page, request_options=request_options
        ).unwrap()

    def team_billable_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Gets billable users information for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            user: A user to retrieve the billable information for. Defaults to all users.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.team_billable_info(
            token, content_type, user=user, request_options=request_options
        ).unwrap()

    def team_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamInfoschema:
        """Gets information about the current team.

        Args:
            token: Authentication token. Requires scope: ``team:read``
            content_type: Value sent with the request.
            team: Team to get info on, if omitted, will return information about the current team. Will only return team
                that the authenticated token is allowed to see through external shared channels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.team_info(
            token, content_type, team=team, request_options=request_options
        ).unwrap()

    def team_integration_logs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        change_type: str | None = None,
        count: str | None = None,
        page: str | None = None,
        service_id: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamIntegrationLogsschema:
        """Gets the integration logs for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            app_id: Filter logs to this Slack app. Defaults to all logs.
            change_type: Filter logs with this change type. Defaults to all logs.
            count: Value sent with the request.
            page: Value sent with the request.
            service_id: Filter logs to this service. Defaults to all logs.
            user: Filter logs generated by this user’s actions. Defaults to all logs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.team_integration_logs(
            token,
            content_type,
            app_id=app_id,
            change_type=change_type,
            count=count,
            page=page,
            service_id=service_id,
            user=user,
            request_options=request_options,
        ).unwrap()

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
    def with_raw_response(self) -> TeamApiWithRawResponse:
        return self._with_raw_response


class AsyncTeamApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTeamApiWithRawResponse(client, server, auth)

    async def team_access_logs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        before: str | None = None,
        count: str | None = None,
        page: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamAccessLogsschema:
        """Gets the access logs for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            before: End of time range of logs to include in results (inclusive).
            count: Value sent with the request.
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            This response demonstrates pagination and two access log entries.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.team_access_logs(
                token, content_type, before=before, count=count, page=page, request_options=request_options
            )
        ).unwrap()

    async def team_billable_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Gets billable users information for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            user: A user to retrieve the billable information for. Defaults to all users.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.team_billable_info(
                token, content_type, user=user, request_options=request_options
            )
        ).unwrap()

    async def team_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamInfoschema:
        """Gets information about the current team.

        Args:
            token: Authentication token. Requires scope: ``team:read``
            content_type: Value sent with the request.
            team: Team to get info on, if omitted, will return information about the current team. Will only return team
                that the authenticated token is allowed to see through external shared channels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.team_info(token, content_type, team=team, request_options=request_options)
        ).unwrap()

    async def team_integration_logs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        change_type: str | None = None,
        count: str | None = None,
        page: str | None = None,
        service_id: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamIntegrationLogsschema:
        """Gets the integration logs for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            app_id: Filter logs to this Slack app. Defaults to all logs.
            change_type: Filter logs with this change type. Defaults to all logs.
            count: Value sent with the request.
            page: Value sent with the request.
            service_id: Filter logs to this service. Defaults to all logs.
            user: Filter logs generated by this user’s actions. Defaults to all logs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.team_integration_logs(
                token,
                content_type,
                app_id=app_id,
                change_type=change_type,
                count=count,
                page=page,
                service_id=service_id,
                user=user,
                request_options=request_options,
            )
        ).unwrap()

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
    def with_raw_response(self) -> AsyncTeamApiWithRawResponse:
        return self._with_raw_response


class TeamApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def team_access_logs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        before: str | None = None,
        count: str | None = None,
        page: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamAccessLogsschema, RawError]:
        """Gets the access logs for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            before: End of time range of logs to include in results (inclusive).
            count: Value sent with the request.
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.accessLogs"),
            query_params=[
                param[str]("token", token),
                param[str | None]("before", before),
                param[str | None]("count", count),
                param[str | None]("page", page),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[TeamAccessLogsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def team_billable_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Gets billable users information for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            user: A user to retrieve the billable information for. Defaults to all users.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.billableInfo"),
            query_params=[param[str]("token", token), param[str | None]("user", user)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def team_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamInfoschema, RawError]:
        """Gets information about the current team.

        Args:
            token: Authentication token. Requires scope: ``team:read``
            content_type: Value sent with the request.
            team: Team to get info on, if omitted, will return information about the current team. Will only return team
                that the authenticated token is allowed to see through external shared channels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.info"),
            query_params=[param[str]("token", token), param[str | None]("team", team)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[TeamInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def team_integration_logs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        change_type: str | None = None,
        count: str | None = None,
        page: str | None = None,
        service_id: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamIntegrationLogsschema, RawError]:
        """Gets the integration logs for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            app_id: Filter logs to this Slack app. Defaults to all logs.
            change_type: Filter logs with this change type. Defaults to all logs.
            count: Value sent with the request.
            page: Value sent with the request.
            service_id: Filter logs to this service. Defaults to all logs.
            user: Filter logs generated by this user’s actions. Defaults to all logs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.integrationLogs"),
            query_params=[
                param[str]("token", token),
                param[str | None]("app_id", app_id),
                param[str | None]("change_type", change_type),
                param[str | None]("count", count),
                param[str | None]("page", page),
                param[str | None]("service_id", service_id),
                param[str | None]("user", user),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[TeamIntegrationLogsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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


class AsyncTeamApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def team_access_logs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        before: str | None = None,
        count: str | None = None,
        page: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamAccessLogsschema, RawError]:
        """Gets the access logs for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            before: End of time range of logs to include in results (inclusive).
            count: Value sent with the request.
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.accessLogs"),
            query_params=[
                param[str]("token", token),
                param[str | None]("before", before),
                param[str | None]("count", count),
                param[str | None]("page", page),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[TeamAccessLogsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def team_billable_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Gets billable users information for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            user: A user to retrieve the billable information for. Defaults to all users.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.billableInfo"),
            query_params=[param[str]("token", token), param[str | None]("user", user)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def team_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        team: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamInfoschema, RawError]:
        """Gets information about the current team.

        Args:
            token: Authentication token. Requires scope: ``team:read``
            content_type: Value sent with the request.
            team: Team to get info on, if omitted, will return information about the current team. Will only return team
                that the authenticated token is allowed to see through external shared channels
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.info"),
            query_params=[param[str]("token", token), param[str | None]("team", team)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[TeamInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def team_integration_logs(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        change_type: str | None = None,
        count: str | None = None,
        page: str | None = None,
        service_id: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamIntegrationLogsschema, RawError]:
        """Gets the integration logs for the current team.

        Args:
            token: Authentication token. Requires scope: ``admin``
            content_type: Value sent with the request.
            app_id: Filter logs to this Slack app. Defaults to all logs.
            change_type: Filter logs with this change type. Defaults to all logs.
            count: Value sent with the request.
            page: Value sent with the request.
            service_id: Filter logs to this service. Defaults to all logs.
            user: Filter logs generated by this user’s actions. Defaults to all logs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team.integrationLogs"),
            query_params=[
                param[str]("token", token),
                param[str | None]("app_id", app_id),
                param[str | None]("change_type", change_type),
                param[str | None]("count", count),
                param[str | None]("page", page),
                param[str | None]("service_id", service_id),
                param[str | None]("user", user),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[TeamIntegrationLogsschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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
