from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.stream1 import Stream1OrStr


class Rent(SdkBaseModel):
    """The Rent interaction for the On Demand video."""

    currency: str | None
    """The currency code for the user's region."""

    display_price: str | None
    """The formatted display price for renting the On Demand video."""

    drm: bool
    """Whether the On Demand video has DRM."""

    expires_time: str | None
    """The time in ISO 8601 format when the rental period for the On Demand video expires."""

    link: str | None
    """The URL to rent the On Demand video on Vimeo."""

    price: float | None
    """The price to buy the On Demand video."""

    purchase_time: str | None
    """The time in ISO 8601 format when the On Demand video was rented."""

    stream: Stream1OrStr
    """The user's streaming access to the On Demand video.

    Option descriptions:
     * ``available`` - The video is available for streaming.
     * ``purchased`` - The user has purchased the video.
     * ``restricted`` - The user isn't permitted to stream the video.
     * ``unavailable`` - The video isn't available for streaming."""

    uri: str | None
    """The product URI to rent the On Demand video."""


class RentDict(TypedDict):
    currency: str | None
    display_price: str | None
    drm: bool
    expires_time: str | None
    link: str | None
    price: float | None
    purchase_time: str | None
    stream: Stream1OrStr
    uri: str | None
