from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EditLiveEvents(SdkBaseModel):
    """An action indicating that the authenticated user can edit event videos inside the showcase. This data requires a
    bearer token with the ``private`` scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class EditLiveEventsDict(TypedDict):
    options: list[str]
    uri: str
