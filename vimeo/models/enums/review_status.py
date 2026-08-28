from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReviewStatus(str, Enum):
    """The review status of the video.

    Option descriptions:
     * ``approved`` - The video review was approved.
     * ``in_progress`` - The video review is in progress.
     * ``needs_review`` - The video needs to be reviewed."""

    APPROVED = "approved"
    IN_PROGRESS = "in_progress"
    NEEDS_REVIEW = "needs_review"

    __str__ = str.__str__


ReviewStatusOrStr: TypeAlias = Annotated[ReviewStatus | str, open_enum_validator(ReviewStatus)]
