from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class DndEndDndschema(SdkBaseModel):
    """Schema for successful response from dnd.endDnd method"""

    ok: Literal["True"] = "True"


class DndEndDndschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
