from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections17 import Connections17, Connections17Dict


class Metadata18(SdkBaseModel):
    """Metadata about the fragments."""

    connections: Connections17
    """A collection of information that is connected to this resource."""


class Metadata18Dict(TypedDict):
    connections: Connections17Dict
