from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type15(str, Enum):
    """The Vimeo content to which the comment relates.

    Option descriptions:
     * ``video`` - The comment is about a video."""

    VIDEO = "video"

    __str__ = str.__str__


Type15OrStr: TypeAlias = Annotated[Type15 | str, open_enum_validator(Type15)]
