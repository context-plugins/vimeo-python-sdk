from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Position1(str, Enum):
    """Where the logo renders relative to the title. Null until the logo is enabled."""

    LEFT = "left"
    RIGHT = "right"

    __str__ = str.__str__


Position1OrStr: TypeAlias = Annotated[Position1 | str, open_enum_validator(Position1)]
