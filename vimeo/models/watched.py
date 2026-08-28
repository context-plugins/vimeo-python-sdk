from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Watched(SdkBaseModel):
    """Information about removing this video from the user's list of watched videos."""

    added: bool
    """Whether the user has watched the video."""

    added_time: str
    """The time in ISO 8601 format when the user watched the video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class WatchedDict(TypedDict):
    added: bool
    added_time: str
    options: list[str]
    uri: str
