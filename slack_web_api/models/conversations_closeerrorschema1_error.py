from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_close_error_enum import ConversationsCloseErrorEnumOrStr


class ConversationsCloseerrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.close method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsCloseErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsCloseerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsCloseErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
