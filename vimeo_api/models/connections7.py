from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .related1 import Related1, Related1Dict


class Connections7(SdkBaseModel):
    """A list of resource URIs related to the activity."""

    related: Related1 | None
    """The activity's related content."""


class Connections7Dict(TypedDict):
    related: Related1Dict | None
