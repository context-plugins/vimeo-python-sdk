from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter18(str, Enum):
    FILM = "film"
    SERIES = "series"

    __str__ = str.__str__


Filter18OrStr: TypeAlias = Annotated[Filter18 | str, open_enum_validator(Filter18)]
