from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .report2 import Report2, Report2Dict


class Interactions9(SdkBaseModel):
    report: Report2


class Interactions9Dict(TypedDict):
    report: Report2 | Report2Dict
