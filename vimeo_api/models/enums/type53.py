from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type53(str, Enum):
    """The type of audio track.

    Option descriptions:
     * ``commentary`` - The audio track is the commentary type.
     * ``descriptive`` - The audio track is the descriptive type.
     * ``main`` - The audio track is the main type."""

    COMMENTARY = "commentary"
    DESCRIPTIVE = "descriptive"
    MAIN = "main"

    __str__ = str.__str__


Type53OrStr: TypeAlias = Annotated[Type53 | str, open_enum_validator(Type53)]
