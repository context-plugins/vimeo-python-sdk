from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Filters(SdkBaseModel):
    """The request filters to use for child text tracks. This data requires a bearer token with the ``private``
    scope."""

    parent_id: Optional[float] = UNSET
    """A filter that represents the ID of the parent text track. This data requires a bearer token with the ``private``
    scope."""


class FiltersDict(TypedDict):
    parent_id: NotRequired[float]
