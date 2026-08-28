from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AdminConversationsArchiveschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.archive"""

    ok: Literal["True"] = "True"


class AdminConversationsArchiveschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
