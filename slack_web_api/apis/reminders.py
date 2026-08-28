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
from ..models.reminders_addschema import RemindersAddschema
from ..models.reminders_completeschema import RemindersCompleteschema
from ..models.reminders_deleteschema import RemindersDeleteschema
from ..models.reminders_infoschema import RemindersInfoschema
from ..models.reminders_listschema import RemindersListschema
from ..server.server import Server


class Reminders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RemindersWithRawResponse(client, server, auth)

    def reminders_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        text: str,
        time: str,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersAddschema:
        """Creates a reminder.

        Args:
            token: Authentication token. Requires scope: ``reminders:write``
            content_type: Value sent with the request.
            text: The content of the reminder
            time: When this reminder should happen: the Unix timestamp (up to five years from now), the number of
                seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes,"
                or "every Thursday")
            user: The user who will receive the reminder. If no user is specified, the reminder will go to user who
                created it.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reminders_add(
            token, content_type, text, time, user=user, request_options=request_options
        ).unwrap()

    def reminders_complete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersCompleteschema:
        """Marks a reminder as complete.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:write``
            reminder: The ID of the reminder to be marked as complete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reminders_complete(
            content_type, token=token, reminder=reminder, request_options=request_options
        ).unwrap()

    def reminders_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersDeleteschema:
        """Deletes a reminder.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:write``
            reminder: The ID of the reminder
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reminders_delete(
            content_type, token=token, reminder=reminder, request_options=request_options
        ).unwrap()

    def reminders_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersInfoschema:
        """Gets information about a reminder.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:read``
            reminder: The ID of the reminder
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reminders_info(
            content_type, token=token, reminder=reminder, request_options=request_options
        ).unwrap()

    def reminders_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersListschema:
        """Lists all reminders created by or for a given user.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:read``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reminders_list(
            content_type, token=token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> RemindersWithRawResponse:
        return self._with_raw_response


class AsyncReminders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRemindersWithRawResponse(client, server, auth)

    async def reminders_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        text: str,
        time: str,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersAddschema:
        """Creates a reminder.

        Args:
            token: Authentication token. Requires scope: ``reminders:write``
            content_type: Value sent with the request.
            text: The content of the reminder
            time: When this reminder should happen: the Unix timestamp (up to five years from now), the number of
                seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes,"
                or "every Thursday")
            user: The user who will receive the reminder. If no user is specified, the reminder will go to user who
                created it.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reminders_add(
                token, content_type, text, time, user=user, request_options=request_options
            )
        ).unwrap()

    async def reminders_complete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersCompleteschema:
        """Marks a reminder as complete.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:write``
            reminder: The ID of the reminder to be marked as complete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reminders_complete(
                content_type, token=token, reminder=reminder, request_options=request_options
            )
        ).unwrap()

    async def reminders_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersDeleteschema:
        """Deletes a reminder.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:write``
            reminder: The ID of the reminder
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reminders_delete(
                content_type, token=token, reminder=reminder, request_options=request_options
            )
        ).unwrap()

    async def reminders_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersInfoschema:
        """Gets information about a reminder.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:read``
            reminder: The ID of the reminder
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reminders_info(
                content_type, token=token, reminder=reminder, request_options=request_options
            )
        ).unwrap()

    async def reminders_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemindersListschema:
        """Lists all reminders created by or for a given user.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:read``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reminders_list(content_type, token=token, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncRemindersWithRawResponse:
        return self._with_raw_response


class RemindersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def reminders_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        text: str,
        time: str,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersAddschema, RawError]:
        """Creates a reminder.

        Args:
            token: Authentication token. Requires scope: ``reminders:write``
            content_type: Value sent with the request.
            text: The content of the reminder
            time: When this reminder should happen: the Unix timestamp (up to five years from now), the number of
                seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes,"
                or "every Thursday")
            user: The user who will receive the reminder. If no user is specified, the reminder will go to user who
                created it.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reminders.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("text", text), param[str]("time", time), param[str | None]("user", user)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersAddschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reminders_complete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersCompleteschema, RawError]:
        """Marks a reminder as complete.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:write``
            reminder: The ID of the reminder to be marked as complete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reminders.complete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("reminder", reminder)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersCompleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reminders_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersDeleteschema, RawError]:
        """Deletes a reminder.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:write``
            reminder: The ID of the reminder
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reminders.delete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("reminder", reminder)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersDeleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reminders_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersInfoschema, RawError]:
        """Gets information about a reminder.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:read``
            reminder: The ID of the reminder
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/reminders.info"),
            query_params=[param[str | None]("token", token), param[str | None]("reminder", reminder)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reminders_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersListschema, RawError]:
        """Lists all reminders created by or for a given user.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:read``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/reminders.list"),
            query_params=[param[str | None]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncRemindersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def reminders_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        text: str,
        time: str,
        *,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersAddschema, RawError]:
        """Creates a reminder.

        Args:
            token: Authentication token. Requires scope: ``reminders:write``
            content_type: Value sent with the request.
            text: The content of the reminder
            time: When this reminder should happen: the Unix timestamp (up to five years from now), the number of
                seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes,"
                or "every Thursday")
            user: The user who will receive the reminder. If no user is specified, the reminder will go to user who
                created it.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reminders.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("text", text), param[str]("time", time), param[str | None]("user", user)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersAddschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reminders_complete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersCompleteschema, RawError]:
        """Marks a reminder as complete.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:write``
            reminder: The ID of the reminder to be marked as complete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reminders.complete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("reminder", reminder)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersCompleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reminders_delete(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersDeleteschema, RawError]:
        """Deletes a reminder.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:write``
            reminder: The ID of the reminder
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/reminders.delete"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type), param[str | None]("token", token)],
            body=form_body([param[str | None]("reminder", reminder)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersDeleteschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reminders_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        reminder: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersInfoschema, RawError]:
        """Gets information about a reminder.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:read``
            reminder: The ID of the reminder
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/reminders.info"),
            query_params=[param[str | None]("token", token), param[str | None]("reminder", reminder)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reminders_list(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemindersListschema, RawError]:
        """Lists all reminders created by or for a given user.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``reminders:read``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/reminders.list"),
            query_params=[param[str | None]("token", token)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[RemindersListschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
