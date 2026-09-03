from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ChannelsVideosPicturesRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the image created by the **time** field should be the default thumbnail for the video."""

    time: Optional[float] = UNSET
    """The time offset in seconds from which to create the thumbnail."""


class ChannelsVideosPicturesRequestDict(TypedDict):
    active: NotRequired[bool]
    time: NotRequired[float]
