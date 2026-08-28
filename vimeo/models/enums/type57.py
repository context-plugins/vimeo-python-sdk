from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type57(str, Enum):
    """The type of audio track.

    Option descriptions:
     * ``commentary`` - The audio track is the commentary type.
     * ``descriptive`` - The audio track is the descriptive type.
     * ``main`` - The audio track is the main type."""

    COMMENTARY = "commentary"
    DESCRIPTIVE = "descriptive"
    MAIN = "main"

    __str__ = str.__str__


Type57OrStr: TypeAlias = Annotated[Type57 | str, open_enum_validator(Type57)]
