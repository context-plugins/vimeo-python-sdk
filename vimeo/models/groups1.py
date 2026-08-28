from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Groups1(SdkBaseModel):
    """Information about the groups created by the authenticated user."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of groups on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class Groups1Dict(TypedDict):
    options: list[str]
    total: float
    uri: str
