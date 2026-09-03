from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .season1 import Season1, Season1Dict


class Connections20(SdkBaseModel):
    season: Season1
    """Information about the video's season."""


class Connections20Dict(TypedDict):
    season: Season1 | Season1Dict
