from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prefs1 import Prefs1, Prefs1Dict


class AdminConversationsGetConversationPrefsschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.getConversationPrefs"""

    ok: Literal["True"] = "True"
    prefs: Optional[Prefs1] = UNSET


class AdminConversationsGetConversationPrefsschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    prefs: NotRequired[Prefs1 | Prefs1Dict]
