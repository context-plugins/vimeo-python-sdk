from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PrivacyUsers(SdkBaseModel):
    """Information provided to channel moderators about which users they have specifically permitted to access this
    private channel. This data requires a bearer token with the ``private`` scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    total: float
    """The total number of users on this connection. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class PrivacyUsersDict(TypedDict):
    options: list[str]
    total: float
    uri: str
