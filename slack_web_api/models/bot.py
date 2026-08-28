from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .icons import Icons, IconsDict


class Bot(SdkBaseModel):
    app_id: str
    deleted: bool
    icons: Icons
    id: str
    name: str
    updated: int
    user_id: Optional[str] = UNSET


class BotDict(TypedDict):
    app_id: str
    deleted: bool
    icons: Icons | IconsDict
    id: str
    name: str
    updated: int
    user_id: NotRequired[str]
