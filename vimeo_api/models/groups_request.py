from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GroupsRequest(SdkBaseModel):
    description: Optional[str] = UNSET
    """The description of the group."""

    name: str
    """The name of the group."""


class GroupsRequestDict(TypedDict):
    description: NotRequired[str]
    name: str
