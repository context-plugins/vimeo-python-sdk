from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections26 import Connections26, Connections26Dict


class Metadata28(SdkBaseModel):
    connections: Connections26


class Metadata28Dict(TypedDict):
    connections: Connections26 | Connections26Dict
