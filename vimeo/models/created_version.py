from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreatedVersion(SdkBaseModel):
    """Information about the video version that is created from the trim operation."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class CreatedVersionDict(TypedDict):
    options: list[str]
    uri: str
