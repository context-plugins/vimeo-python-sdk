from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AdminConversationsSetConversationPrefsschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.setConversationPrefs"""

    ok: Literal["True"] = "True"


class AdminConversationsSetConversationPrefsschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
