from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .messageobject import Messageobject, MessageobjectDict


class ConversationsHistorysuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.history method"""

    channel_actions_count: int
    channel_actions_ts: Any
    has_more: bool
    messages: list[Messageobject]
    ok: Literal["True"] = "True"
    pin_count: int


class ConversationsHistorysuccessschemaDict(TypedDict):
    channel_actions_count: int
    channel_actions_ts: Any
    has_more: bool
    messages: list[Messageobject | MessageobjectDict]
    ok: NotRequired[Literal["True"]]
    pin_count: int
