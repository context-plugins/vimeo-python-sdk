from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .can_thread import CanThread, CanThreadDict
from .who_can_post import WhoCanPost, WhoCanPostDict


class Prefs1(SdkBaseModel):
    can_thread: Optional[CanThread] = UNSET
    who_can_post: Optional[WhoCanPost] = UNSET


class Prefs1Dict(TypedDict):
    can_thread: NotRequired[CanThread | CanThreadDict]
    who_can_post: NotRequired[WhoCanPost | WhoCanPostDict]
