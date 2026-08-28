from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LiveEventsPicturesRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the thumbnail is the event's active thumbnail."""


class LiveEventsPicturesRequestDict(TypedDict):
    active: NotRequired[bool]
