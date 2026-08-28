from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_create_error_enum import ConversationsCreateErrorEnumOrStr


class ConversationsCreateerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.create method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    detail: Optional[str] = UNSET
    error: ConversationsCreateErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsCreateerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    detail: NotRequired[str]
    error: ConversationsCreateErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
