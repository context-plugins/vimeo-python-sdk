from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class View2(SdkBaseModel):
    """The user's view permissions information for this project."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class View2Dict(TypedDict):
    options: list[str]
    uri: str
