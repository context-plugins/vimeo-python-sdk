from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Like(SdkBaseModel):
    """Information about whether the user has liked this video."""

    added: bool
    """Whether the user has liked the video."""

    added_time: str
    """The time in ISO 8601 format when the user liked the video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    show_count: bool
    """Whether the user can access the video's number of likes."""

    uri: str
    """The API URI that resolves to the connection data."""


class LikeDict(TypedDict):
    added: bool
    added_time: str
    options: list[str]
    show_count: bool
    uri: str
