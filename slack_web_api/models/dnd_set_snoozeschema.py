from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class DndSetSnoozeschema(SdkBaseModel):
    """Schema for successful response from dnd.setSnooze method"""

    ok: Literal["True"] = "True"
    snooze_enabled: bool
    snooze_endtime: int
    snooze_remaining: int


class DndSetSnoozeschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    snooze_enabled: bool
    snooze_endtime: int
    snooze_remaining: int
