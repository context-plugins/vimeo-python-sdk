from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reminders_complete_error_enum import RemindersCompleteErrorEnumOrStr


class RemindersCompleteerrorschema1Error(SdkBaseModel):
    """Schema for error response from reminders.complete method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: RemindersCompleteErrorEnumOrStr
    ok: Literal["False"] = "False"


class RemindersCompleteerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: RemindersCompleteErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
