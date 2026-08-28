from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort32(str, Enum):
    ADDED = "added"
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    MODIFIED_TIME = "modified_time"
    NAME = "name"
    PUBLISH_TIME = "publish.time"
    RATING = "rating"

    __str__ = str.__str__


Sort32OrStr: TypeAlias = Annotated[Sort32 | str, open_enum_validator(Sort32)]
