from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter13(str, Enum):
    ONLINE = "online"

    __str__ = str.__str__


Filter13OrStr: TypeAlias = Annotated[Filter13 | str, open_enum_validator(Filter13)]
