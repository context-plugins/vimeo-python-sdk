from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Report(SdkBaseModel):
    """Information about where and how to report the requested user."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    reason: list[str]
    """A list of valid reasons for reporting a video."""

    uri: str
    """The API URI that resolves to the connection data."""


class ReportDict(TypedDict):
    options: list[str]
    reason: list[str]
    uri: str
