from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AddModerators(SdkBaseModel):
    """An action indicating that the authenticated user is the owner of the channel and may therefore add other users as
    channel moderators. This data requires a bearer token with the ``private`` scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class AddModeratorsDict(TypedDict):
    options: list[str]
    uri: str
