from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .user import User, UserDict
from .video import Video, VideoDict


class Assets(SdkBaseModel):
    """The assets that are needed to decorate the text."""

    user: Optional[User] = UNSET
    """The user object associated with the note's text decoration."""

    video: Optional[Video] = UNSET
    """The video object associated with the note's text decoration."""


class AssetsDict(TypedDict):
    user: NotRequired[User | UserDict]
    video: NotRequired[Video | VideoDict]
