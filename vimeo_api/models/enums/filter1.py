from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter1(str, Enum):
    FEATURED = "featured"

    __str__ = str.__str__


Filter1OrStr: TypeAlias = Annotated[Filter1 | str, open_enum_validator(Filter1)]
