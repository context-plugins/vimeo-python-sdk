from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_get_conversation_prefs_error_enum import (
    AdminConversationsGetConversationPrefsErrorEnumOrStr,
)


class AdminConversationsUnarchiveerrorschema1(SdkBaseModel):
    """Schema for error response from admin.conversations.getConversationPrefs"""

    error: AdminConversationsGetConversationPrefsErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsUnarchiveerrorschema1Dict(TypedDict):
    error: AdminConversationsGetConversationPrefsErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
