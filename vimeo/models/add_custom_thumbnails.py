from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AddCustomThumbnails(SdkBaseModel):
    """An action indicating that the authenticated user is an administrator of the showcase and may therefore add custom
    thumbnails. This data requires a bearer token with the ``private`` scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class AddCustomThumbnailsDict(TypedDict):
    options: list[str]
    uri: str
