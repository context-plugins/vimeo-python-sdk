from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StreamPeriod1(str, Enum):
    """The amount of time for which the user can access On Demand content upon redeeming a promotion code. This
    parameter is required only when the streaming period isn't defined in the On Demand container, or when creating
    promotions where **access_type** is ``vip`` or **product_type** is ``rent``.

    Option descriptions:
     * ``1_week`` - The user can access On Demand content for a maximum of 1 week after redeeming a promotion code.
     * ``1_year`` - The user can access On Demand content for a maximum of 1 year after redeeming a promotion code.
     * ``3_month`` - The user can access On Demand content for a maximum of 3 months after redeeming a promotion code.
     * ``6_month`` - The user can access On Demand content for a maximum of 6 months after redeeming a promotion code.
     * ``24_hour`` - The user can access On Demand content for a maximum of 24 hours after redeeming a promotion code.
     * ``30_day`` - The user can access On Demand content for a maximum of 30 days after redeeming a promotion code.
     * ``48_hour`` - The user can access On Demand content for a maximum of 48 hours after redeeming a promotion code.
     * ``72_hour`` - The user can access On Demand content for a maximum of 72 hours after redeeming a promotion
            code."""

    _1_WEEK = "1_week"
    _1_YEAR = "1_year"
    _3_MONTH = "3_month"
    _6_MONTH = "6_month"
    _24_HOUR = "24_hour"
    _30_DAY = "30_day"
    _48_HOUR = "48_hour"
    _72_HOUR = "72_hour"

    __str__ = str.__str__


StreamPeriod1OrStr: TypeAlias = Annotated[StreamPeriod1 | str, open_enum_validator(StreamPeriod1)]
