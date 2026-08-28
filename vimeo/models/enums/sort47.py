from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort47(str, Enum):
    CREATED_TIME = "created_time"
    DURATION = "duration"
    NAME = "name"

    __str__ = str.__str__


Sort47OrStr: TypeAlias = Annotated[Sort47 | str, open_enum_validator(Sort47)]
