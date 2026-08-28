from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_convert_to_private_error_enum import AdminConversationsConvertToPrivateErrorEnumOrStr


class AdminConversationsConvertToPrivateerrorschema1(SdkBaseModel):
    """Schema for error response from admin.conversations.convertToPrivate"""

    error: AdminConversationsConvertToPrivateErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsConvertToPrivateerrorschema1Dict(TypedDict):
    error: AdminConversationsConvertToPrivateErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
