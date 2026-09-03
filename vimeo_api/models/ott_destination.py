from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OttDestination(SdkBaseModel):
    id: str
    """The OTT destination's canonical relative URI."""

    ott_channel_id: float
    """The ID of the OTT channel."""

    ott_channel_name: str
    """The name of the OTT channel."""

    ott_channel_subdomain: str
    """The subdomain of the OTT channel."""

    ott_event_id: float
    """The ID of the OTT event."""

    recurring_live_event_id: float
    """The ID of the current recurring event."""


class OttDestinationDict(TypedDict):
    id: str
    ott_channel_id: float
    ott_channel_name: str
    ott_channel_subdomain: str
    ott_event_id: float
    recurring_live_event_id: float
