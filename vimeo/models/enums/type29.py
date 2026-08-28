from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type29(str, Enum):
    """The type of text track.

    Option descriptions:
     * ``captions`` - The text track is the captions type.
     * ``chapters`` - The text track is the chapters type.
     * ``descriptions`` - The text track is the descriptions type.
     * ``metadata`` - The text track is the metadata type.
     * ``subtitles`` - The text track is the subtitles type."""

    CAPTIONS = "captions"
    CHAPTERS = "chapters"
    DESCRIPTIONS = "descriptions"
    METADATA = "metadata"
    SUBTITLES = "subtitles"

    __str__ = str.__str__


Type29OrStr: TypeAlias = Annotated[Type29 | str, open_enum_validator(Type29)]
