from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .login import Login, LoginDict
from .pagingobject import Pagingobject, PagingobjectDict


class TeamAccessLogsschema(SdkBaseModel):
    """Schema for successful response from team.accessLogs method"""

    logins: list[Login]
    ok: Literal["True"] = "True"
    paging: Pagingobject


class TeamAccessLogsschemaDict(TypedDict):
    logins: list[Login | LoginDict]
    ok: NotRequired[Literal["True"]]
    paging: Pagingobject | PagingobjectDict
