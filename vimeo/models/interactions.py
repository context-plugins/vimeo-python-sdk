from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .follow import Follow, FollowDict


class Interactions(SdkBaseModel):
    """The permissible actions related to the category."""

    follow: Follow
    """An action indicating if the authenticated user has followed the category."""


class InteractionsDict(TypedDict):
    follow: Follow | FollowDict
