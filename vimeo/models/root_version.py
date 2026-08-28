from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RootVersion(SdkBaseModel):
    """Information about the video version that is the source of the trimmed video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class RootVersionDict(TypedDict):
    options: list[str]
    uri: str
