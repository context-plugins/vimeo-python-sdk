from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PlayButtonPosition(str, Enum):
    """The position of the player's play button.

    Option descriptions:
     * ``0`` - The play button has the default position.
     * ``1`` - The play button appears at the bottom of the interface.
     * ``2`` - The play button appears in the center of the interface."""

    _0 = "0"
    _1 = "1"
    _2 = "2"

    __str__ = str.__str__


PlayButtonPositionOrStr: TypeAlias = Annotated[PlayButtonPosition | str, open_enum_validator(PlayButtonPosition)]
