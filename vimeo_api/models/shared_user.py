from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .picture import Picture, PictureDict


class SharedUser(SdkBaseModel):
    """Information about the user who shared the item."""

    link: Optional[str] = UNSET
    """The absolute URL of the users's profile page."""

    name: Optional[str] = UNSET
    """The display name of the user who shared the item."""

    pictures: Optional[Picture] = UNSET
    """Information about the user's portraits."""

    uri: Optional[str] = UNSET
    """The unique identifier to access the user resource."""


class SharedUserDict(TypedDict):
    link: NotRequired[str]
    name: NotRequired[str]
    pictures: NotRequired[PictureDict]
    uri: NotRequired[str]
