from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .join import Join, JoinDict


class Interactions5(SdkBaseModel):
    """User actions that have involved the group. This data requires a bearer token with the ``private`` scope."""

    join: Join
    """An action indicating that someone has joined the group. This data requires a bearer token with the ``private``
    scope."""


class Interactions5Dict(TypedDict):
    join: Join | JoinDict
