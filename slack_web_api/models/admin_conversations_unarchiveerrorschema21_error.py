from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_rename_error_enum import AdminConversationsRenameErrorEnumOrStr


class AdminConversationsUnarchiveerrorschema21Error(SdkBaseModel):
    """Schema for error response from admin.conversations.rename"""

    error: AdminConversationsRenameErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsUnarchiveerrorschema21ErrorDict(TypedDict):
    error: AdminConversationsRenameErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
