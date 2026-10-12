from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .interactions9 import Interactions9, Interactions9Dict


class Metdata(SdkBaseModel):
    interactions: Interactions9


class MetdataDict(TypedDict):
    interactions: Interactions9Dict
