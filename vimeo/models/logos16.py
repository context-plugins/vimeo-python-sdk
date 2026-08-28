from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom16 import Custom16, Custom16Dict


class Logos16(SdkBaseModel):
    custom: Optional[Custom16] = UNSET
    vimeo: Optional[bool] = UNSET
    """Whether to show the Vimeo logo on the embeddable player."""


class Logos16Dict(TypedDict):
    custom: NotRequired[Custom16 | Custom16Dict]
    vimeo: NotRequired[bool]
