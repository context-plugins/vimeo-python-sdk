from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Kind1(str, Enum):
    """The type of caption that the segment originates from.

    Option descriptions:
     * ``captions`` - The segment originates from a captions file.
     * ``subtitles`` - The segment originates from a captions and subtitles file."""

    CAPTIONS = "captions"
    SUBTITLES = "subtitles"

    __str__ = str.__str__


Kind1OrStr: TypeAlias = Annotated[Kind1 | str, open_enum_validator(Kind1)]
