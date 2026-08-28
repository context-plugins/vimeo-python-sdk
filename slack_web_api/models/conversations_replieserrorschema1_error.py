from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_replies_error_enum import ConversationsRepliesErrorEnumOrStr


class ConversationsReplieserrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.replies method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsRepliesErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsReplieserrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsRepliesErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
