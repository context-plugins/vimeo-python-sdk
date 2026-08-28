from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class AdminApps:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminAppsWithRawResponse(client, server, auth)

    def admin_apps_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Approve an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to approve.
            request_id: The id of the request to approve.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_apps_approve(
            token, content_type, app_id=app_id, request_id=request_id, team_id=team_id, request_options=request_options
        ).unwrap()

    def admin_apps_restrict(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Restrict an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to restrict.
            request_id: The id of the request to restrict.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_apps_restrict(
            token, content_type, app_id=app_id, request_id=request_id, team_id=team_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AdminAppsWithRawResponse:
        return self._with_raw_response


class AsyncAdminApps:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminAppsWithRawResponse(client, server, auth)

    async def admin_apps_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Approve an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to approve.
            request_id: The id of the request to approve.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_apps_approve(
                token,
                content_type,
                app_id=app_id,
                request_id=request_id,
                team_id=team_id,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_apps_restrict(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Restrict an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to restrict.
            request_id: The id of the request to restrict.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_apps_restrict(
                token,
                content_type,
                app_id=app_id,
                request_id=request_id,
                team_id=team_id,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAdminAppsWithRawResponse:
        return self._with_raw_response


class AdminAppsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def admin_apps_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Approve an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to approve.
            request_id: The id of the request to approve.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.apps.approve"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("app_id", app_id),
                    param[str | None]("request_id", request_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_apps_restrict(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Restrict an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to restrict.
            request_id: The id of the request to restrict.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.apps.restrict"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("app_id", app_id),
                    param[str | None]("request_id", request_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAdminAppsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def admin_apps_approve(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Approve an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to approve.
            request_id: The id of the request to approve.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.apps.approve"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("app_id", app_id),
                    param[str | None]("request_id", request_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_apps_restrict(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        app_id: str | None = None,
        request_id: str | None = None,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Restrict an app for installation on a workspace.

        Args:
            token: Authentication token. Requires scope: ``admin.apps:write``
            content_type: Value sent with the request.
            app_id: The id of the app to restrict.
            request_id: The id of the request to restrict.
            team_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin.apps.restrict"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("app_id", app_id),
                    param[str | None]("request_id", request_id),
                    param[str | None]("team_id", team_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
