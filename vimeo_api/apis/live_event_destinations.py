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
from ..errors.create_live_event_destination_alt1_error import (
    CreateLiveEventDestinationAlt1ErrorBody,
    create_live_event_destination_alt1_error_mapper,
)
from ..errors.create_live_event_destination_error import (
    CreateLiveEventDestinationErrorBody,
    create_live_event_destination_error_mapper,
)
from ..errors.create_ott_destination_error import CreateOttDestinationErrorBody, create_ott_destination_error_mapper
from ..errors.delete_live_event_destination_error import (
    DeleteLiveEventDestinationErrorBody,
    delete_live_event_destination_error_mapper,
)
from ..errors.delete_ott_destination_error import DeleteOttDestinationErrorBody, delete_ott_destination_error_mapper
from ..errors.get_available_destinations_alt1_error import (
    GetAvailableDestinationsAlt1ErrorBody,
    get_available_destinations_alt1_error_mapper,
)
from ..errors.get_available_destinations_error import (
    GetAvailableDestinationsErrorBody,
    get_available_destinations_error_mapper,
)
from ..errors.get_live_event_destination_error import (
    GetLiveEventDestinationErrorBody,
    get_live_event_destination_error_mapper,
)
from ..errors.get_live_event_destinations_alt1_error import (
    GetLiveEventDestinationsAlt1ErrorBody,
    get_live_event_destinations_alt1_error_mapper,
)
from ..errors.get_live_event_destinations_error import (
    GetLiveEventDestinationsErrorBody,
    get_live_event_destinations_error_mapper,
)
from ..errors.get_ott_destinations_error import GetOttDestinationsErrorBody, get_ott_destinations_error_mapper
from ..errors.update_live_event_destination_error import (
    UpdateLiveEventDestinationErrorBody,
    update_live_event_destination_error_mapper,
)
from ..models.destination_request import DestinationRequest, DestinationRequestDict
from ..models.event_destination import EventDestination
from ..models.event_destination_connection import EventDestinationConnection
from ..models.me_live_events_destinations_request import (
    MeLiveEventsDestinationsRequest,
    MeLiveEventsDestinationsRequestDict,
)
from ..models.ott_destination import OttDestination
from ..models.ott_destination_connection import OttDestinationConnection
from ..models.users_live_events_destinations_request import (
    UsersLiveEventsDestinationsRequest,
    UsersLiveEventsDestinationsRequestDict,
)
from ..server.server import Server


class LiveEventDestinations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEventDestinationsWithRawResponse(client, server, auth)

    def create_live_event_destination(
        self,
        live_event_id: float,
        body: MeLiveEventsDestinationsRequest | MeLiveEventsDestinationsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventDestination:
        """This method creates a destination for the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was created.

        Raises:
            ApiError: * Error code 2204: Parameters are missing, or the body data is invalid. * Error code 13003: You
                can create only one LinkedIn destination per event. * Error code 13004: You can create only one YouTube
                destination per event. * Error code 13008: The Facebook destination is currently connected to someone
                else. Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destinations. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.create_live_event_destination(
            live_event_id, body, request_options=request_options
        ).unwrap()

    def create_live_event_destination_alt1(
        self,
        live_event_id: float,
        user_id: float,
        body: UsersLiveEventsDestinationsRequest | UsersLiveEventsDestinationsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventDestination:
        """This method creates a destination for the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was created.

        Raises:
            ApiError: * Error code 2204: Parameters are missing, or the body data is invalid. * Error code 13003: You
                can create only one LinkedIn destination per event. * Error code 13004: You can create only one YouTube
                destination per event. * Error code 13008: The Facebook destination is currently connected to someone
                else. Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destinations. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.create_live_event_destination_alt1(
            live_event_id, user_id, body, request_options=request_options
        ).unwrap()

    def create_ott_destination(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OttDestination:
        """This method creates an OTT channel as the destination of the specified event. The authenticated user must be
        the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The new OTT destination was created.

        Raises:
            ApiError: Error code 2204: A parameter is missing, or the body data is invalid. Error code 8000: The user
                credentials are invalid. Error code 3200: The authenticated user can't access the event destination. *
                Error code 5000: No such event or user exists. * Error code 5018: The user doesn't have any OTT
                metadata. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.create_ott_destination(
            live_event_id, user_id, request_options=request_options
        ).unwrap()

    def delete_live_event_destination(
        self, destination_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was deleted.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destination. Error code 5000: No such event destination exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.delete_live_event_destination(
            destination_id, request_options=request_options
        ).unwrap()

    def delete_ott_destination(
        self,
        live_event_id: float,
        user_id: float,
        destination_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes an OTT channel as the destination of the specified event. The authenticated user must be
        the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            destination_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The OTT destination was deleted.

        Raises:
            ApiError: Error code 2204: A parameter is missing, or the body data is invalid. Error code 8000: The user
                credentials are invalid. Error code 3200: The authenticated user can't access the event destination. *
                Error code 5000: No such event or user exists. * Error code 5018: The user doesn't have any OTT
                metadata. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.delete_ott_destination(
            live_event_id, user_id, destination_id, request_options=request_options
        ).unwrap()

    def get_available_destinations(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns every available event destination for the authenticated user to stream to.

        Args:
            user_id: The user ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destinations were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. * Error code 3200: The authenticated user can't
                get the available destinations. * Error code 3422: The authenticated user can't live simulcast.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_available_destinations(user_id, request_options=request_options).unwrap()

    def get_available_destinations_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns every available event destination for the authenticated user to stream to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destinations were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. * Error code 3200: The authenticated user can't
                get the available destinations. * Error code 3422: The authenticated user can't live simulcast.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_available_destinations_alt1(request_options=request_options).unwrap()

    def get_live_event_destination(
        self, destination_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventDestination:
        """This method returns the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destination. Error code 5000: No such event destination exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_live_event_destination(
            destination_id, request_options=request_options
        ).unwrap()

    def get_live_event_destinations(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventDestinationConnection:
        """This method returns every destination of the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destinations were returned.

        Raises:
            ApiError: Error code 2204: Parameters are missing, or the body data is invalid. Error code 8000: The user
                credentials are invalid. Error code 3200: The authenticated user can't access the event destination.
                Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_live_event_destinations(
            live_event_id, request_options=request_options
        ).unwrap()

    def get_live_event_destinations_alt1(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventDestinationConnection:
        """This method returns every destination of the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destinations were returned.

        Raises:
            ApiError: Error code 2204: Parameters are missing, or the body data is invalid. Error code 8000: The user
                credentials are invalid. Error code 3200: The authenticated user can't access the event destination.
                Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_live_event_destinations_alt1(
            live_event_id, user_id, request_options=request_options
        ).unwrap()

    def get_ott_destinations(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OttDestinationConnection:
        """This method returns every OTT destination of the specified event. The authenticated user must be the owner of
        the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The OTT destinations were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destination. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.get_ott_destinations(
            live_event_id, user_id, request_options=request_options
        ).unwrap()

    def update_live_event_destination(
        self,
        destination_id: float,
        *,
        body: DestinationRequest | DestinationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventDestination:
        """This method updates the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was updated.

        Raises:
            ApiError: * Error code 13000: The RTMP URL and key are already being used for one of the authenticated
                user's events. * Error code 13001: The authenticated user can simulcast on up to 20 custom RTMP
                destinations at once. * Error code 13002: The authenticated user can simulcast on up to 10 destinations
                on Facebook, YouTube, or LinkedIn. Error code 8000: The user credentials are invalid. Error code 3200:
                The authenticated user can't access the event destination. Error code 5000: No such event destination
                exists. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.update_live_event_destination(
            destination_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> LiveEventDestinationsWithRawResponse:
        return self._with_raw_response


class AsyncLiveEventDestinations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEventDestinationsWithRawResponse(client, server, auth)

    async def create_live_event_destination(
        self,
        live_event_id: float,
        body: MeLiveEventsDestinationsRequest | MeLiveEventsDestinationsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventDestination:
        """This method creates a destination for the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was created.

        Raises:
            ApiError: * Error code 2204: Parameters are missing, or the body data is invalid. * Error code 13003: You
                can create only one LinkedIn destination per event. * Error code 13004: You can create only one YouTube
                destination per event. * Error code 13008: The Facebook destination is currently connected to someone
                else. Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destinations. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.create_live_event_destination(
                live_event_id, body, request_options=request_options
            )
        ).unwrap()

    async def create_live_event_destination_alt1(
        self,
        live_event_id: float,
        user_id: float,
        body: UsersLiveEventsDestinationsRequest | UsersLiveEventsDestinationsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventDestination:
        """This method creates a destination for the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was created.

        Raises:
            ApiError: * Error code 2204: Parameters are missing, or the body data is invalid. * Error code 13003: You
                can create only one LinkedIn destination per event. * Error code 13004: You can create only one YouTube
                destination per event. * Error code 13008: The Facebook destination is currently connected to someone
                else. Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destinations. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.create_live_event_destination_alt1(
                live_event_id, user_id, body, request_options=request_options
            )
        ).unwrap()

    async def create_ott_destination(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OttDestination:
        """This method creates an OTT channel as the destination of the specified event. The authenticated user must be
        the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The new OTT destination was created.

        Raises:
            ApiError: Error code 2204: A parameter is missing, or the body data is invalid. Error code 8000: The user
                credentials are invalid. Error code 3200: The authenticated user can't access the event destination. *
                Error code 5000: No such event or user exists. * Error code 5018: The user doesn't have any OTT
                metadata. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.create_ott_destination(
                live_event_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def delete_live_event_destination(
        self, destination_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was deleted.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destination. Error code 5000: No such event destination exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.delete_live_event_destination(destination_id, request_options=request_options)
        ).unwrap()

    async def delete_ott_destination(
        self,
        live_event_id: float,
        user_id: float,
        destination_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes an OTT channel as the destination of the specified event. The authenticated user must be
        the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            destination_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The OTT destination was deleted.

        Raises:
            ApiError: Error code 2204: A parameter is missing, or the body data is invalid. Error code 8000: The user
                credentials are invalid. Error code 3200: The authenticated user can't access the event destination. *
                Error code 5000: No such event or user exists. * Error code 5018: The user doesn't have any OTT
                metadata. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.delete_ott_destination(
                live_event_id, user_id, destination_id, request_options=request_options
            )
        ).unwrap()

    async def get_available_destinations(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns every available event destination for the authenticated user to stream to.

        Args:
            user_id: The user ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destinations were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. * Error code 3200: The authenticated user can't
                get the available destinations. * Error code 3422: The authenticated user can't live simulcast.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_available_destinations(user_id, request_options=request_options)
        ).unwrap()

    async def get_available_destinations_alt1(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns every available event destination for the authenticated user to stream to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destinations were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. * Error code 3200: The authenticated user can't
                get the available destinations. * Error code 3422: The authenticated user can't live simulcast.
                ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.get_available_destinations_alt1(request_options=request_options)).unwrap()

    async def get_live_event_destination(
        self, destination_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventDestination:
        """This method returns the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destination. Error code 5000: No such event destination exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_live_event_destination(destination_id, request_options=request_options)
        ).unwrap()

    async def get_live_event_destinations(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventDestinationConnection:
        """This method returns every destination of the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destinations were returned.

        Raises:
            ApiError: Error code 2204: Parameters are missing, or the body data is invalid. Error code 8000: The user
                credentials are invalid. Error code 3200: The authenticated user can't access the event destination.
                Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_live_event_destinations(live_event_id, request_options=request_options)
        ).unwrap()

    async def get_live_event_destinations_alt1(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventDestinationConnection:
        """This method returns every destination of the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destinations were returned.

        Raises:
            ApiError: Error code 2204: Parameters are missing, or the body data is invalid. Error code 8000: The user
                credentials are invalid. Error code 3200: The authenticated user can't access the event destination.
                Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_live_event_destinations_alt1(
                live_event_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def get_ott_destinations(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> OttDestinationConnection:
        """This method returns every OTT destination of the specified event. The authenticated user must be the owner of
        the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The OTT destinations were returned.

        Raises:
            ApiError: Error code 8000: The user credentials are invalid. Error code 3200: The authenticated user can't
                access the event destination. Error code 5000: No such event or user exists. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.get_ott_destinations(live_event_id, user_id, request_options=request_options)
        ).unwrap()

    async def update_live_event_destination(
        self,
        destination_id: float,
        *,
        body: DestinationRequest | DestinationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventDestination:
        """This method updates the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The event destination was updated.

        Raises:
            ApiError: * Error code 13000: The RTMP URL and key are already being used for one of the authenticated
                user's events. * Error code 13001: The authenticated user can simulcast on up to 20 custom RTMP
                destinations at once. * Error code 13002: The authenticated user can simulcast on up to 10 destinations
                on Facebook, YouTube, or LinkedIn. Error code 8000: The user credentials are invalid. Error code 3200:
                The authenticated user can't access the event destination. Error code 5000: No such event destination
                exists. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.update_live_event_destination(
                destination_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiveEventDestinationsWithRawResponse:
        return self._with_raw_response


class LiveEventDestinationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_live_event_destination(
        self,
        live_event_id: float,
        body: MeLiveEventsDestinationsRequest | MeLiveEventsDestinationsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventDestination, CreateLiveEventDestinationErrorBody]:
        """This method creates a destination for the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/destinations"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsDestinationsRequest | MeLiveEventsDestinationsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestination],
            error_mapper=create_live_event_destination_error_mapper,
            request_options=request_options,
        )

    def create_live_event_destination_alt1(
        self,
        live_event_id: float,
        user_id: float,
        body: UsersLiveEventsDestinationsRequest | UsersLiveEventsDestinationsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventDestination, CreateLiveEventDestinationAlt1ErrorBody]:
        """This method creates a destination for the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/destinations"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsDestinationsRequest | UsersLiveEventsDestinationsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestination],
            error_mapper=create_live_event_destination_alt1_error_mapper,
            request_options=request_options,
        )

    def create_ott_destination(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OttDestination, CreateOttDestinationErrorBody]:
        """This method creates an OTT channel as the destination of the specified event. The authenticated user must be
        the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/ott_destinations"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OttDestination],
            error_mapper=create_ott_destination_error_mapper,
            request_options=request_options,
        )

    def delete_live_event_destination(
        self, destination_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventDestinationErrorBody]:
        """This method deletes the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/destination/{destination_id}"),
            path_params=[param[float]("destination_id", destination_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_event_destination_error_mapper,
            request_options=request_options,
        )

    def delete_ott_destination(
        self,
        live_event_id: float,
        user_id: float,
        destination_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteOttDestinationErrorBody]:
        """This method deletes an OTT channel as the destination of the specified event. The authenticated user must be
        the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            destination_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/users/{user_id}/live_events/{live_event_id}/ott_destination/{destination_id}"
            ),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("user_id", user_id),
                param[str]("destination_id", destination_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_ott_destination_error_mapper,
            request_options=request_options,
        )

    def get_available_destinations(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAvailableDestinationsErrorBody]:
        """This method returns every available event destination for the authenticated user to stream to.

        Args:
            user_id: The user ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/destinations"),
            path_params=[param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_available_destinations_error_mapper,
            request_options=request_options,
        )

    def get_available_destinations_alt1(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAvailableDestinationsAlt1ErrorBody]:
        """This method returns every available event destination for the authenticated user to stream to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/destinations"),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_available_destinations_alt1_error_mapper,
            request_options=request_options,
        )

    def get_live_event_destination(
        self, destination_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventDestination, GetLiveEventDestinationErrorBody]:
        """This method returns the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/destination/{destination_id}"),
            path_params=[param[float]("destination_id", destination_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestination],
            error_mapper=get_live_event_destination_error_mapper,
            request_options=request_options,
        )

    def get_live_event_destinations(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventDestinationConnection, GetLiveEventDestinationsErrorBody]:
        """This method returns every destination of the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/destinations"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestinationConnection],
            error_mapper=get_live_event_destinations_error_mapper,
            request_options=request_options,
        )

    def get_live_event_destinations_alt1(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventDestinationConnection, GetLiveEventDestinationsAlt1ErrorBody]:
        """This method returns every destination of the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/destinations"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestinationConnection],
            error_mapper=get_live_event_destinations_alt1_error_mapper,
            request_options=request_options,
        )

    def get_ott_destinations(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OttDestinationConnection, GetOttDestinationsErrorBody]:
        """This method returns every OTT destination of the specified event. The authenticated user must be the owner of
        the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/ott_destinations"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OttDestinationConnection],
            error_mapper=get_ott_destinations_error_mapper,
            request_options=request_options,
        )

    def update_live_event_destination(
        self,
        destination_id: float,
        *,
        body: DestinationRequest | DestinationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventDestination, UpdateLiveEventDestinationErrorBody]:
        """This method updates the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/destination/{destination_id}"),
            path_params=[param[float]("destination_id", destination_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DestinationRequest | DestinationRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestination],
            error_mapper=update_live_event_destination_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEventDestinationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_live_event_destination(
        self,
        live_event_id: float,
        body: MeLiveEventsDestinationsRequest | MeLiveEventsDestinationsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventDestination, CreateLiveEventDestinationErrorBody]:
        """This method creates a destination for the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events/{live_event_id}/destinations"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsDestinationsRequest | MeLiveEventsDestinationsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestination],
            error_mapper=create_live_event_destination_error_mapper,
            request_options=request_options,
        )

    async def create_live_event_destination_alt1(
        self,
        live_event_id: float,
        user_id: float,
        body: UsersLiveEventsDestinationsRequest | UsersLiveEventsDestinationsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventDestination, CreateLiveEventDestinationAlt1ErrorBody]:
        """This method creates a destination for the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/destinations"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsDestinationsRequest | UsersLiveEventsDestinationsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestination],
            error_mapper=create_live_event_destination_alt1_error_mapper,
            request_options=request_options,
        )

    async def create_ott_destination(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OttDestination, CreateOttDestinationErrorBody]:
        """This method creates an OTT channel as the destination of the specified event. The authenticated user must be
        the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/ott_destinations"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OttDestination],
            error_mapper=create_ott_destination_error_mapper,
            request_options=request_options,
        )

    async def delete_live_event_destination(
        self, destination_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventDestinationErrorBody]:
        """This method deletes the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/destination/{destination_id}"),
            path_params=[param[float]("destination_id", destination_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_event_destination_error_mapper,
            request_options=request_options,
        )

    async def delete_ott_destination(
        self,
        live_event_id: float,
        user_id: float,
        destination_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteOttDestinationErrorBody]:
        """This method deletes an OTT channel as the destination of the specified event. The authenticated user must be
        the owner of the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            destination_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/users/{user_id}/live_events/{live_event_id}/ott_destination/{destination_id}"
            ),
            path_params=[
                param[float]("live_event_id", live_event_id),
                param[float]("user_id", user_id),
                param[str]("destination_id", destination_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_ott_destination_error_mapper,
            request_options=request_options,
        )

    async def get_available_destinations(
        self, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAvailableDestinationsErrorBody]:
        """This method returns every available event destination for the authenticated user to stream to.

        Args:
            user_id: The user ID of the team owner.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/destinations"),
            path_params=[param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_available_destinations_error_mapper,
            request_options=request_options,
        )

    async def get_available_destinations_alt1(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAvailableDestinationsAlt1ErrorBody]:
        """This method returns every available event destination for the authenticated user to stream to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/destinations"),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_available_destinations_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_destination(
        self, destination_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventDestination, GetLiveEventDestinationErrorBody]:
        """This method returns the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/destination/{destination_id}"),
            path_params=[param[float]("destination_id", destination_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestination],
            error_mapper=get_live_event_destination_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_destinations(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventDestinationConnection, GetLiveEventDestinationsErrorBody]:
        """This method returns every destination of the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}/destinations"),
            path_params=[param[float]("live_event_id", live_event_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestinationConnection],
            error_mapper=get_live_event_destinations_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_destinations_alt1(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventDestinationConnection, GetLiveEventDestinationsAlt1ErrorBody]:
        """This method returns every destination of the specified event. The authenticated user must be the owner of the
        event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/destinations"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestinationConnection],
            error_mapper=get_live_event_destinations_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_ott_destinations(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OttDestinationConnection, GetOttDestinationsErrorBody]:
        """This method returns every OTT destination of the specified event. The authenticated user must be the owner of
        the event.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}/ott_destinations"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[OttDestinationConnection],
            error_mapper=get_ott_destinations_error_mapper,
            request_options=request_options,
        )

    async def update_live_event_destination(
        self,
        destination_id: float,
        *,
        body: DestinationRequest | DestinationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventDestination, UpdateLiveEventDestinationErrorBody]:
        """This method updates the specified event destination belonging to the authenticated user.

        Args:
            destination_id: The ID of the event destination.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/destination/{destination_id}"),
            path_params=[param[float]("destination_id", destination_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DestinationRequest | DestinationRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventDestination],
            error_mapper=update_live_event_destination_error_mapper,
            request_options=request_options,
        )
