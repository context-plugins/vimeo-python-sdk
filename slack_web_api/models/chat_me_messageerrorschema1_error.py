from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_me_message_error_enum import ChatMeMessageErrorEnumOrStr


class ChatMeMessageerrorschema1Error(SdkBaseModel):
    """Schema for error response from chat.meMessage method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatMeMessageErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatMeMessageerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ChatMeMessageErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
