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
from ..models.apps_permissions_resources_listsuccessschema import AppsPermissionsResourcesListsuccessschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class AppsPermissionsResources:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AppsPermissionsResourcesWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AppsPermissionsResourcesWithRawResponse:
        return self._with_raw_response


class AsyncAppsPermissionsResources:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAppsPermissionsResourcesWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAppsPermissionsResourcesWithRawResponse:
        return self._with_raw_response


class AppsPermissionsResourcesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAppsPermissionsResourcesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
