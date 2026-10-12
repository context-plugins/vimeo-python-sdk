from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .live import Live, LiveDict
from .staff_pick import StaffPick, StaffPickDict


class Badges(SdkBaseModel):
    """A collection of the video's badges."""

    dolby_vision: Optional[bool] = UNSET
    """Whether the video was filmed using Dolby Vision."""

    hdr: bool
    """Whether the video has an HDR-compatible transcode."""

    hdr_10: Optional[bool] = UNSET
    """Whether the video was filmed using HDR10."""

    hdr_10_plus: Optional[bool] = UNSET
    """Whether the video was filmed using HDR10 Plus."""

    live: Live
    ott_4k: Optional[bool] = UNSET
    """Whether the video has a 4K-quality transcode."""

    ott_5_1_audio: Optional[bool] = UNSET
    """Whether the video has 5.1 audio."""

    ott_hevc: Optional[bool] = UNSET
    """Whether the video has an HEVC-compatible transcode."""

    staff_pick: StaffPick
    stereo_spatial: Optional[bool] = UNSET
    """Whether the video was filmed using stereo spatial."""

    vod: bool
    """Whether the video is a Vimeo On Demand video."""

    weekend_challenge: bool
    """Whether the video is a Vimeo Weekend Challenge."""


class BadgesDict(TypedDict):
    dolby_vision: NotRequired[bool]
    hdr: bool
    hdr_10: NotRequired[bool]
    hdr_10_plus: NotRequired[bool]
    live: LiveDict
    ott_4k: NotRequired[bool]
    ott_5_1_audio: NotRequired[bool]
    ott_hevc: NotRequired[bool]
    staff_pick: StaffPickDict
    stereo_spatial: NotRequired[bool]
    vod: bool
    weekend_challenge: bool
