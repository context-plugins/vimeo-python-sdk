from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort36(str, Enum):
    DATE = "date"
    DEFAULT = "default"
    MODIFIED_TIME = "modified_time"
    NAME = "name"
    PINNED_ON = "pinned_on"

    __str__ = str.__str__


Sort36OrStr: TypeAlias = Annotated[Sort36 | str, open_enum_validator(Sort36)]
