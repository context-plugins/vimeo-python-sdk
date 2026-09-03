from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort74(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    DURATION = "duration"
    VIDEOS = "videos"

    __str__ = str.__str__


Sort74OrStr: TypeAlias = Annotated[Sort74 | str, open_enum_validator(Sort74)]
