from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .videos13 import Videos13, Videos13Dict


class Connections21(SdkBaseModel):
    """A list of resource URIs related to the portfolio."""

    videos: Videos13
    """Information about the videos contained within the portfolio."""


class Connections21Dict(TypedDict):
    videos: Videos13Dict
