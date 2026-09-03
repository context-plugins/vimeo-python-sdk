from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersFollowingRequest(SdkBaseModel):
    users: list[str]
    """An array of user IDs for the authenticated user to follow."""


class UsersFollowingRequestDict(TypedDict):
    users: list[str]
