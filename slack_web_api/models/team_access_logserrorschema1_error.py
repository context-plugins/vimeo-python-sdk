from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.team_access_logs_error_enum import TeamAccessLogsErrorEnumOrStr


class TeamAccessLogserrorschema1Error(SdkBaseModel):
    """Schema for error response from team.accessLogs method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: TeamAccessLogsErrorEnumOrStr
    ok: Literal["False"] = "False"


class TeamAccessLogserrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: TeamAccessLogsErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
