from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_post_message_error_enum import ChatPostMessageErrorEnumOrStr


class ChatPostMessageerrorschema1(SdkBaseModel):
    """Schema for error response chat.postMessage method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatPostMessageErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatPostMessageerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ChatPostMessageErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
