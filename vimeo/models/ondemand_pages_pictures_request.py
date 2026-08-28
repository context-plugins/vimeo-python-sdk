from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OndemandPagesPicturesRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether this poster is the one that appears on the On Demand page."""


class OndemandPagesPicturesRequestDict(TypedDict):
    active: NotRequired[bool]
