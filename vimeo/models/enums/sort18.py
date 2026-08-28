from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort18(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    DURATION = "duration"
    LAST_MODIFIED = "last_modified"
    VIDEOS = "videos"

    __str__ = str.__str__


Sort18OrStr: TypeAlias = Annotated[Sort18 | str, open_enum_validator(Sort18)]
