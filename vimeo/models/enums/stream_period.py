from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StreamPeriod(str, Enum):
    """The amount of time that the user has access to the On Demand content after redeeming a promotional code.

    Option descriptions:
     * ``1_week`` - Access lasts for one week.
     * ``1_year`` - Access lasts for one year.
     * ``3_month`` - Access lasts for three months.
     * ``6_month`` - Access lasts for six months.
     * ``24_hour`` - Access lasts for 24 hours.
     * ``30_days`` - Access lasts for 30 days.
     * ``48_hour`` - Access lasts for 48 hours.
     * ``72_hour`` - Access lasts for 72 hours."""

    _1_WEEK = "1_week"
    _1_YEAR = "1_year"
    _3_MONTH = "3_month"
    _6_MONTH = "6_month"
    _24_HOUR = "24_hour"
    _30_DAYS = "30_days"
    _48_HOUR = "48_hour"
    _72_HOUR = "72_hour"

    __str__ = str.__str__


StreamPeriodOrStr: TypeAlias = Annotated[StreamPeriod | str, open_enum_validator(StreamPeriod)]
