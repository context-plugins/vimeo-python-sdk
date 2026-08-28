from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Pages(SdkBaseModel):
    """Information about the On Demand pages related to this group."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class PagesDict(TypedDict):
    options: list[str]
    uri: str
