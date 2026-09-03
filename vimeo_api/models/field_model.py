from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.type39 import Type39OrStr


class FieldModel(SdkBaseModel):
    default_value: OptionalNullable[str] = UNSET
    """The value applied by default when a video doesn't specify one. For ``str`` fields, the default can be up to 50
    characters."""

    delete: Optional[bool] = UNSET
    """When ``true``, combined with ``id``, deletes the field and all values assigned to it."""

    description: OptionalNullable[str] = UNSET
    """A short explanation of the field's purpose. Up to 1024 characters."""

    id: Optional[float] = UNSET
    """The ID of an existing field. Omit to create a new field."""

    mandatory: Optional[bool] = UNSET
    """Whether videos must have a value for this field. Required when creating a new field. Can only be relaxed
    (``true`` to ``false``) after creation, not made stricter."""

    name: Optional[str] = UNSET
    """The display name of the field. Required when creating a new field. Up to 255 characters."""

    type_: Optional[Type39OrStr] = Field(default=UNSET, alias="type")
    """The data type of the field. Required when creating a new field. **Immutable** after creation.

    Option descriptions:
     * ``bool`` - Boolean value (``true`` or ``false``).
     * ``date`` - Calendar date in ``YYYY-MM-DD`` format.
     * ``int`` - Integer value.
     * ``multi-select`` - One or more values chosen from the field's ``values`` list.
     * ``select`` - A single value chosen from the field's ``values`` list.
     * ``str`` - Freeform string value."""

    values: Optional[list[str | None]] = UNSET
    """The list of allowed values. Required for ``select`` and ``multi-select`` fields."""


class FieldModelDict(TypedDict):
    default_value: NotRequired[str | None]
    delete: NotRequired[bool]
    description: NotRequired[str | None]
    id: NotRequired[float]
    mandatory: NotRequired[bool]
    name: NotRequired[str]
    type_: NotRequired[Type39OrStr]
    values: NotRequired[list[str | None]]
