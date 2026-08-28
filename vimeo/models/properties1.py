from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Properties1(SdkBaseModel):
    name: str
    """The name of the property to be sent."""

    options: list[str]
    """An array of the field's selectable options."""

    required: bool
    """Whether the field must be sent to achieve the desired action."""


class Properties1Dict(TypedDict):
    name: str
    options: list[str]
    required: bool
