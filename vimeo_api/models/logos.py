from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .custom import Custom, CustomDict


class Logos(SdkBaseModel):
    """A collection of information about the logo in the corner of the embeddable player."""

    custom: Custom
    """A collection of information relating to custom logos in the embeddable player."""

    vimeo: bool
    """Whether the Vimeo logo appears in the embeddable player."""


class LogosDict(TypedDict):
    custom: CustomDict
    vimeo: bool
