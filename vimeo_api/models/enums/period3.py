from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Period3(str, Enum):
    """The renewal frequency of the quota.

    Option descriptions:
     * ``lifetime`` - The user doesn't have a periodic quota.
     * ``month`` - The quota renews monthly.
     * ``week`` - The quota renews weekly.
     * ``year`` - The quota renews yearly."""

    LIFETIME = "lifetime"
    MONTH = "month"
    WEEK = "week"
    YEAR = "year"

    __str__ = str.__str__


Period3OrStr: TypeAlias = Annotated[Period3 | str, open_enum_validator(Period3)]
