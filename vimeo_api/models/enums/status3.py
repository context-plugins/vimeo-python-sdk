from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status3(str, Enum):
    """The play status of the video.

    Option descriptions:
     * ``drm_plays_exceeded`` - The user's quota for DRM plays has been exceeded.
     * ``playable`` - The video is playable.
     * ``purchase_required`` - The video must be purchased.
     * ``restricted`` - Playback for the video is restricted.
     * ``unavailable`` - The video is unavailable."""

    DRM_PLAYS_EXCEEDED = "drm_plays_exceeded"
    PLAYABLE = "playable"
    PURCHASE_REQUIRED = "purchase_required"
    RESTRICTED = "restricted"
    UNAVAILABLE = "unavailable"

    __str__ = str.__str__


Status3OrStr: TypeAlias = Annotated[Status3 | str, open_enum_validator(Status3)]
