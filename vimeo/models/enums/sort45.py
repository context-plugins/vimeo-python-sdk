from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort45(str, Enum):
    DATE = "date"
    DEFAULT = "default"
    EPISODE = "episode"
    MANUAL = "manual"
    NAME = "name"
    PURCHASE_TIME = "purchase_time"
    RELEASE_DATE = "release_date"

    __str__ = str.__str__


Sort45OrStr: TypeAlias = Annotated[Sort45 | str, open_enum_validator(Sort45)]
