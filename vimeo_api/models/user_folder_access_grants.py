from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .folder_permission_policy import FolderPermissionPolicy, FolderPermissionPolicyDict


class UserFolderAccessGrants(SdkBaseModel):
    """Information about the folder's user folder access grants."""

    folder_permission_policies: list[FolderPermissionPolicy]
    """Information about the owner's folder permission policies."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of user folder access grants on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""


class UserFolderAccessGrantsDict(TypedDict):
    folder_permission_policies: list[FolderPermissionPolicy | FolderPermissionPolicyDict]
    options: list[str]
    total: float
    uri: str
