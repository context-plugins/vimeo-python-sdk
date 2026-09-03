from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.showing import ShowingOrStr
from .enums.unit import UnitOrStr


class Space(SdkBaseModel):
    """Information about the authenticated user's upload space remaining for the current period."""

    free: float
    """The number of bytes or videos remaining in the authenticated user's upload quota."""

    max: float | None
    """The maximum number of bytes or videos allotted to the authenticated user's upload quota."""

    showing: ShowingOrStr
    """The type of quota for the values of the **upload_quota.space** field.

    Option descriptions:
     * ``lifetime`` - The quota type is lifetime.
     * ``periodic`` - The quota type is periodic."""

    unit: UnitOrStr | None
    """The unit that's used to compute quota.

    Option descriptions:
     * ``video_count`` - The quota is calculated using the count of the videos.
     * ``video_size`` - The quota is calculated using the byte size of the videos."""

    used: float
    """The number of bytes or videos that the authenticated user has already uploaded against their quota."""


class SpaceDict(TypedDict):
    free: float
    max: float | None
    showing: ShowingOrStr
    unit: UnitOrStr | None
    used: float
