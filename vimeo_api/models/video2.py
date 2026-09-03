from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Video2(SdkBaseModel):
    """Information about the video associated with the trim."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Video2Dict(TypedDict):
    options: list[str]
    uri: str
