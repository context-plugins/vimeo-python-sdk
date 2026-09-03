from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Codes(SdkBaseModel):
    """Information about the codes associated with the promotion."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of uses on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class CodesDict(TypedDict):
    options: list[str]
    total: float
    uri: str
