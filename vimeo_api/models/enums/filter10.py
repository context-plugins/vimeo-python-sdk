from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter10(str, Enum):
    EMBEDDABLE = "embeddable"
    PLAYABLE = "playable"

    __str__ = str.__str__


Filter10OrStr: TypeAlias = Annotated[Filter10 | str, open_enum_validator(Filter10)]
