from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Page1(SdkBaseModel):
    """Information about how the authenticated user can interact with the connection to the video's On Demand page."""

    added: bool
    """Whether the On Demand page was added."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The URI to access the On Demand page."""


class Page1Dict(TypedDict):
    added: bool
    options: list[str]
    uri: str
