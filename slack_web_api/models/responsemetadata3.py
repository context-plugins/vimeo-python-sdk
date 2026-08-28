from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Responsemetadata3(SdkBaseModel):
    warnings: Optional[list[str]] = UNSET


class Responsemetadata3Dict(TypedDict):
    warnings: NotRequired[list[str]]
