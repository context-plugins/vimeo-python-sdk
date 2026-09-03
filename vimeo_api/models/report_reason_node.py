from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.kind import KindOrStr
from .report_reason_gendered_variant import ReportReasonGenderedVariant, ReportReasonGenderedVariantDict


class ReportReasonNode(SdkBaseModel):
    description: str
    """A human-readable description of the category or leaf."""

    external_url: Optional[str] = UNSET
    """For external-handoff leaves, the dedicated form to use instead of this endpoint."""

    gendered: Optional[ReportReasonGenderedVariant] = UNSET
    """For reason leaves with a gender fork, the distinct variant to submit when the target is a woman or girl."""

    id: str
    """Stable identifier for this node: the opaque reason UUID for a submittable leaf, or a slug for a category or
    external-handoff leaf."""

    kind: KindOrStr
    """The node kind.

    Option descriptions:
     * ``category`` - A grouping node; its children reference it via ``parent_id``.
     * ``external`` - Handed off to a dedicated form (see ``external_url``), not POST-able here.
     * ``reason`` - A submittable leaf; its ``id`` is the opaque reason UUID to POST."""

    name: str
    """The display name for the category or leaf."""

    parent_id: str | None
    """The ``id`` of the node this is nested under, or ``null`` at the top level."""


class ReportReasonNodeDict(TypedDict):
    description: str
    external_url: NotRequired[str]
    gendered: NotRequired[ReportReasonGenderedVariant | ReportReasonGenderedVariantDict]
    id: str
    kind: KindOrStr
    name: str
    parent_id: str | None
