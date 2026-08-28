from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AdminConversationsRenameschema1(SdkBaseModel):
    """Schema for successful response of admin.conversations.rename"""

    ok: Literal["True"] = "True"


class AdminConversationsRenameschema1Dict(TypedDict):
    ok: NotRequired[Literal["True"]]
