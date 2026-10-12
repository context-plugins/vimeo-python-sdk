from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .videos2 import Videos2, Videos2Dict


class Connections2(SdkBaseModel):
    """A collection of information that is connected to this resource."""

    videos: Videos2
    """Information about the videos related to this tag."""


class Connections2Dict(TypedDict):
    videos: Videos2Dict
