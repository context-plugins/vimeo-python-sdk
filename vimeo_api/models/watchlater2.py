from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Watchlater2(SdkBaseModel):
    """Information about the authenticated user's interaction to watch the video later."""

    added: bool
    """Whether the authenticated user has added the video to their Watch Later queue."""

    added_time: str
    """The time in ISO 8601 format when the authenticated user added the video to their Watch Later queue."""

    uri: str
    """The URI for the authenticated user to add the video to their Watch Later queue."""


class Watchlater2Dict(TypedDict):
    added: bool
    added_time: str
    uri: str
