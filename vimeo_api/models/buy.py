from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.download import DownloadOrStr
from .enums.stream import StreamOrStr


class Buy(SdkBaseModel):
    """The Buy interaction for the On Demand video."""

    currency: str | None
    """The currency code for the user's region."""

    display_price: str | None
    """The formatted display price for buying the On Demand video."""

    download: DownloadOrStr
    """The user's download access to the On Demand video.

    Option descriptions:
     * ``available`` - The video is available for download.
     * ``purchased`` - The user has purchased the video.
     * ``restricted`` - The user isn't permitted to download the video.
     * ``unavailable`` - The video isn't available for download."""

    drm: bool
    """Whether the On Demand video has DRM."""

    link: str | None
    """The URL to buy the On Demand video on Vimeo."""

    price: float | None
    """The price to buy the On Demand video."""

    purchase_time: str | None
    """The time in ISO 8601 format when the On Demand video was purchased."""

    stream: StreamOrStr
    """The user's streaming access to the On Demand video.

    Option descriptions:
     * ``available`` - The video is available for streaming.
     * ``purchased`` - The user has purchased the video.
     * ``restricted`` - The user isn't permitted to stream the video.
     * ``unavailable`` - The video isn't available for streaming"""

    uri: str | None
    """The product URI to purchase the On Demand video."""


class BuyDict(TypedDict):
    currency: str | None
    display_price: str | None
    download: DownloadOrStr
    drm: bool
    link: str | None
    price: float | None
    purchase_time: str | None
    stream: StreamOrStr
    uri: str | None
