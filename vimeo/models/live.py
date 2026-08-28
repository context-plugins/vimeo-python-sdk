from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Live(SdkBaseModel):
    archived: bool
    """Whether the video was streamed live."""

    streaming: bool
    """Whether the video is currently streaming live."""


class LiveDict(TypedDict):
    archived: bool
    streaming: bool
