from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .picture import Picture, PictureDict


class DeletedBy(SdkBaseModel):
    """The user who deleted this video. Null if the video was moved to cold storage automatically."""

    name: str
    """The display name of the user who deleted the video."""

    pictures: Picture
    """The portrait of the user who deleted the video."""

    uri: str
    """The URI of the user who deleted the video."""


class DeletedByDict(TypedDict):
    name: str
    pictures: PictureDict
    uri: str
