from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .video5 import Video5, Video5Dict


class Videos16(SdkBaseModel):
    video: Optional[Video5] = UNSET


class Videos16Dict(TypedDict):
    video: NotRequired[Video5Dict]
