from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom10 import Custom10, Custom10Dict


class Logos10(SdkBaseModel):
    custom: Optional[Custom10] = UNSET
    vimeo: Optional[bool] = UNSET
    """Whether to show the Vimeo logo on the embeddable player."""


class Logos10Dict(TypedDict):
    custom: NotRequired[Custom10 | Custom10Dict]
    vimeo: NotRequired[bool]
