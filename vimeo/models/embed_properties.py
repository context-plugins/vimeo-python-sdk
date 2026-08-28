from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EmbedProperties(SdkBaseModel):
    """The height, width, and source URL properties used to generate the fixed HTML embed code."""

    height: str
    """The height used to generate the fixed HTML embed code."""

    source_url: str
    """The source URL used to generate the fixed HTML embed code."""

    width: str
    """The width used to generate the fixed HTML embed code."""


class EmbedPropertiesDict(TypedDict):
    height: str
    source_url: str
    width: str
