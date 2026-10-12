from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom8 import Custom8, Custom8Dict


class Logos8(SdkBaseModel):
    custom: Optional[Custom8] = UNSET
    vimeo: Optional[bool] = UNSET
    """Whether to show the Vimeo logo on the embeddable player."""


class Logos8Dict(TypedDict):
    custom: NotRequired[Custom8Dict]
    vimeo: NotRequired[bool]
