from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RequestedClip(SdkBaseModel):
    """Information about the requested video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class RequestedClipDict(TypedDict):
    options: list[str]
    uri: str
