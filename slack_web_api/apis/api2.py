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
from ..models.api_testsuccessschema import ApiTestsuccessschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Api2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api2WithRawResponse(client, server, auth)

    def api_test(
        self,
        content_type: ContentTypeOrStr,
        *,
        error: str | None = None,
        foo: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiTestsuccessschema:
        """Checks API calling code.

        Args:
            content_type: Value sent with the request.
            error: Error response to return
            foo: example property to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.api_test(
            content_type, error=error, foo=foo, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api2WithRawResponse:
        return self._with_raw_response


class AsyncApi2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi2WithRawResponse(client, server, auth)

    async def api_test(
        self,
        content_type: ContentTypeOrStr,
        *,
        error: str | None = None,
        foo: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiTestsuccessschema:
        """Checks API calling code.

        Args:
            content_type: Value sent with the request.
            error: Error response to return
            foo: example property to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.api_test(content_type, error=error, foo=foo, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi2WithRawResponse:
        return self._with_raw_response


class Api2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def api_test(
        self,
        content_type: ContentTypeOrStr,
        *,
        error: str | None = None,
        foo: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiTestsuccessschema, RawError]:
        """Checks API calling code.

        Args:
            content_type: Value sent with the request.
            error: Error response to return
            foo: example property to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api.test"),
            query_params=[param[str | None]("error", error), param[str | None]("foo", foo)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ApiTestsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def api_test(
        self,
        content_type: ContentTypeOrStr,
        *,
        error: str | None = None,
        foo: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiTestsuccessschema, RawError]:
        """Checks API calling code.

        Args:
            content_type: Value sent with the request.
            error: Error response to return
            foo: example property to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api.test"),
            query_params=[param[str | None]("error", error), param[str | None]("foo", foo)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[ApiTestsuccessschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
