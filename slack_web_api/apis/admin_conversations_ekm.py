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


class AdminConversationsEkm:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdminConversationsEkmWithRawResponse(client, server, auth)

    def admin_conversations_ekm_list_original_connected_channel_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel_ids: str | None = None,
        team_ids: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all disconnected channels—i.e., channels that were once connected to other workspaces and then
        disconnected—and the corresponding original channel IDs for key revocation with EKM.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            channel_ids: A comma-separated list of channels to filter to.
            team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_conversations_ekm_list_original_connected_channel_info(
            token,
            content_type,
            channel_ids=channel_ids,
            team_ids=team_ids,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> AdminConversationsEkmWithRawResponse:
        return self._with_raw_response


class AsyncAdminConversationsEkm:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdminConversationsEkmWithRawResponse(client, server, auth)

    async def admin_conversations_ekm_list_original_connected_channel_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel_ids: str | None = None,
        team_ids: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """List all disconnected channels—i.e., channels that were once connected to other workspaces and then
        disconnected—and the corresponding original channel IDs for key revocation with EKM.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            channel_ids: A comma-separated list of channels to filter to.
            team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_conversations_ekm_list_original_connected_channel_info(
                token,
                content_type,
                channel_ids=channel_ids,
                team_ids=team_ids,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAdminConversationsEkmWithRawResponse:
        return self._with_raw_response


class AdminConversationsEkmWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def admin_conversations_ekm_list_original_connected_channel_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel_ids: str | None = None,
        team_ids: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all disconnected channels—i.e., channels that were once connected to other workspaces and then
        disconnected—and the corresponding original channel IDs for key revocation with EKM.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            channel_ids: A comma-separated list of channels to filter to.
            team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.ekm.listOriginalConnectedChannelInfo"),
            query_params=[
                param[str]("token", token),
                param[str | None]("channel_ids", channel_ids),
                param[str | None]("team_ids", team_ids),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAdminConversationsEkmWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def admin_conversations_ekm_list_original_connected_channel_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        channel_ids: str | None = None,
        team_ids: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """List all disconnected channels—i.e., channels that were once connected to other workspaces and then
        disconnected—and the corresponding original channel IDs for key revocation with EKM.

        Args:
            token: Authentication token. Requires scope: ``admin.conversations:read``
            content_type: Value sent with the request.
            channel_ids: A comma-separated list of channels to filter to.
            team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
            limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
            cursor: Set ``cursor`` to ``next_cursor`` returned by the previous call to list items in the next page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin.conversations.ekm.listOriginalConnectedChannelInfo"),
            query_params=[
                param[str]("token", token),
                param[str | None]("channel_ids", channel_ids),
                param[str | None]("team_ids", team_ids),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
