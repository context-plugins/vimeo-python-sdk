from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Rendition2(str, Enum):
    """The rendition of the audio track.

    Option descriptions:
     * ``source`` - The audio is the source file."""

    SOURCE = "source"

    __str__ = str.__str__


Rendition2OrStr: TypeAlias = Annotated[Rendition2 | str, open_enum_validator(Rendition2)]
