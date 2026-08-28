from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentRating1(str, Enum):
    """The content rating of the video, given either as a comma-separated list or as a JSON array, depending on the
    request format.

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


ContentRating1OrStr: TypeAlias = Annotated[ContentRating1 | str, open_enum_validator(ContentRating1)]
