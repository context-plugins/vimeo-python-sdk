from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AdminConversationsRenameschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.disconnectShared"""

    ok: Literal["True"] = "True"


class AdminConversationsRenameschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
