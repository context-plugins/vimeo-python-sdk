from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort41(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    NAME = "name"
    PUBLISH_TIME = "publish.time"
    VIDEOS = "videos"

    __str__ = str.__str__


Sort41OrStr: TypeAlias = Annotated[Sort41 | str, open_enum_validator(Sort41)]
