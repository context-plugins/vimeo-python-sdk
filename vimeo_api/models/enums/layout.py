from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Layout(str, Enum):
    """The type of layout for presenting the showcase.

    Option descriptions:
     * ``grid`` - The showcase videos appear in a grid.
     * ``player`` - The showcase videos appear in the player."""

    GRID = "grid"
    PLAYER = "player"

    __str__ = str.__str__


LayoutOrStr: TypeAlias = Annotated[Layout | str, open_enum_validator(Layout)]
