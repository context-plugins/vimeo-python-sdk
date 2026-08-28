from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class HasRestrictedPrivacyOptions(SdkBaseModel):
    """Information about whether the video has restricted privacy options."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class HasRestrictedPrivacyOptionsDict(TypedDict):
    options: list[str]
    uri: str
