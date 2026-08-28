from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Schedule(SdkBaseModel):
    """Information about the time or times that the event is expected to be live."""

    end_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the event is expected to end."""

    rrule: Optional[str] = UNSET
    """The recurrence rule for the event's schedule according to `RFC 5545
    <https://datatracker.ietf.org/doc/html/rfc5545>`__."""

    start_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the event is expected to be live."""

    time_zone: Optional[str] = UNSET
    """The time zone used in resolving the timestamps."""


class ScheduleDict(TypedDict):
    end_time: NotRequired[str]
    rrule: NotRequired[str]
    start_time: NotRequired[str]
    time_zone: NotRequired[str]
