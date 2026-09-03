from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersLiveEventsRequest(SdkBaseModel):
    events: list[str]
    """An array of event URIs."""


class UsersLiveEventsRequestDict(TypedDict):
    events: list[str]
