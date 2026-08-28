from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.migration_exchange_error_enum import MigrationExchangeErrorEnumOrStr


class MigrationExchangeerrorschema1Error(SdkBaseModel):
    """Schema for error response from migration.exchange method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: MigrationExchangeErrorEnumOrStr
    ok: Literal["False"] = "False"


class MigrationExchangeerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: MigrationExchangeErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
