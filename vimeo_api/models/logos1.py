from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom1 import Custom1, Custom1Dict


class Logos1(SdkBaseModel):
    """A collection of information about the logo in the corner of the onsite player."""

    custom: Optional[Custom1] = UNSET
    """A collection of information relating to custom logos in the onsite player."""

    vimeo: Optional[bool] = UNSET
    """Whether the Vimeo logo appears in the onsite player."""


class Logos1Dict(TypedDict):
    custom: NotRequired[Custom1Dict]
    vimeo: NotRequired[bool]
