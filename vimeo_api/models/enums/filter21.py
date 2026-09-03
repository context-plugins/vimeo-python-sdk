from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter21(str, Enum):
    FOLDER = "folder"
    LIVE_EVENT = "live_event"
    VIDEO = "video"

    __str__ = str.__str__


Filter21OrStr: TypeAlias = Annotated[Filter21 | str, open_enum_validator(Filter21)]
