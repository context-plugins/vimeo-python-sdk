from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CustomMetadatum(SdkBaseModel):
    default: OptionalNullable[str] = UNSET
    """Default value for the metadata field."""

    description: OptionalNullable[str] = UNSET
    """Optional description of the metadata field."""

    field_id: float
    """The unique identifier of the metadata field."""

    field_value: OptionalNullable[str] = UNSET
    """The current value of this metadata field for the video."""

    mandatory: bool
    """Whether this metadata field is required."""

    name: str
    """The name of the metadata field."""

    type_: str = Field(alias="type")
    """The data type of the metadata field."""

    values: OptionalNullable[list[str]] = UNSET
    """Allowed values for select/multi-select types."""


class CustomMetadatumDict(TypedDict):
    default: NotRequired[str | None]
    description: NotRequired[str | None]
    field_id: float
    field_value: NotRequired[str | None]
    mandatory: bool
    name: str
    type_: str
    values: NotRequired[list[str] | None]
