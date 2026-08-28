from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bot_profile_object import BotProfileObject, BotProfileObjectDict


class Message(SdkBaseModel):
    bot_id: str
    bot_profile: Optional[BotProfileObject] = UNSET
    team: str
    text: str
    type_: str = Field(alias="type")
    user: str
    username: Optional[str] = UNSET


class MessageDict(TypedDict):
    bot_id: str
    bot_profile: NotRequired[BotProfileObject | BotProfileObjectDict]
    team: str
    text: str
    type_: str
    user: str
    username: NotRequired[str]
