from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type37(str, Enum):
    """The type of the On Demand page.

    Option descriptions:
     * ``film`` - The On Demand page is a film.
     * ``series`` - The On Demand page is a series."""

    FILM = "film"
    SERIES = "series"

    __str__ = str.__str__


Type37OrStr: TypeAlias = Annotated[Type37 | str, open_enum_validator(Type37)]
