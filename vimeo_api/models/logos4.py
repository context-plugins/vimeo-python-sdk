from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom4 import Custom4, Custom4Dict


class Logos4(SdkBaseModel):
    custom: Optional[Custom4] = UNSET
    vimeo: Optional[bool] = UNSET
    """Whether to show the Vimeo logo on the embed player."""


class Logos4Dict(TypedDict):
    custom: NotRequired[Custom4 | Custom4Dict]
    vimeo: NotRequired[bool]
