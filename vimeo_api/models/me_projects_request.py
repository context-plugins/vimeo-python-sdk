from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeProjectsRequest(SdkBaseModel):
    name: str
    """The name of the folder."""

    parent_folder_uri: Optional[str] = UNSET
    """The URI of the parent folder."""


class MeProjectsRequestDict(TypedDict):
    name: str
    parent_folder_uri: NotRequired[str]
