from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScheduledMessage(SdkBaseModel):
    channel_id: str
    date_created: int
    id: str
    post_at: int
    text: Optional[str] = UNSET


class ScheduledMessageDict(TypedDict):
    channel_id: str
    date_created: int
    id: str
    post_at: int
    text: NotRequired[str]
