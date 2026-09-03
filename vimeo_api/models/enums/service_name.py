from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceName(str, Enum):
    """The name of the destination service.

    Option descriptions:
     * ``custom_rtmp`` - The destination service is custom RTMP.
     * ``facebook`` - The destination service is Facebook Live.
     * ``linkedin`` - The destination service is LinkedIn Live.
     * ``youtube`` - The destination service is YouTube Live."""

    CUSTOM_RTMP = "custom_rtmp"
    FACEBOOK = "facebook"
    LINKEDIN = "linkedin"
    YOUTUBE = "youtube"

    __str__ = str.__str__


ServiceNameOrStr: TypeAlias = Annotated[ServiceName | str, open_enum_validator(ServiceName)]
