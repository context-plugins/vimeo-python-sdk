from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MeLiveEventsRequest(SdkBaseModel):
    events: list[str]
    """An array of event URIs."""


class MeLiveEventsRequestDict(TypedDict):
    events: list[str]
