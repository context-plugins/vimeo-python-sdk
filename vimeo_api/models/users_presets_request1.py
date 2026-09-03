from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .embed17 import Embed17, Embed17Dict
from .enums.outro1 import Outro1OrStr


class UsersPresetsRequest1(SdkBaseModel):
    embed: Optional[Embed17] = UNSET
    name: Optional[str] = UNSET
    """The name of the embed preset."""

    outro: Optional[Outro1OrStr] = UNSET
    """What to do with the outro.

    Option descriptions:
     * ``nothing`` - Disable the outro."""


class UsersPresetsRequest1Dict(TypedDict):
    embed: NotRequired[Embed17 | Embed17Dict]
    name: NotRequired[str]
    outro: NotRequired[Outro1OrStr]
