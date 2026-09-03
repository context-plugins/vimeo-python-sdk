from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Likes3(SdkBaseModel):
    """Information about the authenticated user's interaction to like the video."""

    added: bool
    """Whether the authenticated user has liked the video."""

    added_time: str
    """The time in ISO 8601 format when the authenticated user liked the video."""

    uri: str
    """The URI for the authenticated user to like the video."""


class Likes3Dict(TypedDict):
    added: bool
    added_time: str
    uri: str
