from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Name1(str, Enum):
    """How to handle the video title in the title bar of the embeddable player.

    Option descriptions:
     * ``hide`` - Hide the video title.
     * ``show`` - Show the video title.
     * ``user`` - Enable the user to decide."""

    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    __str__ = str.__str__


Name1OrStr: TypeAlias = Annotated[Name1 | str, open_enum_validator(Name1)]
