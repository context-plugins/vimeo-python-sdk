from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CustomMetadataValues(SdkBaseModel):
    default: OptionalNullable[str] = UNSET
    """Default value."""

    description: OptionalNullable[str] = UNSET
    """Optional description."""

    field_id: float
    """The unique identifier of the metadata field."""

    field_value: OptionalNullable[str] = UNSET
    """The current value for the video."""

    mandatory: bool
    """Whether this metadata field is required."""

    name: str
    """The name of the metadata field."""

    type_: str = Field(alias="type")
    """The data type of the metadata field."""

    values: Optional[list[str | None]] = UNSET
    """Allowed values for select/multi-select types."""


class CustomMetadataValuesDict(TypedDict):
    default: NotRequired[str | None]
    description: NotRequired[str | None]
    field_id: float
    field_value: NotRequired[str | None]
    mandatory: bool
    name: str
    type_: str
    values: NotRequired[list[str | None]]
