from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LiveEventsRequest(SdkBaseModel):
    events: list[str]
    """An array of event URIs."""


class LiveEventsRequestDict(TypedDict):
    events: list[str]
