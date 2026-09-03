from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter30(str, Enum):
    VIDEO = "video"

    __str__ = str.__str__


Filter30OrStr: TypeAlias = Annotated[Filter30 | str, open_enum_validator(Filter30)]
