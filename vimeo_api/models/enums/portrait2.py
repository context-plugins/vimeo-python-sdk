from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Portrait2(str, Enum):
    """How to handle the owner portrait in the title bar of the embeddable player.

    Option descriptions:
     * ``hide`` - Hide the portrait.
     * ``show`` - Show the portrait.
     * ``user`` - Enable the user to decide."""

    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    __str__ = str.__str__


Portrait2OrStr: TypeAlias = Annotated[Portrait2 | str, open_enum_validator(Portrait2)]
