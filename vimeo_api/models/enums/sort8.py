from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort8(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"

    __str__ = str.__str__


Sort8OrStr: TypeAlias = Annotated[Sort8 | str, open_enum_validator(Sort8)]
