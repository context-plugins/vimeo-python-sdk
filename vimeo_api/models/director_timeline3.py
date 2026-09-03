from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DirectorTimeline3(SdkBaseModel):
    pitch: float
    """The 360 director timeline pitch. This value must be between −90 and 90, and you must specify it only when
    **spatial.director_timeline** is defined."""

    roll: Optional[float] = UNSET
    """The 360 director timeline roll."""

    time_code: float
    """The 360 director timeline time code. This paramater is required only when **spatial.director_timeline** is
    defined."""

    yaw: float
    """The 360 director timeline yaw. This value must be between 0 and 360, and you must specify it only when
    **spatial.director_timeline** is defined."""


class DirectorTimeline3Dict(TypedDict):
    pitch: float
    roll: NotRequired[float]
    time_code: float
    yaw: float
