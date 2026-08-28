from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Published(SdkBaseModel):
    enabled: bool
    """Whether the On Demand page has been published."""

    time: str
    """The time in ISO 8601 format when this page was published."""


class PublishedDict(TypedDict):
    enabled: bool
    time: str
