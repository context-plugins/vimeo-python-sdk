from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter3(str, Enum):
    EMBEDDABLE = "embeddable"

    __str__ = str.__str__


Filter3OrStr: TypeAlias = Annotated[Filter3 | str, open_enum_validator(Filter3)]
