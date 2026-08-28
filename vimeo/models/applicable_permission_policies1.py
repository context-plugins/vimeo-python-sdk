from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .regional_delivery import RegionalDelivery, RegionalDeliveryDict


class ApplicablePermissionPolicies1(SdkBaseModel):
    """The applicable permission policies for the role."""

    folder: Optional[list[str]] = UNSET
    """The applicable folder-related permission policies for the role."""

    regional_delivery: Optional[list[RegionalDelivery]] = UNSET
    """The applicable permission policies related to regional delivery for the role."""

    video: Optional[list[str]] = UNSET
    """The applicable video-related permission policies for the role."""


class ApplicablePermissionPolicies1Dict(TypedDict):
    folder: NotRequired[list[str]]
    regional_delivery: NotRequired[list[RegionalDelivery | RegionalDeliveryDict]]
    video: NotRequired[list[str]]
