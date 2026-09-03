from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter27(str, Enum):
    VIEWABLE = "viewable"

    __str__ = str.__str__


Filter27OrStr: TypeAlias = Annotated[Filter27 | str, open_enum_validator(Filter27)]
