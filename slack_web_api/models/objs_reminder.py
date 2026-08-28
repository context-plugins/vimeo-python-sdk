from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ObjsReminder(SdkBaseModel):
    complete_ts: Optional[int] = UNSET
    creator: str
    id: str
    recurring: bool
    text: str
    time: Optional[int] = UNSET
    user: str


class ObjsReminderDict(TypedDict):
    complete_ts: NotRequired[int]
    creator: str
    id: str
    recurring: bool
    text: str
    time: NotRequired[int]
    user: str
