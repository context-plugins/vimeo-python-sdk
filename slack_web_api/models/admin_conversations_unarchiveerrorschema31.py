from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_unarchive_error_enum import AdminConversationsUnarchiveErrorEnumOrStr


class AdminConversationsUnarchiveerrorschema31(SdkBaseModel):
    """Schema for error response from admin.conversations.unarchive"""

    error: AdminConversationsUnarchiveErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsUnarchiveerrorschema31Dict(TypedDict):
    error: AdminConversationsUnarchiveErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
