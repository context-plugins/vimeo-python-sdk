from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.type13 import Type13OrStr


class CustomMetadataSettings(SdkBaseModel):
    default: OptionalNullable[str] = UNSET
    """Default value for the metadata field."""

    description: OptionalNullable[str] = UNSET
    """Optional description of the metadata field."""

    id: float
    """The unique identifier of the metadata field."""

    mandatory: bool
    """Whether this metadata field is required."""

    name: str
    """The name of the metadata field."""

    type_: Type13OrStr = Field(alias="type")
    """The data type of the metadata field.

    Option descriptions:
     * ``bool`` - Boolean value.
     * ``date`` - Date value.
     * ``int`` - Integer value.
     * ``multi-select`` - Multi-select from allowed values.
     * ``select`` - Single-select from allowed values.
     * ``str`` - String value."""

    values: Optional[list[str | None]] = UNSET
    """Allowed values for select/multi-select types."""


class CustomMetadataSettingsDict(TypedDict):
    default: NotRequired[str | None]
    description: NotRequired[str | None]
    id: float
    mandatory: bool
    name: str
    type_: Type13OrStr
    values: NotRequired[list[str | None]]
