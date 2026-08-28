from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.position import PositionOrStr


class PlayButton(SdkBaseModel):
    """A representation of the play button's settings."""

    position: PositionOrStr
    """The position of the play button within the embeddable player.

    Option descriptions:
     * ``auto`` - Use Vimeo's default positioning for the play button.
     * ``bottom`` - The play button is positioned at the bottom of the player, except when in tiny mode.
     * ``center`` - The play button is positioned in the center of the player."""


class PlayButtonDict(TypedDict):
    position: PositionOrStr
