from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .user import User, UserDict
from .video import Video, VideoDict


class UploadAttempt(SdkBaseModel):
    clip: Optional[Video] = UNSET
    """The video to upload."""

    form: Optional[str] = UNSET
    """The HTML upload form."""

    ticket_id: str
    """The ticket identifier string for the upload."""

    upload_link: str
    """The upload URL."""

    uri: str
    """The upload URI."""

    user: User
    """The owner of the uploaded video."""


class UploadAttemptDict(TypedDict):
    clip: NotRequired[Video | VideoDict]
    form: NotRequired[str]
    ticket_id: str
    upload_link: str
    uri: str
    user: User | UserDict
