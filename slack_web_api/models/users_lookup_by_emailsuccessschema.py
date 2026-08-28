from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UsersLookupByEmailsuccessschema(SdkBaseModel):
    """Schema for successful response from users.lookupByEmail method"""

    ok: Literal["True"] = "True"
    user: Any


class UsersLookupByEmailsuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    user: Any
