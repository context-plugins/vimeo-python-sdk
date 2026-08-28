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


class Calls:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CallsWithRawResponse(client, server, auth)

    def calls_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        external_unique_id: str,
        join_url: str,
        *,
        external_display_id: str | None = None,
        desktop_app_join_url: str | None = None,
        date_start: int | None = None,
        title: str | None = None,
        created_by: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers a new Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            external_unique_id: An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from
                that service.
            join_url: The URL required for a client to join the Call.
            external_display_id: An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied,
                this ID will be displayed in the Call object.
            desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party
                Call with this URL.
            date_start: Call start time in UTC UNIX timestamp format
            title: The name of the Call.
            created_by: The valid Slack user ID of the user who created this Call. When this method is called with a
                user token, the ``created_by`` field is optional and defaults to the authed user of the token.
                Otherwise, the field is required.
            users: The list of users to register as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.calls_add(
            token,
            content_type,
            external_unique_id,
            join_url,
            external_display_id=external_display_id,
            desktop_app_join_url=desktop_app_join_url,
            date_start=date_start,
            title=title,
            created_by=created_by,
            users=users,
            request_options=request_options,
        ).unwrap()

    def calls_end(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        *,
        duration: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Ends a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned when registering the call using the /methods/calls.add method.
            duration: Call duration in seconds
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.calls_end(
            token, content_type, id, duration=duration, request_options=request_options
        ).unwrap()

    def calls_info(
        self,
        id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Returns information about a Call.

        Args:
            id: ``id`` of the Call returned by the /methods/calls.add method.
            token: Authentication token. Requires scope: ``calls:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.calls_info(id, token, content_type, request_options=request_options).unwrap()

    def calls_participants_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers new participants added to a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            users: The list of users to add as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.calls_participants_add(
            token, content_type, id, users, request_options=request_options
        ).unwrap()

    def calls_participants_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers participants removed from a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            users: The list of users to remove as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.calls_participants_remove(
            token, content_type, id, users, request_options=request_options
        ).unwrap()

    def calls_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        *,
        title: str | None = None,
        join_url: str | None = None,
        desktop_app_join_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Updates information about a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            title: The name of the Call.
            join_url: The URL required for a client to join the Call.
            desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party
                Call with this URL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.calls_update(
            token,
            content_type,
            id,
            title=title,
            join_url=join_url,
            desktop_app_join_url=desktop_app_join_url,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> CallsWithRawResponse:
        return self._with_raw_response


class AsyncCalls:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCallsWithRawResponse(client, server, auth)

    async def calls_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        external_unique_id: str,
        join_url: str,
        *,
        external_display_id: str | None = None,
        desktop_app_join_url: str | None = None,
        date_start: int | None = None,
        title: str | None = None,
        created_by: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers a new Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            external_unique_id: An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from
                that service.
            join_url: The URL required for a client to join the Call.
            external_display_id: An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied,
                this ID will be displayed in the Call object.
            desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party
                Call with this URL.
            date_start: Call start time in UTC UNIX timestamp format
            title: The name of the Call.
            created_by: The valid Slack user ID of the user who created this Call. When this method is called with a
                user token, the ``created_by`` field is optional and defaults to the authed user of the token.
                Otherwise, the field is required.
            users: The list of users to register as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.calls_add(
                token,
                content_type,
                external_unique_id,
                join_url,
                external_display_id=external_display_id,
                desktop_app_join_url=desktop_app_join_url,
                date_start=date_start,
                title=title,
                created_by=created_by,
                users=users,
                request_options=request_options,
            )
        ).unwrap()

    async def calls_end(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        *,
        duration: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Ends a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned when registering the call using the /methods/calls.add method.
            duration: Call duration in seconds
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.calls_end(
                token, content_type, id, duration=duration, request_options=request_options
            )
        ).unwrap()

    async def calls_info(
        self,
        id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Returns information about a Call.

        Args:
            id: ``id`` of the Call returned by the /methods/calls.add method.
            token: Authentication token. Requires scope: ``calls:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.calls_info(id, token, content_type, request_options=request_options)
        ).unwrap()

    async def calls_participants_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers new participants added to a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            users: The list of users to add as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.calls_participants_add(
                token, content_type, id, users, request_options=request_options
            )
        ).unwrap()

    async def calls_participants_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers participants removed from a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            users: The list of users to remove as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.calls_participants_remove(
                token, content_type, id, users, request_options=request_options
            )
        ).unwrap()

    async def calls_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        *,
        title: str | None = None,
        join_url: str | None = None,
        desktop_app_join_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Updates information about a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            title: The name of the Call.
            join_url: The URL required for a client to join the Call.
            desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party
                Call with this URL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.calls_update(
                token,
                content_type,
                id,
                title=title,
                join_url=join_url,
                desktop_app_join_url=desktop_app_join_url,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCallsWithRawResponse:
        return self._with_raw_response


class CallsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def calls_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        external_unique_id: str,
        join_url: str,
        *,
        external_display_id: str | None = None,
        desktop_app_join_url: str | None = None,
        date_start: int | None = None,
        title: str | None = None,
        created_by: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers a new Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            external_unique_id: An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from
                that service.
            join_url: The URL required for a client to join the Call.
            external_display_id: An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied,
                this ID will be displayed in the Call object.
            desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party
                Call with this URL.
            date_start: Call start time in UTC UNIX timestamp format
            title: The name of the Call.
            created_by: The valid Slack user ID of the user who created this Call. When this method is called with a
                user token, the ``created_by`` field is optional and defaults to the authed user of the token.
                Otherwise, the field is required.
            users: The list of users to register as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("external_unique_id", external_unique_id),
                    param[str]("join_url", join_url),
                    param[str | None]("external_display_id", external_display_id),
                    param[str | None]("desktop_app_join_url", desktop_app_join_url),
                    param[int | None]("date_start", date_start),
                    param[str | None]("title", title),
                    param[str | None]("created_by", created_by),
                    param[str | None]("users", users),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def calls_end(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        *,
        duration: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Ends a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned when registering the call using the /methods/calls.add method.
            duration: Call duration in seconds
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.end"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("id", id), param[int | None]("duration", duration)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def calls_info(
        self,
        id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Returns information about a Call.

        Args:
            id: ``id`` of the Call returned by the /methods/calls.add method.
            token: Authentication token. Requires scope: ``calls:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/calls.info"),
            query_params=[param[str]("id", id)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def calls_participants_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers new participants added to a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            users: The list of users to add as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.participants.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("id", id), param[str]("users", users)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def calls_participants_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers participants removed from a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            users: The list of users to remove as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.participants.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("id", id), param[str]("users", users)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def calls_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        *,
        title: str | None = None,
        join_url: str | None = None,
        desktop_app_join_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Updates information about a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            title: The name of the Call.
            join_url: The URL required for a client to join the Call.
            desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party
                Call with this URL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.update"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("id", id),
                    param[str | None]("title", title),
                    param[str | None]("join_url", join_url),
                    param[str | None]("desktop_app_join_url", desktop_app_join_url),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCallsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def calls_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        external_unique_id: str,
        join_url: str,
        *,
        external_display_id: str | None = None,
        desktop_app_join_url: str | None = None,
        date_start: int | None = None,
        title: str | None = None,
        created_by: str | None = None,
        users: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers a new Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            external_unique_id: An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from
                that service.
            join_url: The URL required for a client to join the Call.
            external_display_id: An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied,
                this ID will be displayed in the Call object.
            desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party
                Call with this URL.
            date_start: Call start time in UTC UNIX timestamp format
            title: The name of the Call.
            created_by: The valid Slack user ID of the user who created this Call. When this method is called with a
                user token, the ``created_by`` field is optional and defaults to the authed user of the token.
                Otherwise, the field is required.
            users: The list of users to register as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("external_unique_id", external_unique_id),
                    param[str]("join_url", join_url),
                    param[str | None]("external_display_id", external_display_id),
                    param[str | None]("desktop_app_join_url", desktop_app_join_url),
                    param[int | None]("date_start", date_start),
                    param[str | None]("title", title),
                    param[str | None]("created_by", created_by),
                    param[str | None]("users", users),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def calls_end(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        *,
        duration: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Ends a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned when registering the call using the /methods/calls.add method.
            duration: Call duration in seconds
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.end"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("id", id), param[int | None]("duration", duration)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def calls_info(
        self,
        id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Returns information about a Call.

        Args:
            id: ``id`` of the Call returned by the /methods/calls.add method.
            token: Authentication token. Requires scope: ``calls:read``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/calls.info"),
            query_params=[param[str]("id", id)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def calls_participants_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers new participants added to a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            users: The list of users to add as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.participants.add"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("id", id), param[str]("users", users)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def calls_participants_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers participants removed from a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            users: The list of users to remove as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.participants.remove"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body([param[str]("id", id), param[str]("users", users)]),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def calls_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id: str,
        *,
        title: str | None = None,
        join_url: str | None = None,
        desktop_app_join_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Updates information about a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id: ``id`` returned by the /methods/calls.add method.
            title: The name of the Call.
            join_url: The URL required for a client to join the Call.
            desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party
                Call with this URL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.update"),
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            body=form_body(
                [
                    param[str]("id", id),
                    param[str | None]("title", title),
                    param[str | None]("join_url", join_url),
                    param[str | None]("desktop_app_join_url", desktop_app_join_url),
                ],
            ),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
