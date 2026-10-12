from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price7 import Price7, Price7Dict


class Buy5(SdkBaseModel):
    price: Optional[Price7] = UNSET


class Buy5Dict(TypedDict):
    price: NotRequired[Price7Dict]
