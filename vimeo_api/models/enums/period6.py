from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Period6(str, Enum):
    """The rental period of the video.

    Option descriptions:
     * ``1 week`` - The video can be rented for a maximum of 1 week.
     * ``1 year`` - The video can be rented for a maximum of 1 year.
     * ``3 month`` - The video can be rented for a maximum of 3 months.
     * ``6 month`` - The video can be rented for a maximum of 6 months.
     * ``24 hour`` - The video can be rented for a maximum of 24 hours.
     * ``30 day`` - The video can be rented for a maximum of 30 days.
     * ``48 hour`` - The video can be rented for a maximum of 48 hours.
     * ``72 hour`` - The video can be rented for a maximum of 72 hours."""

    _1_WEEK = "1 week"
    _1_YEAR = "1 year"
    _3_MONTH = "3 month"
    _6_MONTH = "6 month"
    _24_HOUR = "24 hour"
    _30_DAY = "30 day"
    _48_HOUR = "48 hour"
    _72_HOUR = "72 hour"

    __str__ = str.__str__


Period6OrStr: TypeAlias = Annotated[Period6 | str, open_enum_validator(Period6)]
