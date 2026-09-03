from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .video3 import Video3, Video3Dict


class Connections27(SdkBaseModel):
    video: Video3
    """Data from the video associated with the version."""


class Connections27Dict(TypedDict):
    video: Video3 | Video3Dict
