from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections12 import Connections12, Connections12Dict


class Metadata12(SdkBaseModel):
    connections: Connections12


class Metadata12Dict(TypedDict):
    connections: Connections12 | Connections12Dict
