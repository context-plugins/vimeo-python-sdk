from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .privacy_users import PrivacyUsers, PrivacyUsersDict
from .requested_clip import RequestedClip, RequestedClipDict
from .users1 import Users1, Users1Dict
from .videos1 import Videos1, Videos1Dict


class Connections1(SdkBaseModel):
    """A collection of information that is connected to this resource."""

    privacy_users: PrivacyUsers
    """Information provided to channel moderators about which users they have specifically permitted to access this
    private channel. This data requires a bearer token with the ``private`` scope."""

    requested_clip: RequestedClip
    """Information about the requested video."""

    users: Users1
    """Information about the users following or moderating this channel."""

    videos: Videos1
    """Information about the videos that belong to this channel."""


class Connections1Dict(TypedDict):
    privacy_users: PrivacyUsersDict
    requested_clip: RequestedClipDict
    users: Users1Dict
    videos: Videos1Dict
