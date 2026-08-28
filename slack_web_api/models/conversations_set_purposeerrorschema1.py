from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_set_purpose_error_enum import ConversationsSetPurposeErrorEnumOrStr


class ConversationsSetPurposeerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.setPurpose method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsSetPurposeErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsSetPurposeerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsSetPurposeErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
