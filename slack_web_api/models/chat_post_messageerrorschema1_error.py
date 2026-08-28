from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_post_message_error_enum import ChatPostMessageErrorEnumOrStr


class ChatPostMessageerrorschema1Error(SdkBaseModel):
    """Schema for error response chat.postMessage method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatPostMessageErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatPostMessageerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ChatPostMessageErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
