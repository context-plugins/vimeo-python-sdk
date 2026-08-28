from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ObjsTeamProfileFieldOption(SdkBaseModel):
    is_custom: OptionalNullable[bool] = UNSET
    is_multiple_entry: OptionalNullable[bool] = UNSET
    is_protected: OptionalNullable[bool] = UNSET
    is_scim: OptionalNullable[bool] = UNSET


class ObjsTeamProfileFieldOptionDict(TypedDict):
    is_custom: NotRequired[bool | None]
    is_multiple_entry: NotRequired[bool | None]
    is_protected: NotRequired[bool | None]
    is_scim: NotRequired[bool | None]
