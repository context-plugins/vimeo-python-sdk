from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type24(str, Enum):
    """The type of text track.

    Option descriptions:
     * ``captions`` - The text track is for captions.
     * ``subtitles`` - The text track is for subtitles."""

    CAPTIONS = "captions"
    SUBTITLES = "subtitles"

    __str__ = str.__str__


Type24OrStr: TypeAlias = Annotated[Type24 | str, open_enum_validator(Type24)]
