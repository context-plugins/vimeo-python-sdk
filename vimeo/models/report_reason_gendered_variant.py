from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReportReasonGenderedVariant(SdkBaseModel):
    description: str
    """A human-readable description of the gendered variant."""

    name: str
    """The display name of the gendered variant."""

    uuid: str
    """The opaque reason UUID to submit when the target is a woman or girl."""


class ReportReasonGenderedVariantDict(TypedDict):
    description: str
    name: str
    uuid: str
