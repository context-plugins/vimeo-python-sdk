from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_update_error_enum import ChatUpdateErrorEnumOrStr


class ChatUpdateerrorschema1Error(SdkBaseModel):
    """Schema for error response chat.update method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatUpdateErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatUpdateerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ChatUpdateErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
