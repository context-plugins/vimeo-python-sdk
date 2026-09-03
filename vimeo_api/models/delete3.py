from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Delete3(SdkBaseModel):
    """Information about where and how to delete an item."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Delete3Dict(TypedDict):
    options: list[str]
    uri: str
