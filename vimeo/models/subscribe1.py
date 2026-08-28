from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.stream2 import Stream2OrStr


class Subscribe1(SdkBaseModel):
    """Information on subscribing to the On Demand video."""

    drm: Optional[bool] = UNSET
    """Whether the On Demand subscription has DRM."""

    expires_time: OptionalNullable[str] = UNSET
    """The time in ISO 8601 format when the On Demand video expires."""

    link: OptionalNullable[str] = UNSET
    """The URL to purchase the On Demand subscription on Vimeo."""

    purchase_time: OptionalNullable[str] = UNSET
    """The time in ISO 8601 format when the On Demand video was purchased."""

    stream: Optional[Stream2OrStr] = UNSET
    """The user's streaming access to the On Demand subscription.

    Option descriptions:
     * ``available`` - The On Demand subscription is available for streaming.
     * ``purchased`` - The On Demand subscription has been purchased.
     * ``restricted`` - Streaming for the On Demand subscription is restricted.
     * ``unavailable`` - The On Demand subscription is unavailable."""

    uri: OptionalNullable[str] = UNSET
    """The On Demand subscription's product URI."""


class Subscribe1Dict(TypedDict):
    drm: NotRequired[bool]
    expires_time: NotRequired[str | None]
    link: NotRequired[str | None]
    purchase_time: NotRequired[str | None]
    stream: NotRequired[Stream2OrStr]
    uri: NotRequired[str | None]
