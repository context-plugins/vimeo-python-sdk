from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .connections25 import Connections25, Connections25Dict


class Metadata27(SdkBaseModel):
    connections: Optional[Connections25] = UNSET


class Metadata27Dict(TypedDict):
    connections: NotRequired[Connections25Dict]
