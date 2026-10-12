from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category import Category, CategoryDict
from .metadata1 import Metadata1, Metadata1Dict
from .picture import Picture, PictureDict
from .privacy import Privacy, PrivacyDict
from .tag_model import TagModel, TagModelDict
from .user import User, UserDict


class Channel(SdkBaseModel):
    categories: list[Category]
    """The categories to which the channel belongs as specified by the channel moderators."""

    created_time: str
    """The time in ISO 8601 format when the channel was created."""

    description: str | None
    """A brief explanation of the channel's content."""

    header: Picture
    """The banner that appears by default at the top of the channel page."""

    link: str
    """The URL to access the channel in a browser."""

    metadata: Metadata1
    """Metadata about the channel."""

    modified_time: str
    """The time in ISO 8601 format when the channel was last modified."""

    name: str
    """The display name that identifies the channel."""

    pictures: Picture
    """The active image for the channel. The default is the thumbnail of the last video added to the channel."""

    privacy: Privacy
    """The privacy settings of the channel."""

    resource_key: str
    """The channel resource key."""

    tags: list[TagModel]
    """An array of all tags assigned to the channel."""

    uri: str
    """The unique identifier to access the channel resource."""

    user: User
    """The Vimeo user who owns the channel."""


class ChannelDict(TypedDict):
    categories: list[CategoryDict]
    created_time: str
    description: str | None
    header: PictureDict
    link: str
    metadata: Metadata1Dict
    modified_time: str
    name: str
    pictures: PictureDict
    privacy: PrivacyDict
    resource_key: str
    tags: list[TagModelDict]
    uri: str
    user: UserDict
