from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Albums(SdkBaseModel):
    """Information about the showcases created by the authenticated user."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of showcases on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class AlbumsDict(TypedDict):
    options: list[str]
    total: float
    uri: str
