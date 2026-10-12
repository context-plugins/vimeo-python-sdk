from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .activate import Activate, ActivateDict
from .delete3 import Delete3, Delete3Dict
from .edit3 import Edit3, Edit3Dict


class Interactions10(SdkBaseModel):
    """A list of resource URIs related to the event."""

    activate: Activate | None
    """Information about where and how to activate the event."""

    delete: Delete3 | None
    """Information about where and how to delete an item."""

    edit: Edit3 | None
    """Information about where and how to edit an item."""


class Interactions10Dict(TypedDict):
    activate: ActivateDict | None
    delete: Delete3Dict | None
    edit: Edit3Dict | None
