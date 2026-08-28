from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Period4(str, Enum):
    """The rental period for the video.

    Option descriptions:
     * ``1 day`` - The rental period is one day.
     * ``1 month`` - The rental period is one month.
     * ``1 week`` - The rental period is one week.
     * ``1 year`` - The rental period is one year.
     * ``2 day`` - The rental period is two days.
     * ``3 day`` - The rental period is three days.
     * ``3 month`` - The rental period is three months.
     * ``6 month`` - The rental period is six months.
     * ``7 day`` - The rental period is seven days.
     * ``24 hour`` - The rental period is 24 hours.
     * ``30 day`` - The rental period is 30 days.
     * ``48 hour`` - The rental period is 48 hours.
     * ``60 day`` - The rental period is 60 days.
     * ``72 hour`` - The rental period is 72 hours."""

    _1_DAY = "1 day"
    _1_MONTH = "1 month"
    _1_WEEK = "1 week"
    _1_YEAR = "1 year"
    _2_DAY = "2 day"
    _3_DAY = "3 day"
    _3_MONTH = "3 month"
    _6_MONTH = "6 month"
    _7_DAY = "7 day"
    _24_HOUR = "24 hour"
    _30_DAY = "30 day"
    _48_HOUR = "48 hour"
    _60_DAY = "60 day"
    _72_HOUR = "72 hour"

    __str__ = str.__str__


Period4OrStr: TypeAlias = Annotated[Period4 | str, open_enum_validator(Period4)]
