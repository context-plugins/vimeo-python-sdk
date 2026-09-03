from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentRating2(str, Enum):
    """The event's granular content ratings.

    Option descriptions:
     * ``advertisement`` - The event contains advertisements.
     * ``drugs`` - The event contains drug or alcohol use.
     * ``language`` - The event contains profanity or sexually suggestive content.
     * ``nudity`` - The event contains nudity.
     * ``safe`` - The event is safe for all audiences.
     * ``unrated`` - The event hasn't been rated.
     * ``violence`` - The event contains violence."""

    ADVERTISEMENT = "advertisement"
    DRUGS = "drugs"
    LANGUAGE = "language"
    NUDITY = "nudity"
    SAFE = "safe"
    UNRATED = "unrated"
    VIOLENCE = "violence"

    __str__ = str.__str__


ContentRating2OrStr: TypeAlias = Annotated[ContentRating2 | str, open_enum_validator(ContentRating2)]
