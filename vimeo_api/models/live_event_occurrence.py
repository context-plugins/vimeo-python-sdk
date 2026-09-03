from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .recurring_event import RecurringEvent, RecurringEventDict


class LiveEventOccurrence(SdkBaseModel):
    end_time: str | None
    """The end time of this occurrence in ISO 8601 format."""

    event: RecurringEvent | None
    """The full live event resource that owns this occurrence. Use sub-fields (e.g. ``event.parentFolder``,
    ``event.pictures``, ``event.metadata.interactions.delete``) to opt into specific event data without paying for the
    full event payload."""

    event_title: str
    """The title of the live event."""

    event_type: str
    """The type of the live event."""

    event_uri: str
    """The URI of the parent live event."""

    has_registration: bool
    """Whether the event has registration enabled."""

    link: str
    """The URI to access the event on Vimeo."""

    settings_link: str | None
    """The URI to access the event settings."""

    start_time: str
    """The start time of this occurrence in ISO 8601 format."""

    status: str
    """The status of the live event."""

    thumbnail: str | None
    """The thumbnail URL of the live event."""


class LiveEventOccurrenceDict(TypedDict):
    end_time: str | None
    event: RecurringEvent | RecurringEventDict | None
    event_title: str
    event_type: str
    event_uri: str
    has_registration: bool
    link: str
    settings_link: str | None
    start_time: str
    status: str
    thumbnail: str | None
