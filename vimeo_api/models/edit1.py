from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Edit1(SdkBaseModel):
    """The user's edit permissions information for this project."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Edit1Dict(TypedDict):
    options: list[str]
    uri: str
