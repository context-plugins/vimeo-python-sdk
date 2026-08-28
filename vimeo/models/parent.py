from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Parent(SdkBaseModel):
    """The container of the category's parent category, if the current category is a subcategory."""

    link: str
    """The URL to access the parent category in a browser."""

    name: str
    """The display name that identifies the parent category."""

    uri: str
    """The unique identifier to access the parent of the category resource."""


class ParentDict(TypedDict):
    link: str
    name: str
    uri: str
