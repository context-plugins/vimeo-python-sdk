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


class Views:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ViewsWithRawResponse(client, server, auth)

    def views_open(
        self,
        trigger_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Open a view for a user.

        Args:
            trigger_id: Exchange a trigger to post to the user.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response includes the opened view payload.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.views_open(
            trigger_id, view, token, content_type, request_options=request_options
        ).unwrap()

    def views_publish(
        self,
        user_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        hash: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Publish a static view for a User.

        Args:
            user_id: ``id`` of the user you want publish a view to.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            hash: A string that represents view state to protect against possible race conditions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response includes the published view payload.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.views_publish(
            user_id, view, token, content_type, hash=hash, request_options=request_options
        ).unwrap()

    def views_push(
        self,
        trigger_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Push a view onto the stack of a root view.

        Args:
            trigger_id: Exchange a trigger to post to the user.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response includes the pushed view payload.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.views_push(
            trigger_id, view, token, content_type, request_options=request_options
        ).unwrap()

    def views_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        view_id: str | None = None,
        external_id: str | None = None,
        view: str | None = None,
        hash: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Update an existing view.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            view_id: A unique identifier of the view to be updated. Either ``view_id`` or ``external_id`` is required.
            external_id: A unique identifier of the view set by the developer. Must be unique for all views on a team.
                Max length of 255 characters. Either ``view_id`` or ``external_id`` is required.
            view: A `view object </reference/surfaces/views>`__. This must be a JSON-encoded string.
            hash: A string that represents view state to protect against possible race conditions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response includes the updated view payload.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.views_update(
            token,
            content_type,
            view_id=view_id,
            external_id=external_id,
            view=view,
            hash=hash,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ViewsWithRawResponse:
        return self._with_raw_response


class AsyncViews:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncViewsWithRawResponse(client, server, auth)

    async def views_open(
        self,
        trigger_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Open a view for a user.

        Args:
            trigger_id: Exchange a trigger to post to the user.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response includes the opened view payload.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.views_open(
                trigger_id, view, token, content_type, request_options=request_options
            )
        ).unwrap()

    async def views_publish(
        self,
        user_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        hash: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Publish a static view for a User.

        Args:
            user_id: ``id`` of the user you want publish a view to.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            hash: A string that represents view state to protect against possible race conditions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response includes the published view payload.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.views_publish(
                user_id, view, token, content_type, hash=hash, request_options=request_options
            )
        ).unwrap()

    async def views_push(
        self,
        trigger_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Push a view onto the stack of a root view.

        Args:
            trigger_id: Exchange a trigger to post to the user.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response includes the pushed view payload.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.views_push(
                trigger_id, view, token, content_type, request_options=request_options
            )
        ).unwrap()

    async def views_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        view_id: str | None = None,
        external_id: str | None = None,
        view: str | None = None,
        hash: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Update an existing view.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            view_id: A unique identifier of the view to be updated. Either ``view_id`` or ``external_id`` is required.
            external_id: A unique identifier of the view set by the developer. Must be unique for all views on a team.
                Max length of 255 characters. Either ``view_id`` or ``external_id`` is required.
            view: A `view object </reference/surfaces/views>`__. This must be a JSON-encoded string.
            hash: A string that represents view state to protect against possible race conditions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response includes the updated view payload.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.views_update(
                token,
                content_type,
                view_id=view_id,
                external_id=external_id,
                view=view,
                hash=hash,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncViewsWithRawResponse:
        return self._with_raw_response


class ViewsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def views_open(
        self,
        trigger_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Open a view for a user.

        Args:
            trigger_id: Exchange a trigger to post to the user.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/views.open"),
            query_params=[param[str]("trigger_id", trigger_id), param[str]("view", view)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def views_publish(
        self,
        user_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        hash: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Publish a static view for a User.

        Args:
            user_id: ``id`` of the user you want publish a view to.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            hash: A string that represents view state to protect against possible race conditions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/views.publish"),
            query_params=[param[str]("user_id", user_id), param[str]("view", view), param[str | None]("hash", hash)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def views_push(
        self,
        trigger_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Push a view onto the stack of a root view.

        Args:
            trigger_id: Exchange a trigger to post to the user.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/views.push"),
            query_params=[param[str]("trigger_id", trigger_id), param[str]("view", view)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def views_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        view_id: str | None = None,
        external_id: str | None = None,
        view: str | None = None,
        hash: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Update an existing view.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            view_id: A unique identifier of the view to be updated. Either ``view_id`` or ``external_id`` is required.
            external_id: A unique identifier of the view set by the developer. Must be unique for all views on a team.
                Max length of 255 characters. Either ``view_id`` or ``external_id`` is required.
            view: A `view object </reference/surfaces/views>`__. This must be a JSON-encoded string.
            hash: A string that represents view state to protect against possible race conditions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/views.update"),
            query_params=[
                param[str | None]("view_id", view_id),
                param[str | None]("external_id", external_id),
                param[str | None]("view", view),
                param[str | None]("hash", hash),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncViewsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def views_open(
        self,
        trigger_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Open a view for a user.

        Args:
            trigger_id: Exchange a trigger to post to the user.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/views.open"),
            query_params=[param[str]("trigger_id", trigger_id), param[str]("view", view)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def views_publish(
        self,
        user_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        hash: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Publish a static view for a User.

        Args:
            user_id: ``id`` of the user you want publish a view to.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            hash: A string that represents view state to protect against possible race conditions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/views.publish"),
            query_params=[param[str]("user_id", user_id), param[str]("view", view), param[str | None]("hash", hash)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def views_push(
        self,
        trigger_id: str,
        view: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Push a view onto the stack of a root view.

        Args:
            trigger_id: Exchange a trigger to post to the user.
            view: A `view payload </reference/surfaces/views>`__. This must be a JSON-encoded string.
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/views.push"),
            query_params=[param[str]("trigger_id", trigger_id), param[str]("view", view)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def views_update(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        view_id: str | None = None,
        external_id: str | None = None,
        view: str | None = None,
        hash: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Update an existing view.

        Args:
            token: Authentication token. Requires scope: ``none``
            content_type: Value sent with the request.
            view_id: A unique identifier of the view to be updated. Either ``view_id`` or ``external_id`` is required.
            external_id: A unique identifier of the view set by the developer. Must be unique for all views on a team.
                Max length of 255 characters. Either ``view_id`` or ``external_id`` is required.
            view: A `view object </reference/surfaces/views>`__. This must be a JSON-encoded string.
            hash: A string that represents view state to protect against possible race conditions.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/views.update"),
            query_params=[
                param[str | None]("view_id", view_id),
                param[str | None]("external_id", external_id),
                param[str | None]("view", view),
                param[str | None]("hash", hash),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
