from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Dimension(str, Enum):
    BROWSER = "browser"
    CITY = "city"
    COUNTRY = "country"
    DEVICE_TYPE = "device_type"
    EMBED_DOMAIN = "embed_domain"
    EMBED_DOMAIN_PATH = "embed_domain_path"
    OS = "os"
    REGION = "region"
    STREAMING_TYPE = "streaming_type"
    TOTAL = "total"
    VIDEO = "video"

    __str__ = str.__str__


DimensionOrStr: TypeAlias = Annotated[Dimension | str, open_enum_validator(Dimension)]
