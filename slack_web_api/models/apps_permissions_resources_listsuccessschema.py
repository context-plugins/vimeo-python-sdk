from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .resource import Resource, ResourceDict
from .response_metadata import ResponseMetadata, ResponseMetadataDict


class AppsPermissionsResourcesListsuccessschema(SdkBaseModel):
    """Schema for successful response apps.permissions.resources.list method"""

    ok: Literal["True"] = "True"
    resources: list[Resource]
    response_metadata: Optional[ResponseMetadata] = UNSET


class AppsPermissionsResourcesListsuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    resources: list[Resource | ResourceDict]
    response_metadata: NotRequired[ResponseMetadata | ResponseMetadataDict]
