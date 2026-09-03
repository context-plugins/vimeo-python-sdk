from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosPicturesRequest1(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether this thumbnail is the default."""


class VideosPicturesRequest1Dict(TypedDict):
    active: NotRequired[bool]
