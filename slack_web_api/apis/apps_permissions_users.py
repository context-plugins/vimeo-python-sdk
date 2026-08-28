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
from ..server.server import Server


class AppsPermissionsUsers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AppsPermissionsUsersWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AppsPermissionsUsersWithRawResponse:
        return self._with_raw_response


class AsyncAppsPermissionsUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAppsPermissionsUsersWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAppsPermissionsUsersWithRawResponse:
        return self._with_raw_response


class AppsPermissionsUsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAppsPermissionsUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
