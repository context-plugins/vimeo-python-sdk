from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceName1(str, Enum):
    """The service to simulcast to.

    Option descriptions:
     * ``custom_rtmp`` - Simulcast to a custom service.
     * ``facebook`` - Simulcast to Facebook Live.
     * ``linkedin`` - Simulcast to LinkedIn Live.
     * ``youtube`` - Simulcast to YouTube Live."""

    CUSTOM_RTMP = "custom_rtmp"
    FACEBOOK = "facebook"
    LINKEDIN = "linkedin"
    YOUTUBE = "youtube"

    __str__ = str.__str__


ServiceName1OrStr: TypeAlias = Annotated[ServiceName1 | str, open_enum_validator(ServiceName1)]
