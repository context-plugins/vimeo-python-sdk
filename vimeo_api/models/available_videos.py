from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AvailableVideos(SdkBaseModel):
    """Information about the authenticated user's videos that can be added to or removed from this showcase. This data
    requires a bearer token with the ``private`` scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    total: float
    """The total number of videos on this connection. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class AvailableVideosDict(TypedDict):
    options: list[str]
    total: float
    uri: str
