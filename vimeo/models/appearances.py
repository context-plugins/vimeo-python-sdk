from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Appearances(SdkBaseModel):
    """Information about the appearances of the authenticated user in other videos."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of appearances on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class AppearancesDict(TypedDict):
    options: list[str]
    total: float
    uri: str
