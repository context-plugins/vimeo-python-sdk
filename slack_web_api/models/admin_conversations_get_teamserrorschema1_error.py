from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.admin_conversations_get_teams_error_enum import AdminConversationsGetTeamsErrorEnumOrStr


class AdminConversationsGetTeamserrorschema1Error(SdkBaseModel):
    """Schema for error response from admin.conversations.getTeams"""

    error: AdminConversationsGetTeamsErrorEnumOrStr
    ok: Literal["False"] = "False"


class AdminConversationsGetTeamserrorschema1ErrorDict(TypedDict):
    error: AdminConversationsGetTeamsErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
