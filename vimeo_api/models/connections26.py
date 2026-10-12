from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .created_version import CreatedVersion, CreatedVersionDict
from .root_version import RootVersion, RootVersionDict
from .video2 import Video2, Video2Dict


class Connections26(SdkBaseModel):
    created_version: CreatedVersion
    """Information about the video version that is created from the trim operation."""

    root_version: RootVersion
    """Information about the video version that is the source of the trimmed video."""

    video: Video2
    """Information about the video associated with the trim."""


class Connections26Dict(TypedDict):
    created_version: CreatedVersionDict
    root_version: RootVersionDict
    video: Video2Dict
