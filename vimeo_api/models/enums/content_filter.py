from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentFilter(str, Enum):
    """The authenticated user's content filters.

    Option descriptions:
     * ``drugs`` - The content contains drug or alcohol use.
     * ``language`` - The content contains profanity or sexually suggestive language.
     * ``nudity`` - The content contains nudity.
     * ``safe`` - The content is suitable for all audiences.
     * ``unrated`` - The content hasn't been rated.
     * ``violence`` - The content contains violence or is graphic."""

    DRUGS = "drugs"
    LANGUAGE = "language"
    NUDITY = "nudity"
    SAFE = "safe"
    UNRATED = "unrated"
    VIOLENCE = "violence"

    __str__ = str.__str__


ContentFilterOrStr: TypeAlias = Annotated[ContentFilter | str, open_enum_validator(ContentFilter)]
