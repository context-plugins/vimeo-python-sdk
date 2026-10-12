from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .segment1 import Segment1, Segment1Dict


class VideosAiTexttracksRequest(SdkBaseModel):
    segments: Optional[list[Segment1]] = UNSET
    """The segments to edit."""


class VideosAiTexttracksRequestDict(TypedDict):
    segments: NotRequired[list[Segment1Dict]]
