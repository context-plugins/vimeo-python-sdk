from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_archive_error_enum import ConversationsArchiveErrorEnumOrStr


class ConversationsArchiveerrorschema1(SdkBaseModel):
    """Schema for error response from conversations.archive method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ConversationsArchiveErrorEnumOrStr
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsArchiveerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ConversationsArchiveErrorEnumOrStr
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
