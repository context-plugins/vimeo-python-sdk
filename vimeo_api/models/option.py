from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Option(SdkBaseModel):
    new_value: OptionalNullable[str] = UNSET
    """The replacement value. Required for rename and add; omit (or set to ``null``) when deleting."""

    old_value: OptionalNullable[str] = UNSET
    """The existing value the operation targets. Required for rename and delete; omit (or set to ``null``) when adding a
    new value."""


class OptionDict(TypedDict):
    new_value: NotRequired[str | None]
    old_value: NotRequired[str | None]
