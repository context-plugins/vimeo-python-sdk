from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ModeratedChannels(SdkBaseModel):
    """Information about the channels that the authenticated user moderates."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of channels on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class ModeratedChannelsDict(TypedDict):
    options: list[str]
    total: float
    uri: str
