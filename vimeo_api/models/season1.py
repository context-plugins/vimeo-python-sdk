from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Season1(SdkBaseModel):
    """Information about the video's season."""

    name: str
    """The name of the season on this connection."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Season1Dict(TypedDict):
    name: str
    options: list[str]
    uri: str
