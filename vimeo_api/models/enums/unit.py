from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Unit(str, Enum):
    """The unit that's used to compute quota.

    Option descriptions:
     * ``video_count`` - The quota is calculated using the count of the videos.
     * ``video_size`` - The quota is calculated using the byte size of the videos."""

    VIDEO_COUNT = "video_count"
    VIDEO_SIZE = "video_size"

    __str__ = str.__str__


UnitOrStr: TypeAlias = Annotated[Unit | str, open_enum_validator(Unit)]
