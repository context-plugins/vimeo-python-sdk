from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CanUpdatePrivacyToPublic(SdkBaseModel):
    """Whether a user can update the video privacy to public."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class CanUpdatePrivacyToPublicDict(TypedDict):
    options: list[str]
    uri: str
