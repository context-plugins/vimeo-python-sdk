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
from ..models.files_comments_deleteschema import FilesCommentsDeleteschema
from ..models.files_deleteschema import FilesDeleteschema
from ..models.files_infoschema import FilesInfoschema
from ..models.files_listschema import FilesListschema
from ..models.files_revoke_public_urlschema import FilesRevokePublicUrlschema
from ..models.files_shared_public_urlschema import FilesSharedPublicUrlschema
from ..models.files_uploadschema import FilesUploadschema
from ..server.server import Server


class Files:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FilesWithRawResponse(client, server, auth)

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

    def files_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesDeleteschema:
        """Deletes a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: ID of file to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_delete(
            content_type, token=token, file=file, request_options=request_options
        ).unwrap()

    def files_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        count: str | None = None,
        page: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesInfoschema:
        """Gets information about a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:read``
            file: Specify a file by providing its ID.
            count: Value sent with the request.
            page: Value sent with the request.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached.
            cursor: Parameter for pagination. File comments are paginated for a single file. Set ``cursor`` equal to the
                ``next_cursor`` attribute returned by the previous request's ``response_metadata``. This parameter is
                optional, but pagination is mandatory: the default value simply fetches the first "page" of the
                collection of comments.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_info(
            content_type,
            token=token,
            file=file,
            count=count,
            page=page,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def files_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        channel: str | None = None,
        ts_from: float | None = None,
        ts_to: float | None = None,
        types: str | None = None,
        count: str | None = None,
        page: str | None = None,
        show_files_hidden_by_limit: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesListschema:
        """List for a team, in a channel, or from a user with applied filters.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:read``
            user: Filter files created by a single user.
            channel: Filter files appearing in a specific channel, indicated by its ID.
            ts_from: Filter files created after this timestamp (inclusive).
            ts_to: Filter files created before this timestamp (inclusive).
            types: Filter files by type (`see below <#file_types>`__). You can pass multiple values in the types
                argument, like ``types=spaces,snippets``.The default value is ``all``, which does not filter the list.
            count: Value sent with the request.
            page: Value sent with the request.
            show_files_hidden_by_limit: Show truncated file info for files hidden due to being too old, and the team who
                owns the file being over the file limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_list(
            content_type,
            token=token,
            user=user,
            channel=channel,
            ts_from=ts_from,
            ts_to=ts_to,
            types=types,
            count=count,
            page=page,
            show_files_hidden_by_limit=show_files_hidden_by_limit,
            request_options=request_options,
        ).unwrap()

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

    def files_revoke_public_url(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesRevokePublicUrlschema:
        """Revokes public/external sharing access for a file

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to revoke
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_revoke_public_url(
            content_type, token=token, file=file, request_options=request_options
        ).unwrap()

    def files_shared_public_url(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesSharedPublicUrlschema:
        """Enables a file for public/external sharing.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to share
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_shared_public_url(
            content_type, token=token, file=file, request_options=request_options
        ).unwrap()

    def files_upload(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        content: str | None = None,
        filetype: str | None = None,
        filename: str | None = None,
        title: str | None = None,
        initial_comment: str | None = None,
        channels: str | None = None,
        thread_ts: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesUploadschema:
        """Uploads or creates a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File contents via ``multipart/form-data``. If omitting this parameter, you must submit ``content``.
            content: File contents via a POST variable. If omitting this parameter, you must provide a ``file``.
            filetype: A `file type </types/file#file_types>`__ identifier.
            filename: Filename of file.
            title: Title of file.
            initial_comment: The message text introducing the file in specified ``channels``.
            channels: Comma-separated list of channel names or IDs where the file will be shared.
            thread_ts: Provide another message's ``ts`` value to upload this file as a reply. Never use a reply's ``ts``
                value; use its parent instead.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response after uploading a file to a channel with an initial message

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.files_upload(
            content_type,
            token=token,
            file=file,
            content=content,
            filetype=filetype,
            filename=filename,
            title=title,
            initial_comment=initial_comment,
            channels=channels,
            thread_ts=thread_ts,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FilesWithRawResponse:
        return self._with_raw_response


class AsyncFiles:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFilesWithRawResponse(client, server, auth)

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

    async def files_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesDeleteschema:
        """Deletes a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: ID of file to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_delete(
                content_type, token=token, file=file, request_options=request_options
            )
        ).unwrap()

    async def files_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        count: str | None = None,
        page: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesInfoschema:
        """Gets information about a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:read``
            file: Specify a file by providing its ID.
            count: Value sent with the request.
            page: Value sent with the request.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached.
            cursor: Parameter for pagination. File comments are paginated for a single file. Set ``cursor`` equal to the
                ``next_cursor`` attribute returned by the previous request's ``response_metadata``. This parameter is
                optional, but pagination is mandatory: the default value simply fetches the first "page" of the
                collection of comments.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_info(
                content_type,
                token=token,
                file=file,
                count=count,
                page=page,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def files_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        channel: str | None = None,
        ts_from: float | None = None,
        ts_to: float | None = None,
        types: str | None = None,
        count: str | None = None,
        page: str | None = None,
        show_files_hidden_by_limit: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesListschema:
        """List for a team, in a channel, or from a user with applied filters.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:read``
            user: Filter files created by a single user.
            channel: Filter files appearing in a specific channel, indicated by its ID.
            ts_from: Filter files created after this timestamp (inclusive).
            ts_to: Filter files created before this timestamp (inclusive).
            types: Filter files by type (`see below <#file_types>`__). You can pass multiple values in the types
                argument, like ``types=spaces,snippets``.The default value is ``all``, which does not filter the list.
            count: Value sent with the request.
            page: Value sent with the request.
            show_files_hidden_by_limit: Show truncated file info for files hidden due to being too old, and the team who
                owns the file being over the file limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_list(
                content_type,
                token=token,
                user=user,
                channel=channel,
                ts_from=ts_from,
                ts_to=ts_to,
                types=types,
                count=count,
                page=page,
                show_files_hidden_by_limit=show_files_hidden_by_limit,
                request_options=request_options,
            )
        ).unwrap()

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

    async def files_revoke_public_url(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesRevokePublicUrlschema:
        """Revokes public/external sharing access for a file

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to revoke
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_revoke_public_url(
                content_type, token=token, file=file, request_options=request_options
            )
        ).unwrap()

    async def files_shared_public_url(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesSharedPublicUrlschema:
        """Enables a file for public/external sharing.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to share
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_shared_public_url(
                content_type, token=token, file=file, request_options=request_options
            )
        ).unwrap()

    async def files_upload(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        content: str | None = None,
        filetype: str | None = None,
        filename: str | None = None,
        title: str | None = None,
        initial_comment: str | None = None,
        channels: str | None = None,
        thread_ts: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FilesUploadschema:
        """Uploads or creates a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File contents via ``multipart/form-data``. If omitting this parameter, you must submit ``content``.
            content: File contents via a POST variable. If omitting this parameter, you must provide a ``file``.
            filetype: A `file type </types/file#file_types>`__ identifier.
            filename: Filename of file.
            title: Title of file.
            initial_comment: The message text introducing the file in specified ``channels``.
            channels: Comma-separated list of channel names or IDs where the file will be shared.
            thread_ts: Provide another message's ``ts`` value to upload this file as a reply. Never use a reply's ``ts``
                value; use its parent instead.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response after uploading a file to a channel with an initial message

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.files_upload(
                content_type,
                token=token,
                file=file,
                content=content,
                filetype=filetype,
                filename=filename,
                title=title,
                initial_comment=initial_comment,
                channels=channels,
                thread_ts=thread_ts,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFilesWithRawResponse:
        return self._with_raw_response


class FilesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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

    def files_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesDeleteschema, RawError]:
        """Deletes a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: ID of file to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.delete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("file", file)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesDeleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        count: str | None = None,
        page: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesInfoschema, RawError]:
        """Gets information about a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:read``
            file: Specify a file by providing its ID.
            count: Value sent with the request.
            page: Value sent with the request.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached.
            cursor: Parameter for pagination. File comments are paginated for a single file. Set ``cursor`` equal to the
                ``next_cursor`` attribute returned by the previous request's ``response_metadata``. This parameter is
                optional, but pagination is mandatory: the default value simply fetches the first "page" of the
                collection of comments.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.info"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("file", file),
                param[str | None]("count", count),
                param[str | None]("page", page),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        channel: str | None = None,
        ts_from: float | None = None,
        ts_to: float | None = None,
        types: str | None = None,
        count: str | None = None,
        page: str | None = None,
        show_files_hidden_by_limit: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesListschema, RawError]:
        """List for a team, in a channel, or from a user with applied filters.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:read``
            user: Filter files created by a single user.
            channel: Filter files appearing in a specific channel, indicated by its ID.
            ts_from: Filter files created after this timestamp (inclusive).
            ts_to: Filter files created before this timestamp (inclusive).
            types: Filter files by type (`see below <#file_types>`__). You can pass multiple values in the types
                argument, like ``types=spaces,snippets``.The default value is ``all``, which does not filter the list.
            count: Value sent with the request.
            page: Value sent with the request.
            show_files_hidden_by_limit: Show truncated file info for files hidden due to being too old, and the team who
                owns the file being over the file limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.list"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("user", user),
                param[str | None]("channel", channel),
                param[float | None]("ts_from", ts_from),
                param[float | None]("ts_to", ts_to),
                param[str | None]("types", types),
                param[str | None]("count", count),
                param[str | None]("page", page),
                param[bool | None]("show_files_hidden_by_limit", show_files_hidden_by_limit),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def files_revoke_public_url(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesRevokePublicUrlschema, RawError]:
        """Revokes public/external sharing access for a file

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to revoke
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.revokePublicURL"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("file", file)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesRevokePublicUrlschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_shared_public_url(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesSharedPublicUrlschema, RawError]:
        """Enables a file for public/external sharing.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to share
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.sharedPublicURL"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("file", file)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesSharedPublicUrlschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def files_upload(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        content: str | None = None,
        filetype: str | None = None,
        filename: str | None = None,
        title: str | None = None,
        initial_comment: str | None = None,
        channels: str | None = None,
        thread_ts: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesUploadschema, RawError]:
        """Uploads or creates a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File contents via ``multipart/form-data``. If omitting this parameter, you must submit ``content``.
            content: File contents via a POST variable. If omitting this parameter, you must provide a ``file``.
            filetype: A `file type </types/file#file_types>`__ identifier.
            filename: Filename of file.
            title: Title of file.
            initial_comment: The message text introducing the file in specified ``channels``.
            channels: Comma-separated list of channel names or IDs where the file will be shared.
            thread_ts: Provide another message's ``ts`` value to upload this file as a reply. Never use a reply's ``ts``
                value; use its parent instead.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.upload"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("token", token),
                    param[str | None]("file", file),
                    param[str | None]("content", content),
                    param[str | None]("filetype", filetype),
                    param[str | None]("filename", filename),
                    param[str | None]("title", title),
                    param[str | None]("initial_comment", initial_comment),
                    param[str | None]("channels", channels),
                    param[float | None]("thread_ts", thread_ts),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesUploadschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFilesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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

    async def files_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesDeleteschema, RawError]:
        """Deletes a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: ID of file to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.delete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("file", file)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesDeleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        count: str | None = None,
        page: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesInfoschema, RawError]:
        """Gets information about a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:read``
            file: Specify a file by providing its ID.
            count: Value sent with the request.
            page: Value sent with the request.
            limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even
                if the end of the list hasn't been reached.
            cursor: Parameter for pagination. File comments are paginated for a single file. Set ``cursor`` equal to the
                ``next_cursor`` attribute returned by the previous request's ``response_metadata``. This parameter is
                optional, but pagination is mandatory: the default value simply fetches the first "page" of the
                collection of comments.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.info"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("file", file),
                param[str | None]("count", count),
                param[str | None]("page", page),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        channel: str | None = None,
        ts_from: float | None = None,
        ts_to: float | None = None,
        types: str | None = None,
        count: str | None = None,
        page: str | None = None,
        show_files_hidden_by_limit: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesListschema, RawError]:
        """List for a team, in a channel, or from a user with applied filters.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:read``
            user: Filter files created by a single user.
            channel: Filter files appearing in a specific channel, indicated by its ID.
            ts_from: Filter files created after this timestamp (inclusive).
            ts_to: Filter files created before this timestamp (inclusive).
            types: Filter files by type (`see below <#file_types>`__). You can pass multiple values in the types
                argument, like ``types=spaces,snippets``.The default value is ``all``, which does not filter the list.
            count: Value sent with the request.
            page: Value sent with the request.
            show_files_hidden_by_limit: Show truncated file info for files hidden due to being too old, and the team who
                owns the file being over the file limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/files.list"),
            query_params=[
                param[str | None]("token", token),
                param[str | None]("user", user),
                param[str | None]("channel", channel),
                param[float | None]("ts_from", ts_from),
                param[float | None]("ts_to", ts_to),
                param[str | None]("types", types),
                param[str | None]("count", count),
                param[str | None]("page", page),
                param[bool | None]("show_files_hidden_by_limit", show_files_hidden_by_limit),
            ],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    async def files_revoke_public_url(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesRevokePublicUrlschema, RawError]:
        """Revokes public/external sharing access for a file

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to revoke
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.revokePublicURL"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("file", file)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesRevokePublicUrlschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_shared_public_url(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesSharedPublicUrlschema, RawError]:
        """Enables a file for public/external sharing.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File to share
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.sharedPublicURL"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("file", file)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesSharedPublicUrlschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def files_upload(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        file: str | None = None,
        content: str | None = None,
        filetype: str | None = None,
        filename: str | None = None,
        title: str | None = None,
        initial_comment: str | None = None,
        channels: str | None = None,
        thread_ts: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FilesUploadschema, RawError]:
        """Uploads or creates a file.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``files:write:user``
            file: File contents via ``multipart/form-data``. If omitting this parameter, you must submit ``content``.
            content: File contents via a POST variable. If omitting this parameter, you must provide a ``file``.
            filetype: A `file type </types/file#file_types>`__ identifier.
            filename: Filename of file.
            title: Title of file.
            initial_comment: The message text introducing the file in specified ``channels``.
            channels: Comma-separated list of channel names or IDs where the file will be shared.
            thread_ts: Provide another message's ``ts`` value to upload this file as a reply. Never use a reply's ``ts``
                value; use its parent instead.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/files.upload"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str | None]("token", token),
                    param[str | None]("file", file),
                    param[str | None]("content", content),
                    param[str | None]("filetype", filetype),
                    param[str | None]("filename", filename),
                    param[str | None]("title", title),
                    param[str | None]("initial_comment", initial_comment),
                    param[str | None]("channels", channels),
                    param[float | None]("thread_ts", thread_ts),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[FilesUploadschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
