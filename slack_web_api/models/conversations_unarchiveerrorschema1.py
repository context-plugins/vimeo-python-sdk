from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_unarchive_error_enum import ConversationsUnarchiveErrorEnumOrStr


class ConversationsUnarchiveerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.unarchive method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsUnarchiveErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsUnarchiveerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsUnarchiveErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
