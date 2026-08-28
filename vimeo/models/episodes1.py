from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buy4 import Buy4, Buy4Dict
from .rent3 import Rent3, Rent3Dict


class Episodes1(SdkBaseModel):
    buy: Optional[Buy4] = UNSET
    rent: Optional[Rent3] = UNSET


class Episodes1Dict(TypedDict):
    buy: NotRequired[Buy4 | Buy4Dict]
    rent: NotRequired[Rent3 | Rent3Dict]
