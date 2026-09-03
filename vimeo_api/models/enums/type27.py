from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type27(str, Enum):
    ALL = "all"
    ONE_TIME = "one_time"
    RECURRING = "recurring"

    __str__ = str.__str__


Type27OrStr: TypeAlias = Annotated[Type27 | str, open_enum_validator(Type27)]
