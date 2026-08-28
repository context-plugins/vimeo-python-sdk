from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .scopes import Scopes, ScopesDict


class ApiPermissionsScopesListsuccessschema(SdkBaseModel):
    """Schema for successful response api.permissions.scopes.list method"""

    ok: Literal["True"] = "True"
    scopes: Scopes


class ApiPermissionsScopesListsuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    scopes: Scopes | ScopesDict
