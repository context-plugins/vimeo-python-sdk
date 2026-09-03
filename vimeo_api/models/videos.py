from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Videos(SdkBaseModel):
    """Information about the videos related to this category."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of videos on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class VideosDict(TypedDict):
    options: list[str]
    total: float
    uri: str
