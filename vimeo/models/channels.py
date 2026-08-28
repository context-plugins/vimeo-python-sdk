from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Channels(SdkBaseModel):
    """Information about the channels related to this category."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of channels on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class ChannelsDict(TypedDict):
    options: list[str]
    total: float
    uri: str
