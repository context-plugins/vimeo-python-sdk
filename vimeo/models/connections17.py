from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .clip import Clip, ClipDict


class Connections17(SdkBaseModel):
    """A collection of information that is connected to this resource."""

    clip: Clip
    """Information about the videos that belong to this channel."""


class Connections17Dict(TypedDict):
    clip: Clip | ClipDict
