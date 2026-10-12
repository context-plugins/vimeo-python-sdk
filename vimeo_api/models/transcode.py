from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status6 import Status6OrStr


class Transcode(SdkBaseModel):
    """The transcode information of the video upload."""

    status: Optional[Status6OrStr] = UNSET
    """The video's availability status.

    Option descriptions:
     * ``complete`` - Transcoding is complete. The video is available.
     * ``error`` - There was a transcoding error. The video isn't available.
     * ``in_progress`` - Transcoding is currently underway. The video isn't available yet."""


class TranscodeDict(TypedDict):
    status: NotRequired[Status6OrStr]
