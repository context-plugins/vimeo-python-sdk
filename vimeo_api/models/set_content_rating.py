from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SetContentRating(SdkBaseModel):
    """Information about setting a content rating for the video."""

    content_rating: list[str]
    """A list of valid content rating flags for the video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class SetContentRatingDict(TypedDict):
    content_rating: list[str]
    options: list[str]
    uri: str
