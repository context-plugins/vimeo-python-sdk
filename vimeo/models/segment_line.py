from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SegmentLine(SdkBaseModel):
    text: str
    """The text from the segment line."""

    voice: str | None
    """The speaker of the segment line."""


class SegmentLineDict(TypedDict):
    text: str
    voice: str | None
