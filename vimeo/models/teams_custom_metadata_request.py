from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .field_model import FieldModel, FieldModelDict


class TeamsCustomMetadataRequest(SdkBaseModel):
    fields: Optional[list[FieldModel]] = UNSET
    """The custom metadata fields to create, update, or delete."""


class TeamsCustomMetadataRequestDict(TypedDict):
    fields: NotRequired[list[FieldModel | FieldModelDict]]
