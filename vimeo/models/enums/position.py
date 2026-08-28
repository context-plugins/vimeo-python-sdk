from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Position(str, Enum):
    """The position of the play button within the embeddable player.

    Option descriptions:
     * ``auto`` - Use Vimeo's default positioning for the play button.
     * ``bottom`` - The play button is positioned at the bottom of the player, except when in tiny mode.
     * ``center`` - The play button is positioned in the center of the player."""

    AUTO = "auto"
    BOTTOM = "bottom"
    CENTER = "center"

    __str__ = str.__str__


PositionOrStr: TypeAlias = Annotated[Position | str, open_enum_validator(Position)]
