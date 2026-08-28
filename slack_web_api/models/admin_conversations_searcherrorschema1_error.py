from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_search_error_enum import AdminConversationsSearchErrorEnumOrStr


class AdminConversationsSearcherrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.search"""

    error: AdminConversationsSearchErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsSearcherrorschema1ErrorDict(TypedDict):
    error: AdminConversationsSearchErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
