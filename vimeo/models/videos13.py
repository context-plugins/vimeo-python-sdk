from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Videos13(SdkBaseModel):
    """Information about the videos contained within the portfolio."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of videos on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class Videos13Dict(TypedDict):
    options: list[str]
    total: float
    uri: str
