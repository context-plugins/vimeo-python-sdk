from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .icons import Icons, IconsDict


class BotProfileObject(SdkBaseModel):
    app_id: str
    deleted: bool
    icons: Icons
    id: str
    name: str
    team_id: str
    updated: int


class BotProfileObjectDict(TypedDict):
    app_id: str
    deleted: bool
    icons: Icons | IconsDict
    id: str
    name: str
    team_id: str
    updated: int
