from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type9(str, Enum):
    """The type of the On Demand page.

    Option descriptions:
     * ``film`` - The On Demand page is for a film.
     * ``series`` - The On Demand page is for a series."""

    FILM = "film"
    SERIES = "series"

    __str__ = str.__str__


Type9OrStr: TypeAlias = Annotated[Type9 | str, open_enum_validator(Type9)]
