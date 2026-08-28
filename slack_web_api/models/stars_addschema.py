from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class StarsAddschema(SdkBaseModel):
    """Schema for successful response from stars.add method"""

    ok: Literal["True"] = "True"


class StarsAddschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
