from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter46(str, Enum):
    RELATED = "related"

    __str__ = str.__str__


Filter46OrStr: TypeAlias = Annotated[Filter46 | str, open_enum_validator(Filter46)]
