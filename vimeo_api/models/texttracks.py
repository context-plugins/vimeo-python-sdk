from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Texttracks(SdkBaseModel):
    """Information about the video's text tracks."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of text tracks on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class TexttracksDict(TypedDict):
    options: list[str]
    total: float
    uri: str
