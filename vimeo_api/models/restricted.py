from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Restricted(SdkBaseModel):
    """The restricted video storage quota (for embeddable and private videos)."""

    free: float | None
    """The number of bytes remaining in the authenticated user's restricted video storage quota."""

    max: float | None
    """The total number of bytes that the authenticated user can use for restricted videos (embeddable or private)."""

    unit: Literal["video_size"] = "video_size"
    """The unit that's used to compute quota.

    Option descriptions:
     * ``video_size`` - The quota is calculated using the byte size of the videos."""

    used: float
    """The number of bytes that the authenticated user has already used for restricted videos."""


class RestrictedDict(TypedDict):
    free: float | None
    max: float | None
    unit: NotRequired[Literal["video_size"]]
    used: float
