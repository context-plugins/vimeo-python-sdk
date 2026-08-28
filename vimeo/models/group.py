from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .metadata6 import Metadata6, Metadata6Dict
from .picture import Picture, PictureDict
from .privacy4 import Privacy4, Privacy4Dict
from .user import User, UserDict


class Group(SdkBaseModel):
    created_time: str
    """The time in ISO 8601 format when the group was created."""

    description: str | None
    """The group's description."""

    link: str
    """The link to the group."""

    metadata: Metadata6
    """Metadata about the group."""

    modified_time: str
    """The time in ISO 8601 format when the group was last modified."""

    name: str
    """The group's display name."""

    pictures: Picture
    """The active picture for the group."""

    privacy: Privacy4
    """The group's privacy settings."""

    resource_key: str
    """The resource key of the group."""

    uri: str
    """The canonical relative URI of the group."""

    user: OptionalNullable[User] = UNSET
    """The owner of the group."""


class GroupDict(TypedDict):
    created_time: str
    description: str | None
    link: str
    metadata: Metadata6 | Metadata6Dict
    modified_time: str
    name: str
    pictures: Picture | PictureDict
    privacy: Privacy4 | Privacy4Dict
    resource_key: str
    uri: str
    user: NotRequired[User | UserDict | None]
