from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Pictures1(SdkBaseModel):
    """Information about the video's thumbnails."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """Total number of thumbnails on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class Pictures1Dict(TypedDict):
    options: list[str]
    total: float
    uri: str
