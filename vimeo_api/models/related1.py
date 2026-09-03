from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Related1(SdkBaseModel):
    """The activity's related content."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Related1Dict(TypedDict):
    options: list[str]
    uri: str
