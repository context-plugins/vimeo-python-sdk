from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ParentFolder(SdkBaseModel):
    """A standard connection object indicating how to return the folder's parent folder."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class ParentFolderDict(TypedDict):
    options: list[str]
    uri: str
