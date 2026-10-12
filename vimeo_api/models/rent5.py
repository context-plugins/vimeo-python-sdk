from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price8 import Price8, Price8Dict


class Rent5(SdkBaseModel):
    price: Optional[Price8] = UNSET


class Rent5Dict(TypedDict):
    price: NotRequired[Price8Dict]
