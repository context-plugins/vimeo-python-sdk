from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersProjectsRequest(SdkBaseModel):
    name: str
    """The name of the folder."""

    parent_folder_uri: Optional[str] = UNSET
    """The URI of the parent folder."""


class UsersProjectsRequestDict(TypedDict):
    name: str
    parent_folder_uri: NotRequired[str]
