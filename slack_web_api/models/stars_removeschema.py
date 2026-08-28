from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class StarsRemoveschema(SdkBaseModel):
    """Schema for successful response from stars.remove method"""

    ok: Literal["True"] = "True"


class StarsRemoveschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
