from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Approach5(str, Enum):
    """The type of upload approach. For more information about upload approaches, refer to `Working with Video Uploads
    <https://developer.vimeo.com/api/upload/videos#understanding-upload-approaches>`__.

    Option descriptions:
     * ``post`` - The upload approach is POST.
     * ``pull`` - The upload approach is pull.
     * ``tus`` - The upload approach is tus."""

    POST = "post"
    PULL = "pull"
    TUS = "tus"

    __str__ = str.__str__


Approach5OrStr: TypeAlias = Annotated[Approach5 | str, open_enum_validator(Approach5)]
