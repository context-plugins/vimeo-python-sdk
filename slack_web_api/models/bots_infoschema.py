from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .bot import Bot, BotDict


class BotsInfoschema(SdkBaseModel):
    """Schema for successful response from bots.info method"""

    bot: Bot
    ok: Literal["True"] = "True"


class BotsInfoschemaDict(TypedDict):
    bot: Bot | BotDict
    ok: NotRequired[Literal["True"]]
