from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PersonalTeamFolder(SdkBaseModel):
    """A standard connection object indicating how to return personal team folders."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of personal team folders on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class PersonalTeamFolderDict(TypedDict):
    options: list[str]
    total: float
    uri: str
