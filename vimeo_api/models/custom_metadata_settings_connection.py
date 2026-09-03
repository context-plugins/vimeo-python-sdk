from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_metadata_settings import CustomMetadataSettings, CustomMetadataSettingsDict
from .paging import Paging, PagingDict


class CustomMetadataSettingsConnection(SdkBaseModel):
    total: Optional[int] = UNSET
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    paging: Optional[Paging] = UNSET
    data: Optional[list[CustomMetadataSettings]] = UNSET


class CustomMetadataSettingsConnectionDict(TypedDict):
    total: NotRequired[int]
    page: NotRequired[int]
    per_page: NotRequired[int]
    paging: NotRequired[Paging | PagingDict]
    data: NotRequired[list[CustomMetadataSettings | CustomMetadataSettingsDict]]
