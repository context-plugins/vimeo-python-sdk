from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort3(str, Enum):
    LAST_VIDEO_FEATURED_TIME = "last_video_featured_time"
    NAME = "name"

    __str__ = str.__str__


Sort3OrStr: TypeAlias = Annotated[Sort3 | str, open_enum_validator(Sort3)]
