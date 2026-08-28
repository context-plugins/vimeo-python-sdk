from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Album4(SdkBaseModel):
    """Information about adding or removing a video from the showcase. This information is included only when the video
    is referenced by the URI of a showcase that's moderated by the user."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Album4Dict(TypedDict):
    options: list[str]
    uri: str
