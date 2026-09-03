from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections13 import Connections13, Connections13Dict
from .interactions8 import Interactions8, Interactions8Dict


class Metadata13(SdkBaseModel):
    connections: Connections13
    interactions: Interactions8
    """An object containing the actions that the user can perform on the comment."""


class Metadata13Dict(TypedDict):
    connections: Connections13 | Connections13Dict
    interactions: Interactions8 | Interactions8Dict
