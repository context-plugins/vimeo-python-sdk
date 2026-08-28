from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type13(str, Enum):
    """The Vimeo content to which the reply relates.

    Option descriptions:
     * ``video`` - The comment is about a video."""

    VIDEO = "video"

    __str__ = str.__str__


Type13OrStr: TypeAlias = Annotated[Type13 | str, open_enum_validator(Type13)]
