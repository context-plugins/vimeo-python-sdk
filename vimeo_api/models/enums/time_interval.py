from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TimeInterval(str, Enum):
    DAY = "day"
    MONTH = "month"
    NONE = "none"
    WEEK = "week"
    YEAR = "year"

    __str__ = str.__str__


TimeIntervalOrStr: TypeAlias = Annotated[TimeInterval | str, open_enum_validator(TimeInterval)]
