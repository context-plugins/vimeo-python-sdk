from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DndInfoschema(SdkBaseModel):
    """Schema for successful response from dnd.info method"""

    dnd_enabled: bool
    next_dnd_end_ts: int
    next_dnd_start_ts: int
    ok: Literal["True"] = "True"
    snooze_enabled: Optional[bool] = UNSET
    snooze_endtime: Optional[int] = UNSET
    snooze_remaining: Optional[int] = UNSET


class DndInfoschemaDict(TypedDict):
    dnd_enabled: bool
    next_dnd_end_ts: int
    next_dnd_start_ts: int
    ok: NotRequired[Literal["True"]]
    snooze_enabled: NotRequired[bool]
    snooze_endtime: NotRequired[int]
    snooze_remaining: NotRequired[int]
