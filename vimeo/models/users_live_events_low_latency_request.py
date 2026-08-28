from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersLiveEventsLowLatencyRequest(SdkBaseModel):
    low_latency: Optional[bool] = UNSET
    """Whether the event is low latency."""


class UsersLiveEventsLowLatencyRequestDict(TypedDict):
    low_latency: NotRequired[bool]
