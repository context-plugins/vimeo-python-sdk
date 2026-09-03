from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Folders(SdkBaseModel):
    """A standard connection object indicating how to return all the subfolders in the folder."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of subfolders on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class FoldersDict(TypedDict):
    options: list[str]
    total: float
    uri: str
