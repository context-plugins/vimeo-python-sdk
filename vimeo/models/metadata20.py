from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections19 import Connections19, Connections19Dict


class Metadata20(SdkBaseModel):
    connections: Connections19


class Metadata20Dict(TypedDict):
    connections: Connections19 | Connections19Dict
