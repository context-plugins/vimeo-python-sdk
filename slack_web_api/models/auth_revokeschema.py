from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AuthRevokeschema(SdkBaseModel):
    """Schema for successful response from auth.revoke method"""

    ok: Literal["True"] = "True"
    revoked: bool


class AuthRevokeschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    revoked: bool
