from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .video1 import Video1, Video1Dict


class Connections12(SdkBaseModel):
    video: Video1
    """The associated video object. This data requires a bearer token with the ``private`` scope."""


class Connections12Dict(TypedDict):
    video: Video1 | Video1Dict
