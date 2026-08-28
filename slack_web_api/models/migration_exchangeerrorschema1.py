from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.migration_exchange_error_enum import MigrationExchangeErrorEnumOrStr


class MigrationExchangeerrorschema1(SdkBaseModel):
    """Schema for error response from migration.exchange method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: MigrationExchangeErrorEnumOrStr
    ok: Literal["False"] = "False"


class MigrationExchangeerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: MigrationExchangeErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
