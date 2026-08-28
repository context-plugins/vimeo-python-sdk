from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter25(str, Enum):
    EXTRA = "extra"
    MAIN = "main"
    TRAILER = "trailer"

    __str__ = str.__str__


Filter25OrStr: TypeAlias = Annotated[Filter25 | str, open_enum_validator(Filter25)]
