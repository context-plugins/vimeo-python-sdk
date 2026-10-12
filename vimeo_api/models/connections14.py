from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .guest_user import GuestUser, GuestUserDict
from .user2 import User2, User2Dict


class Connections14(SdkBaseModel):
    guest_user: GuestUser
    """Information about the guest user who posted the comment."""

    user: User2
    """Information about the user who posted the reply."""


class Connections14Dict(TypedDict):
    guest_user: GuestUserDict
    user: User2Dict
