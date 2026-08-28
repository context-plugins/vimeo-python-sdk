from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class PinsRemoveschema(SdkBaseModel):
    """Schema for successful response from pins.remove method"""

    ok: Literal["True"] = "True"


class PinsRemoveschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
