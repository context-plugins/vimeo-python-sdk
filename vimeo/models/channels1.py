from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Channels1(SdkBaseModel):
    """Information about the channels to which the authenticated user subscribes."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of channels on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class Channels1Dict(TypedDict):
    options: list[str]
    total: float
    uri: str
