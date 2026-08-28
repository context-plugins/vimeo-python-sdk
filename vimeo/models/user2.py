from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .picture import Picture, PictureDict


class User2(SdkBaseModel):
    """Information about the user who posted the reply."""

    badge: str | None
    """The user's badge type, if applicable."""

    is_staff_picked: bool
    """Whether the user has had a staff-picked video."""

    link: str
    """The absolute URL of the authenticated users's profile page."""

    name: str
    """The display name of the user who posted the reply."""

    pictures: Picture
    """Information about the user's portraits."""

    uri: str
    """The unique identifier to access the user resource."""


class User2Dict(TypedDict):
    badge: str | None
    is_staff_picked: bool
    link: str
    name: str
    pictures: Picture | PictureDict
    uri: str
