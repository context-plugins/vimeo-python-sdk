from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response_metadata import ResponseMetadata, ResponseMetadataDict


class AdminConversationsGetTeamsschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.getTeams"""

    ok: Literal["True"] = "True"
    response_metadata: Optional[ResponseMetadata] = UNSET
    team_ids: list[str]


class AdminConversationsGetTeamsschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    response_metadata: NotRequired[ResponseMetadata | ResponseMetadataDict]
    team_ids: list[str]
