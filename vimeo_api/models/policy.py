from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Policy(SdkBaseModel):
    """Information about the folder's data retention policy. This data requires a bearer token with the ``private``
    scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    title: str
    """The title of the data retention policy. This data requires a bearer token with the ``private`` scope."""

    uri: str
    """The URI of the data retention policy. This data requires a bearer token with the ``private`` scope."""


class PolicyDict(TypedDict):
    options: list[str]
    title: str
    uri: str
