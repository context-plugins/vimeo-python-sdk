from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ApiTesterrorschema1(SdkBaseModel):
    """Schema for error response api.test method"""

    error: str
    ok: Literal["False"] = "False"


class ApiTesterrorschema1Dict(TypedDict):
    error: str
    ok: NotRequired[Literal["False"]]
