from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_delete_scheduled_message_error_enum import ChatDeleteScheduledMessageErrorEnumOrStr


class ChatDeleteScheduledMessageerrorschema1Error(SdkBaseModel):
    """Schema for error response from chat.deleteScheduledMessage method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatDeleteScheduledMessageErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatDeleteScheduledMessageerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ChatDeleteScheduledMessageErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
