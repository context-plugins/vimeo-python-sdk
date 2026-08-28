from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MigrationExchangesuccessschema(SdkBaseModel):
    """Schema for successful response from migration.exchange method"""

    enterprise_id: str
    invalid_user_ids: Optional[list[str]] = UNSET
    ok: Literal["True"] = "True"
    team_id: str
    user_id_map: Optional[Any] = UNSET


class MigrationExchangesuccessschemaDict(TypedDict):
    enterprise_id: str
    invalid_user_ids: NotRequired[list[str]]
    ok: NotRequired[Literal["True"]]
    team_id: str
    user_id_map: NotRequired[Any]
