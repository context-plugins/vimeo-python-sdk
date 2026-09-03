from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .report_reason_node import ReportReasonNode, ReportReasonNodeDict


class VideoReportReason(SdkBaseModel):
    reasons: list[ReportReasonNode]
    """The DSA-aligned report reason taxonomy, flattened to a parent-referenced node list (categories, submittable
    leaves, and external-handoff leaves). A parent always precedes its descendants, so the tree rebuilds in one pass."""


class VideoReportReasonDict(TypedDict):
    reasons: list[ReportReasonNode | ReportReasonNodeDict]
