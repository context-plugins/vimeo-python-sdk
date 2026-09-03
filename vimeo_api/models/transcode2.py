from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status20 import Status20OrStr


class Transcode2(SdkBaseModel):
    """The version's transcode information."""

    status: Optional[Status20OrStr] = UNSET
    """The status code for the availability of the video version.

    Option descriptions:
     * ``complete`` - Transcoding is complete. The video version is available.
     * ``error`` - There was a transcoding error. The video version isn't available.
     * ``in_progress`` - Transcoding is in progress. The video version isn't available yet."""


class Transcode2Dict(TypedDict):
    status: NotRequired[Status20OrStr]
