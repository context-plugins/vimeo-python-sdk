from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Rating1(str, Enum):
    """An array of the user's default content ratings.

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


Rating1OrStr: TypeAlias = Annotated[Rating1 | str, open_enum_validator(Rating1)]
