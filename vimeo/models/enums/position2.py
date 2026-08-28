from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Position2(str, Enum):
    """The position of the play button within the video page player.

    Option descriptions:
     * ``auto`` - Use Vimeo's default positioning for the play button.
     * ``bottom`` - The play button is positioned at the bottom of the player, except when in tiny mode.
     * ``center`` - The play button is positioned in the center of the player."""

    AUTO = "auto"
    BOTTOM = "bottom"
    CENTER = "center"

    __str__ = str.__str__


Position2OrStr: TypeAlias = Annotated[Position2 | str, open_enum_validator(Position2)]
