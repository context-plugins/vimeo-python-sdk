from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reminders_add_error_enum import RemindersAddErrorEnumOrStr


class RemindersAdderrorschema1(SdkBaseModel):
    """Schema for error response from reminders.add method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: RemindersAddErrorEnumOrStr
    ok: Literal["False"] = "False"


class RemindersAdderrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: RemindersAddErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
