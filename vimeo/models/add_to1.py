from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AddTo1(SdkBaseModel):
    """Information about adding or removing a video from the showcase. This data requires a bearer token with the
    ``private`` scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class AddTo1Dict(TypedDict):
    options: list[str]
    uri: str
