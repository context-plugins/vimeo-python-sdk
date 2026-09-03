from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Report1(SdkBaseModel):
    """Information about where and how to report a video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    reason: list[str]
    """A list of valid reasons for reporting a video."""

    uri: str
    """The API URI that resolves to the connection data."""


class Report1Dict(TypedDict):
    options: list[str]
    reason: list[str]
    uri: str
