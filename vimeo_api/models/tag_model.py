from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .metadata2 import Metadata2, Metadata2Dict


class TagModel(SdkBaseModel):
    canonical: str
    """The normalized canonical tag name."""

    metadata: Metadata2
    """Metadata about the tag."""

    name: str
    """The tag value."""

    resource_key: str
    """The tag's resource key string."""

    uri: str
    """The canonical relative URI of the tag."""


class TagModelDict(TypedDict):
    canonical: str
    metadata: Metadata2Dict
    name: str
    resource_key: str
    uri: str
