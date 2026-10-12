from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .videos16 import Videos16, Videos16Dict


class LiveEventsVideosRequest(SdkBaseModel):
    videos: Optional[list[Videos16]] = UNSET
    """An array of video objects."""


class LiveEventsVideosRequestDict(TypedDict):
    videos: NotRequired[list[Videos16Dict]]
