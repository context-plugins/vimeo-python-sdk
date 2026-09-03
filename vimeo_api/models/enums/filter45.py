from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter45(str, Enum):
    CC = "CC"
    CC_BY = "CC-BY"
    CC_BY_NC = "CC-BY-NC"
    CC_BY_NC_ND = "CC-BY-NC-ND"
    CC_BY_NC_SA = "CC-BY-NC-SA"
    CC_BY_ND = "CC-BY-ND"
    CC_BY_SA = "CC-BY-SA"
    CC0 = "CC0"
    CATEGORIES = "categories"
    DURATION = "duration"
    IN_PROGRESS = "in-progress"
    MINIMUM_LIKES = "minimum_likes"
    TRENDING = "trending"
    UPLOAD_DATE = "upload_date"

    __str__ = str.__str__


Filter45OrStr: TypeAlias = Annotated[Filter45 | str, open_enum_validator(Filter45)]
