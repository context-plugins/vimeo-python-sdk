from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_rename_error_enum import ConversationsRenameErrorEnumOrStr


class ConversationsRenameerrorschema1Error(SdkBaseModel):
    """Schema for error response from conversations.rename method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsRenameErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsRenameerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsRenameErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
