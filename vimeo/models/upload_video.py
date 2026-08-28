from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UploadVideo(SdkBaseModel):
    """The user's upload permissions information for this project."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class UploadVideoDict(TypedDict):
    options: list[str]
    uri: str
