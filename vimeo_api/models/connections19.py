from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .videos12 import Videos12, Videos12Dict


class Connections19(SdkBaseModel):
    videos: Videos12
    """The connection to the associated videos."""


class Connections19Dict(TypedDict):
    videos: Videos12 | Videos12Dict
