from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosPicturesRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the image created by the **time** field should be the default thumbnail for the video."""

    time: Optional[float] = UNSET
    """The time offset in seconds from which to create the thumbnail."""


class VideosPicturesRequestDict(TypedDict):
    active: NotRequired[bool]
    time: NotRequired[float]
