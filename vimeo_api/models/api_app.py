from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiApp(SdkBaseModel):
    capabilities: Any
    """The app's capabilities list."""

    name: str
    """The name of the API app."""

    uri: str
    """The canonical URI of the API app."""


class ApiAppDict(TypedDict):
    capabilities: Any
    name: str
    uri: str
