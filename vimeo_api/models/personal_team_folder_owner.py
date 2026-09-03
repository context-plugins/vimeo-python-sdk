from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PersonalTeamFolderOwner(SdkBaseModel):
    """Information about the owner of the personal team folder."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The URI of the owner of the personal team folder."""


class PersonalTeamFolderOwnerDict(TypedDict):
    options: list[str]
    uri: str
