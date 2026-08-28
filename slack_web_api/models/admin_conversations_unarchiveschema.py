from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AdminConversationsUnarchiveschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.unarchive"""

    ok: Literal["True"] = "True"


class AdminConversationsUnarchiveschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
