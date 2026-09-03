from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Portfolios(SdkBaseModel):
    """Information about the authenticated user's portfolios."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of portfolios on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class PortfoliosDict(TypedDict):
    options: list[str]
    total: float
    uri: str
