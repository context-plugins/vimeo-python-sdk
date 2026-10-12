from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .metadata10 import Metadata10, Metadata10Dict


class Connections9(SdkBaseModel):
    """A collection of information that is connected to this resource, including videos, genres, and pictures
    connections."""

    metadata: Metadata10


class Connections9Dict(TypedDict):
    metadata: Metadata10Dict
