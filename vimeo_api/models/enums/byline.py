from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Byline(str, Enum):
    """How the embeddable player handles the video owner's information.

    Option descriptions:
     * ``hide`` - The owner's information is hidden.
     * ``show`` - The owner's information is shown.
     * ``user`` - The owner's information can be toggled to ``show`` or ``hide`` by the user."""

    HIDE = "hide"
    SHOW = "show"
    USER = "user"

    __str__ = str.__str__


BylineOrStr: TypeAlias = Annotated[Byline | str, open_enum_validator(Byline)]
