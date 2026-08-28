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
from ..models.dialog_openschema import DialogOpenschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Dialog:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DialogWithRawResponse(client, server, auth)

    def dialog_open(
        self,
        dialog: str,
        trigger_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DialogOpenschema:
        """Open a dialog with a user

        Args:
            dialog: The dialog definition. This must be a JSON-encoded string.
            trigger_id: Exchange a trigger to post to the user.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response is quite minimal.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dialog_open(
            dialog, trigger_id, token, content_type, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DialogWithRawResponse:
        return self._with_raw_response


class AsyncDialog:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDialogWithRawResponse(client, server, auth)

    async def dialog_open(
        self,
        dialog: str,
        trigger_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DialogOpenschema:
        """Open a dialog with a user

        Args:
            dialog: The dialog definition. This must be a JSON-encoded string.
            trigger_id: Exchange a trigger to post to the user.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response is quite minimal.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dialog_open(
                dialog, trigger_id, token, content_type, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDialogWithRawResponse:
        return self._with_raw_response


class DialogWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def dialog_open(
        self,
        dialog: str,
        trigger_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DialogOpenschema, RawError]:
        """Open a dialog with a user

        Args:
            dialog: The dialog definition. This must be a JSON-encoded string.
            trigger_id: Exchange a trigger to post to the user.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/dialog.open"),
            query_params=[param[str]("dialog", dialog), param[str]("trigger_id", trigger_id)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DialogOpenschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDialogWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def dialog_open(
        self,
        dialog: str,
        trigger_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DialogOpenschema, RawError]:
        """Open a dialog with a user

        Args:
            dialog: The dialog definition. This must be a JSON-encoded string.
            trigger_id: Exchange a trigger to post to the user.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/dialog.open"),
            query_params=[param[str]("dialog", dialog), param[str]("trigger_id", trigger_id)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DialogOpenschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
