from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TeamPermissions1(SdkBaseModel):
    """Information about the folder's team permissions list. This data requires a bearer token with the ``private``
    scope."""

    options: list[str]
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""


class TeamPermissions1Dict(TypedDict):
    options: list[str]
