from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Follow(SdkBaseModel):
    """An action indicating if the authenticated user has followed the category."""

    added: bool
    """Whether the authenticated user has followed the category."""

    added_time: str | None
    """The time in ISO 8601 format when the user followed the category, or the null value if the user hasn't followed
    the category."""

    uri: str
    """The URI for following or unfollowing the category: PUT to this URI to follow the category, or DELETE to this URI
    to unfollow the category."""


class FollowDict(TypedDict):
    added: bool
    added_time: str | None
    uri: str
