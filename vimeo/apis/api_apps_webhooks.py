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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.add_webhook_error import AddWebhookErrorBody, add_webhook_error_mapper
from ..errors.delete_webhook_error import DeleteWebhookErrorBody, delete_webhook_error_mapper
from ..errors.get_webhook_error import GetWebhookErrorBody, get_webhook_error_mapper
from ..errors.update_webhook_error import UpdateWebhookErrorBody, update_webhook_error_mapper
from ..models.api_app_webhook import ApiAppWebhook
from ..models.api_app_webhook_connection import ApiAppWebhookConnection
from ..models.apps_webhooks_request import AppsWebhooksRequest, AppsWebhooksRequestDict
from ..models.apps_webhooks_request1 import AppsWebhooksRequest1, AppsWebhooksRequest1Dict
from ..server.server import Server


class ApiAppsWebhooks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApiAppsWebhooksWithRawResponse(client, server, auth)

    def add_webhook(
        self,
        app_id: float,
        *,
        body: AppsWebhooksRequest | AppsWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppWebhook:
        """This method adds a webhook for the specified app.

        Args:
            app_id: The ID of the app for which the webhook is created.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The webhook was added.

        Raises:
            ApiError: Error code 3143: The request is invalid because the webhook type already exists and can't be
                duplicated. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.add_webhook(app_id, body=body, request_options=request_options).unwrap()

    def delete_webhook(
        self, app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The webhook was deleted.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't delete the
                webhook. No webhook exists with the supplied ID. ``error`` is ``LegacyError | RawError``."""
        return self._with_raw_response.delete_webhook(app_id, webhook_id, request_options=request_options).unwrap()

    def get_webhook(
        self, app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiAppWebhook:
        """This method returns the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The webhook was returned.

        Raises:
            ApiError: Error code 5000: No such API app webhook exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_webhook(app_id, webhook_id, request_options=request_options).unwrap()

    def get_webhooks(
        self,
        app_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppWebhookConnection:
        """This method returns every webhook for the specified app.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of webhooks was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_webhooks(
            app_id, page=page, per_page=per_page, request_options=request_options
        ).unwrap()

    def update_webhook(
        self,
        app_id: float,
        webhook_id: float,
        *,
        body: AppsWebhooksRequest1 | AppsWebhooksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppWebhook:
        """This method updates the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The webhook was updated.

        Raises:
            ApiError: * Error code 2204: A parameter is invalid. * Error code 3143: The request is invalid because the
                webhook type already exists and can't be duplicated. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.update_webhook(
            app_id, webhook_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ApiAppsWebhooksWithRawResponse:
        return self._with_raw_response


class AsyncApiAppsWebhooks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApiAppsWebhooksWithRawResponse(client, server, auth)

    async def add_webhook(
        self,
        app_id: float,
        *,
        body: AppsWebhooksRequest | AppsWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppWebhook:
        """This method adds a webhook for the specified app.

        Args:
            app_id: The ID of the app for which the webhook is created.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The webhook was added.

        Raises:
            ApiError: Error code 3143: The request is invalid because the webhook type already exists and can't be
                duplicated. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.add_webhook(app_id, body=body, request_options=request_options)).unwrap()

    async def delete_webhook(
        self, app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The webhook was deleted.

        Raises:
            ApiError: The supplied token doesn't have the proper scopes, or the authenticated user can't delete the
                webhook. No webhook exists with the supplied ID. ``error`` is ``LegacyError | RawError``."""
        return (
            await self._with_raw_response.delete_webhook(app_id, webhook_id, request_options=request_options)
        ).unwrap()

    async def get_webhook(
        self, app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiAppWebhook:
        """This method returns the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The webhook was returned.

        Raises:
            ApiError: Error code 5000: No such API app webhook exists. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.get_webhook(app_id, webhook_id, request_options=request_options)).unwrap()

    async def get_webhooks(
        self,
        app_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppWebhookConnection:
        """This method returns every webhook for the specified app.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of webhooks was returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_webhooks(
                app_id, page=page, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def update_webhook(
        self,
        app_id: float,
        webhook_id: float,
        *,
        body: AppsWebhooksRequest1 | AppsWebhooksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppWebhook:
        """This method updates the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The webhook was updated.

        Raises:
            ApiError: * Error code 2204: A parameter is invalid. * Error code 3143: The request is invalid because the
                webhook type already exists and can't be duplicated. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.update_webhook(app_id, webhook_id, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApiAppsWebhooksWithRawResponse:
        return self._with_raw_response


class ApiAppsWebhooksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_webhook(
        self,
        app_id: float,
        *,
        body: AppsWebhooksRequest | AppsWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppWebhook, AddWebhookErrorBody]:
        """This method adds a webhook for the specified app.

        Args:
            app_id: The ID of the app for which the webhook is created.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/apps/{app_id}/webhooks"),
            path_params=[param[float]("app_id", app_id)],
            body=json_body[AppsWebhooksRequest | AppsWebhooksRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ApiAppWebhook],
            error_mapper=add_webhook_error_mapper,
            request_options=request_options,
        )

    def delete_webhook(
        self, app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteWebhookErrorBody]:
        """This method deletes the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/apps/{app_id}/webhooks/{webhook_id}"),
            path_params=[param[float]("app_id", app_id), param[float]("webhook_id", webhook_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_webhook_error_mapper,
            request_options=request_options,
        )

    def get_webhook(
        self, app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiAppWebhook, GetWebhookErrorBody]:
        """This method returns the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps/{app_id}/webhooks/{webhook_id}"),
            path_params=[param[float]("app_id", app_id), param[float]("webhook_id", webhook_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ApiAppWebhook],
            error_mapper=get_webhook_error_mapper,
            request_options=request_options,
        )

    def get_webhooks(
        self,
        app_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppWebhookConnection, RawError]:
        """This method returns every webhook for the specified app.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps/{app_id}/webhooks"),
            path_params=[param[float]("app_id", app_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ApiAppWebhookConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_webhook(
        self,
        app_id: float,
        webhook_id: float,
        *,
        body: AppsWebhooksRequest1 | AppsWebhooksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppWebhook, UpdateWebhookErrorBody]:
        """This method updates the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/apps/{app_id}/webhooks/{webhook_id}"),
            path_params=[param[float]("app_id", app_id), param[float]("webhook_id", webhook_id)],
            body=json_body[AppsWebhooksRequest1 | AppsWebhooksRequest1Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ApiAppWebhook],
            error_mapper=update_webhook_error_mapper,
            request_options=request_options,
        )


class AsyncApiAppsWebhooksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_webhook(
        self,
        app_id: float,
        *,
        body: AppsWebhooksRequest | AppsWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppWebhook, AddWebhookErrorBody]:
        """This method adds a webhook for the specified app.

        Args:
            app_id: The ID of the app for which the webhook is created.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/apps/{app_id}/webhooks"),
            path_params=[param[float]("app_id", app_id)],
            body=json_body[AppsWebhooksRequest | AppsWebhooksRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ApiAppWebhook],
            error_mapper=add_webhook_error_mapper,
            request_options=request_options,
        )

    async def delete_webhook(
        self, app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteWebhookErrorBody]:
        """This method deletes the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/apps/{app_id}/webhooks/{webhook_id}"),
            path_params=[param[float]("app_id", app_id), param[float]("webhook_id", webhook_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_webhook_error_mapper,
            request_options=request_options,
        )

    async def get_webhook(
        self, app_id: float, webhook_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiAppWebhook, GetWebhookErrorBody]:
        """This method returns the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps/{app_id}/webhooks/{webhook_id}"),
            path_params=[param[float]("app_id", app_id), param[float]("webhook_id", webhook_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ApiAppWebhook],
            error_mapper=get_webhook_error_mapper,
            request_options=request_options,
        )

    async def get_webhooks(
        self,
        app_id: float,
        *,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppWebhookConnection, RawError]:
        """This method returns every webhook for the specified app.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/apps/{app_id}/webhooks"),
            path_params=[param[float]("app_id", app_id)],
            query_params=[param[float | None]("page", page), param[float | None]("per_page", per_page)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ApiAppWebhookConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_webhook(
        self,
        app_id: float,
        webhook_id: float,
        *,
        body: AppsWebhooksRequest1 | AppsWebhooksRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppWebhook, UpdateWebhookErrorBody]:
        """This method updates the specified webhook.

        Args:
            app_id: The ID of the app that the webhook is associated with.
            webhook_id: The ID of the webhook.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/apps/{app_id}/webhooks/{webhook_id}"),
            path_params=[param[float]("app_id", app_id), param[float]("webhook_id", webhook_id)],
            body=json_body[AppsWebhooksRequest1 | AppsWebhooksRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[ApiAppWebhook],
            error_mapper=update_webhook_error_mapper,
            request_options=request_options,
        )
