from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.position2 import Position2OrStr


class PlayButton1(SdkBaseModel):
    """A representation of the play button's settings."""

    position: Optional[Position2OrStr] = UNSET
    """The position of the play button within the video page player.

    Option descriptions:
     * ``auto`` - Use Vimeo's default positioning for the play button.
     * ``bottom`` - The play button is positioned at the bottom of the player, except when in tiny mode.
     * ``center`` - The play button is positioned in the center of the player."""


class PlayButton1Dict(TypedDict):
    position: NotRequired[Position2OrStr]
