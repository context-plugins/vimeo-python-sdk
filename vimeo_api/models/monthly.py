from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price6 import Price6, Price6Dict


class Monthly(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether a monthly subscription is active. This parameter is required when **rent.active** and **buy.active** are
    ``false``."""

    price: Optional[Price6] = UNSET


class MonthlyDict(TypedDict):
    active: NotRequired[bool]
    price: NotRequired[Price6 | Price6Dict]
