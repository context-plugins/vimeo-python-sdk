from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status4 import Status4OrStr
from .hls_dash_video_file import HlsDashVideoFile, HlsDashVideoFileDict
from .progressive import Progressive, ProgressiveDict


class Play(SdkBaseModel):
    dash: Optional[HlsDashVideoFile] = UNSET
    """The DASH video file."""

    hls: Optional[HlsDashVideoFile] = UNSET
    """The HLS video file."""

    player_fairplay_certificate_url: str
    """The player URL hosting the FairPlay certification that's required for the digital rights management playback."""

    player_license_url: str
    """The player license URL related to DRM playback."""

    progressive: Optional[list[Progressive]] = UNSET
    """The progressive video files."""

    status: Status4OrStr
    """The play status of the video.

    Option descriptions:
     * ``drm_plays_exceeded`` - The user's quota for DRM plays has been exceeded.
     * ``playable`` - The video is playable.
     * ``purchase_required`` - The video must be purchased.
     * ``restricted`` - Playback for the video is restricted.
     * ``unavailable`` - The video is unavailable."""


class PlayDict(TypedDict):
    dash: NotRequired[HlsDashVideoFileDict]
    hls: NotRequired[HlsDashVideoFileDict]
    player_fairplay_certificate_url: str
    player_license_url: str
    progressive: NotRequired[list[ProgressiveDict]]
    status: Status4OrStr
