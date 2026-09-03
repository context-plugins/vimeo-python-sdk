from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.position import PositionOrStr


class PlayButton3(SdkBaseModel):
    """An object representing the play button's settings."""

    position: Optional[PositionOrStr] = UNSET
    """The position of the play button within the embeddable player.

    Option descriptions:
     * ``auto`` - Use Vimeo's default positioning for the play button.
     * ``bottom`` - The play button is positioned at the bottom of the player, except when in tiny mode.
     * ``center`` - The play button is positioned in the center of the player."""


class PlayButton3Dict(TypedDict):
    position: NotRequired[PositionOrStr]
