from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .videos14 import Videos14, Videos14Dict


class Connections22(SdkBaseModel):
    """A list of resource URIs related to the preset."""

    videos: Videos14
    """Information about the videos in the preset."""


class Connections22Dict(TypedDict):
    videos: Videos14 | Videos14Dict
