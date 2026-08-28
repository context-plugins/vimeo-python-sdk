from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type1 import Type1OrStr


class Follow1(SdkBaseModel):
    """An action indicating if the authenticated user has followed this channel. This data requires a bearer token with
    the ``private`` scope."""

    added: bool
    """Whether the authenticated user has followed this channel. This data requires a bearer token with the ``private``
    scope."""

    added_time: str | None
    """The time in ISO 8601 format that the user followed this channel, or the null value if the user hasn't followed
    the channel. This data requires a bearer token with the ``private`` scope."""

    type_: Type1OrStr | None = Field(alias="type")
    """The authenticated user's role type. This data requires a bearer token with the ``private`` scope.

    Option descriptions:
     * ``moderator`` - The authenticated user is a moderator.
     * ``subscriber`` - The authenticated user is a subscriber."""

    uri: str
    """The URI for following or unfollowing this channel. PUT to this URI to follow the channel, or DELETE to this URI
    to unfollow the channel. This data requires a bearer token with the ``private`` scope."""


class Follow1Dict(TypedDict):
    added: bool
    added_time: str | None
    type_: Type1OrStr | None
    uri: str
