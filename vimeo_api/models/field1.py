from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Field1(SdkBaseModel):
    field_id: Optional[float] = UNSET
    """The ID of the custom metadata field, as returned by ``GET /teams/{user_id}/custom_metadata``."""

    field_value: OptionalNullable[str] = UNSET
    """The value to assign to the field. Send ``null`` to clear an existing value. For ``str`` fields, the value can be
    up to 50 characters; other types have their own format constraints (see the description above)."""


class Field1Dict(TypedDict):
    field_id: NotRequired[float]
    field_value: NotRequired[str | None]
