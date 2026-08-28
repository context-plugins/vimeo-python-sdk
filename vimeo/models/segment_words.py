from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SegmentWords(SdkBaseModel):
    end_time: float | None
    """The end time of the word in milliseconds."""

    start_time: float | None
    """The start time of the word in milliseconds."""

    word: str
    """The word text."""


class SegmentWordsDict(TypedDict):
    end_time: float | None
    start_time: float | None
    word: str
