from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_unfurl_error_enum import ChatUnfurlErrorEnumOrStr


class ChatUnfurlerrorschema1Error(SdkBaseModel):
    """Schema for error response from chat.unfurl method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatUnfurlErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatUnfurlerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ChatUnfurlErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
