from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .video6 import Video6, Video6Dict


class Videos17(SdkBaseModel):
    video: Optional[Video6] = UNSET


class Videos17Dict(TypedDict):
    video: NotRequired[Video6Dict]
