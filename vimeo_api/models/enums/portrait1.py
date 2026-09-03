from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Portrait1(str, Enum):
    """How the embeddable player handles the video owner's portrait.

    Option descriptions:
     * ``hide`` - The owner's portrait is hidden.
     * ``show`` - The owner's portrait is shown.
     * ``user`` - The owner's portrait can be toggled to ``show`` or ``hide`` by the user."""

    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    __str__ = str.__str__


Portrait1OrStr: TypeAlias = Annotated[Portrait1 | str, open_enum_validator(Portrait1)]
