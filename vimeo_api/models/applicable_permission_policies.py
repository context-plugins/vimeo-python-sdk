from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .permission_policy import PermissionPolicy, PermissionPolicyDict


class ApplicablePermissionPolicies(SdkBaseModel):
    """Information about permission policies that can apply to the team member."""

    folder: list[PermissionPolicy]
    """An array of folder permission policies that can apply to the team member."""

    regional_delivery: list[PermissionPolicy]
    """An array of regional delivery permission policies that can apply to the team member."""

    video: list[PermissionPolicy]
    """An array of video permission policies that can apply to the team member."""


class ApplicablePermissionPoliciesDict(TypedDict):
    folder: list[PermissionPolicyDict]
    regional_delivery: list[PermissionPolicyDict]
    video: list[PermissionPolicyDict]
