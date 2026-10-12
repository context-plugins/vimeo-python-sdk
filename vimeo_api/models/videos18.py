from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.rating1 import Rating1OrStr
from .privacy10 import Privacy10, Privacy10Dict


class Videos18(SdkBaseModel):
    privacy: Optional[Privacy10] = UNSET
    rating: Optional[Rating1OrStr] = UNSET
    """An array of the user's default content ratings.

    Option descriptions:
     * ``drugs`` - The video contains drug or alcohol use.
     * ``language`` - The video contains profanity or sexually suggestive content.
     * ``nudity`` - The video contains nudity.
     * ``safe`` - The video is suitable for all audiences.
     * ``unrated`` - The video hasn't been rated.
     * ``violence`` - The video contains violent or graphic content."""


class Videos18Dict(TypedDict):
    privacy: NotRequired[Privacy10Dict]
    rating: NotRequired[Rating1OrStr]
