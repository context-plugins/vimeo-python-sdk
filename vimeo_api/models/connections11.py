from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .available_videos import AvailableVideos, AvailableVideosDict
from .requested_clip import RequestedClip, RequestedClipDict
from .videos9 import Videos9, Videos9Dict


class Connections11(SdkBaseModel):
    """Information about showcase connections."""

    available_videos: AvailableVideos
    """Information about the authenticated user's videos that can be added to or removed from this showcase. This data
    requires a bearer token with the ``private`` scope."""

    requested_clip: RequestedClip
    """Information about the requested video."""

    videos: Videos9
    """Information about the videos that belong to the showcase."""


class Connections11Dict(TypedDict):
    available_videos: AvailableVideosDict
    requested_clip: RequestedClipDict
    videos: Videos9Dict
