from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections14 import Connections14, Connections14Dict


class Metadata14(SdkBaseModel):
    connections: Connections14


class Metadata14Dict(TypedDict):
    connections: Connections14 | Connections14Dict
