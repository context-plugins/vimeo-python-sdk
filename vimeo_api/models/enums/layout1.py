from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Layout1(str, Enum):
    """The type of layout for presenting the showcase.

    Option descriptions:
     * ``grid`` - The videos appear in a grid.
     * ``player`` - The videos appear in the player."""

    GRID = "grid"
    PLAYER = "player"

    __str__ = str.__str__


Layout1OrStr: TypeAlias = Annotated[Layout1 | str, open_enum_validator(Layout1)]
