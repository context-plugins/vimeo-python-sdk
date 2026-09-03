from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Segment1(SdkBaseModel):
    end_time: Optional[float] = UNSET
    """The end time in milliseconds. Must be non-negative. Cannot overlap with the next segment's start time."""

    id: Optional[str] = UNSET
    """The segment UUID."""

    start_time: Optional[float] = UNSET
    """The start time in milliseconds. Must be non-negative and less than ``end_time``. Cannot overlap with the previous
    segment's end time."""

    text: Optional[str] = UNSET
    """The updated text for the segment. Required for text edits; omit for timestamp-only changes."""


class Segment1Dict(TypedDict):
    end_time: NotRequired[float]
    id: NotRequired[str]
    start_time: NotRequired[float]
    text: NotRequired[str]
