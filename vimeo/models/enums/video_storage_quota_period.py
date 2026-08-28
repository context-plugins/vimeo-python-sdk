from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VideoStorageQuotaPeriod(str, Enum):
    """The video storage quota period for the annual plan.

    Option descriptions:
     * ``lifetime`` - The product has a lifetime video storage quota period.
     * ``month`` - The product has a monthly video storage quota period.
     * ``week`` - The product has a weekly video storage quota period.
     * ``year`` - The product has a yearly video storage quota period."""

    LIFETIME = "lifetime"
    MONTH = "month"
    WEEK = "week"
    YEAR = "year"

    __str__ = str.__str__


VideoStorageQuotaPeriodOrStr: TypeAlias = Annotated[
    VideoStorageQuotaPeriod | str, open_enum_validator(VideoStorageQuotaPeriod)
]
