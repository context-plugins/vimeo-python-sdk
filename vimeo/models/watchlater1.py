from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Watchlater1(SdkBaseModel):
    """Information about whether this video appears on the user's Watch Later list."""

    added: bool
    """Whether the user has added the video to their Watch Later list."""

    added_time: str
    """The time in ISO 8601 format when the user added the video to their Watch Later list."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Watchlater1Dict(TypedDict):
    added: bool
    added_time: str
    options: list[str]
    uri: str
