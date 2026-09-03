from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status19 import Status19OrStr


class EditSession(SdkBaseModel):
    """Information about the video's Vimeo Create editing session. This data requires a bearer token with the
    ``private`` scope."""

    status: Status19OrStr
    """The status of the video's edit session. This data requires a bearer token with the ``private`` scope.

    Option descriptions:
     * ``done`` - The video is finished processing.
     * ``failed`` - Video processing has failed.
     * ``processing`` - The video is still being processed."""


class EditSessionDict(TypedDict):
    status: Status19OrStr
