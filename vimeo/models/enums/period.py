from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Period(str, Enum):
    """The time period for which the AI credit activity is evaluated.

    Option descriptions:
     * ``lifetime`` - The quota period is for the lifetime of the account.
     * ``month`` - The quota period is one month.
     * ``week`` - The quota period is one week.
     * ``year`` - The quota period is one year."""

    LIFETIME = "lifetime"
    MONTH = "month"
    WEEK = "week"
    YEAR = "year"

    __str__ = str.__str__


PeriodOrStr: TypeAlias = Annotated[Period | str, open_enum_validator(Period)]
