from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AdminConversationsInviteschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.invite"""

    ok: Literal["True"] = "True"


class AdminConversationsInviteschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
