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
from ..models.dnd_end_dndschema import DndEndDndschema
from ..models.dnd_end_snoozeschema import DndEndSnoozeschema
from ..models.dnd_infoschema import DndInfoschema
from ..models.dnd_set_snoozeschema import DndSetSnoozeschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Dnd:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DndWithRawResponse(client, server, auth)

    def dnd_end_dnd(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> DndEndDndschema:
        """Ends the current user's Do Not Disturb session immediately.

        Args:
            token: Authentication token. Requires scope: ``dnd:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dnd_end_dnd(token, content_type, request_options=request_options).unwrap()

    def dnd_end_snooze(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> DndEndSnoozeschema:
        """Ends the current user's snooze mode immediately.

        Args:
            token: Authentication token. Requires scope: ``dnd:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dnd_end_snooze(token, content_type, request_options=request_options).unwrap()

    def dnd_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DndInfoschema:
        """Retrieves a user's current Do Not Disturb status.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:read``
            user: User to fetch status for (defaults to current user)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dnd_info(
            content_type, token=token, user=user, request_options=request_options
        ).unwrap()

    def dnd_set_snooze(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        num_minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DndSetSnoozeschema:
        """Turns on Do Not Disturb mode for the current user, or changes its duration.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:write``
            num_minutes: Number of minutes, from now, to snooze until.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dnd_set_snooze(
            content_type, token, num_minutes, request_options=request_options
        ).unwrap()

    def dnd_team_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Retrieves the Do Not Disturb status for up to 50 users on a team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:read``
            users: Comma-separated list of users to fetch Do Not Disturb status for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dnd_team_info(
            content_type, token=token, users=users, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DndWithRawResponse:
        return self._with_raw_response


class AsyncDnd:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDndWithRawResponse(client, server, auth)

    async def dnd_end_dnd(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> DndEndDndschema:
        """Ends the current user's Do Not Disturb session immediately.

        Args:
            token: Authentication token. Requires scope: ``dnd:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dnd_end_dnd(token, content_type, request_options=request_options)
        ).unwrap()

    async def dnd_end_snooze(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> DndEndSnoozeschema:
        """Ends the current user's snooze mode immediately.

        Args:
            token: Authentication token. Requires scope: ``dnd:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dnd_end_snooze(token, content_type, request_options=request_options)
        ).unwrap()

    async def dnd_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DndInfoschema:
        """Retrieves a user's current Do Not Disturb status.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:read``
            user: User to fetch status for (defaults to current user)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dnd_info(
                content_type, token=token, user=user, request_options=request_options
            )
        ).unwrap()

    async def dnd_set_snooze(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        num_minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DndSetSnoozeschema:
        """Turns on Do Not Disturb mode for the current user, or changes its duration.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:write``
            num_minutes: Number of minutes, from now, to snooze until.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dnd_set_snooze(
                content_type, token, num_minutes, request_options=request_options
            )
        ).unwrap()

    async def dnd_team_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Retrieves the Do Not Disturb status for up to 50 users on a team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:read``
            users: Comma-separated list of users to fetch Do Not Disturb status for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dnd_team_info(
                content_type, token=token, users=users, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDndWithRawResponse:
        return self._with_raw_response


class DndWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def dnd_end_dnd(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DndEndDndschema, RawError]:
        """Ends the current user's Do Not Disturb session immediately.

        Args:
            token: Authentication token. Requires scope: ``dnd:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/dnd.endDnd"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DndEndDndschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def dnd_end_snooze(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DndEndSnoozeschema, RawError]:
        """Ends the current user's snooze mode immediately.

        Args:
            token: Authentication token. Requires scope: ``dnd:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/dnd.endSnooze"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DndEndSnoozeschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def dnd_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DndInfoschema, RawError]:
        """Retrieves a user's current Do Not Disturb status.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:read``
            user: User to fetch status for (defaults to current user)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/dnd.info"),
            query_params=[param[str | None]("token", token), param[str | None]("user", user)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DndInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def dnd_set_snooze(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        num_minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DndSetSnoozeschema, RawError]:
        """Turns on Do Not Disturb mode for the current user, or changes its duration.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:write``
            num_minutes: Number of minutes, from now, to snooze until.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/dnd.setSnooze"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("num_minutes", num_minutes)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DndSetSnoozeschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def dnd_team_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Retrieves the Do Not Disturb status for up to 50 users on a team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:read``
            users: Comma-separated list of users to fetch Do Not Disturb status for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/dnd.teamInfo"),
            query_params=[param[str | None]("token", token), param[str | None]("users", users)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDndWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def dnd_end_dnd(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DndEndDndschema, RawError]:
        """Ends the current user's Do Not Disturb session immediately.

        Args:
            token: Authentication token. Requires scope: ``dnd:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/dnd.endDnd"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DndEndDndschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def dnd_end_snooze(
        self, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DndEndSnoozeschema, RawError]:
        """Ends the current user's snooze mode immediately.

        Args:
            token: Authentication token. Requires scope: ``dnd:write``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/dnd.endSnooze"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DndEndSnoozeschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def dnd_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        user: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DndInfoschema, RawError]:
        """Retrieves a user's current Do Not Disturb status.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:read``
            user: User to fetch status for (defaults to current user)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/dnd.info"),
            query_params=[param[str | None]("token", token), param[str | None]("user", user)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DndInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def dnd_set_snooze(
        self,
        content_type: ContentTypeOrStr,
        token: str,
        num_minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DndSetSnoozeschema, RawError]:
        """Turns on Do Not Disturb mode for the current user, or changes its duration.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:write``
            num_minutes: Number of minutes, from now, to snooze until.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/dnd.setSnooze"),
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("token", token), param[str]("num_minutes", num_minutes)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[DndSetSnoozeschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def dnd_team_info(
        self,
        content_type: ContentTypeOrStr,
        *,
        token: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Retrieves the Do Not Disturb status for up to 50 users on a team.

        Args:
            content_type: Value sent with the request.
            token: Authentication token. Requires scope: ``dnd:read``
            users: Comma-separated list of users to fetch Do Not Disturb status for
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/dnd.teamInfo"),
            query_params=[param[str | None]("token", token), param[str | None]("users", users)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
