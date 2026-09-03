from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .user import User, UserDict
from .video import Video, VideoDict


class Credit(SdkBaseModel):
    name: str
    """The name of the person credited."""

    role: str
    """The character that the person portrayed, or the job that the person performed."""

    uri: str
    """The unique identifier to access the credit resource."""

    user: Optional[User] = UNSET
    """The Vimeo user associated with the credit."""

    video: Optional[Video] = UNSET
    """The video associated with the credit."""


class CreditDict(TypedDict):
    name: str
    role: str
    uri: str
    user: NotRequired[User | UserDict]
    video: NotRequired[Video | VideoDict]
