from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_delete_error_enum import ChatDeleteErrorEnumOrStr


class ChatDeleteerrorschema1(SdkBaseModel):
    """Schema for error response from chat.delete method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatDeleteErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatDeleteerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ChatDeleteErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
