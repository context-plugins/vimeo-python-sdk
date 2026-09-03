from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Subscribe(SdkBaseModel):
    """Subscription information for an On Demand video."""

    drm: Optional[bool] = UNSET
    """Whether the On Demand video has DRM."""

    expires_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the subscription expires."""

    purchase_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the subscription was purchased."""

    stream: Optional[str] = UNSET
    """The stream type."""


class SubscribeDict(TypedDict):
    drm: NotRequired[bool]
    expires_time: NotRequired[str]
    purchase_time: NotRequired[str]
    stream: NotRequired[str]
