from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .live1 import Live1, Live1Dict


class Video1(SdkBaseModel):
    """The associated video object. This data requires a bearer token with the ``private`` scope."""

    comments: float
    """The number of comments on the associated video. This data requires a bearer token with the ``private`` scope."""

    created_time: str
    """The time in ISO 8601 format when the video was created. This data requires a bearer token with the ``private``
    scope."""

    duration: float
    """The duration of the associated video. This data requires a bearer token with the ``private`` scope."""

    likes: float
    """The number of likes on the associated video. This data requires a bearer token with the ``private`` scope."""

    live: Live1
    """The associated live stream object. This data requires a bearer token with the ``private`` scope."""

    manage_link: str
    """The link to the video management page. This data requires a bearer token with the ``private`` scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    title: str
    """The title of the associated video. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class Video1Dict(TypedDict):
    comments: float
    created_time: str
    duration: float
    likes: float
    live: Live1Dict
    manage_link: str
    options: list[str]
    title: str
    uri: str
