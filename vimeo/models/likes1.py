from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Likes1(SdkBaseModel):
    """Information about the users who have liked the video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of likes on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class Likes1Dict(TypedDict):
    options: list[str]
    total: float
    uri: str
