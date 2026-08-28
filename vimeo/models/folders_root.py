from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FoldersRoot(SdkBaseModel):
    """Information about the authenticated user's root level folders and videos."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class FoldersRootDict(TypedDict):
    options: list[str]
    uri: str
