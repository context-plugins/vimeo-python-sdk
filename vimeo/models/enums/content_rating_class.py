from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentRatingClass(str, Enum):
    """The video's high-level content rating class.

    Option descriptions:
     * ``explicit`` - The video contains one or more explicit content rating types.
     * ``safe`` - The video contains no explicit content rating types.
     * ``unrated`` - The video doesn't belong to a content rating class."""

    EXPLICIT = "explicit"
    SAFE = "safe"
    UNRATED = "unrated"

    __str__ = str.__str__


ContentRatingClassOrStr: TypeAlias = Annotated[ContentRatingClass | str, open_enum_validator(ContentRatingClass)]
