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
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class FilesRemote:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FilesRemoteWithRawResponse(client, server, auth)

    def files_remote_add(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        external_id: str | None = None,
        title: str | None = None,
        filetype: str | None = None,
        external_url: str | None = None,
        preview_image: str | None = None,
        indexable_file_contents: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Adds a file from a remote service

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            external_id: Creator defined GUID for the file.
            title: Title of the file being shared.
            filetype: type of file
            external_url: URL of the remote file.
            preview_image: Preview of the document via ``multipart/form-data``.
            indexable_file_contents: A text file (txt, pdf, doc, etc.) containing textual search terms that are used to
                improve discovery of the remote file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_remote_add(
            content_type,
            token=token,
            external_id=external_id,
            title=title,
            filetype=filetype,
            external_url=external_url,
            preview_image=preview_image,
            indexable_file_contents=indexable_file_contents,
            request_options=request_options,
        ).unwrap()

    def files_remote_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Retrieve information about a remote file added to Slack

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:read``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_remote_info(
            content_type, token=token, file=file, external_id=external_id, request_options=request_options
        ).unwrap()

    def files_remote_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts_from: float | None = None,
        ts_to: float | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Retrieve information about a remote file added to Slack

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:read``
            channel: Filter files appearing in a specific channel, indicated by its ID.
            ts_from: Filter files created after this timestamp (inclusive).
            ts_to: Filter files created before this timestamp (inclusive).
            limit: The maximum number of items to return.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_remote_list(
            content_type,
            token=token,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def files_remote_remove(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove a remote file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_remote_remove(
            content_type, token=token, file=file, external_id=external_id, request_options=request_options
        ).unwrap()

    def files_remote_share(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        channels: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Share a remote file into a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:share``
            file: Specify a file registered with Slack by providing its ID. Either this field or ``external_id`` or both
                are required.
            external_id: The globally unique identifier (GUID) for the file, as set by the app registering the file with
                Slack. Either this field or ``file`` or both are required.
            channels: Comma-separated list of channel IDs where the file will be shared.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_remote_share(
            content_type,
            token=token,
            file=file,
            external_id=external_id,
            channels=channels,
            request_options=request_options,
        ).unwrap()

    def files_remote_update(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        title: str | None = None,
        filetype: str | None = None,
        external_url: str | None = None,
        preview_image: str | None = None,
        indexable_file_contents: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Updates an existing remote file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            title: Title of the file being shared.
            filetype: type of file
            external_url: URL of the remote file.
            preview_image: Preview of the document via ``multipart/form-data``.
            indexable_file_contents: File containing contents that can be used to improve searchability for the remote
                file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_remote_update(
            content_type,
            token=token,
            file=file,
            external_id=external_id,
            title=title,
            filetype=filetype,
            external_url=external_url,
            preview_image=preview_image,
            indexable_file_contents=indexable_file_contents,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FilesRemoteWithRawResponse:
        return self._with_raw_response


class AsyncFilesRemote:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFilesRemoteWithRawResponse(client, server, auth)

    async def files_remote_add(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        external_id: str | None = None,
        title: str | None = None,
        filetype: str | None = None,
        external_url: str | None = None,
        preview_image: str | None = None,
        indexable_file_contents: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Adds a file from a remote service

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            external_id: Creator defined GUID for the file.
            title: Title of the file being shared.
            filetype: type of file
            external_url: URL of the remote file.
            preview_image: Preview of the document via ``multipart/form-data``.
            indexable_file_contents: A text file (txt, pdf, doc, etc.) containing textual search terms that are used to
                improve discovery of the remote file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_remote_add(
                content_type,
                token=token,
                external_id=external_id,
                title=title,
                filetype=filetype,
                external_url=external_url,
                preview_image=preview_image,
                indexable_file_contents=indexable_file_contents,
                request_options=request_options,
            )
        ).unwrap()

    async def files_remote_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Retrieve information about a remote file added to Slack

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:read``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_remote_info(
                content_type, token=token, file=file, external_id=external_id, request_options=request_options
            )
        ).unwrap()

    async def files_remote_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts_from: float | None = None,
        ts_to: float | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Retrieve information about a remote file added to Slack

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:read``
            channel: Filter files appearing in a specific channel, indicated by its ID.
            ts_from: Filter files created after this timestamp (inclusive).
            ts_to: Filter files created before this timestamp (inclusive).
            limit: The maximum number of items to return.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_remote_list(
                content_type,
                token=token,
                channel=channel,
                ts_from=ts_from,
                ts_to=ts_to,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def files_remote_remove(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Remove a remote file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_remote_remove(
                content_type, token=token, file=file, external_id=external_id, request_options=request_options
            )
        ).unwrap()

    async def files_remote_share(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        channels: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Share a remote file into a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:share``
            file: Specify a file registered with Slack by providing its ID. Either this field or ``external_id`` or both
                are required.
            external_id: The globally unique identifier (GUID) for the file, as set by the app registering the file with
                Slack. Either this field or ``file`` or both are required.
            channels: Comma-separated list of channel IDs where the file will be shared.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_remote_share(
                content_type,
                token=token,
                file=file,
                external_id=external_id,
                channels=channels,
                request_options=request_options,
            )
        ).unwrap()

    async def files_remote_update(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        title: str | None = None,
        filetype: str | None = None,
        external_url: str | None = None,
        preview_image: str | None = None,
        indexable_file_contents: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Updates an existing remote file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            title: Title of the file being shared.
            filetype: type of file
            external_url: URL of the remote file.
            preview_image: Preview of the document via ``multipart/form-data``.
            indexable_file_contents: File containing contents that can be used to improve searchability for the remote
                file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_remote_update(
                content_type,
                token=token,
                file=file,
                external_id=external_id,
                title=title,
                filetype=filetype,
                external_url=external_url,
                preview_image=preview_image,
                indexable_file_contents=indexable_file_contents,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFilesRemoteWithRawResponse:
        return self._with_raw_response


class FilesRemoteWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def files_remote_add(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        external_id: str | None = None,
        title: str | None = None,
        filetype: str | None = None,
        external_url: str | None = None,
        preview_image: str | None = None,
        indexable_file_contents: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Adds a file from a remote service

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            external_id: Creator defined GUID for the file.
            title: Title of the file being shared.
            filetype: type of file
            external_url: URL of the remote file.
            preview_image: Preview of the document via ``multipart/form-data``.
            indexable_file_contents: A text file (txt, pdf, doc, etc.) containing textual search terms that are used to
                improve discovery of the remote file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.remote.add"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("token", token),
                    param[str | None]("external_id", external_id),
                    param[str | None]("title", title),
                    param[str | None]("filetype", filetype),
                    param[str | None]("external_url", external_url),
                    param[str | None]("preview_image", preview_image),
                    param[str | None]("indexable_file_contents", indexable_file_contents),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_remote_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Retrieve information about a remote file added to Slack

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:read``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.remote.info"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("file", file),
                param[str | None]("external_id", external_id),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_remote_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts_from: float | None = None,
        ts_to: float | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Retrieve information about a remote file added to Slack

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:read``
            channel: Filter files appearing in a specific channel, indicated by its ID.
            ts_from: Filter files created after this timestamp (inclusive).
            ts_to: Filter files created before this timestamp (inclusive).
            limit: The maximum number of items to return.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.remote.list"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[float | None]("ts_from", ts_from),
                param[float | None]("ts_to", ts_to),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_remote_remove(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove a remote file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.remote.remove"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("token", token),
                    param[str | None]("file", file),
                    param[str | None]("external_id", external_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_remote_share(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        channels: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Share a remote file into a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:share``
            file: Specify a file registered with Slack by providing its ID. Either this field or ``external_id`` or both
                are required.
            external_id: The globally unique identifier (GUID) for the file, as set by the app registering the file with
                Slack. Either this field or ``file`` or both are required.
            channels: Comma-separated list of channel IDs where the file will be shared.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.remote.share"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("file", file),
                param[str | None]("external_id", external_id),
                param[str | None]("channels", channels),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_remote_update(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        title: str | None = None,
        filetype: str | None = None,
        external_url: str | None = None,
        preview_image: str | None = None,
        indexable_file_contents: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Updates an existing remote file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            title: Title of the file being shared.
            filetype: type of file
            external_url: URL of the remote file.
            preview_image: Preview of the document via ``multipart/form-data``.
            indexable_file_contents: File containing contents that can be used to improve searchability for the remote
                file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.remote.update"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("token", token),
                    param[str | None]("file", file),
                    param[str | None]("external_id", external_id),
                    param[str | None]("title", title),
                    param[str | None]("filetype", filetype),
                    param[str | None]("external_url", external_url),
                    param[str | None]("preview_image", preview_image),
                    param[str | None]("indexable_file_contents", indexable_file_contents),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFilesRemoteWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def files_remote_add(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        external_id: str | None = None,
        title: str | None = None,
        filetype: str | None = None,
        external_url: str | None = None,
        preview_image: str | None = None,
        indexable_file_contents: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Adds a file from a remote service

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            external_id: Creator defined GUID for the file.
            title: Title of the file being shared.
            filetype: type of file
            external_url: URL of the remote file.
            preview_image: Preview of the document via ``multipart/form-data``.
            indexable_file_contents: A text file (txt, pdf, doc, etc.) containing textual search terms that are used to
                improve discovery of the remote file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.remote.add"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("token", token),
                    param[str | None]("external_id", external_id),
                    param[str | None]("title", title),
                    param[str | None]("filetype", filetype),
                    param[str | None]("external_url", external_url),
                    param[str | None]("preview_image", preview_image),
                    param[str | None]("indexable_file_contents", indexable_file_contents),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_remote_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Retrieve information about a remote file added to Slack

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:read``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.remote.info"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("file", file),
                param[str | None]("external_id", external_id),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_remote_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        channel: str | None = None,
        ts_from: float | None = None,
        ts_to: float | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Retrieve information about a remote file added to Slack

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:read``
            channel: Filter files appearing in a specific channel, indicated by its ID.
            ts_from: Filter files created after this timestamp (inclusive).
            ts_to: Filter files created before this timestamp (inclusive).
            limit: The maximum number of items to return.
            cursor: Paginate through collections of data by setting the ``cursor`` parameter to a ``next_cursor``
                attribute returned by a previous request's ``response_metadata``. Default value fetches the first "page"
                of the collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.remote.list"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("channel", channel),
                param[float | None]("ts_from", ts_from),
                param[float | None]("ts_to", ts_to),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_remote_remove(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Remove a remote file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.remote.remove"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("token", token),
                    param[str | None]("file", file),
                    param[str | None]("external_id", external_id),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_remote_share(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        channels: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Share a remote file into a channel.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:share``
            file: Specify a file registered with Slack by providing its ID. Either this field or ``external_id`` or both
                are required.
            external_id: The globally unique identifier (GUID) for the file, as set by the app registering the file with
                Slack. Either this field or ``file`` or both are required.
            channels: Comma-separated list of channel IDs where the file will be shared.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.remote.share"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("file", file),
                param[str | None]("external_id", external_id),
                param[str | None]("channels", channels),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_remote_update(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        external_id: str | None = None,
        title: str | None = None,
        filetype: str | None = None,
        external_url: str | None = None,
        preview_image: str | None = None,
        indexable_file_contents: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Updates an existing remote file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``remote_files:write``
            file: Specify a file by providing its ID.
            external_id: Creator defined GUID for the file.
            title: Title of the file being shared.
            filetype: type of file
            external_url: URL of the remote file.
            preview_image: Preview of the document via ``multipart/form-data``.
            indexable_file_contents: File containing contents that can be used to improve searchability for the remote
                file.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.remote.update"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("token", token),
                    param[str | None]("file", file),
                    param[str | None]("external_id", external_id),
                    param[str | None]("title", title),
                    param[str | None]("filetype", filetype),
                    param[str | None]("external_url", external_url),
                    param[str | None]("preview_image", preview_image),
                    param[str | None]("indexable_file_contents", indexable_file_contents),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
