from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdminConversationsCreateschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.create"""

    channel_id: Optional[str] = UNSET
    ok: Literal["True"] = "True"


class AdminConversationsCreateschemaDict(TypedDict):
    channel_id: NotRequired[str]
    ok: NotRequired[Literal["True"]]
