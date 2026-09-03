from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .interactions6 import Interactions6, Interactions6Dict
from .metadata8 import Metadata8, Metadata8Dict


class OnDemandGenre(SdkBaseModel):
    canonical: str
    """The canonical name or URL slug of the genre."""

    interactions: Interactions6
    link: str
    """The Vimeo URL for the genre."""

    metadata: Metadata8
    name: str
    """The descriptive name of the genre."""

    uri: str
    """The relative URI of the On Demand genre."""


class OnDemandGenreDict(TypedDict):
    canonical: str
    interactions: Interactions6 | Interactions6Dict
    link: str
    metadata: Metadata8 | Metadata8Dict
    name: str
    uri: str
