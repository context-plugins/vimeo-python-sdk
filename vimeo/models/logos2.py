from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .custom2 import Custom2, Custom2Dict


class Logos2(SdkBaseModel):
    """A collection of information about the logo in the corner of the embeddable player."""

    custom: Custom2
    """A collection of information relating to custom logos in the embeddable player."""

    vimeo: bool
    """Whether the Vimeo logo appears in the embeddable player for the video."""


class Logos2Dict(TypedDict):
    custom: Custom2 | Custom2Dict
    vimeo: bool
