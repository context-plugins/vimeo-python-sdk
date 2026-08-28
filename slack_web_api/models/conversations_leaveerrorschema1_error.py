from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_leave_error_enum import ConversationsLeaveErrorEnumOrStr


class ConversationsLeaveerrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.leave method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsLeaveErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsLeaveerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsLeaveErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
