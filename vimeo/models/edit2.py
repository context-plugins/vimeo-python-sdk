from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Edit2(SdkBaseModel):
    """Information about where and how to edit a showcase."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Edit2Dict(TypedDict):
    options: list[str]
    uri: str
