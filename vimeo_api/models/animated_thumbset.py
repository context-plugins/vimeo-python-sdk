from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .animated_thumbnail import AnimatedThumbnail, AnimatedThumbnailDict
from .enums.status9 import Status9OrStr


class AnimatedThumbset(SdkBaseModel):
    clip_uri: str
    """The URI of the video from which the sets of animated thumbnails were created."""

    created_on: str
    """The time in ISO 8601 format when the GIF was created."""

    sizes: list[AnimatedThumbnail]
    """An array of all the animated thumbnails in the set."""

    status: Status9OrStr
    """The availability of the animated thumbnail.

    Option descriptions:
     * ``cancelled`` - The animated thumbnail's creation has been cancelled.
     * ``completed`` - The animated thumbnail has been created.
     * ``failed`` - The animated thumbnail's creation has failed.
     * ``started`` - The animated thumbnail's creation has started."""

    uri: str
    """The URI of the set of animated thumbnails."""


class AnimatedThumbsetDict(TypedDict):
    clip_uri: str
    created_on: str
    sizes: list[AnimatedThumbnail | AnimatedThumbnailDict]
    status: Status9OrStr
    uri: str
