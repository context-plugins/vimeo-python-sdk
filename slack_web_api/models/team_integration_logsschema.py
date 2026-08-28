from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .log import Log, LogDict
from .pagingobject import Pagingobject, PagingobjectDict


class TeamIntegrationLogsschema(SdkBaseModel):
    """Schema for successful response from team.integrationLogs method"""

    logs: list[Log]
    ok: Literal["True"] = "True"
    paging: Pagingobject


class TeamIntegrationLogsschemaDict(TypedDict):
    logs: list[Log | LogDict]
    ok: NotRequired[Literal["True"]]
    paging: Pagingobject | PagingobjectDict
