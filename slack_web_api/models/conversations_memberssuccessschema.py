from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .response_metadata import ResponseMetadata, ResponseMetadataDict


class ConversationsMemberssuccessschema(SdkBaseModel):
    """Schema for successful response conversations.members method"""

    members: list[str]
    ok: Literal["True"] = "True"
    response_metadata: ResponseMetadata


class ConversationsMemberssuccessschemaDict(TypedDict):
    members: list[str]
    ok: NotRequired[Literal["True"]]
    response_metadata: ResponseMetadata | ResponseMetadataDict
