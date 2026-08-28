from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.type import TypeOrStr


class ObjsTeamProfileField(SdkBaseModel):
    field_name: OptionalNullable[str] = UNSET
    hint: str
    id: str
    is_hidden: Optional[bool] = UNSET
    label: str
    options: Optional[Any] = UNSET
    ordering: float
    possible_values: Optional[list[str | None]] = UNSET
    type_: TypeOrStr = Field(alias="type")


class ObjsTeamProfileFieldDict(TypedDict):
    field_name: NotRequired[str | None]
    hint: str
    id: str
    is_hidden: NotRequired[bool]
    label: str
    options: NotRequired[Any]
    ordering: float
    possible_values: NotRequired[list[str | None]]
    type_: TypeOrStr
