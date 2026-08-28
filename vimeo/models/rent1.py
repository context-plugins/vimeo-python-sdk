from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.period4 import Period4OrStr


class Rent1(SdkBaseModel):
    active: bool
    """Whether all the videos on the On Demand page can be rented as a whole."""

    period: Period4OrStr | None
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

    price: float | None
    """The default price to rent an episode."""


class Rent1Dict(TypedDict):
    active: bool
    period: Period4OrStr | None
    price: float | None
