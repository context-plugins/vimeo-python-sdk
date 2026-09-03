from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeLiveEventsLowLatencyRequest(SdkBaseModel):
    low_latency: Optional[bool] = UNSET
    """Whether the event is low latency."""


class MeLiveEventsLowLatencyRequestDict(TypedDict):
    low_latency: NotRequired[bool]
