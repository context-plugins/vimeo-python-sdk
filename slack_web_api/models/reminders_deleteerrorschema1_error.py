from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reminders_delete_error_enum import RemindersDeleteErrorEnumOrStr


class RemindersDeleteerrorschema1Error(SdkBaseModel):
    """Schema for error response from reminders.delete method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: RemindersDeleteErrorEnumOrStr
    ok: Literal["False"] = "False"


class RemindersDeleteerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: RemindersDeleteErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
