from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_info_error_enum import ConversationsInfoErrorEnumOrStr


class ConversationsInfoerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.info method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsInfoErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsInfoerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsInfoErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
