from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Owner2(str, Enum):
    """How to handle the owner information in the title bar of the embeddable player.

    Option descriptions:
     * ``hide`` - Hide the owner info.
     * ``show`` - Show the owner info.
     * ``user`` - Enable the user to decide."""

    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    __str__ = str.__str__


Owner2OrStr: TypeAlias = Annotated[Owner2 | str, open_enum_validator(Owner2)]
