from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_members_error_enum import ConversationsMembersErrorEnumOrStr


class ConversationsMemberserrorschema1(SdkBaseModel):
    """Schema for error response conversations.members method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsMembersErrorEnumOrStr
    ok: Literal["False"] = "False"


class ConversationsMemberserrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsMembersErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
