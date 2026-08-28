from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UsergroupsUsersListschema(SdkBaseModel):
    """Schema for successful response from usergroups.users.list method"""

    ok: Literal["True"] = "True"
    users: list[str]


class UsergroupsUsersListschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    users: list[str]
