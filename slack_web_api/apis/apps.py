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
from ..models.api_permissions_scopes_listsuccessschema import ApiPermissionsScopesListsuccessschema
from ..models.apps_permissions_infoschema import AppsPermissionsInfoschema
from ..models.apps_permissions_requestschema import AppsPermissionsRequestschema
from ..models.apps_permissions_resources_listsuccessschema import AppsPermissionsResourcesListsuccessschema
from ..models.apps_uninstallschema import AppsUninstallschema
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Apps:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AppsWithRawResponse(client, server, auth)

    def apps_event_authorizations_list(
        self,
        event_context: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Get a list of authorizations for the given event context. Each authorization represents an app installation
        that the event is visible to.

        Args:
            event_context: Value sent with the request.
            token: Authentication token. Requires scope: ``authorizations:read``
            content_type: Value sent with the request.
            cursor: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.apps_event_authorizations_list(
            event_context, token, content_type, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

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

    def apps_permissions_resources_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AppsPermissionsResourcesListsuccessschema:
        """Returns list of resource grants this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            limit: The maximum number of items to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical successful paginated response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.apps_permissions_resources_list(
            token, content_type, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def apps_permissions_scopes_list(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiPermissionsScopesListsuccessschema:
        """Returns list of scopes this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical successful paginated response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.apps_permissions_scopes_list(
            token, content_type, request_options=request_options
        ).unwrap()

    def apps_permissions_users_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Returns list of user grants and corresponding scopes this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            limit: The maximum number of items to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical successful paginated response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.apps_permissions_users_list(
            token, content_type, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def apps_permissions_users_request(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Enables an app to trigger a permissions modal to grant an app access to a user access scope.

        Args:
            token: Authentication token. Requires scope: ``none``
            scopes: A comma separated list of user scopes to request for
            trigger_id: Token used to trigger the request
            user: The user this scope is being requested for
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.apps_permissions_users_request(
            token, scopes, trigger_id, user, content_type, request_options=request_options
        ).unwrap()

    def apps_uninstall(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AppsUninstallschema:
        """Uninstalls your app from a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``none``
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.apps_uninstall(
            content_type, token=token, client_id=client_id, client_secret=client_secret, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AppsWithRawResponse:
        return self._with_raw_response


class AsyncApps:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAppsWithRawResponse(client, server, auth)

    async def apps_event_authorizations_list(
        self,
        event_context: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Get a list of authorizations for the given event context. Each authorization represents an app installation
        that the event is visible to.

        Args:
            event_context: Value sent with the request.
            token: Authentication token. Requires scope: ``authorizations:read``
            content_type: Value sent with the request.
            cursor: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.apps_event_authorizations_list(
                event_context, token, content_type, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

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

    async def apps_permissions_resources_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AppsPermissionsResourcesListsuccessschema:
        """Returns list of resource grants this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            limit: The maximum number of items to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical successful paginated response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.apps_permissions_resources_list(
                token, content_type, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def apps_permissions_scopes_list(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiPermissionsScopesListsuccessschema:
        """Returns list of scopes this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical successful paginated response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.apps_permissions_scopes_list(
                token, content_type, request_options=request_options
            )
        ).unwrap()

    async def apps_permissions_users_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Returns list of user grants and corresponding scopes this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            limit: The maximum number of items to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical successful paginated response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.apps_permissions_users_list(
                token, content_type, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def apps_permissions_users_request(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Enables an app to trigger a permissions modal to grant an app access to a user access scope.

        Args:
            token: Authentication token. Requires scope: ``none``
            scopes: A comma separated list of user scopes to request for
            trigger_id: Token used to trigger the request
            user: The user this scope is being requested for
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response when used with a user token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.apps_permissions_users_request(
                token, scopes, trigger_id, user, content_type, request_options=request_options
            )
        ).unwrap()

    async def apps_uninstall(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AppsUninstallschema:
        """Uninstalls your app from a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``none``
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.apps_uninstall(
                content_type,
                token=token,
                client_id=client_id,
                client_secret=client_secret,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAppsWithRawResponse:
        return self._with_raw_response


class AppsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def apps_event_authorizations_list(
        self,
        event_context: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Get a list of authorizations for the given event context. Each authorization represents an app installation
        that the event is visible to.

        Args:
            event_context: Value sent with the request.
            token: Authentication token. Requires scope: ``authorizations:read``
            content_type: Value sent with the request.
            cursor: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.event.authorizations.list"),
            query_params=[
                param[str]("event_context", event_context),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def apps_permissions_resources_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AppsPermissionsResourcesListsuccessschema, RawError]:
        """Returns list of resource grants this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            limit: The maximum number of items to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.resources.list"),
            query_params=[
                param[str]("token", token), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AppsPermissionsResourcesListsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def apps_permissions_scopes_list(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiPermissionsScopesListsuccessschema, RawError]:
        """Returns list of scopes this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.scopes.list"),
            query_params=[param[str]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ApiPermissionsScopesListsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def apps_permissions_users_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Returns list of user grants and corresponding scopes this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            limit: The maximum number of items to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.users.list"),
            query_params=[
                param[str]("token", token), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def apps_permissions_users_request(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Enables an app to trigger a permissions modal to grant an app access to a user access scope.

        Args:
            token: Authentication token. Requires scope: ``none``
            scopes: A comma separated list of user scopes to request for
            trigger_id: Token used to trigger the request
            user: The user this scope is being requested for
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.users.request"),
            query_params=[
                param[str]("token", token),
                param[str]("scopes", scopes),
                param[str]("trigger_id", trigger_id),
                param[str]("user", user),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def apps_uninstall(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AppsUninstallschema, RawError]:
        """Uninstalls your app from a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``none``
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.uninstall"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AppsUninstallschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAppsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def apps_event_authorizations_list(
        self,
        event_context: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Get a list of authorizations for the given event context. Each authorization represents an app installation
        that the event is visible to.

        Args:
            event_context: Value sent with the request.
            token: Authentication token. Requires scope: ``authorizations:read``
            content_type: Value sent with the request.
            cursor: Value sent with the request.
            limit: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.event.authorizations.list"),
            query_params=[
                param[str]("event_context", event_context),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    async def apps_permissions_resources_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AppsPermissionsResourcesListsuccessschema, RawError]:
        """Returns list of resource grants this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            limit: The maximum number of items to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.resources.list"),
            query_params=[
                param[str]("token", token), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AppsPermissionsResourcesListsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def apps_permissions_scopes_list(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiPermissionsScopesListsuccessschema, RawError]:
        """Returns list of scopes this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.scopes.list"),
            query_params=[param[str]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ApiPermissionsScopesListsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def apps_permissions_users_list(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Returns list of user grants and corresponding scopes this app has on a team.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            limit: The maximum number of items to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.users.list"),
            query_params=[
                param[str]("token", token), param[str | None]("cursor", cursor), param[int | None]("limit", limit)
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def apps_permissions_users_request(
        self,
        token: str,
        scopes: str,
        trigger_id: str,
        user: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Enables an app to trigger a permissions modal to grant an app access to a user access scope.

        Args:
            token: Authentication token. Requires scope: ``none``
            scopes: A comma separated list of user scopes to request for
            trigger_id: Token used to trigger the request
            user: The user this scope is being requested for
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.permissions.users.request"),
            query_params=[
                param[str]("token", token),
                param[str]("scopes", scopes),
                param[str]("trigger_id", trigger_id),
                param[str]("user", user),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def apps_uninstall(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AppsUninstallschema, RawError]:
        """Uninstalls your app from a workspace.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``none``
            client_id: Issued when you created your application.
            client_secret: Issued when you created your application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps.uninstall"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[AppsUninstallschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
