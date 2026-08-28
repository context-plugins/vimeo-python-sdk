from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .channel_object import ChannelObject, ChannelObjectDict


class AdminConversationsSearchschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.search"""

    channels: list[ChannelObject]
    next_cursor: str


class AdminConversationsSearchschemaDict(TypedDict):
    channels: list[ChannelObject | ChannelObjectDict]
    next_cursor: str
