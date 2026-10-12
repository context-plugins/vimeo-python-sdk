from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price2 import Price2, Price2Dict


class Buy3(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the video can be purchased. This parameter is required when **rent.active** is ``false``."""

    download: Optional[bool] = UNSET
    """Whether people who buy the video can download it. To use this parameter, **type** must be ``film``."""

    price: Optional[Price2] = UNSET


class Buy3Dict(TypedDict):
    active: NotRequired[bool]
    download: NotRequired[bool]
    price: NotRequired[Price2Dict]
