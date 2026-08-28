from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .likes3 import Likes3, Likes3Dict
from .watchlater2 import Watchlater2, Watchlater2Dict


class Interactions14(SdkBaseModel):
    likes: Likes3
    """Information about the authenticated user's interaction to like the video."""

    watchlater: Watchlater2
    """Information about the authenticated user's interaction to watch the video later."""


class Interactions14Dict(TypedDict):
    likes: Likes3 | Likes3Dict
    watchlater: Watchlater2 | Watchlater2Dict
