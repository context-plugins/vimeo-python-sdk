from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentRating4(str, Enum):
    """The video's granular content rating.

    Option descriptions:
     * ``advertisement`` - The video contains advertisements.
     * ``drugs`` - The video contains drug or alcohol use.
     * ``language`` - The video contains profanity or sexually suggestive content.
     * ``nudity`` - The video contains nudity.
     * ``safe`` - The video is safe for all audiences.
     * ``unrated`` - The video hasn't been rated.
     * ``violence`` - The video contains violence."""

    ADVERTISEMENT = "advertisement"
    DRUGS = "drugs"
    LANGUAGE = "language"
    NUDITY = "nudity"
    SAFE = "safe"
    UNRATED = "unrated"
    VIOLENCE = "violence"

    __str__ = str.__str__


ContentRating4OrStr: TypeAlias = Annotated[ContentRating4 | str, open_enum_validator(ContentRating4)]
