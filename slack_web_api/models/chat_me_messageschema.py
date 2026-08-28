from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ChatMeMessageschema(SdkBaseModel):
    """Schema for successful response from chat.meMessage method"""

    channel: Optional[str] = UNSET
    ok: Literal["True"] = "True"
    ts: Optional[str] = UNSET


class ChatMeMessageschemaDict(TypedDict):
    channel: NotRequired[str]
    ok: NotRequired[Literal["True"]]
    ts: NotRequired[str]
