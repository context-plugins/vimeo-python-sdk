from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_mark_error_enum import ConversationsMarkErrorEnumOrStr


class ConversationsMarkerrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.mark method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsMarkErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsMarkerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsMarkErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
