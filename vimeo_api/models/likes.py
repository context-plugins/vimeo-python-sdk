from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Likes(SdkBaseModel):
    """Information about the videos that the authenticated user has liked."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of likes on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class LikesDict(TypedDict):
    options: list[str]
    total: float
    uri: str
