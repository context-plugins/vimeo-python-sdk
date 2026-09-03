from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status8 import Status8OrStr


class Transcode1(SdkBaseModel):
    """The transcode information for the audio track."""

    status: Status8OrStr
    """The transcode status of the audio track.

    Option descriptions:
     * ``complete`` - Transcoding is complete. The audio track is available.
     * ``error`` - There was a transcoding error. The audio track isn't available.
     * ``in_progress`` - Transcoding is in progress. The audio track isn't available yet."""


class Transcode1Dict(TypedDict):
    status: Status8OrStr
