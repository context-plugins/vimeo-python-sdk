from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type11(str, Enum):
    """The type of audio track.

    Option descriptions:
     * ``commentary`` - The audio track is a commentary.
     * ``descriptive`` - The audio track is descriptive for accessibility.
     * ``main`` - The audio track is dubbed audio.
     * ``unknown`` - The audio track category is unknown."""

    COMMENTARY = "commentary"
    DESCRIPTIVE = "descriptive"
    MAIN = "main"
    UNKNOWN = "unknown"

    __str__ = str.__str__


Type11OrStr: TypeAlias = Annotated[Type11 | str, open_enum_validator(Type11)]
