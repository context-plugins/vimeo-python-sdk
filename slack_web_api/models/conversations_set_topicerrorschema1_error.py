from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_set_purpose_error_enum import ConversationsSetPurposeErrorEnumOrStr


class ConversationsSetTopicerrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.setTopic method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsSetPurposeErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsSetTopicerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsSetPurposeErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
