from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class QuotaUnit(str, Enum):
    """The unit of the video storage for the user's periodic quota for the annual plan.

    Option descriptions:
     * ``video_count`` - The product has video storage based on video count.
     * ``video_size`` - The product has video storage based on video size."""

    VIDEO_COUNT = "video_count"
    VIDEO_SIZE = "video_size"

    __str__ = str.__str__


QuotaUnitOrStr: TypeAlias = Annotated[QuotaUnit | str, open_enum_validator(QuotaUnit)]
