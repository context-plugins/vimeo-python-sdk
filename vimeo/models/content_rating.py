from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.code import CodeOrStr


class ContentRating(SdkBaseModel):
    code: CodeOrStr
    """The reason for the content rating.

    Option descriptions:
     * ``advertisement`` - The content contains an advertisement.
     * ``drugs`` - The content contains drug or alcohol use.
     * ``language`` - The content contains profanity or sexually suggestive language.
     * ``nudity`` - The content contains nudity.
     * ``safe`` - The content is suitable for all audiences.
     * ``unrated`` - The content hasn't been rated.
     * ``violence`` - The content contains violence or is graphic."""

    name: str
    """The name of the content rating."""

    uri: str | None
    """The canonical relative URI of the content rating."""


class ContentRatingDict(TypedDict):
    code: CodeOrStr
    name: str
    uri: str | None
