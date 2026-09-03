from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort33(str, Enum):
    ADDED = "added"
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    NAME = "name"
    PURCHASE_TIME = "purchase_time"
    RATING = "rating"
    RELEASE_DATE = "release_date"

    __str__ = str.__str__


Sort33OrStr: TypeAlias = Annotated[Sort33 | str, open_enum_validator(Sort33)]
