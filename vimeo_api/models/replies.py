from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Replies(SdkBaseModel):
    """Information about the replies to the comment."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of replies on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class RepliesDict(TypedDict):
    options: list[str]
    total: float
    uri: str
