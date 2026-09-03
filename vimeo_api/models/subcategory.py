from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Subcategory(SdkBaseModel):
    link: str
    """The URL to access the subcategory in a browser."""

    name: str
    """The display name that identifies the subcategory."""

    uri: str
    """The unique identifier to access the subcategory."""


class SubcategoryDict(TypedDict):
    link: str
    name: str
    uri: str
