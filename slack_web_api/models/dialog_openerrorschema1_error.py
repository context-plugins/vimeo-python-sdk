from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dialog_open_error_enum import DialogOpenErrorEnumOrStr


class DialogOpenerrorschema1Error(SdkBaseModel):
    """Schema for error response from dialog.open method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: DialogOpenErrorEnumOrStr
    ok: Literal["False"] = "False"


class DialogOpenerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: DialogOpenErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
