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


class AppsEventAuthorizations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AppsEventAuthorizationsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AppsEventAuthorizationsWithRawResponse:
        return self._with_raw_response


class AsyncAppsEventAuthorizations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAppsEventAuthorizationsWithRawResponse(client, server, auth)

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

    @property
    def with_raw_response(self) -> AsyncAppsEventAuthorizationsWithRawResponse:
        return self._with_raw_response


class AppsEventAuthorizationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncAppsEventAuthorizationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
