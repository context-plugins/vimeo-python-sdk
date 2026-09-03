from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditsPeriod(str, Enum):
    """The quota period unit for the user's AI credits quota.

    Option descriptions:
     * ``month`` - The product has a monthly AI credits quota period.
     * ``week`` - The product has a weekly AI credits quota period.
     * ``year`` - The product has a yearly AI credits quota period."""

    MONTH = "month"
    WEEK = "week"
    YEAR = "year"

    __str__ = str.__str__


CreditsPeriodOrStr: TypeAlias = Annotated[CreditsPeriod | str, open_enum_validator(CreditsPeriod)]
