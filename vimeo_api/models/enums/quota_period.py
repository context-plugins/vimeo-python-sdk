from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class QuotaPeriod(str, Enum):
    """The quota period unit for the user's bandwidth quota.

    Option descriptions:
     * ``month`` - The product has a monthly bandwidth quota period.
     * ``week`` - The product has a weekly bandwidth quota period.
     * ``year`` - The product has a yearly bandwidth quota period."""

    MONTH = "month"
    WEEK = "week"
    YEAR = "year"

    __str__ = str.__str__


QuotaPeriodOrStr: TypeAlias = Annotated[QuotaPeriod | str, open_enum_validator(QuotaPeriod)]
