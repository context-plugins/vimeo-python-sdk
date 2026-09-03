from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Rating(str, Enum):
    """An array of the authorized user's default content ratings.

    Option descriptions:
     * ``drugs`` - The video contains drug or alcohol use.
     * ``language`` - The video contains profanity or sexually suggestive content.
     * ``nudity`` - The video contains nudity.
     * ``safe`` - The video is suitable for all audiences.
     * ``unrated`` - The video hasn't been rated.
     * ``violence`` - The video contains violent or graphic content."""

    DRUGS = "drugs"
    LANGUAGE = "language"
    NUDITY = "nudity"
    SAFE = "safe"
    UNRATED = "unrated"
    VIOLENCE = "violence"

    __str__ = str.__str__


RatingOrStr: TypeAlias = Annotated[Rating | str, open_enum_validator(Rating)]
