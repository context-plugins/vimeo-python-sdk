from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AddTo(SdkBaseModel):
    """When a channel appears in the context of adding or removing a video from it
    (``/videos/{video_id}/available_channels``), include information about adding or removing the video. This data
    requires a bearer token with the ``private`` scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class AddToDict(TypedDict):
    options: list[str]
    uri: str
