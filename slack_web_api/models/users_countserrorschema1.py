from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UsersCountserrorschema1(SdkBaseModel):
    """Schema for error response users.getPresence method"""

    error: str
    ok: Literal["False"] = "False"


class UsersCountserrorschema1Dict(TypedDict):
    error: str
    ok: NotRequired[Literal["False"]]
