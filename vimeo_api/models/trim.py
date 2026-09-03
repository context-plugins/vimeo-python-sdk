from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Trim(SdkBaseModel):
    """Information about where and how to trim the video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class TrimDict(TypedDict):
    options: list[str]
    uri: str
