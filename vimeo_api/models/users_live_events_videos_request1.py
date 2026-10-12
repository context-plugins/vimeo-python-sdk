from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .videos17 import Videos17, Videos17Dict


class UsersLiveEventsVideosRequest1(SdkBaseModel):
    videos: Optional[list[Videos17]] = UNSET
    """An array of video objects."""


class UsersLiveEventsVideosRequest1Dict(TypedDict):
    videos: NotRequired[list[Videos17Dict]]
