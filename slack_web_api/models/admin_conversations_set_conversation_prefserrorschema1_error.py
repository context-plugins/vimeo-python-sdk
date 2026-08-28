from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_set_conversation_prefs_error_enum import (
    AdminConversationsSetConversationPrefsErrorEnumOrStr,
)


class AdminConversationsSetConversationPrefserrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.setConversationPrefs"""

    error: AdminConversationsSetConversationPrefsErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsSetConversationPrefserrorschema1ErrorDict(TypedDict):
    error: AdminConversationsSetConversationPrefsErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
