from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .message import Message, MessageDict


class ChatScheduleMessagesuccessschema(SdkBaseModel):
    """Schema for successful response of chat.scheduleMessage method"""

    channel: str
    message: Message
    ok: Literal["True"] = "True"
    post_at: int
    scheduled_message_id: str


class ChatScheduleMessagesuccessschemaDict(TypedDict):
    channel: str
    message: Message | MessageDict
    ok: NotRequired[Literal["True"]]
    post_at: int
    scheduled_message_id: str
