from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections10 import Connections10, Connections10Dict


class Metadata10(SdkBaseModel):
    connections: Connections10


class Metadata10Dict(TypedDict):
    connections: Connections10Dict
