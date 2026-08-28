from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ViewPrivacy(SdkBaseModel):
    """Information about whether a user has permissions to view the privacy of the video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class ViewPrivacyDict(TypedDict):
    options: list[str]
    uri: str
