from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type8 import Type8OrStr


class Join(SdkBaseModel):
    """An action indicating that someone has joined the group. This data requires a bearer token with the ``private``
    scope."""

    added: bool
    """Whether the user has followed the group. This data requires a bearer token with the ``private`` scope."""

    added_time: str | None
    """The time in ISO 8601 format when the user joined the group. This data requires a bearer token with the
    ``private`` scope."""

    title: str | None
    """The user's title. If this field isn't applicable, it takes the null value. This data requires a bearer token with
    the ``private`` scope."""

    type_: Type8OrStr | None = Field(alias="type")
    """The user's role type. This data requires a bearer token with the ``private`` scope.

    Option descriptions:
     * ``member`` - The user is a member.
     * ``moderator`` - The user is a moderator."""

    uri: str
    """The URI for following the group. PUT to this URI to follow the group, or DELETE to this URI to unfollow the
    group. This data requires a bearer token with the ``private`` scope."""


class JoinDict(TypedDict):
    added: bool
    added_time: str | None
    title: str | None
    type_: Type8OrStr | None
    uri: str
