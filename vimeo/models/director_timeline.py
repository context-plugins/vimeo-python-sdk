from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DirectorTimeline(SdkBaseModel):
    pitch: Optional[float] = UNSET
    """The timeline pitch value, ranging from a minimum of ``-90`` to a maximum of ``90``."""

    roll: Optional[float] = UNSET
    """The timeline roll value."""

    time_code: Optional[float] = UNSET
    """The timeline time code."""

    yaw: Optional[float] = UNSET
    """The timeline yaw value, ranging from a minimum of ``0`` to a maximum of ``360``."""


class DirectorTimelineDict(TypedDict):
    pitch: NotRequired[float]
    roll: NotRequired[float]
    time_code: NotRequired[float]
    yaw: NotRequired[float]
