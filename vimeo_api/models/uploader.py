from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .picture import Picture, PictureDict


class Uploader(SdkBaseModel):
    """The video's uploader."""

    link: str
    """The profile link of the user who uploaded the video."""

    name: str
    """The display name of the user who uploaded the video."""

    pictures: Picture
    """The active portrait of the user who uploaded the video."""


class UploaderDict(TypedDict):
    link: str
    name: str
    pictures: Picture | PictureDict
