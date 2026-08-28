from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Code(str, Enum):
    """The reason for the content rating.

    Option descriptions:
     * ``advertisement`` - The content contains an advertisement.
     * ``drugs`` - The content contains drug or alcohol use.
     * ``language`` - The content contains profanity or sexually suggestive language.
     * ``nudity`` - The content contains nudity.
     * ``safe`` - The content is suitable for all audiences.
     * ``unrated`` - The content hasn't been rated.
     * ``violence`` - The content contains violence or is graphic."""

    ADVERTISEMENT = "advertisement"
    DRUGS = "drugs"
    LANGUAGE = "language"
    NUDITY = "nudity"
    SAFE = "safe"
    UNRATED = "unrated"
    VIOLENCE = "violence"

    __str__ = str.__str__


CodeOrStr: TypeAlias = Annotated[Code | str, open_enum_validator(Code)]
