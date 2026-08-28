from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type31(str, Enum):
    ALL = "all"
    ONE_TIME = "one_time"
    RECURRING = "recurring"

    __str__ = str.__str__


Type31OrStr: TypeAlias = Annotated[Type31 | str, open_enum_validator(Type31)]
