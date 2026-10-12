from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.period6 import Period6OrStr
from .price5 import Price5, Price5Dict


class Rent4(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the video can be rented. This parameter is required when **episodes.rent.active** is ``true``."""

    period: Optional[Period6OrStr] = UNSET
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

    price: Optional[Price5] = UNSET


class Rent4Dict(TypedDict):
    active: NotRequired[bool]
    period: NotRequired[Period6OrStr]
    price: NotRequired[Price5Dict]
