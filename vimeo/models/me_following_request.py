from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MeFollowingRequest(SdkBaseModel):
    users: list[str]
    """An array of user IDs for the authenticated user to follow."""


class MeFollowingRequestDict(TypedDict):
    users: list[str]
