from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Page(SdkBaseModel):
    """Interactions for On Demand pages that belong to the genre."""

    added: bool
    """Whether the On Demand genre was added."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The URI to access the On Demand page."""


class PageDict(TypedDict):
    added: bool
    options: list[str]
    uri: str
