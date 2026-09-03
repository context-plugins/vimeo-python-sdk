from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_live_event_whitelist_alt1_error import (
    GetLiveEventWhitelistAlt1ErrorBody,
    get_live_event_whitelist_alt1_error_mapper,
)
from ..errors.get_live_event_whitelist_alt2_error import (
    GetLiveEventWhitelistAlt2ErrorBody,
    get_live_event_whitelist_alt2_error_mapper,
)
from ..errors.get_live_event_whitelist_error import (
    GetLiveEventWhitelistErrorBody,
    get_live_event_whitelist_error_mapper,
)
from ..errors.set_live_event_whitelist_alt1_error import (
    SetLiveEventWhitelistAlt1ErrorBody,
    set_live_event_whitelist_alt1_error_mapper,
)
from ..errors.set_live_event_whitelist_alt2_error import (
    SetLiveEventWhitelistAlt2ErrorBody,
    set_live_event_whitelist_alt2_error_mapper,
)
from ..errors.set_live_event_whitelist_error import (
    SetLiveEventWhitelistErrorBody,
    set_live_event_whitelist_error_mapper,
)
from ..models.domain_connection import DomainConnection
from ..models.live_events_privacy_domains_request import (
    LiveEventsPrivacyDomainsRequest,
    LiveEventsPrivacyDomainsRequestDict,
)
from ..models.me_live_events_privacy_domains_request import (
    MeLiveEventsPrivacyDomainsRequest,
    MeLiveEventsPrivacyDomainsRequestDict,
)
from ..models.users_live_events_privacy_domains_request import (
    UsersLiveEventsPrivacyDomainsRequest,
    UsersLiveEventsPrivacyDomainsRequestDict,
)
from ..server.server import Server


class LiveEmbedPrivacy:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEmbedPrivacyWithRawResponse(client, server, auth)

    def get_live_event_whitelist(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> DomainConnection:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The permitted domains for the event were returned.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't get domains for the event. Error code 5000: No such event exists. Error code 4016: An unexpected
                error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_live_event_whitelist(
            live_event_id, user_id, request_options=request_options
        ).unwrap()

    def get_live_event_whitelist_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> DomainConnection:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The permitted domains for the event were returned.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't get domains for the event. Error code 5000: No such event exists. Error code 4016: An unexpected
                error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_live_event_whitelist_alt1(
            live_event_id, request_options=request_options
        ).unwrap()

    def get_live_event_whitelist_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> DomainConnection:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The permitted domains for the event were returned.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't get domains for the event. Error code 5000: No such event exists. Error code 4016: An unexpected
                error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_live_event_whitelist_alt2(
            live_event_id, request_options=request_options
        ).unwrap()

    def set_live_event_whitelist(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPrivacyDomainsRequest | UsersLiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was embedded on the specified domains.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't edit domains for the event. Error code 5000: No such event exists under the user. Error code 4016:
                An unexpected error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.set_live_event_whitelist(
            live_event_id, user_id, body=body, request_options=request_options
        ).unwrap()

    def set_live_event_whitelist_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsPrivacyDomainsRequest | LiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was embedded on the specified domains.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't edit domains for the event. Error code 5000: No such event exists under the user. Error code 4016:
                An unexpected error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.set_live_event_whitelist_alt1(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    def set_live_event_whitelist_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsPrivacyDomainsRequest | MeLiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was embedded on the specified domains.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't edit domains for the event. Error code 5000: No such event exists under the user. Error code 4016:
                An unexpected error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.set_live_event_whitelist_alt2(
            live_event_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveEmbedPrivacyWithRawResponse:
        return self._with_raw_response


class AsyncLiveEmbedPrivacy:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEmbedPrivacyWithRawResponse(client, server, auth)

    async def get_live_event_whitelist(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> DomainConnection:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The permitted domains for the event were returned.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't get domains for the event. Error code 5000: No such event exists. Error code 4016: An unexpected
                error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_live_event_whitelist(
                live_event_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def get_live_event_whitelist_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> DomainConnection:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The permitted domains for the event were returned.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't get domains for the event. Error code 5000: No such event exists. Error code 4016: An unexpected
                error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_live_event_whitelist_alt1(live_event_id, request_options=request_options)
        ).unwrap()

    async def get_live_event_whitelist_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> DomainConnection:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The permitted domains for the event were returned.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't get domains for the event. Error code 5000: No such event exists. Error code 4016: An unexpected
                error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_live_event_whitelist_alt2(live_event_id, request_options=request_options)
        ).unwrap()

    async def set_live_event_whitelist(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPrivacyDomainsRequest | UsersLiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was embedded on the specified domains.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't edit domains for the event. Error code 5000: No such event exists under the user. Error code 4016:
                An unexpected error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_live_event_whitelist(
                live_event_id, user_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def set_live_event_whitelist_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsPrivacyDomainsRequest | LiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was embedded on the specified domains.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't edit domains for the event. Error code 5000: No such event exists under the user. Error code 4016:
                An unexpected error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_live_event_whitelist_alt1(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def set_live_event_whitelist_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsPrivacyDomainsRequest | MeLiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event was embedded on the specified domains.

        Raises:
            ApiError: Error code 2518: The embed permission isn't ``whitelist``. Error code 3200: The authenticated user
                can't edit domains for the event. Error code 5000: No such event exists under the user. Error code 4016:
                An unexpected error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_live_event_whitelist_alt2(
                live_event_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveEmbedPrivacyWithRawResponse:
        return self._with_raw_response


class LiveEmbedPrivacyWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_live_event_whitelist(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DomainConnection, GetLiveEventWhitelistErrorBody]:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[DomainConnection],
            error_mapper=get_live_event_whitelist_error_mapper,
            request_options=request_options,
        )

    def get_live_event_whitelist_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DomainConnection, GetLiveEventWhitelistAlt1ErrorBody]:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[DomainConnection],
            error_mapper=get_live_event_whitelist_alt1_error_mapper,
            request_options=request_options,
        )

    def get_live_event_whitelist_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DomainConnection, GetLiveEventWhitelistAlt2ErrorBody]:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[DomainConnection],
            error_mapper=get_live_event_whitelist_alt2_error_mapper,
            request_options=request_options,
        )

    def set_live_event_whitelist(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPrivacyDomainsRequest | UsersLiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SetLiveEventWhitelistErrorBody]:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsPrivacyDomainsRequest | UsersLiveEventsPrivacyDomainsRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=set_live_event_whitelist_error_mapper,
            request_options=request_options,
        )

    def set_live_event_whitelist_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsPrivacyDomainsRequest | LiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SetLiveEventWhitelistAlt1ErrorBody]:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsPrivacyDomainsRequest | LiveEventsPrivacyDomainsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=set_live_event_whitelist_alt1_error_mapper,
            request_options=request_options,
        )

    def set_live_event_whitelist_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsPrivacyDomainsRequest | MeLiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SetLiveEventWhitelistAlt2ErrorBody]:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsPrivacyDomainsRequest | MeLiveEventsPrivacyDomainsRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=set_live_event_whitelist_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEmbedPrivacyWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_live_event_whitelist(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DomainConnection, GetLiveEventWhitelistErrorBody]:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[DomainConnection],
            error_mapper=get_live_event_whitelist_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_whitelist_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DomainConnection, GetLiveEventWhitelistAlt1ErrorBody]:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[DomainConnection],
            error_mapper=get_live_event_whitelist_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_whitelist_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DomainConnection, GetLiveEventWhitelistAlt2ErrorBody]:
        """This method returns every permitted domain for an event. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[DomainConnection],
            error_mapper=get_live_event_whitelist_alt2_error_mapper,
            request_options=request_options,
        )

    async def set_live_event_whitelist(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsPrivacyDomainsRequest | UsersLiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SetLiveEventWhitelistErrorBody]:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsPrivacyDomainsRequest | UsersLiveEventsPrivacyDomainsRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=set_live_event_whitelist_error_mapper,
            request_options=request_options,
        )

    async def set_live_event_whitelist_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsPrivacyDomainsRequest | LiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SetLiveEventWhitelistAlt1ErrorBody]:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsPrivacyDomainsRequest | LiveEventsPrivacyDomainsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=set_live_event_whitelist_alt1_error_mapper,
            request_options=request_options,
        )

    async def set_live_event_whitelist_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsPrivacyDomainsRequest | MeLiveEventsPrivacyDomainsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SetLiveEventWhitelistAlt2ErrorBody]:
        """This method embeds an event on the specified domains. The embed privacy setting must be ``whitelist``.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/me/live_events/{live_event_id}/privacy/domains"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsPrivacyDomainsRequest | MeLiveEventsPrivacyDomainsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=set_live_event_whitelist_alt2_error_mapper,
            request_options=request_options,
        )
