from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_history_error_enum import ConversationsHistoryErrorEnumOrStr


class ConversationsHistoryerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.history method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsHistoryErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsHistoryerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsHistoryErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
