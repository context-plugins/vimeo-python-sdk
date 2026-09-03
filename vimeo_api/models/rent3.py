from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.period5 import Period5OrStr
from .price4 import Price4, Price4Dict


class Rent3(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether episodes can be rented."""

    period: Optional[Period5OrStr] = UNSET
    """The rental period of the episode.

    Option descriptions:
     * ``1 week`` - The episode can be rented for a maximum of 1 week.
     * ``1 year`` - The episode can be rented for a maximum of 1 year.
     * ``3 month`` - The episode can be rented for a maximum of 3 months.
     * ``6 month`` - The episode can be rented for a maximum of 6 months.
     * ``24 hour`` - The episode can be rented for a maximum of 24 hours.
     * ``30 day`` - The episode can be rented for a maximum of 30 days.
     * ``48 hour`` - The episode can be rented for a maximum of 48 hours.
     * ``72 hour`` - The episode can be rented for a maximum of 72 hours."""

    price: Optional[Price4] = UNSET


class Rent3Dict(TypedDict):
    active: NotRequired[bool]
    period: NotRequired[Period5OrStr]
    price: NotRequired[Price4 | Price4Dict]
