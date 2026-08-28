from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type23(str, Enum):
    """The type of video.

    Option descriptions:
     * ``extra`` - The video is an extra feature.
     * ``main`` - The video is a main feature.
     * ``trailer`` - The video is a trailer."""

    EXTRA = "extra"
    MAIN = "main"
    TRAILER = "trailer"

    __str__ = str.__str__


Type23OrStr: TypeAlias = Annotated[Type23 | str, open_enum_validator(Type23)]
