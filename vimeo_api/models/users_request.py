from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.gender import GenderOrStr
from .videos18 import Videos18, Videos18Dict


class UsersRequest(SdkBaseModel):
    bio: Optional[str] = UNSET
    """The user's bio."""

    content_filter: Optional[list[str]] = UNSET
    """A list of values describing the content in the user's videos. Find the full list in the `/contentratings
    <https://developer.vimeo.com/api/reference/videos#get_content_ratings>`__ endpoint. You must provide a
    comma-separated list if you're using a query string or an array if you're using JSON."""

    gender: Optional[GenderOrStr] = UNSET
    """The authenticated user's gender.

    Option descriptions:
     * ``f`` - The user's preferred pronouns are she and her.
     * ``m`` - The user's preferred pronouns are he and him.
     * ``n`` - The user would rather not give preferred pronouns.
     * ``o`` - The user's preferred pronouns are they and them."""

    link: Optional[str] = UNSET
    """The user's custom Vimeo URL."""

    location: Optional[str] = UNSET
    """The user's location."""

    name: Optional[str] = UNSET
    """The user's display name."""

    password: Optional[str] = UNSET
    """The default password for all future videos that this user uploads. To use this field, the **videos.privacy.view**
    field must be ``password``."""

    videos: Optional[Videos18] = UNSET


class UsersRequestDict(TypedDict):
    bio: NotRequired[str]
    content_filter: NotRequired[list[str]]
    gender: NotRequired[GenderOrStr]
    link: NotRequired[str]
    location: NotRequired[str]
    name: NotRequired[str]
    password: NotRequired[str]
    videos: NotRequired[Videos18Dict]
