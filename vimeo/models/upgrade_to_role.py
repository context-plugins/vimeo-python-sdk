from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpgradeToRole(SdkBaseModel):
    """An object containing data on the value of **upgrade_to_role** and whether it's required for the interaction."""

    required: bool
    """Whether the upgrade role must be sent to achieve the desired action."""

    value: float
    """The value of the team role to which the user should be upgraded."""


class UpgradeToRoleDict(TypedDict):
    required: bool
    value: float
