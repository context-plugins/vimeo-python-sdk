from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .metadata import Metadata, MetadataDict
from .parent import Parent, ParentDict
from .picture import Picture, PictureDict
from .subcategory import Subcategory, SubcategoryDict


class Category(SdkBaseModel):
    icon: Optional[Picture] = UNSET
    """The active icon for the category."""

    is_deprecated: bool
    """Whether the category is deprecated and should not be used for new categorization."""

    last_video_featured_time: str
    """The most recent time in ISO 8601 format when the video was featured."""

    link: str
    """The URL to access the category in a browser."""

    metadata: Metadata
    """Metadata about the category."""

    name: str
    """The display name that identifies the category."""

    parent: Parent | None
    """The container of the category's parent category, if the current category is a subcategory."""

    pictures: Picture
    """The active picture for this category. The default shows vertical color bars."""

    resource_key: str
    """The resource key of the category."""

    subcategories: Optional[list[Subcategory]] = UNSET
    """All the subcategories that belong to the category, if the current category is a top-level parent."""

    top_level: bool
    """Whether the category isn't a subcategory of another category."""

    uri: str
    """The unique identifier to access the category resource."""


class CategoryDict(TypedDict):
    icon: NotRequired[Picture | PictureDict]
    is_deprecated: bool
    last_video_featured_time: str
    link: str
    metadata: Metadata | MetadataDict
    name: str
    parent: Parent | ParentDict | None
    pictures: Picture | PictureDict
    resource_key: str
    subcategories: NotRequired[list[Subcategory | SubcategoryDict]]
    top_level: bool
    uri: str
