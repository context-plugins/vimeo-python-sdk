from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Period1(str, Enum):
    """The quota period for which the bandwidth is evaluated.

    Option descriptions:
     * ``calendar_month`` - The quota period is one month.
     * ``year`` - The quota period is one year."""

    CALENDAR_MONTH = "calendar_month"
    YEAR = "year"

    __str__ = str.__str__


Period1OrStr: TypeAlias = Annotated[Period1 | str, open_enum_validator(Period1)]
