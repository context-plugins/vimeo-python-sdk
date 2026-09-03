from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Users2(SdkBaseModel):
    """Information about the members or moderators of the group."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of users on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class Users2Dict(TypedDict):
    options: list[str]
    total: float
    uri: str
