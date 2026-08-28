from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort43(str, Enum):
    DATE = "date"
    MANUAL = "manual"

    __str__ = str.__str__


Sort43OrStr: TypeAlias = Annotated[Sort43 | str, open_enum_validator(Sort43)]
