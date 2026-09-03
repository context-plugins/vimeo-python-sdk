from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort44(str, Enum):
    DATE = "date"
    DEFAULT = "default"
    MANUAL = "manual"
    NAME = "name"
    PURCHASE_TIME = "purchase_time"
    RELEASE_DATE = "release_date"

    __str__ = str.__str__


Sort44OrStr: TypeAlias = Annotated[Sort44 | str, open_enum_validator(Sort44)]
