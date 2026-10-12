from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections2 import Connections2, Connections2Dict


class Metadata2(SdkBaseModel):
    """Metadata about the tag."""

    connections: Connections2
    """A collection of information that is connected to this resource."""


class Metadata2Dict(TypedDict):
    connections: Connections2Dict
