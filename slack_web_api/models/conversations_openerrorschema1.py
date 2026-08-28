from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_open_error_enum import ConversationsOpenErrorEnumOrStr


class ConversationsOpenerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.open method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsOpenErrorEnumOrStr
    ok: Literal["False"] = "False"


class ConversationsOpenerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsOpenErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
