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
from ..models.apps_permissions_infoschema import AppsPermissionsInfoschema
from ..models.apps_permissions_requestschema import AppsPermissionsRequestschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class AppsPermissions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AppsPermissionsWithRawResponse(client, server, auth)

    def apps_permissions_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AppsPermissionsInfoschema:
        """Returns list of permissions this app has on a team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``none``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.apps_permissions_info(
            content_type, token=token, request_options=request_options
        ).unwrap()

    def apps_permissions_request(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AppsPermissionsRequestschema:
        """Allows an app to request additional scopes

        Args:
            token: Authentication token. Requires scope: ``none``
            scopes: A comma separated list of scopes to request for
            trigger_id: Token used to trigger the permissions API
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.apps_permissions_request(
            token, scopes, trigger_id, content_type, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AppsPermissionsWithRawResponse:
        return self._with_raw_response


class AsyncAppsPermissions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAppsPermissionsWithRawResponse(client, server, auth)

    async def apps_permissions_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AppsPermissionsInfoschema:
        """Returns list of permissions this app has on a team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``none``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.apps_permissions_info(
                content_type, token=token, request_options=request_options
            )
        ).unwrap()

    async def apps_permissions_request(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AppsPermissionsRequestschema:
        """Allows an app to request additional scopes

        Args:
            token: Authentication token. Requires scope: ``none``
            scopes: A comma separated list of scopes to request for
            trigger_id: Token used to trigger the permissions API
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.apps_permissions_request(
                token, scopes, trigger_id, content_type, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAppsPermissionsWithRawResponse:
        return self._with_raw_response


class AppsPermissionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def apps_permissions_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AppsPermissionsInfoschema, RawError]:
        """Returns list of permissions this app has on a team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``none``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.info"),
            query_params=[param[str | None]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AppsPermissionsInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def apps_permissions_request(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AppsPermissionsRequestschema, RawError]:
        """Allows an app to request additional scopes

        Args:
            token: Authentication token. Requires scope: ``none``
            scopes: A comma separated list of scopes to request for
            trigger_id: Token used to trigger the permissions API
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.request"),
            query_params=[
                param[str]("token", token), param[str]("scopes", scopes), param[str]("trigger_id", trigger_id)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AppsPermissionsRequestschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAppsPermissionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def apps_permissions_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AppsPermissionsInfoschema, RawError]:
        """Returns list of permissions this app has on a team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``none``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.info"),
            query_params=[param[str | None]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AppsPermissionsInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def apps_permissions_request(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AppsPermissionsRequestschema, RawError]:
        """Allows an app to request additional scopes

        Args:
            token: Authentication token. Requires scope: ``none``
            scopes: A comma separated list of scopes to request for
            trigger_id: Token used to trigger the permissions API
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.request"),
            query_params=[
                param[str]("token", token), param[str]("scopes", scopes), param[str]("trigger_id", trigger_id)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AppsPermissionsRequestschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
