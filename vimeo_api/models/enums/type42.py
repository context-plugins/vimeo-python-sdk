from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type42(str, Enum):
    """The type of the video.

    Option descriptions:
     * ``extra`` - The video type is extra footage.
     * ``main`` - The video type is the main video.
     * ``trailer`` - The video type is a trailer."""

    EXTRA = "extra"
    MAIN = "main"
    TRAILER = "trailer"

    __str__ = str.__str__


Type42OrStr: TypeAlias = Annotated[Type42 | str, open_enum_validator(Type42)]
