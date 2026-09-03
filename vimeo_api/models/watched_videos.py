from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WatchedVideos(SdkBaseModel):
    """Information about the videos that the authenticated user has watched."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    total: Optional[float] = UNSET
    """The total number of videos on this connection."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class WatchedVideosDict(TypedDict):
    options: NotRequired[list[str]]
    total: NotRequired[float]
    uri: NotRequired[str]
