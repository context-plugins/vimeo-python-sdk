from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.rendition2 import Rendition2OrStr


class Download1(SdkBaseModel):
    expires: str
    """The time in ISO 8601 format when the audio track link expires."""

    extension: str
    """The file extension of the audio file."""

    link: str
    """The URL of the audio track download."""

    rendition: Rendition2OrStr
    """The rendition of the audio track.

    Option descriptions:
     * ``source`` - The audio is the source file."""


class Download1Dict(TypedDict):
    expires: str
    extension: str
    link: str
    rendition: Rendition2OrStr
