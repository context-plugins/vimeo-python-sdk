from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .guest_user import GuestUser, GuestUserDict
from .replies import Replies, RepliesDict
from .user1 import User1, User1Dict


class Connections13(SdkBaseModel):
    guest_user: GuestUser
    """Information about the guest user who posted the comment."""

    replies: Replies
    """Information about the replies to the comment."""

    user: User1
    """Information about the user who posted the comment."""


class Connections13Dict(TypedDict):
    guest_user: GuestUserDict
    replies: RepliesDict
    user: User1Dict
