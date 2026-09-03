from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PermissionPolicy(SdkBaseModel):
    created_on: str
    """The time at which the permission policy was created."""

    display_description: str
    """The display description of the permission policy, translated where applicable."""

    display_name: str
    """The display name of the permission policy, translated where applicable."""

    modified_on: str | None
    """The time at which the permission policy was last modified."""

    name: str
    """The name of the permission policy."""

    permission_actions: Any
    """The permission actions associated with the policy."""

    uri: str
    """The URI of the permission policy."""


class PermissionPolicyDict(TypedDict):
    created_on: str
    display_description: str
    display_name: str
    modified_on: str | None
    name: str
    permission_actions: Any
    uri: str
