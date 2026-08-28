from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_delete_error_enum import AdminConversationsDeleteErrorEnumOrStr


class AdminConversationsDeleteerrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.delete"""

    error: AdminConversationsDeleteErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsDeleteerrorschema1ErrorDict(TypedDict):
    error: AdminConversationsDeleteErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
