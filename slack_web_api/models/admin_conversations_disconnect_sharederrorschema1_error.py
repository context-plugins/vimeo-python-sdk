from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_disconnect_shared_error_enum import AdminConversationsDisconnectSharedErrorEnumOrStr


class AdminConversationsDisconnectSharederrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.disconnectShared"""

    error: AdminConversationsDisconnectSharedErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsDisconnectSharederrorschema1ErrorDict(TypedDict):
    error: AdminConversationsDisconnectSharedErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
