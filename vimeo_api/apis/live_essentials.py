from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.create_live_event_alt1_error import CreateLiveEventAlt1ErrorBody, create_live_event_alt1_error_mapper
from ..errors.create_live_event_alt2_error import CreateLiveEventAlt2ErrorBody, create_live_event_alt2_error_mapper
from ..errors.create_live_event_error import CreateLiveEventErrorBody, create_live_event_error_mapper
from ..errors.delete_live_event_alt1_error import DeleteLiveEventAlt1ErrorBody, delete_live_event_alt1_error_mapper
from ..errors.delete_live_event_alt2_error import DeleteLiveEventAlt2ErrorBody, delete_live_event_alt2_error_mapper
from ..errors.delete_live_event_error import DeleteLiveEventErrorBody, delete_live_event_error_mapper
from ..errors.delete_live_events_alt1_error import DeleteLiveEventsAlt1ErrorBody, delete_live_events_alt1_error_mapper
from ..errors.delete_live_events_alt2_error import DeleteLiveEventsAlt2ErrorBody, delete_live_events_alt2_error_mapper
from ..errors.delete_live_events_error import DeleteLiveEventsErrorBody, delete_live_events_error_mapper
from ..errors.get_live_event_alt1_error import GetLiveEventAlt1ErrorBody, get_live_event_alt1_error_mapper
from ..errors.get_live_event_alt2_error import GetLiveEventAlt2ErrorBody, get_live_event_alt2_error_mapper
from ..errors.get_live_event_error import GetLiveEventErrorBody, get_live_event_error_mapper
from ..errors.update_live_event_alt1_error import UpdateLiveEventAlt1ErrorBody, update_live_event_alt1_error_mapper
from ..errors.update_live_event_alt2_error import UpdateLiveEventAlt2ErrorBody, update_live_event_alt2_error_mapper
from ..errors.update_live_event_error import UpdateLiveEventErrorBody, update_live_event_error_mapper
from ..models.enums.direction import DirectionOrStr
from ..models.enums.filter8 import Filter8OrStr
from ..models.enums.sort8 import Sort8OrStr
from ..models.enums.type31 import Type31OrStr
from ..models.event_connection import EventConnection
from ..models.live_event_occurrence_connection import LiveEventOccurrenceConnection
from ..models.live_events_request import LiveEventsRequest, LiveEventsRequestDict
from ..models.live_events_request1 import LiveEventsRequest1, LiveEventsRequest1Dict
from ..models.live_events_request2 import LiveEventsRequest2, LiveEventsRequest2Dict
from ..models.me_live_events_request import MeLiveEventsRequest, MeLiveEventsRequestDict
from ..models.me_live_events_request1 import MeLiveEventsRequest1, MeLiveEventsRequest1Dict
from ..models.me_live_events_request2 import MeLiveEventsRequest2, MeLiveEventsRequest2Dict
from ..models.recurring_event import RecurringEvent
from ..models.users_live_events_request import UsersLiveEventsRequest, UsersLiveEventsRequestDict
from ..models.users_live_events_request1 import UsersLiveEventsRequest1, UsersLiveEventsRequest1Dict
from ..models.users_live_events_request2 import UsersLiveEventsRequest2, UsersLiveEventsRequest2Dict
from ..server.server import Server


class LiveEssentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiveEssentialsWithRawResponse(client, server, auth)

    def create_live_event(
        self,
        user_id: float,
        body: UsersLiveEventsRequest1 | UsersLiveEventsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method creates a new event for the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was created.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't create an
                event. * Error code 8000: The user credentials are invalid. * Error code 3422: The authenticated user
                can't create an event. * Error code 3439: The authenticated user can't edit the content rating of an
                event. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.create_live_event(user_id, body, request_options=request_options))

    def create_live_event_alt1(
        self, body: LiveEventsRequest1 | LiveEventsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> RecurringEvent:
        """This method creates a new event for the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was created.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't create an
                event. * Error code 8000: The user credentials are invalid. * Error code 3422: The authenticated user
                can't create an event. * Error code 3439: The authenticated user can't edit the content rating of an
                event. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.create_live_event_alt1(body, request_options=request_options))

    def create_live_event_alt2(
        self,
        body: MeLiveEventsRequest1 | MeLiveEventsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method creates a new event for the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was created.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't create an
                event. * Error code 8000: The user credentials are invalid. * Error code 3422: The authenticated user
                can't create an event. * Error code 3439: The authenticated user can't edit the content rating of an
                event. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.create_live_event_alt2(body, request_options=request_options))

    def delete_live_event(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user doesn't have the necessary permissions to delete the
                event. * Error code 3422: The authenticated user can't delete the event. Error code 5000: No such event
                or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.delete_live_event(live_event_id, user_id, request_options=request_options)
        )

    def delete_live_event_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user doesn't have the necessary permissions to delete the
                event. * Error code 3422: The authenticated user can't delete the event. Error code 5000: No such event
                or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.delete_live_event_alt1(live_event_id, request_options=request_options))

    def delete_live_event_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user doesn't have the necessary permissions to delete the
                event. * Error code 3422: The authenticated user can't delete the event. Error code 5000: No such event
                or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.delete_live_event_alt2(live_event_id, request_options=request_options))

    def delete_live_events(
        self,
        user_id: float,
        body: UsersLiveEventsRequest | UsersLiveEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the specified events. * Error code 8000:
                The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.delete_live_events(user_id, body, request_options=request_options))

    def delete_live_events_alt1(
        self, body: LiveEventsRequest | LiveEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the specified events. * Error code 8000:
                The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.delete_live_events_alt1(body, request_options=request_options))

    def delete_live_events_alt2(
        self,
        body: MeLiveEventsRequest | MeLiveEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the specified events. * Error code 8000:
                The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(self._with_raw_response.delete_live_events_alt2(body, request_options=request_options))

    def get_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event(
                live_event_id, user_id, password=password, request_options=request_options
            ),
        )

    def get_live_event_alt1(
        self, live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RecurringEvent:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_alt1(
                live_event_id, password=password, request_options=request_options
            ),
        )

    def get_live_event_alt2(
        self, live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RecurringEvent:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_alt2(
                live_event_id, password=password, request_options=request_options
            ),
        )

    def get_live_event_occurrences(
        self,
        user_id: float,
        start_date: str,
        *,
        end_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LiveEventOccurrenceConnection:
        """Returns all live event occurrences for the user within the given date range.

        For recurring events (with rrule), each occurrence within the range is returned as a separate entry. For
        one-time events (no rrule), the event is included if its start_time falls within the range.

        Args:
            user_id: The ID of the user.
            start_date: The start of the date range in ISO 8601 format.
            end_date: The end of the date range in ISO 8601 format. Defaults to 7 days after start.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The occurrences were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_live_event_occurrences(
                user_id, start_date, end_date=end_date, page=page, per_page=per_page, request_options=request_options
            ),
        )

    def get_live_events(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventConnection:
        """The method returns every event belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_live_events(
                user_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                type_=type_,
                request_options=request_options,
            ),
        )

    def get_live_events_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventConnection:
        """The method returns every event belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_live_events_alt1(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                type_=type_,
                request_options=request_options,
            ),
        )

    def get_live_events_alt2(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventConnection:
        """The method returns every event belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_live_events_alt2(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                type_=type_,
                request_options=request_options,
            ),
        )

    def update_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsRequest2 | UsersLiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was updated.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user doesn't have
                the necessary permissions to update the event. * Error code 3422: The authenticated user can't update
                the event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.update_live_event(
                live_event_id, user_id, body=body, request_options=request_options
            ),
        )

    def update_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsRequest2 | LiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was updated.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user doesn't have
                the necessary permissions to update the event. * Error code 3422: The authenticated user can't update
                the event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.update_live_event_alt1(live_event_id, body=body, request_options=request_options)
        )

    def update_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsRequest2 | MeLiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was updated.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user doesn't have
                the necessary permissions to update the event. * Error code 3422: The authenticated user can't update
                the event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            self._with_raw_response.update_live_event_alt2(live_event_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> LiveEssentialsWithRawResponse:
        return self._with_raw_response


class AsyncLiveEssentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiveEssentialsWithRawResponse(client, server, auth)

    async def create_live_event(
        self,
        user_id: float,
        body: UsersLiveEventsRequest1 | UsersLiveEventsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method creates a new event for the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was created.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't create an
                event. * Error code 8000: The user credentials are invalid. * Error code 3422: The authenticated user
                can't create an event. * Error code 3439: The authenticated user can't edit the content rating of an
                event. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.create_live_event(user_id, body, request_options=request_options))

    async def create_live_event_alt1(
        self, body: LiveEventsRequest1 | LiveEventsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> RecurringEvent:
        """This method creates a new event for the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was created.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't create an
                event. * Error code 8000: The user credentials are invalid. * Error code 3422: The authenticated user
                can't create an event. * Error code 3439: The authenticated user can't edit the content rating of an
                event. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.create_live_event_alt1(body, request_options=request_options))

    async def create_live_event_alt2(
        self,
        body: MeLiveEventsRequest1 | MeLiveEventsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method creates a new event for the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was created.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user can't create an
                event. * Error code 8000: The user credentials are invalid. * Error code 3422: The authenticated user
                can't create an event. * Error code 3439: The authenticated user can't edit the content rating of an
                event. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.create_live_event_alt2(body, request_options=request_options))

    async def delete_live_event(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user doesn't have the necessary permissions to delete the
                event. * Error code 3422: The authenticated user can't delete the event. Error code 5000: No such event
                or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_live_event(live_event_id, user_id, request_options=request_options)
        )

    async def delete_live_event_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user doesn't have the necessary permissions to delete the
                event. * Error code 3422: The authenticated user can't delete the event. Error code 5000: No such event
                or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_live_event_alt1(live_event_id, request_options=request_options)
        )

    async def delete_live_event_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user doesn't have the necessary permissions to delete the
                event. * Error code 3422: The authenticated user can't delete the event. Error code 5000: No such event
                or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_live_event_alt2(live_event_id, request_options=request_options)
        )

    async def delete_live_events(
        self,
        user_id: float,
        body: UsersLiveEventsRequest | UsersLiveEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the specified events. * Error code 8000:
                The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.delete_live_events(user_id, body, request_options=request_options))

    async def delete_live_events_alt1(
        self, body: LiveEventsRequest | LiveEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the specified events. * Error code 8000:
                The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.delete_live_events_alt1(body, request_options=request_options))

    async def delete_live_events_alt2(
        self,
        body: MeLiveEventsRequest | MeLiveEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were deleted.

        Raises:
            ApiError: * Error code 3200: The authenticated user can't delete the specified events. * Error code 8000:
                The user credentials are invalid. ``error`` is ``Error | RawError``."""
        return unwrap(await self._with_raw_response.delete_live_events_alt2(body, request_options=request_options))

    async def get_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event(
                live_event_id, user_id, password=password, request_options=request_options
            ),
        )

    async def get_live_event_alt1(
        self, live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RecurringEvent:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_alt1(
                live_event_id, password=password, request_options=request_options
            ),
        )

    async def get_live_event_alt2(
        self, live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RecurringEvent:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was returned.

        Raises:
            ApiError: Error code 2204: A password is required for password-protected events. Error code 3200: The
                authenticated user can't access the event. Error code 5000: No such event exists. ``error`` is ``Error |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_alt2(
                live_event_id, password=password, request_options=request_options
            ),
        )

    async def get_live_event_occurrences(
        self,
        user_id: float,
        start_date: str,
        *,
        end_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LiveEventOccurrenceConnection:
        """Returns all live event occurrences for the user within the given date range.

        For recurring events (with rrule), each occurrence within the range is returned as a separate entry. For
        one-time events (no rrule), the event is included if its start_time falls within the range.

        Args:
            user_id: The ID of the user.
            start_date: The start of the date range in ISO 8601 format.
            end_date: The end of the date range in ISO 8601 format. Defaults to 7 days after start.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The occurrences were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_event_occurrences(
                user_id, start_date, end_date=end_date, page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def get_live_events(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventConnection:
        """The method returns every event belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_events(
                user_id,
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                type_=type_,
                request_options=request_options,
            ),
        )

    async def get_live_events_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventConnection:
        """The method returns every event belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_events_alt1(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                type_=type_,
                request_options=request_options,
            ),
        )

    async def get_live_events_alt2(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EventConnection:
        """The method returns every event belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The events were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_live_events_alt2(
                direction=direction,
                filter_=filter_,
                page=page,
                per_page=per_page,
                query=query,
                sort=sort,
                type_=type_,
                request_options=request_options,
            ),
        )

    async def update_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsRequest2 | UsersLiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was updated.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user doesn't have
                the necessary permissions to update the event. * Error code 3422: The authenticated user can't update
                the event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.update_live_event(
                live_event_id, user_id, body=body, request_options=request_options
            ),
        )

    async def update_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsRequest2 | LiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was updated.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user doesn't have
                the necessary permissions to update the event. * Error code 3422: The authenticated user can't update
                the event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.update_live_event_alt1(
                live_event_id, body=body, request_options=request_options
            ),
        )

    async def update_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsRequest2 | MeLiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringEvent:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The event was updated.

        Raises:
            ApiError: Error code 2204: A parameter is invalid. * Error code 3200: The authenticated user doesn't have
                the necessary permissions to update the event. * Error code 3422: The authenticated user can't update
                the event. Error code 5000: No such event or user exists. ``error`` is ``Error | RawError``."""
        return unwrap(
            await self._with_raw_response.update_live_event_alt2(
                live_event_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncLiveEssentialsWithRawResponse:
        return self._with_raw_response


class LiveEssentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_live_event(
        self,
        user_id: float,
        body: UsersLiveEventsRequest1 | UsersLiveEventsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, CreateLiveEventErrorBody]:
        """This method creates a new event for the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsRequest1 | UsersLiveEventsRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=create_live_event_error_mapper,
            request_options=request_options,
        )

    def create_live_event_alt1(
        self, body: LiveEventsRequest1 | LiveEventsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RecurringEvent, CreateLiveEventAlt1ErrorBody]:
        """This method creates a new event for the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsRequest1 | LiveEventsRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=create_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    def create_live_event_alt2(
        self,
        body: MeLiveEventsRequest1 | MeLiveEventsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, CreateLiveEventAlt2ErrorBody]:
        """This method creates a new event for the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsRequest1 | MeLiveEventsRequest1Dict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=create_live_event_alt2_error_mapper,
            request_options=request_options,
        )

    def delete_live_event(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventErrorBody]:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_event_error_mapper,
            request_options=request_options,
        )

    def delete_live_event_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventAlt1ErrorBody]:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_live_event_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventAlt2ErrorBody]:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_event_alt2_error_mapper,
            request_options=request_options,
        )

    def delete_live_events(
        self,
        user_id: float,
        body: UsersLiveEventsRequest | UsersLiveEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteLiveEventsErrorBody]:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/live_events"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsRequest | UsersLiveEventsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_events_error_mapper,
            request_options=request_options,
        )

    def delete_live_events_alt1(
        self, body: LiveEventsRequest | LiveEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventsAlt1ErrorBody]:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsRequest | LiveEventsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_events_alt1_error_mapper,
            request_options=request_options,
        )

    def delete_live_events_alt2(
        self,
        body: MeLiveEventsRequest | MeLiveEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteLiveEventsAlt2ErrorBody]:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/live_events"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsRequest | MeLiveEventsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=delete_live_events_alt2_error_mapper,
            request_options=request_options,
        )

    def get_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, GetLiveEventErrorBody]:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=get_live_event_error_mapper,
            request_options=request_options,
        )

    def get_live_event_alt1(
        self, live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RecurringEvent, GetLiveEventAlt1ErrorBody]:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=get_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    def get_live_event_alt2(
        self, live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RecurringEvent, GetLiveEventAlt2ErrorBody]:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=get_live_event_alt2_error_mapper,
            request_options=request_options,
        )

    def get_live_event_occurrences(
        self,
        user_id: float,
        start_date: str,
        *,
        end_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LiveEventOccurrenceConnection, RawError]:
        """Returns all live event occurrences for the user within the given date range.

        For recurring events (with rrule), each occurrence within the range is returned as a separate entry. For
        one-time events (no rrule), the event is included if its start_time falls within the range.

        Args:
            user_id: The ID of the user.
            start_date: The start of the date range in ISO 8601 format.
            end_date: The end of the date range in ISO 8601 format. Defaults to 7 days after start.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events_occurrences"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[str]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[LiveEventOccurrenceConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_live_events(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventConnection, RawError]:
        """The method returns every event belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter8OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
                param[Type31OrStr | None]("type", type_),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_live_events_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventConnection, RawError]:
        """The method returns every event belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter8OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
                param[Type31OrStr | None]("type", type_),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_live_events_alt2(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventConnection, RawError]:
        """The method returns every event belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter8OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
                param[Type31OrStr | None]("type", type_),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[EventConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsRequest2 | UsersLiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, UpdateLiveEventErrorBody]:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsRequest2 | UsersLiveEventsRequest2Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=update_live_event_error_mapper,
            request_options=request_options,
        )

    def update_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsRequest2 | LiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, UpdateLiveEventAlt1ErrorBody]:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsRequest2 | LiveEventsRequest2Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=update_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    def update_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsRequest2 | MeLiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, UpdateLiveEventAlt2ErrorBody]:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsRequest2 | MeLiveEventsRequest2Dict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[RecurringEvent],
            error_mapper=update_live_event_alt2_error_mapper,
            request_options=request_options,
        )


class AsyncLiveEssentialsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_live_event(
        self,
        user_id: float,
        body: UsersLiveEventsRequest1 | UsersLiveEventsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, CreateLiveEventErrorBody]:
        """This method creates a new event for the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/users/{user_id}/live_events"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsRequest1 | UsersLiveEventsRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=create_live_event_error_mapper,
            request_options=request_options,
        )

    async def create_live_event_alt1(
        self, body: LiveEventsRequest1 | LiveEventsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RecurringEvent, CreateLiveEventAlt1ErrorBody]:
        """This method creates a new event for the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/live_events"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsRequest1 | LiveEventsRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=create_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    async def create_live_event_alt2(
        self,
        body: MeLiveEventsRequest1 | MeLiveEventsRequest1Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, CreateLiveEventAlt2ErrorBody]:
        """This method creates a new event for the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/me/live_events"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsRequest1 | MeLiveEventsRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=create_live_event_alt2_error_mapper,
            request_options=request_options,
        )

    async def delete_live_event(
        self, live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventErrorBody]:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_event_error_mapper,
            request_options=request_options,
        )

    async def delete_live_event_alt1(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventAlt1ErrorBody]:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_live_event_alt2(
        self, live_event_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventAlt2ErrorBody]:
        """This method deletes a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_event_alt2_error_mapper,
            request_options=request_options,
        )

    async def delete_live_events(
        self,
        user_id: float,
        body: UsersLiveEventsRequest | UsersLiveEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteLiveEventsErrorBody]:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/users/{user_id}/live_events"),
            path_params=[param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsRequest | UsersLiveEventsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_events_error_mapper,
            request_options=request_options,
        )

    async def delete_live_events_alt1(
        self, body: LiveEventsRequest | LiveEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteLiveEventsAlt1ErrorBody]:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/live_events"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsRequest | LiveEventsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_events_alt1_error_mapper,
            request_options=request_options,
        )

    async def delete_live_events_alt2(
        self,
        body: MeLiveEventsRequest | MeLiveEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteLiveEventsAlt2ErrorBody]:
        """This method deletes multiple events belonging to the authenticated user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/me/live_events"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsRequest | MeLiveEventsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_empty_response,
            error_mapper=delete_live_events_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        password: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, GetLiveEventErrorBody]:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=get_live_event_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_alt1(
        self, live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RecurringEvent, GetLiveEventAlt1ErrorBody]:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=get_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_alt2(
        self, live_event_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RecurringEvent, GetLiveEventAlt2ErrorBody]:
        """This method returns a single event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            password: The password of the event when the privacy is set to ``password``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            query_params=[param[str | None]("password", password)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=get_live_event_alt2_error_mapper,
            request_options=request_options,
        )

    async def get_live_event_occurrences(
        self,
        user_id: float,
        start_date: str,
        *,
        end_date: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LiveEventOccurrenceConnection, RawError]:
        """Returns all live event occurrences for the user within the given date range.

        For recurring events (with rrule), each occurrence within the range is returned as a separate entry. For
        one-time events (no rrule), the event is included if its start_time falls within the range.

        Args:
            user_id: The ID of the user.
            start_date: The start of the date range in ISO 8601 format.
            end_date: The end of the date range in ISO 8601 format. Defaults to 7 days after start.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events_occurrences"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[str]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[LiveEventOccurrenceConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_live_events(
        self,
        user_id: float,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventConnection, RawError]:
        """The method returns every event belonging to the authenticated user.

        Args:
            user_id: The ID of the user.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/live_events"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter8OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
                param[Type31OrStr | None]("type", type_),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[EventConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_live_events_alt1(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventConnection, RawError]:
        """The method returns every event belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/live_events"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter8OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
                param[Type31OrStr | None]("type", type_),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[EventConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_live_events_alt2(
        self,
        *,
        direction: DirectionOrStr | None = None,
        filter_: Filter8OrStr | None = None,
        page: float | None = None,
        per_page: float | None = None,
        query: str | None = None,
        sort: Sort8OrStr | None = None,
        type_: Type31OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EventConnection, RawError]:
        """The method returns every event belonging to the authenticated user.

        Args:
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_: The attribute by which to filter the results. Option descriptions: * ``not_in_folder`` - Show only
                events that aren't in a folder. * ``not_in_showcase`` - Show only events that aren't in a showcase.
            page: The page number of the results to show.
            per_page: The number of items to show on each page of results, up to a maximum of 100.
            query: The search query to use to filter the results.
            sort: The way to sort the results. Option descriptions: * ``alphabetical`` - Sort the results
                alphabetically. * ``date`` - Sort the results by creation date.
            type_: The type of event to return. Option descriptions: * ``all`` - Return all events. * ``one_time`` -
                Return one-time events only. * ``recurring`` - Return recurring events only.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/live_events"),
            query_params=[
                param[DirectionOrStr | None]("direction", direction),
                param[Filter8OrStr | None]("filter", filter_),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[str | None]("query", query),
                param[Sort8OrStr | None]("sort", sort),
                param[Type31OrStr | None]("type", type_),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[EventConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_live_event(
        self,
        live_event_id: float,
        user_id: float,
        *,
        body: UsersLiveEventsRequest2 | UsersLiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, UpdateLiveEventErrorBody]:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            user_id: The ID of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/users/{user_id}/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id), param[float]("user_id", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersLiveEventsRequest2 | UsersLiveEventsRequest2Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=update_live_event_error_mapper,
            request_options=request_options,
        )

    async def update_live_event_alt1(
        self,
        live_event_id: float,
        *,
        body: LiveEventsRequest2 | LiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, UpdateLiveEventAlt1ErrorBody]:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiveEventsRequest2 | LiveEventsRequest2Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=update_live_event_alt1_error_mapper,
            request_options=request_options,
        )

    async def update_live_event_alt2(
        self,
        live_event_id: float,
        *,
        body: MeLiveEventsRequest2 | MeLiveEventsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringEvent, UpdateLiveEventAlt2ErrorBody]:
        """This method updates an event belonging to the authenticated user.

        Args:
            live_event_id: The ID of the event.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/me/live_events/{live_event_id}"),
            path_params=[param[float]("live_event_id", live_event_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MeLiveEventsRequest2 | MeLiveEventsRequest2Dict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=async_json_decoder[RecurringEvent],
            error_mapper=update_live_event_alt2_error_mapper,
            request_options=request_options,
        )
