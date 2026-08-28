from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_get_permalink_error_enum import ChatGetPermalinkErrorEnumOrStr


class ChatGetPermalinkerrorschema1(SdkBaseModel):
    """Schema for error response from chat.getPermalink method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatGetPermalinkErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatGetPermalinkerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ChatGetPermalinkErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
