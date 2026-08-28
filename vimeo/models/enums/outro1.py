from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Outro1(str, Enum):
    """What to do with the outro.

    Option descriptions:
     * ``nothing`` - Disable the outro."""

    NOTHING = "nothing"

    __str__ = str.__str__


Outro1OrStr: TypeAlias = Annotated[Outro1 | str, open_enum_validator(Outro1)]
