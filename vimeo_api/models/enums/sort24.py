from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort24(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    NAME = "name"

    __str__ = str.__str__


Sort24OrStr: TypeAlias = Annotated[Sort24 | str, open_enum_validator(Sort24)]
