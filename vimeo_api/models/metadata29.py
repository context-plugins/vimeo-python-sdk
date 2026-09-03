from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections27 import Connections27, Connections27Dict


class Metadata29(SdkBaseModel):
    """The video version's metadata."""

    connections: Connections27


class Metadata29Dict(TypedDict):
    connections: Connections27 | Connections27Dict
