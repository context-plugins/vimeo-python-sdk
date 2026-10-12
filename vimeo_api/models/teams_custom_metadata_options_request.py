from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .option import Option, OptionDict


class TeamsCustomMetadataOptionsRequest(SdkBaseModel):
    field_id: float
    """The ID of the ``select`` or ``multi-select`` custom metadata field to modify."""

    options: list[Option]
    """The list of changes to apply to the field's allowed values."""


class TeamsCustomMetadataOptionsRequestDict(TypedDict):
    field_id: float
    options: list[OptionDict]
