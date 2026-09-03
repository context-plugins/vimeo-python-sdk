from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TeamsCustomMetadataBackfillRequest(SdkBaseModel):
    field_id: float
    """The ID of the custom metadata field to populate."""

    field_value: str
    """The value to assign to the field. Must match the field's data type. For ``str`` fields, the value can be up to 50
    characters."""

    override_existing: Optional[bool] = UNSET
    """Whether to overwrite values that are already set. When ``false`` (the default), only videos that don't yet have a
    value are updated."""


class TeamsCustomMetadataBackfillRequestDict(TypedDict):
    field_id: float
    field_value: str
    override_existing: NotRequired[bool]
