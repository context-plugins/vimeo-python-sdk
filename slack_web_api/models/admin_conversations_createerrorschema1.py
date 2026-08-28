from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_create_error_enum import AdminConversationsCreateErrorEnumOrStr


class AdminConversationsCreateerrorschema1(SdkBaseModel):
    """Schema for error response from admin.conversations.create"""

    error: AdminConversationsCreateErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsCreateerrorschema1Dict(TypedDict):
    error: AdminConversationsCreateErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
