from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Download1(SdkBaseModel):
    expires: str
    """The time in ISO 8601 format when the audio track link expires."""

    extension: str
    """The file extension of the audio file."""

    link: str
    """The URL of the audio track download."""

    rendition: Literal["source"] = "source"
    """The rendition of the audio track.

    Option descriptions:
     * ``source`` - The audio is the source file."""


class Download1Dict(TypedDict):
    expires: str
    extension: str
    link: str
    rendition: NotRequired[Literal["source"]]
