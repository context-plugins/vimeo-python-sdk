from __future__ import annotations

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
from ..models.files_comments_deleteschema import FilesCommentsDeleteschema
from ..server.server import Server


class FilesComments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FilesCommentsWithRawResponse(client, server, auth)

    def files_comments_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesCommentsDeleteschema:
        """Deletes an existing comment on a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to delete a comment from.
            id: The comment to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response is very simple

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_comments_delete(
            content_type, token=token, file=file, id=id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FilesCommentsWithRawResponse:
        return self._with_raw_response


class AsyncFilesComments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFilesCommentsWithRawResponse(client, server, auth)

    async def files_comments_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesCommentsDeleteschema:
        """Deletes an existing comment on a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to delete a comment from.
            id: The comment to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Standard success response is very simple

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_comments_delete(
                content_type, token=token, file=file, id=id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFilesCommentsWithRawResponse:
        return self._with_raw_response


class FilesCommentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def files_comments_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesCommentsDeleteschema, RawError]:
        """Deletes an existing comment on a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to delete a comment from.
            id: The comment to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.comments.delete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("file", file), param[str | None]("id", id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesCommentsDeleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFilesCommentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def files_comments_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesCommentsDeleteschema, RawError]:
        """Deletes an existing comment on a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to delete a comment from.
            id: The comment to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.comments.delete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("file", file), param[str | None]("id", id)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesCommentsDeleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
