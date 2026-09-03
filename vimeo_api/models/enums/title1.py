from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Title1(str, Enum):
    """How the embeddable player handles the video title.

    Option descriptions:
     * ``hide`` - The title is hidden.
     * ``show`` - The title is shown.
     * ``user`` - The title can be toggled to ``show`` or ``hide`` by the user."""

    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    __str__ = str.__str__


Title1OrStr: TypeAlias = Annotated[Title1 | str, open_enum_validator(Title1)]
