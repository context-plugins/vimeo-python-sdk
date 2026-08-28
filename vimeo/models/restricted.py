from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.unit2 import Unit2OrStr


class Restricted(SdkBaseModel):
    """The restricted video storage quota (for embeddable and private videos)."""

    free: float | None
    """The number of bytes remaining in the authenticated user's restricted video storage quota."""

    max: float | None
    """The total number of bytes that the authenticated user can use for restricted videos (embeddable or private)."""

    unit: Unit2OrStr
    """The unit that's used to compute quota.

    Option descriptions:
     * ``video_size`` - The quota is calculated using the byte size of the videos."""

    used: float
    """The number of bytes that the authenticated user has already used for restricted videos."""


class RestrictedDict(TypedDict):
    free: float | None
    max: float | None
    unit: Unit2OrStr
    used: float
