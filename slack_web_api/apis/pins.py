from __future__ import annotations

from typing import Any

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
from ..models.enums.content_type import ContentTypeOrStr
from ..models.pins_addschema import PinsAddschema
from ..models.pins_removeschema import PinsRemoveschema
from ..server.server import Server


class Pins:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PinsWithRawResponse(client, server, auth)

    def pins_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PinsAddschema:
        """Pins an item to a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:write``
            content_type: Value sent with the request.
            channel: Channel to pin the item in.
            timestamp: Timestamp of the message to pin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pins_add(
            token, content_type, channel, timestamp=timestamp, request_options=request_options
        ).unwrap()

    def pins_list(
        self,
        token: str,
        channel: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Lists items pinned to a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:read``
            channel: Channel to get pinned items for.
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pins_list(token, channel, content_type, request_options=request_options).unwrap()

    def pins_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PinsRemoveschema:
        """Un-pins an item from a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:write``
            content_type: Value sent with the request.
            channel: Channel where the item is pinned to.
            timestamp: Timestamp of the message to un-pin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pins_remove(
            token, content_type, channel, timestamp=timestamp, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PinsWithRawResponse:
        return self._with_raw_response


class AsyncPins:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPinsWithRawResponse(client, server, auth)

    async def pins_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PinsAddschema:
        """Pins an item to a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:write``
            content_type: Value sent with the request.
            channel: Channel to pin the item in.
            timestamp: Timestamp of the message to pin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pins_add(
                token, content_type, channel, timestamp=timestamp, request_options=request_options
            )
        ).unwrap()

    async def pins_list(
        self,
        token: str,
        channel: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Lists items pinned to a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:read``
            channel: Channel to get pinned items for.
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pins_list(token, channel, content_type, request_options=request_options)
        ).unwrap()

    async def pins_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PinsRemoveschema:
        """Un-pins an item from a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:write``
            content_type: Value sent with the request.
            channel: Channel where the item is pinned to.
            timestamp: Timestamp of the message to un-pin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pins_remove(
                token, content_type, channel, timestamp=timestamp, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPinsWithRawResponse:
        return self._with_raw_response


class PinsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def pins_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PinsAddschema, RawError]:
        """Pins an item to a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:write``
            content_type: Value sent with the request.
            channel: Channel to pin the item in.
            timestamp: Timestamp of the message to pin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pins.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel", channel), param[str | None]("timestamp", timestamp)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[PinsAddschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pins_list(
        self,
        token: str,
        channel: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Lists items pinned to a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:read``
            channel: Channel to get pinned items for.
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/pins.list"),
            query_params=[param[str]("token", token), param[str]("channel", channel)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pins_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PinsRemoveschema, RawError]:
        """Un-pins an item from a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:write``
            content_type: Value sent with the request.
            channel: Channel where the item is pinned to.
            timestamp: Timestamp of the message to un-pin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pins.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel", channel), param[str | None]("timestamp", timestamp)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[PinsRemoveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPinsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def pins_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PinsAddschema, RawError]:
        """Pins an item to a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:write``
            content_type: Value sent with the request.
            channel: Channel to pin the item in.
            timestamp: Timestamp of the message to pin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pins.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel", channel), param[str | None]("timestamp", timestamp)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[PinsAddschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pins_list(
        self,
        token: str,
        channel: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Lists items pinned to a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:read``
            channel: Channel to get pinned items for.
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/pins.list"),
            query_params=[param[str]("token", token), param[str]("channel", channel)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pins_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        channel: str,
        *,
        timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PinsRemoveschema, RawError]:
        """Un-pins an item from a channel.

        Args:
            token: Authentication token. Requires scope: ``pins:write``
            content_type: Value sent with the request.
            channel: Channel where the item is pinned to.
            timestamp: Timestamp of the message to un-pin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/pins.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("channel", channel), param[str | None]("timestamp", timestamp)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[PinsRemoveschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
