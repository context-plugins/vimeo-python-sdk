from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FolderPermissionPolicy(SdkBaseModel):
    name: str
    """The permission policy's name."""

    uri: str
    """The permission policy's API URI."""


class FolderPermissionPolicyDict(TypedDict):
    name: str
    uri: str
