from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_invite_error_enum import AdminConversationsInviteErrorEnumOrStr


class AdminConversationsInviteerrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.invite"""

    error: AdminConversationsInviteErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsInviteerrorschema1ErrorDict(TypedDict):
    error: AdminConversationsInviteErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
