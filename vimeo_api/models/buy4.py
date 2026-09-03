from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price3 import Price3, Price3Dict


class Buy4(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether episodes can be purchased."""

    download: Optional[bool] = UNSET
    """Whether people who buy episodes can download them. To use this parameter, **type** must be ``series``."""

    price: Optional[Price3] = UNSET


class Buy4Dict(TypedDict):
    active: NotRequired[bool]
    download: NotRequired[bool]
    price: NotRequired[Price3 | Price3Dict]
