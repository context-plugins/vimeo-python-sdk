from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DownloadLinks(SdkBaseModel):
    """A map of read-only download URLs for the text track, keyed by file format."""

    srt: Optional[str] = UNSET
    """The download URL for the SubRip representation."""

    ttml: Optional[str] = UNSET
    """The download URL for the TTML representation."""

    vtt: Optional[str] = UNSET
    """The download URL for the WebVTT representation."""


class DownloadLinksDict(TypedDict):
    srt: NotRequired[str]
    ttml: NotRequired[str]
    vtt: NotRequired[str]
