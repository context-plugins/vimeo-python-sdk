from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .edit3 import Edit3, Edit3Dict


class Interactions11(SdkBaseModel):
    """A list of resource URIs related to the event destination."""

    edit: Edit3 | None
    """Information about where and how to edit an item."""


class Interactions11Dict(TypedDict):
    edit: Edit3 | Edit3Dict | None
