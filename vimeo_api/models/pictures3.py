from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Pictures3(SdkBaseModel):
    """Information about the event's thumbnails."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Pictures3Dict(TypedDict):
    options: list[str]
    uri: str
