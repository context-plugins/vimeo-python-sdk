from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CanUpdatePrivacyToPublic1(SdkBaseModel):
    """Whether the user can update the showcase privacy to public."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class CanUpdatePrivacyToPublic1Dict(TypedDict):
    options: list[str]
    uri: str
