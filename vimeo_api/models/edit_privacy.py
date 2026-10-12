from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .properties1 import Properties1, Properties1Dict


class EditPrivacy(SdkBaseModel):
    """Information about editing the privacy of the video."""

    content_rating: list[str]
    """A list of valid content rating flags for the video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    properties: list[Properties1]
    """An array of suggested fields to be used for this interaction."""

    uri: str
    """The API URI that resolves to the connection data."""


class EditPrivacyDict(TypedDict):
    content_rating: list[str]
    options: list[str]
    properties: list[Properties1Dict]
    uri: str
