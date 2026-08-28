from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Clip(SdkBaseModel):
    """Information about the videos that belong to this channel."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class ClipDict(TypedDict):
    options: list[str]
    uri: str
