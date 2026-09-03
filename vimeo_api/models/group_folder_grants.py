from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GroupFolderGrants(SdkBaseModel):
    """Information about the folder's group access grants."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of group access grants on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class GroupFolderGrantsDict(TypedDict):
    options: list[str]
    total: float
    uri: str
