from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_kick_error_enum import ConversationsKickErrorEnumOrStr


class ConversationsKickerrorschema1Error(SdkBaseModel):
    """Schema for error response conversations.kick method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsKickErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsKickerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsKickErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
