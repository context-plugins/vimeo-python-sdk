from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response_metadata import ResponseMetadata, ResponseMetadataDict


class UsersConversationssuccessschema(SdkBaseModel):
    """Schema for successful response from users.conversations method. Returned conversation objects do not include
    ``num_members`` or ``is_member``"""

    channels: list[Any]
    ok: Literal["True"] = "True"
    response_metadata: Optional[ResponseMetadata] = UNSET


class UsersConversationssuccessschemaDict(TypedDict):
    channels: list[Any]
    ok: NotRequired[Literal["True"]]
    response_metadata: NotRequired[ResponseMetadata | ResponseMetadataDict]
