from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections8 import Connections8, Connections8Dict


class Metadata8(SdkBaseModel):
    connections: Connections8
    """A collection of information connected to this resource."""


class Metadata8Dict(TypedDict):
    connections: Connections8 | Connections8Dict
